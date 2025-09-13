import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# ---------------- Step 1: Load & Inspect ----------------
df = pd.read_csv("car_l3_dataset.csv")

print("=== Step 1: Load & Inspect ===")
print(df.head(10))
print("\nShape:", df.shape)
print("\nInfo:")
print(df.info())
print("\nMissing counts:")
print(df.isnull().sum())
print("\nLocation value counts (including NaN):")
print(df['Location'].value_counts(dropna=False))

# ---------------- Step 2: Clean Target Formatting ----------------
df['Price'] = df['Price'].replace('[\$,]', '', regex=True).astype(float)
print("\n=== Step 2: Clean Price ===")
print("Price dtype:", df['Price'].dtype)
print("Price skewness:", df['Price'].skew())

# ---------------- Step 3: Fix Category Errors before Imputation ----------------
df['Location'] = df['Location'].str.strip().str.title()
df['Location'] = df['Location'].replace({
    "Subrb": "Suburb",
    "??": np.nan
})
print("\n=== Step 3: Location cleanup ===")
print(df['Location'].value_counts(dropna=False))

# ---------------- Step 4: Impute Missing Values ----------------
df['Odometer_km'] = df['Odometer_km'].fillna(df['Odometer_km'].median())
for col in ['Doors', 'Accidents', 'Location']:
    df[col] = df[col].fillna(df[col].mode()[0])
print("\n=== Step 4: After Imputation ===")
print(df.isnull().sum())

# ---------------- Step 5: Remove Duplicates ----------------
before = df.shape[0]
df = df.drop_duplicates()
after = df.shape[0]
print("\n=== Step 5: Remove Duplicates ===")
print(f"Removed {before - after} duplicate rows.")

# ---------------- Step 6: Outliers (IQR capping) ----------------
for col in ['Price', 'Odometer_km']:
    Q1, Q3 = df[col].quantile([0.25, 0.75])
    IQR = Q3 - Q1
    lower, upper = Q1 - 1.5*IQR, Q3 + 1.5*IQR
    df[col] = df[col].clip(lower, upper)
print("\n=== Step 6: After Outlier Capping ===")
print(df[['Price', 'Odometer_km']].describe())

# ---------------- Step 7: One-Hot Encode Categorical(s) ----------------
df = pd.get_dummies(df, columns=['Location'], drop_first=False)
print("\n=== Step 7: One-Hot Encoding ===")
print("New columns:", [c for c in df.columns if "Location_" in c])

# ---------------- Step 8: Feature Engineering ----------------
df['CarAge'] = 2025 - df['Year']
df['Km_per_year'] = df['Odometer_km'] / (df['CarAge'] + 1)  # avoid div by 0
df['Is_Urban'] = df.filter(like="Location_").idxmax(axis=1).apply(lambda x: 1 if "City" in x else 0)
df['LogPrice'] = np.log1p(df['Price'])
print("\n=== Step 8: Feature Engineering ===")
print(df[['CarAge', 'Km_per_year', 'Is_Urban', 'LogPrice']].head())

# ---------------- Step 9: Feature Scaling ----------------
scaler = StandardScaler()
cont_cols = ['Odometer_km', 'CarAge', 'Km_per_year']
df[cont_cols] = scaler.fit_transform(df[cont_cols])
print("\n=== Step 9: Scaled Features (sample) ===")
print(df[cont_cols].head())

# ---------------- Step 10: Final Checks & Save ----------------
print("\n=== Step 10: Final Checks ===")
print(df.info())
print("Missing counts:\n", df.isnull().sum())
print(df.describe().T.head())

df.to_csv("car_l3_clean_ready.csv", index=False)
print("\nSaved cleaned dataset to car_l3_clean_ready.csv")
