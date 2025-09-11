import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# CSV_PATH = 'car_l3_dataset.csv' /* wuu iishaqayn waayey pathkan */
# df= pd.read_csv(CSV_PATH)
df = pd.read_csv("C:/Users/MyLearning/Desktop/ds-ml-bootcamp/submissions/Sofia-Asad/Assignment3/car_13_dataset.csv")


# print(df.head(10))
# print(df.shape)
# print(df.info())


# print("initial missing values")
# print(df.isnull().sum())


df["Price"] = df["Price"].replace(r"[$,]", "", regex=True).astype(float)
# print(df.head(10))

# print(df["Location"].value_counts(dropna=False))

df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??": pd.NA})


df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"]  = df["Doors"].fillna(df["Doors"].mode()[0])
df["Location"]  = df["Location"].fillna(df["Location"].mode()[0])
# print(df.head(20))

before = df.shape
df = df.drop_duplicates()
after = df.shape

def iqrr(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper

low_price, high_price = iqrr(df["Price"])
low_Odometer_km,  high_Odometer_km  = iqrr(df["Odometer_km"])

df["Price"]     = df["Price"].clip(lower=low_price, upper=high_price)
df["Odometer_km"] = df["Odometer_km"].clip(lower=low_Odometer_km,  upper=high_Odometer_km)

# print("IQR of Price")
# print("low_price: ", low_price, "high_price: ", high_price)
# print("IQR of Odometer_km")
# print("low_Odometer_km: ", low_Odometer_km, "high_Odometer_km: ", high_Odometer_km)


df = pd.get_dummies(df, columns=["Location"], drop_first=False, dtype="int")
# print(df.head())

CURRENT_YEAR = 2025
df["CarAge"] = CURRENT_YEAR - df["Year"]
df["Km_per_year"] = df["Odometer_km"] / df["Year"].replace(0, np.nan) 
df["Is_Rural"] = df["Location_Rural"].astype(int)
df["LogPrice"] = np.log1p(df["Price"])
# print("After Price log: ")



dont_scale = {"Price", "LogPrice"}
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()
exclude = [c for c in df.columns if c.startswith("Location_")] + ["Is_Rural"]
number_features_to_scale = [c for c in numeric_cols if c not in dont_scale and c not in exclude]

scale = StandardScaler()

df[number_features_to_scale] = scale.fit_transform(df[number_features_to_scale])



# print(df.head())
# print(df.info())
# print(df.isnull().sum())

OUT_PATH = "car_l3_clean_ready.csv."
df.to_csv(OUT_PATH, index=False)

