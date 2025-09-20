import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# === 1) Load dataset ===
car_dataset = "car_l3_dataset.csv"
df = pd.read_csv(car_dataset)

print("\n=== displaying the first 10 rows ===")
print(df.head(10))

print("\n=== SHAPE ===")
print(df.shape)

print("\n=== INFO ===")
print(df.info())

print("\n=== INITIAL MISSING VALUES ===")
print(df.isnull().sum())

# === 2) Clean Price symbols ===
df["Price"] = df["Price"].replace(r"[\$,]", "", regex=True).astype(float)

# === 3) Fix categorical issues BEFORE imputation ===
df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??": pd.NA})

# === 4) Impute missing values ===
print("\n--- Imputation Check ---")
print("before Doors:", df["Doors"].isna().sum())
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
print("after Doors:", df["Doors"].isna().sum())

print("before Accidents:", df["Accidents"].isna().sum())
df["Accidents"] = df["Accidents"].fillna(df["Accidents"].mode()[0])
print("after Accidents:", df["Accidents"].isna().sum())

print("before Odometer_km:", df["Odometer_km"].isna().sum())
df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
print("after Odometer_km:", df["Odometer_km"].isna().sum())

print("before Location:", df["Location"].isna().sum())
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])
print("after Location:", df["Location"].isna().sum())

# === 5) Remove duplicates ===
before = df.shape
df = df.drop_duplicates()
after = df.shape
print(f"\nDropped duplicates: {before} → {after}")

# === 6) IQR capping ===


def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper


low_price, high_price = iqr_fun(df["Price"])
low_odo, high_odo = iqr_fun(df["Odometer_km"])

df["Price"] = df["Price"].clip(lower=low_price, upper=high_price)
df["Odometer_km"] = df["Odometer_km"].clip(lower=low_odo, upper=high_odo)

# === 7) One-hot encode ===
df = pd.get_dummies(df, columns=["Location"], drop_first=False, dtype="int")

# === 8) Feature engineering (no leakage) ===
CURRENT_YEAR = 2025
df["CarAge"] = CURRENT_YEAR - df["Year"]
df["Km_per_year"] = df["Odometer_km"] / (df["CarAge"] + 1)
df["Is_Urban"] = (df.get("Location_City", 0) +
                  df.get("Location_Suburb", 0)).clip(0, 1)
df["LogPrice"] = np.log1p(df["Price"])

# === 9) Feature scaling (X only; keep targets & dummies unscaled) ===
dont_scale = {"Price", "LogPrice"}
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()
exclude = [c for c in df.columns if c.startswith("Location_")] + ["Is_Urban"]

num_features_to_scale = [
    c for c in numeric_cols if c not in dont_scale and c not in exclude
]

scaler = StandardScaler()
df[num_features_to_scale] = scaler.fit_transform(df[num_features_to_scale])

# === FINAL SNAPSHOT ===
print("\n=== FINAL HEAD ===")
print(df.head())

print("\n=== FINAL INFO ===")
print(df.info())

print("\n=== FINAL MISSING VALUES ===")
print(df.isnull().sum())

# === 10) Save cleaned dataset ===
OUT_PATH = "car_l3_clean_ready.csv"
df.to_csv(OUT_PATH, index=False)
print(f"\nCleaned dataset saved to {OUT_PATH}")
