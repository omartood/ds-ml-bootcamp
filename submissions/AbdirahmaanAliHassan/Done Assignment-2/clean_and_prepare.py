import pandas as pd
import numpy as np
import re
from pathlib import Path
from collections import Counter
import sys

# -------- CONFIG --------
# Haddii faylkaagu yahay mid kale, beddel 'in_path'
# Waxa kale oo script-ku si toos ah u aqrin karaa .csv
in_path = Path("social_media_usage_academic_performance_102.csv.xlsx")
clean_out = Path("social_media_usage_academic_performance_CLEAN.csv")
ml_out = Path("social_media_usage_academic_performance_ML_READY.csv")
# ------------------------


def normalize_col(col: str) -> str:
    """Magaca tiirka u rogo snake_case oo nadiif ah."""
    col = col.strip()
    col = re.sub(r"[^\w\s]", "", col)      # saar calaamadaha (punctuation)
    col = re.sub(r"\s+", "_", col.lower()) # meel bannaan -> _
    return col


def find_col(df: pd.DataFrame, candidates):
    """Raadi tiir u dhigma liiska 'candidates' (exact or contains)."""
    for cand in candidates:
        if cand in df.columns:
            return cand
    for cand in candidates:
        for c in df.columns:
            if cand in c:
                return c
    return None


def normalize_yes_no(x):
    """U midayn qiimaha Yes/No ee group_study."""
    s = str(x).strip().lower()
    if s in {"yes", "y", "haa", "haa/yes", "true", "1"}:
        return "Yes"
    if s in {"no", "n", "maya", "false", "0"}:
        return "No"
    return np.nan


def load_any(path: Path) -> pd.DataFrame:
    """Akhriso Excel ama CSV iyadoo ku xiran suffix."""
    if not path.exists():
        # Haddii user-ku ku siiyay .csv halkii .xlsx, isku day fallback
        alt_csv = path.with_suffix(".csv")
        alt_xlsx = path.with_suffix(".xlsx")
        tried = [str(path)]
        for alt in [alt_csv, alt_xlsx]:
            if alt.exists():
                path = alt
                break
            tried.append(str(alt))
        else:
            raise FileNotFoundError(f"File not found. Tried: {', '.join(tried)}")

    if path.suffix.lower() in [".xlsx", ".xls"]:
        return pd.read_excel(path)
    elif path.suffix.lower() == ".csv":
        return pd.read_csv(path)
    else:
        # isku day akhris CSV haddii suffix aan la aqoon
        try:
            return pd.read_csv(path)
        except Exception:
            return pd.read_excel(path)


def main():
    # 1) Load
    df_raw = load_any(in_path)

    # 2) Normalize column names
    df = df_raw.copy()
    df.columns = [normalize_col(c) for c in df.columns]

    # 3) Identify likely columns (magacyada aad isticmaaleysay)
    social_col    = find_col(df, ["social_media_hours_per_day", "social_media_hours", "daily_social_media_hours", "social_hours", "social_media"])
    study_col     = find_col(df, ["study_hours_per_day", "study_hours", "daily_study_hours"])
    sleep_col     = find_col(df, ["sleep_hours_per_day", "sleep_hours", "daily_sleep_hours"])
    platform_col  = find_col(df, ["preferred_platform", "platform", "social_media_platform"])
    group_col     = find_col(df, ["group_study", "group_study_participation", "group", "study_group"])
    gpa_col       = find_col(df, ["gpa", "cgpa", "grade_point_average"])
    performance_col = find_col(df, ["academic_performance", "performance", "label", "target"])

    # 4) Trim strings
    for c in df.select_dtypes(include="object").columns:
        df[c] = df[c].astype(str).str.strip()

    # 5) Coerce numeric columns
    for c in [social_col, study_col, sleep_col, gpa_col]:
        if c and c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")

    # 6) Clip hour-like columns to [0, 24]
    for c in [social_col, study_col, sleep_col]:
        if c and c in df.columns:
            df[c] = df[c].clip(lower=0, upper=24)

    # 7) Normalize categorical columns
    # preferred_platform
    if platform_col and platform_col in df.columns:
        platform_map = {
            "fb": "Facebook", "facebook": "Facebook",
            "tik_tok": "TikTok", "tiktok": "TikTok",
            "instagram": "Instagram", "ig": "Instagram",
            "twitter": "Twitter", "x": "Twitter",
            "youtube": "YouTube", "yt": "YouTube",
        }
        df[platform_col] = (
            df[platform_col]
            .str.lower()
            .map(platform_map)
            .fillna(df[platform_col])  # haddii aanu match-garin, sii kii hore
        )

    # group_study
    if group_col and group_col in df.columns:
        df[group_col] = df[group_col].apply(normalize_yes_no)

    # 8) Handle missing values
    for c in df.columns:
        if df[c].dtype.kind in "iufc":  # numeric
            if df[c].isna().any():
                df[c] = df[c].fillna(df[c].median())
        else:  # categorical / object
            if df[c].isna().any():
                vals = df[c].dropna().tolist()
                if vals:
                    df[c] = df[c].fillna(Counter(vals).most_common(1)[0][0])

    # 9) Create/clean label
    label_col = None
    if performance_col and performance_col in df.columns:
        label_col = performance_col
        # Normalize text labels to High/Low haddii ay jiraan
        def norm_label(x):
            s = str(x).strip().lower()
            if s in {"high", "1", "good", "above"}:
                return "High"
            if s in {"low", "0", "poor", "below"}:
                return "Low"
            return x
        df[label_col] = df[label_col].apply(norm_label)
    elif gpa_col and gpa_col in df.columns:
        # Haddii label la waayo laakiin GPA jiro, ka samee performance (>=3.0 High else Low)
        label_col = "performance"
        df[label_col] = np.where(df[gpa_col] >= 3.0, "High", "Low")

    # 10) Save CLEAN
    df.to_csv(clean_out, index=False)

    # 11) Build ML-READY (one-hot for categoricals)
    categorical_cols = []
    if platform_col and platform_col in df.columns: categorical_cols.append(platform_col)
    if group_col and group_col in df.columns: categorical_cols.append(group_col)

    numeric_cols = []
    for c in [social_col, study_col, sleep_col, gpa_col]:
        if c and c in df.columns:
            numeric_cols.append(c)

    # Haddii label laga dhisay GPA, iska saar GPA si leakage looga fogaado
    numeric_ml = numeric_cols.copy()
    if gpa_col in numeric_ml and label_col == "performance":
        numeric_ml.remove(gpa_col)

    df_ml = df.copy()
    if categorical_cols:
        dummies = pd.get_dummies(
            df_ml[categorical_cols], drop_first=False, dtype=int, prefix=categorical_cols
        )
        df_ml = pd.concat([df_ml.drop(columns=categorical_cols), dummies], axis=1)

    keep_cols = list(dict.fromkeys(numeric_ml))  # preserve order + unique
    # keep encoded categoricals
    for col in df_ml.columns:
        if any(col.startswith(c + "_") for c in categorical_cols):
            keep_cols.append(col)
    if label_col:
        keep_cols.append(label_col)

    df_ml[keep_cols].to_csv(ml_out, index=False)

    # 12) Console summary
    print("\n=== DATA CLEANING SUMMARY ===")
    print(f"Input file:          {in_path}")
    print(f"Rows x Cols (raw):   {df_raw.shape}")
    print(f"Rows x Cols (clean): {df.shape}")
    print(f"Saved CLEAN:         {clean_out}")
    print(f"Saved ML_READY:      {ml_out}")
    print("\nIdentified columns:")
    print(f"  social_media_hours -> {social_col}")
    print(f"  study_hours        -> {study_col}")
    print(f"  sleep_hours        -> {sleep_col}")
    print(f"  preferred_platform -> {platform_col}")
    print(f"  group_study        -> {group_col}")
    print(f"  gpa                -> {gpa_col}")
    print(f"  label_col          -> {label_col}")
    print("\nPreview (CLEAN):")
    print(df.head(5))
    print("\nPreview (ML_READY):")
    print(df_ml[keep_cols].head(5))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("ERROR:", e)
        sys.exit(1)
