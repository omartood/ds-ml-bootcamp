import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

CSV_PATH = '../../../../dataset/car_l3_dataset.csv'
df = pd.read_csv(CSV_PATH)

df['Price'] = df['Price'].replace(r'[\$,]', '', regex=True).astype(float)
df['Location'] = df['Location'].replace({'Subrb': 'Suburb', '??': pd.NA})
df['Odometer_km'] = df['Odometer_km'].fillna(df['Odometer_km'].median())
df['Doors'] = df['Doors'].fillna(df['Doors'].mode()[0])


df.drop_duplicates(inplace=True)

def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper

low_price, high_price = iqr_fun(df["Price"])
low_Odometer,  high_Odometer = iqr_fun(df["Odometer_km"])

df['Price'] = df['Price'].clip(lower=low_price, upper=high_price)
df['Odometer_km'] = df['Odometer_km'].clip(lower=low_Odometer, upper=high_Odometer)

YEAR = 2025

df['CarAge'] = YEAR - df['Year']
df = pd.get_dummies(df, columns=["Location"], drop_first=False, dtype="int")
df["Is_Cheap"] = np.where(df["Price"] <= 2000, 1, 0)
df["Mileage_per_Year"] = df["Odometer_km"] / df["CarAge"]
df["High_Accident_Risk"] = np.where(df["Accidents"] >= 2, 1, 0)
# df["High_Accident_Risk"] = (df["Accidents"] >= 2).astype(int) 

dont_scale = {"Price", "is_Cheap"}
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()
exclude = [c for c in df.columns if c.startswith("Location_")] + ["mileage_per_year", "high_accident_risk"]
num_features_to_scale = [c for c in numeric_cols if c not in dont_scale and c not in exclude]

scaler = StandardScaler()
df[num_features_to_scale] = scaler.fit_transform(df[num_features_to_scale])

OUT_PATH = 'Caring_cleared.csv'
df.to_csv(OUT_PATH, index=False)