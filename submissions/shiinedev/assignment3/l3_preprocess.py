import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

CSV_PATH = "dataset/car_l3_dataset.csv"

df = pd.read_csv(CSV_PATH)


# === INITIAL SNAPSHOT ===
print("\n=== INITIAL HEAD ===")
print(df.head())

print("\n=== INITIAL INFO ===")
print(df.info())

print("\n=== INITIAL MISSING VALUES ===")
print(df.isnull().sum())


# 2) Clean target formatting
df["Price"] = df["Price"].replace(r"[$,]","", regex=True).astype(float)

# 3) Fix categorical issues BEFORE imputation
df["Location"] = df["Location"].replace({"Subrb":"Suburb","??":pd.NA})


# 4) Impute missing values
df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])

# 5) Remove duplicates
# print ("before:",df.shape)
df = df.drop_duplicates()
# print("after",df.shape)


# 6) IQR capping
def iqr_fun(series,k=1.5):
    q1,q3 = series.quantile([0.25,0.75])
    iqr = q3 - q1
    lower = q1 -k * iqr
    upper = q3 + k * iqr
    return lower,upper

low_price,high_price = iqr_fun(df["Price"])
low_Odometer,high_Odometer = iqr_fun(df["Odometer_km"])


df["Price"] = df["Price"].clip(lower=low_price, upper=high_price)
df["Odometer_km"] = df["Odometer_km"].clip(lower=low_Odometer, upper=high_Odometer)

# 7) One-hot encode
df = pd.get_dummies(df,columns=["Location"],drop_first=False,dtype="int")

# 8) Feature engineering (no leakage)
CURRENT_YEAR = 2025

df["CarAge"] = CURRENT_YEAR - df["Year"]
df["Had_Accident"] = df["Accidents"].astype(bool)
df["Accidents_per_year"] =(df["Accidents"] / df["CarAge"]).astype(int)
df["Odometer_per_Year"] = (df["Odometer_km"] / df["CarAge"].replace(0,np.nan)).astype(int)
df["LogPrice"] = np.log1p(df["Odometer_per_Year"])


# 9) Feature scaling (X only; keep targets & dummies unscaled)
dont_scale = {"Price","LogPrice","Had_Accident"}
numeric_columns = df.select_dtypes(include=["int64","float64"]).columns.to_list()
exclude = [c for c in df.columns if c.startswith("Location_")] 
num_feature_scale = [c for c in df.columns if c not in dont_scale and c not in exclude ]

scaler = StandardScaler()
df[num_feature_scale] = scaler.fit_transform(df[num_feature_scale])

# === FINAL SNAPSHOT ===
print("\n=== FINAL HEAD ===")
print(df.head())

print("\n=== FINAL INFO ===")
print(df.info())

print("\n=== FINAL MISSING VALUES ===")
print(df.isnull().sum())

# 10) Save
OUT_PATH = "dataset/car_l3_clean_ready.csv"
df.to_csv(OUT_PATH,index=False)