import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

CVS_PATH = '../../../dataset/car_l3_dataset.csv'
df = pd.read_csv(CVS_PATH);


# === INITIAL SNAPSHOT ===
# print("=== INITIAL SNAPSHOT ===")
# print(df.head(10));

# print("\n=== INITIAL SHAPE ===")
# print(df.shape);

# print("\n=== INITIAL INFO ===")
# print(df.info());

# print("\n=== Location value counts ===")
# print(df['Location'].value_counts());

# print("\n=== INITIAL MISSING VALUES ===")
# print(df.isnull().sum());

# 2. Cleanning the price formating and removing the commas and the $ signs
# print(df['Price'].head(10));
df['Price'] = df['Price'].str.replace(',', '').str.replace('$', '').astype(float);
# print(df['Price'].head(10));


# 3. Fix Category Errors before Imputation - normalize Location text, map typos (e.g., Subrb→Suburb), convert unknowns (e.g., “??”) to missing
df['Location'] = df['Location'].replace({'Subrb': 'Suburb', '??': np.nan, 'N/A': np.nan})
# print(df['Location'].value_counts());

# 4. Impute Missing Values
df['Location'] = df['Location'].fillna(df['Location'].mode()[0])
df['Odometer_km'] = df['Odometer_km'].fillna(df['Odometer_km'].median())
df['Year'] = df['Year'].fillna(df['Year'].median())
df['Accidents'] = df['Accidents'].fillna(df['Accidents'].mode()[0])
df['Doors'] = df['Doors'].fillna(df['Doors'].mode()[0])

# print("\n=== MISSING VALUES AFTER IMPUTATION ===")
# print(df.isnull().sum());

# 5. Remove Duplicates
df = df.drop_duplicates()
# print("\n=== SHAPE AFTER REMOVING DUPLICATES ===")
# print(df.shape);

# 6. Outliers (IQR capping) compute bounds and clip for Price and Odometer_km; show a short summary after capping.

def IQR_capping(series, k=1.5):
    q1, q3 = series.quantile([0.25,0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper


lower_bound_price, upper_bound_price = IQR_capping(df['Price'])
lower_bound_Odometer_km , upper_bound_Odometer_km = IQR_capping(df['Odometer_km']) 

# 7.  One-hot encode
df = pd.get_dummies(df, columns=["Location"], drop_first=False, dtype="int");

# 8. Feature Engineering (no leakage) add at least three sensible features (e.g., CarAge, Km_per_year with safe handling, Is_Urban). Add LogPrice = log(Price+1) as an alternative target (not a feature).
df['CarAge'] = 2024 - df['Year']
df['Km_per_year'] = df['Odometer_km'] / df['CarAge'].replace(0, 1)  # Avoid division by zero
df['Is_Urban'] = df[[col for col in df.columns if col.startswith('Location_')]].sum(axis=1).apply(lambda x: 1 if x > 0 else 0)
df['LogPrice'] = np.log1p(df['Price'])
df['NewAccidents'] = df['Accidents'].apply(lambda x: 1 if x > 0 else 0)

# 9. Feature Scaling (X only) — standardize continuous features; do not scale Price or LogPrice; prefer leaving 0/1 dummies unscaled; show a small sample of scaled values.
dont_scale = {"Price", "LogPrice"}
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()
exclude = [c for c in df.columns if c.startswith("Location_")] + ["Is_Urban"]
num_features_to_scale = [c for c in numeric_cols if c not in dont_scale and c not in exclude]

scaler = StandardScaler()
df[num_features_to_scale] = scaler.fit_transform(df[num_features_to_scale])

# 10. Final Checks & Save — final info, missing counts (all zero), a small describe table; save to car_l3_clean_ready.csv.
# print("\n=== FINAL INFO ===")
# print(df.info());
# print("\n=== FINAL MISSING VALUES ===")
# print(df.isnull().sum());
# print("\n=== FINAL DESCRIBE ===")
# print(df.describe().T);

df.to_csv('car_l3_clean_ready.csv', index=False)
# print("\n=== CLEANED DATA SAVED TO car_l3_clean_ready.csv ===")

