import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

CSV_PATH = 'submissions/khadracajeb/Assignment3/car_data.csv'
df = pd.read_csv(CSV_PATH)

print("\n=== INITIAL HEAD ===")
print(df.head())

print("\n=== INFO ===")
print(df.info())

print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

# 2) $1,5000 --- 1500.0 removes $ and ,
df["Price"] = df["Price"].replace(r"[\$,]", "", regex=True).astype(float)


# 3) Fix categorical issues BEFORE imputation
df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??": pd.NA})

# 4) buuxin qimaashaya maqan e 3 feuters iyo float to int
df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median()).astype(int)
df["Doors"] = df["Doors"].fillna(df["Doors"].median()).astype(int)
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])

# 5) saarista kuwa soo noqnoqday
before = df.shape
df = df.drop_duplicates()
after = df.shape
print(f"Dropped duplicates: {before} -> {after}")

# ka hor IQR min and max of price and Odometer_km
print("\n before clip cheching price and odometer")
print(df["Price"].min(), df["Price"].max())
print(df["Odometer_km"].min(), df["Odometer_km"].max())

# === 6) IQR capping for Price and Odometer_km ===
def iqr_fun(series, k=1.5):
    """Calculate lower and upper bounds using IQR."""
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper

# Compute bounds
low_price, high_price = iqr_fun(df["Price"])
low_odo, high_odo   = iqr_fun(df["Odometer_km"])

# Apply capping (clip)
df["Price"]= df["Price"].clip(lower=low_price, upper=high_price)
df["Odometer_km"] = df["Odometer_km"].clip(lower=low_odo, upper=high_odo)

#after cheching 
print("\n after clip cheching price and odometer")
print(df["Price"].min(), df["Price"].max())
print(df["Odometer_km"].min(), df["Odometer_km"].max())

# 7) One-hot encode
df = pd.get_dummies(df, columns=["Location"], drop_first=False, dtype="int")
print(df.columns)


# 8) Feature engineering
CURRENT_YEAR = 2025
# intee sano uu jiro gaarigu
df["CarAge"] = CURRENT_YEAR - df["Year"]
# yareenta outliers 
df["LogPrice"] = np.log1p(df["Price"])
# shilal sanadkiiba
df["Accidents_per_Year"] = df["Accidents"] / df["CarAge"].replace(0, np.nan)
# celceliska km sanadkiiba
df["Km_per_Year"] = df["Odometer_km"] / df["CarAge"].replace(0, np.nan)
#mesha gariga laga ibsaday
df["Is_City"] = df["Location_City"].astype(int)



# 9) Feature scaling
# lama scale gareyn doono Price and LogPrice
dont_scale = {"Price", "LogPrice"}
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()

# Ka reebis dummies iyo binary location iyo is-city
exclude = [c for c in df.columns if c.startswith("Location_")] + ["Is_City"]

# Features numbers ka scale dheh
num_features_to_scale = [c for c in numeric_cols if c not in dont_scale and c not in exclude]

# ku dabaqittaan 
scaler = StandardScaler()
df[num_features_to_scale] = scaler.fit_transform(df[num_features_to_scale])


# dhamaad iyo so bandhigida
print("\n=== shanta u horeysa  ===")
print(df.head())

print("\n=== xogtooda===")
print(df.info())

print("\n=== dhamaan meelaha labuuxiyey ===")
print(df.isnull().sum())

# 10) Save
OUT_PATH = "submissions/khadracajeb/Assignment3/car_l3_clean_ready.csv"
df.to_csv(OUT_PATH, index=False)