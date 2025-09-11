import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# 1)Load the dataset
CSV_FILE_PATH = 'Car.csv'
df= pd.read_csv(CSV_FILE_PATH)

# === INITIAL SNAPSHOT ===
print("\n=== INITIAL HEAD ===")
print(df.head())

print("\n=== INITIAL INFO ===")
print(df.info())

print("\n=== INITIAL MISSING VALUES ===")
print(df.isnull().sum())

# 2)cleaning the price
df['Price']=df['Price'].replace(r"[\$,]","",regex=True).astype(float)
# fixing the location
df['Location']=df['Location'].replace({"Suburb":"Subrb", "??": pd.NA})


# 3)filling missing values
df['Odometer_km']=df['Odometer_km'].fillna(df['Odometer_km'].median())
df['Doors']=df['Doors'].fillna(df['Doors'].mode()[0])
df['Location']=df['Location'].fillna(df['Location'].mode()[0])

# 4)Removing duplicates
before_dedup_shape = df.shape
df = df.drop_duplicates()
after_dedup_shape = df.shape

# 5)IQR capping for Price
def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper

low_price, high_price = iqr_fun(df["Price"])
low_size,  high_size  = iqr_fun(df["Odometer_km"])

df["Price"] = df["Price"].clip(lower=low_price, upper=high_price)
df["Odometer_km"] = df["Odometer_km"].clip(lower=low_size,  upper=high_size)

# 6)One-hot encode
df=pd.get_dummies(df, columns=["Location"], drop_first=False, dtype="int")

# 7)Feature engineering 
curent_year=2025
df["Year"]=curent_year - df["Year"]
df["Price_per_km"] = df["Price"] / df["Odometer_km"].replace(0, np.nan)
df["Had_Accident"] = (df["Accidents"] > 0).astype(int)
df["Small_Car"] = (df["Doors"] <= 3).astype(int)
df["Medium_Car"] = (df["Doors"] == 4).astype(int)
df["Large_Car"] = (df["Doors"] >= 5).astype(int)
df["Is_City"] = df["Location_City"].astype(int)
df["LogPrice"] = np.log1p(df["Price"])

# 8)Feature scaling 
dont_scale = {"Price", "LogPrice"}
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()
exclude = [c for c in df.columns if c.startswith("Location_")] + ["Is_City"]
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


# 9) Save
OUT_PATH = "Car_Clean.csv"
df.to_csv(OUT_PATH, index=False)


# summary of we did
# 1)Load the dataset
# 2)cleaning the price
# 3)filling missing values
# 4)Removing duplicates
# 5)IQR capping for Price
# 6)One-hot encode
# 7)Feature engineering
# 8)Feature scaling
# 9) Save