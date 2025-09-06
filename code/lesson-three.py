import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

CSV_PATH = 'dataset/house_dataset.csv'

df = pd.read_csv(CSV_PATH)

df["Price"] = df["Price"].replace(r"[\$,]", "", regex=True).astype(float)

df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??": pd.NA})

df["Size_sqft"] = df["Size_sqft"].fillna(df["Size_sqft"].median())
df["Bedrooms"] = df["Bedrooms"].fillna(df["Bedrooms"].mode()[0])
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])

bofore = df.shape

df = df.drop_duplicates()

after = df.shape


def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper


low_price, high_price = iqr_fun(df["Price"])
low_size, high_size = iqr_fun(df["Size_sqft"])

df["Price"] = df["Price"].clip(lower=low_price, upper=high_price)
df["Size_sqft"] = df["Size_sqft"].clip(lower=low_size, upper=high_size)

df = pd.get_dummies(df, columns=["Location"], drop_first=False)

loc_cols = [c for c in df.columns if c.startswith("Location")]

df[loc_cols] = df[loc_cols].astype(int)

CURRENT_YEAR = 2025

df["HouseAge"] = CURRENT_YEAR - df["YearBuilt"]

df["Rooms_per_1000sqft"] = (
    df["Bedrooms"] + df["Bathrooms"]) / (df["Size_sqft"] / 1000)

df["Size_per_Bedroom"] = df["Size_sqft"] / df["Bathrooms"].replace(0, np.nan)

df["Is_City"] = df["Location_City"].astype(int)

df["LogPrice"] = np.log1p(df["Price"])

dont_scale = {"Price", "LogPrice"}

numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()

exclude = [c for c in df.columns if c.startswith("Location_")] + ["Is_City"]

num_features_to_scale = [
    c for c in numeric_cols if c not in dont_scale and c not in exclude]

scaler = StandardScaler()

df[num_features_to_scale] = scaler.fit_transform(df[num_features_to_scale])

OUT_PATH = "Housing_Clean.csv"

df.to_csv(OUT_PATH)
