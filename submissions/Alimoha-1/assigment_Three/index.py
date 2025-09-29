import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

CSV_PATH = "car_data.csv"
df = pd.read_csv(CSV_PATH)

print("\n=== INITIAL HEAD ===")
print(df.head())

print("\n=== INITIAL INFO ===")
print(df.info())

print("\n=== INITIAL MISSING VALUES ===")
print(df.isnull().sum())


df["Price"] = df["Price"].replace(r"[\$,]", "", regex=True).astype(float)


df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??": pd.NA})

df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"]       = df["Doors"].fillna(df["Doors"].mode()[0])
df["Accidents"]   = df["Accidents"].fillna(df["Accidents"].mode()[0])
df["Location"]    = df["Location"].fillna(df["Location"].mode()[0])

before = df.shape
df = df.drop_duplicates()
after = df.shape


def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper

low_price, high_price = iqr_fun(df["Price"])
low_odo,   high_odo   = iqr_fun(df["Odometer_km"])

df["Price"]       = df["Price"].clip(lower=low_price, upper=high_price)
df["Odometer_km"] = df["Odometer_km"].clip(lower=low_odo, upper=high_odo)

df = pd.get_dummies(df, columns=["Location"], drop_first=False, dtype="int")


CURRENT_YEAR = 2025
df["CarAge"] = CURRENT_YEAR - df["Year"]
df["Is_City"] = df.get("Location_City", pd.Series([0]*len(df))).astype(int)
df["LogPrice"] = np.log1p(df["Price"])

dont_scale = {"Price", "LogPrice"}
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()
exclude = [c for c in df.columns if c.startswith("Location_")] + ["Is_City"]
num_features_to_scale = [c for c in numeric_cols if c not in dont_scale and c not in exclude]

scaler = StandardScaler()
df[num_features_to_scale] = scaler.fit_transform(df[num_features_to_scale])

print("\n=== FINAL HEAD ===")
print(df.head())

print("\n=== FINAL INFO ===")
print(df.info())

print("\n=== FINAL MISSING VALUES ===")
print(df.isnull().sum())

OUT_PATH = "Cars_Clean.csv"
df.to_csv(OUT_PATH, index=False)
print(f"\nCleaned dataset saved to: {OUT_PATH}")
