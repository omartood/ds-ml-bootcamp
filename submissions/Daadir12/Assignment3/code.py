import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


CSV_PATH = "car_dataset.csv"

df = pd.read_csv(CSV_PATH)


# print(df.head(10))
# print(df.info)
# print(df.isnull().sum())

# (1) saxitaanka Price waxyaabaha ka qaldan

df["Price"] = df["Price"].replace(r"[\$,]", "", regex=True).astype(float)

# print(df["Price"])
# print(df["Location"].value_counts(dropna=False))

# (2) Saxitaanka Locationka Ereyada Ka qaldan

df["Location"] = df["Location"].replace(
    {"Subrb": "Suburb",
     "city": "City",
     "??": pd.NA})

# print(df["Location"].value_counts(dropna=False))

# (3) Buuxinta waxyaabaha Maqan

df["Price"] = df["Price"].fillna(df["Price"].median())
df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"] = df["Doors"].fillna(df["Doors"].median())
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])

# print(df.isnull().sum())


# (4) Removing dublicate

before = df.shape
df = df.drop_duplicates()
after = df.shape

# print("Before :",  before, "After :", after)


# (5) IQR capping --- Waa qeybkii iigu adkeyd iiguna cilad badneyd----

def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper


low_price, high_price = iqr_fun(df["Price"])
low_Odometer_km,  high_Odometer_km = iqr_fun(df["Odometer_km"])

df["Price"] = df["Price"].clip(lower=low_price, upper=high_price)
df["Odometer_km"] = df["Odometer_km"].clip(
    lower=low_Odometer_km,  upper=high_Odometer_km)

# print("IQR Price is: ")
# print("high_price: ", high_price, "low_price:", low_price)

# print("IQR KiloMeter is: ")
# print("high_Odometer_km: ", high_Odometer_km,
#      "low_Odometer_km:", low_Odometer_km)
# print(df["Price"].describe())
# print(df["Odometer_km"].describe())


# (6) making one-hot encoding

df = pd.get_dummies(df, columns=["Location"], drop_first=False, dtype=int)

# print("One Hot encoding: ")
# print([c for c in df.columns if c.startswith("Location")])
# print(df.head(10))


# (7) feature  Engineering

Current_year = 2025

df["CarYear"] = Current_year - df["Year"]
df["Is_City"] = df["Location_City"].astype(int)
df["LogPrice"] = np.log1p(df["Price"])
# print(df.head(10))


# (8) feature scaling

dont_scale = {"Price", "LogPrice"}
numeric_cols = df.select_dtypes(include=["Int64", "Float64"]).columns.to_list()

exclude = [c for c in df.columns if c.startswith("Location")] + ["Is_City"]
num_features_to_scale = [
    c for c in numeric_cols if c not in dont_scale and c not in exclude]

scaler = StandardScaler()
df[num_features_to_scale] = scaler.fit_transform(df[num_features_to_scale])

# print(df.head)


# (9) save the data --- last step--

OUT_PATH = "data_Clean.csv"

df.to_csv(OUT_PATH, )
print("Data saved: ", OUT_PATH)


# (10)=== FINAL SNAPSHOT ===
print("\n=== FINAL HEAD ===")
print(df.head())

print("\n=== FINAL INFO ===")
print(df.info())

print("\n=== FINAL MISSING VALUES ===")
print(df.isnull().sum())
