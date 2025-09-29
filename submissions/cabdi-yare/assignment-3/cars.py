import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

CSV_PATH = "car_l3_dataset.csv" 
df = pd.read_csv(CSV_PATH)

# === INITIAL SNAPSHOT ===
print("\n=== INITIAL HEAD ===")
print(df.head(10))
print("\n=== SHAPE ===", df.shape)
print("\n=== INFO ===")
print(df.info())
print("\n=== MISSING VALUES ===")
print(df.isnull().sum())
print("\n=== LOCATION VALUE COUNTS ===")
print(df["Location"].value_counts(dropna=False))

# 2) Clean target formatting (Price)
df["Price"] = df["Price"].replace(r"[\$,]", "", regex=True).astype(float)
print("\nPrice dtype:", df["Price"].dtype, "Skew:", df["Price"].skew())

# 3) Fix categorical issues BEFORE imputation
df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??": pd.NA})
print("\nLocation counts after normalization:")
print(df["Location"].value_counts(dropna=False))

# 4) Impute missing values
df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"]       = df["Doors"].fillna(df["Doors"].mode()[0])
df["Accidents"]   = df["Accidents"].fillna(df["Accidents"].mode()[0])
df["Location"]    = df["Location"].fillna(df["Location"].mode()[0])

print("\nMissing after imputation:")
print(df.isnull().sum())

# 5) Remove duplicates
before = df.shape
df = df.drop_duplicates()
after = df.shape
print(f"\nDropped duplicates: {before} → {after}")

# 6) Outliers (IQR capping)
def iqr_cap(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return series.clip(lower, upper)

df["Price"] = iqr_cap(df["Price"])
df["Odometer_km"] = iqr_cap(df["Odometer_km"])

# 7) One-hot encode Location
df = pd.get_dummies(df, columns=["Location"], drop_first=False, dtype=int)
print("\nColumns after one-hot encoding:", df.columns)

# 8) Feature engineering 
CURRENT_YEAR = 2025
df["CarAge"] = CURRENT_YEAR - df["Year"]
df["Km_per_year"] = df["Odometer_km"] / df["CarAge"].replace(0, np.nan)
df["Is_Urban"] = df["Location_City"].astype(int) 
df["LogPrice"] = np.log1p(df["Price"])

# 9) Feature scaling 
dont_scale = {"Price", "LogPrice"}
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()
exclude = [c for c in df.columns if c.startswith("Location_")] + ["Is_Urban"]
num_features_to_scale = [c for c in numeric_cols if c not in dont_scale and c not in exclude]

scaler = StandardScaler()
df[num_features_to_scale] = scaler.fit_transform(df[num_features_to_scale])

# === FINAL SNAPSHOT ===
print("\n=== FINAL HEAD ===")
print(df.head())
print("\n=== FINAL INFO ===")
print(df.info())
print("\n=== FINAL MISSING VALUES ===")
print(df.isnull().sum())

# 10) Save cleaned dataset
OUT_PATH = "car_l3_clean.csv"
df.to_csv(OUT_PATH, index=False)
print(f"\nCleaned dataset saved to {OUT_PATH}")