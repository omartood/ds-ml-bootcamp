import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


CSV_PATH = 'assignment3/car_l3_dataset.csv'
df = pd.read_csv(CSV_PATH)

# INITIAL SNAPSHOT
# print('\n ==intial head==')
# print(df.head(50))

# print('\n ==intial info==')
# print(df.info)

# print('\n ==intial missing value==')
# print(df.isnull().sum())

# 2) Clean target formating
df['Price'] = df['Price'].replace(r"[\$,]", "", regex=True).astype(float)
# print(df.isnull().sum())


# 3) fix categorial issues before imputation
df['Location'] = df['Location'].replace(
    {"Subrb": "Suburb", "??": pd.NA})
# print(df.isnull().sum())
# print(df.info())

# 4) impute missing values
df['Odometer_km'] = df['Odometer_km'].fillna(df['Odometer_km'].median())
df['Doors'] = df['Doors'].fillna(df['Doors'].mode()[0])
df['Location'] = df['Location'].fillna(df['Location'].mode()[0])
# print(df.info())
# print(df.isnull().sum())

# 5) remove duplicate
before = df.shape
df = df.drop_duplicates()
after = df.shape
# print("before: ", before, "->", "after: ", after)

# 6)IQR Capping


def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3-q1
    lower = q1-k*iqr
    upper = q3+k*iqr
    return lower, upper


low_price, high_price = iqr_fun(df['Price'])
low_odo_km, high_odo_km = iqr_fun(df["Odometer_km"])
# print('IQR PRICE: ')
# print('low_price: ', low_price, 'high_price: ', high_price)
# print('low_odo_km: ', low_odo_km, 'high_odo_km: ', high_odo_km)

df['Price'] = df['Price'].clip(lower=low_price, upper=high_price)
df['Odometer_km'] = df['Odometer_km'].clip(lower=low_odo_km, upper=high_odo_km)
# print('PRICE AFTER IQR CLIPPING: ')
# print(df['Price'].describe())
# print(df['Odometer_km'].describe())


# 7)one-hot encode
df = pd.get_dummies(df, columns=['Location'], drop_first=False, dtype=int)
# print('Hot encoded: ')
# # print(df.head(10))
# print([c for c in df.columns if c.startswith('Location')])

# 8)Feature engineering

CURRENT_YEAR = 2025
df["CarAge"] = CURRENT_YEAR - df["Year"]
df["Mileage_per_Year"] = df["Odometer_km"] / df["CarAge"].replace(0, np.nan)
df["IsAccident"] = np.where(df["Accidents"] >= 1, 1, 0)
df["Is_FamilyCar"] = (df["Doors"] >= 4).astype(int)
df['LogPrice'] = np.log1p(df['Price'])
# print(df.head(10))

# 8) Feature Scaling( X only: keeping target, dummies unscaled)

dont_scale = {'Price', 'LogPrice'}
numeric_col = df.select_dtypes(include=['int64', 'float64']).columns.to_list()
exclude = [c for c in df.columns if c.startswith('Location')] + ['IsAccident']
num_features_to_scale = [
    c for c in numeric_col if c not in dont_scale and c not in exclude]

scaler = StandardScaler()
df[num_features_to_scale] = scaler.fit_transform(df[num_features_to_scale])

# === FINAL SNAPSHOT ===
print("\n=== FINAL HEAD ===")
print(df.head())

print("\n=== FINAL INFO ===")
print(df.info())

print("\n=== FINAL MISSING VALUES ===")
print(df.isnull().sum())

# 10) save cleaned data

OUT_PATH = 'assignment3/car_l3_dataset_Clean.csv'
df.to_csv(OUT_PATH, index=False)
print(f'\n clean dataset saved to {OUT_PATH}')
