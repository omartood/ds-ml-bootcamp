import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

CSV_PATH = 'dataset.csv'
df = pd.read_csv(CSV_PATH)

# === INITIAL SNAPSHOT ===
print("\n=== INITIAL HEAD ===")
print(df.head(10))

print("\n=== INITIAL INFO ===")
print(df.info())

print("\n=== INITIAL MISSING VALUES ===")
print(df.isnull().sum())

# 2) Clean target formatting
df["Price"] = df["Price"].replace(r"[\$,]", "", regex=True).astype(float)
#print(df.head(10))

# 3) Fix categorical issues BEFORE imputation
df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??": pd.NA})
#print(df.head(10))

# 4) Impute missing values
df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"]  = df["Doors"].fillna(df["Doors"].mode()[0])
df["Location"]  = df["Location"].fillna(df["Location"].mode()[0])
print(df.head(10))

# 5) Remove duplicates
before = df.shape
df = df.drop_duplicates()
after = df.shape
print(f"Dropped duplicates: {before} → {after}")

# 6) IQR capping
def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper

# Compute IQR bounds
low_price, high_price = iqr_fun(df["Price"])
low_odo, high_odo     = iqr_fun(df["Odometer_km"])

# Clip (cap) outliers
df["Price"]        = df["Price"].clip(lower=low_price, upper=high_price)
df["Odometer_km"]  = df["Odometer_km"].clip(lower=low_odo, upper=high_odo)

# print summary
print(" Price after IQR capping:")
print(df["Price"].describe())

print("\n Odometer_km after IQR capping:")
print(df["Odometer_km"].describe())

print(f"Price IQR bounds: lower = {low_price}, upper = {high_price}")
print(f"Odometer_km IQR bounds: lower = {low_odo}, upper = {high_odo}")

# 7) One-hot encode
df = pd.get_dummies(df, columns=["Location"], drop_first=False, dtype="int")
print(df.head())

# 8) Feature engineering (no leakage)
CURRENT_YEAR = 2025

# Car age
df["CarAge"] = CURRENT_YEAR - df["Year"]

# Km per year (safe denominator to avoid division by zero)
df["Km_per_year"] = df["Odometer_km"] / df["CarAge"].replace(0, 1)

# Size of accident history as binary flag
df["AccidentFlag"] = (df["Accidents"] > 0).astype(int)

# Urban flag (based on Location_City / Location_Suburb)
df["Is_Urban"] = (
    df.get("Location_City", 0) + df.get("Location_Suburb", 0)
).astype(int)

# Alternative target (not a feature)
df["LogPrice"] = np.log1p(df["Price"])

# 9) Feature scaling (X only; keep targets & dummies unscaled)
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

# 10) Save
OUT_PATH = "car_l3_clean_ready.csv"
df.to_csv(OUT_PATH, index=False)


