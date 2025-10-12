import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# 1 - Load & Inspect Dataset - Car Prices
# === LOAD DATASET FROM CSV FILE
CSV_FILE_PATH = r"D:\Cousers\Data Science & Machine Learning Bootcamp - Beggining\ds-ml-bootcamp\submissions\Ali Omar - Ali Key\Assignment-Three\car_l3_dataset.csv"
df = pd.read_csv(CSV_FILE_PATH)

# === INITIAL SNAPSHOT
print("\n===  INITIAL HEAD:")
print(df.head())

# === INITIAL INFO
print("\n===  INITIAL INFO:")
print(df.info())

# === INITIAL SHAPE
print("\n===  INITIAL SHAPE:")
print(df.shape)

# === INITIAL MISSING VALUES
print("\n===  INITIAL MISSING VALUES:")
print(df.isnull().sum())

# === COUNT UNIQUE VALUES
print("\n===  COUNT UNIQUE VALUES:")
print(df.nunique())

# === LOCATION COUNTS
print("\n===  LOCATION COUNTS:")
print(df["Location"].value_counts(dropna=False))

# # 2 - Clean Target Formatting (Price)  - remove currency/commas; ensure numeric; report dtype and skewness.
df["Price"] = df["Price"].str.replace("[$,]", "", regex=True).astype(float)
print("\n===  PRICE DATATYPE AND SKEWNESS:")
print("Price Datatype:", df["Price"].dtype)
print("Price Skewness:" ,df['Price'].skew())

# 3 - Fix Category Errors before Imputation — normalize Location text, map typos (e.g., Subrb→Suburb), convert unknowns (e.g., “??”) to missing; recount including missing.
df['Location'] =df ["Location"].replace({"Subrb": "Suburb", "??": pd.NA})
print("\n===  LOCATION COUNTS:")
print(df["Location"].value_counts(dropna=False))

# 4 -Impute Missing Values (justify choices) — Odometer_km→median; Doors/Accidents→mode; Location→mode; confirm post-imputation missing counts.
df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
df["Accidents"] = df["Accidents"].fillna(df["Accidents"].mode()[0])
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])

# 5 - Remove Duplicates — report shape before/after and rows removed.
Before = df.shape
df= df.drop_duplicates()
After = df.shape
print(f"\n===  SHAPE BEFORE DROPPING DUPLICATES: {Before}, AFTER: {After}")

# 6 - Outliers (IQR capping) — compute bounds and clip for Price and Odometer_km; show a short summary after capping.
def iqr_function(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper
price_lower, price_upper = iqr_function(df["Price"])
odometer_lower, odometer_upper = iqr_function(df["Odometer_km"])
df["Price"] = df["Price"].clip(price_lower, price_upper)
df["Odometer_km"] = df["Odometer_km"].clip(odometer_lower, odometer_upper)

print("\n===  PRICE AND ODOMETER_KM SUMMARY AFTER CAPPING:")
print(df[["Price", "Odometer_km"]].describe())

# 7 - One-Hot Encode Categorical(s) — encode Location as 0/1 columns; list the new columns created.
df = pd.get_dummies(df, columns=["Location"], drop_first=False, dtype="int")
print("\n===  NEW COLUMNS AFTER ONE-HOT ENCODING LOCATION:")
print([col for col in df.columns if col.startswith("Location_")])

# 8 - Feature Engineering (no leakage) — add at least three sensible features (e.g., CarAge, Km_per_year with safe handling, Is_Urban). Add LogPrice = log(Price+1) as an alternative target (not a feature).
df["CarAge"] = 2024 - df["Year"]
df["Km_per_year"] = df["Odometer_km"] / df["CarAge"].replace(0, 1)  # Avoid division by zero
df["Is_Urban"] = np.where(df[[col for col in df.columns if col.startswith("Location_")]].sum(axis=1) > 0, 1, 0)
df["LogPrice"] = np.log1p(df["Price"])
print("\n===  NEW FEATURES SAMPLE:")
print(df[["CarAge", "Km_per_year", "Is_Urban", "LogPrice"]].head())

# 9 - Feature Scaling (X only) — standardize continuous features; do not scale Price or LogPrice; prefer leaving 0/1 dummies unscaled; show a small sample of scaled values.
scaler = StandardScaler()
df[["Odometer_km", "CarAge", "Km_per_year"]] = scaler.fit_transform(df[["Odometer_km", "CarAge", "Km_per_year"]])
print("\n===  SCALED FEATURES SAMPLE:")
print(df[["Odometer_km", "CarAge", "Km_per_year"]].head())

# +10 -Final Checks & Save — final info, missing counts (all zero), a small describe table; save to car_l3_clean_ready.csv.
print("\n===  FINAL HEAD:")
print(df.head())

print("\n===  FINAL INFO:")
print(df.info())

print("\n===  FINAL MISSING VALUES:")
print(df.isnull().sum())

print("\n===  FINAL DESCRIBE:")
print(df.describe())

OUT_PATH = 'car_l3_clean_ready.csv'
df.to_csv(OUT_PATH, index=False)
print(f"\nCleaned dataset saved to {OUT_PATH}")
