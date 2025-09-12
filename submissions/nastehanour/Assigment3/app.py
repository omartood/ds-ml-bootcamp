import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

CSV_PATH = "car_l3_dataset.csv"
df = pd.read_csv(CSV_PATH)

# 1. Load & Inspect
print("First 10 rows (10):")
print(df.head(10))
print(" shape:", df.shape)
print(" info:")
print(df.info())
print("missing values:")
print(df.isnull().sum())
print(" Location counts:")
print(df["Location"].value_counts(dropna=False))

# 2. Clean Target Formatting (Price)
df["Price"] = df["Price"].replace(r"[\$,]", "", regex=True).astype(float)
print("Price datatype and skewness after cleaning:")
print("Price dtype:", df["Price"].dtype, "Price skewness:", df["Price"].skew())

# 3. Fix Category Errors before Imputation
df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??": pd.NA})
print("Location counts after fix:")
print(df["Location"].value_counts(dropna=False))

# 4. Impute Missing Values
df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
df["Accidents"] = df["Accidents"].fillna(df["Accidents"].mode()[0])
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])
print("Missing values after impute:")
print(df.isnull().sum())

# 5. Remove Duplicates
before = df.shape
df = df.drop_duplicates()
after = df.shape
print("Duplicates removed:", before, "to", after)

# 6. Outliers (IQR capping)
def iqr_bounds(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper

# Compute bounds
low_price, high_price = iqr_bounds(df["Price"])
low_odometer, high_odometer = iqr_bounds(df["Odometer_km"])

# Clip outliers
df["Price"] = df["Price"].clip(lower=low_price, upper=high_price)
df["Odometer_km"] = df["Odometer_km"].clip(lower=low_odometer, upper=high_odometer)

print("Price and Odometer summary after capping:")
print(df[["Price", "Odometer_km"]].describe())

# 7. One-Hot Encode Categorical(s)
df = pd.get_dummies(df, columns=["Location"], drop_first=False, dtype="int")
print("Location columns after encoding:", [col for col in df.columns if col.startswith("Location_")])


# 8. Feature Engineering
CURRENT_YEAR = 2025
df["CarAge"]        = CURRENT_YEAR - df["Year"]
df["Km_per_year"]   = df["Odometer_km"] / df["CarAge"].replace(0, np.nan)
df["Accident_Rate"] = df["Accidents"] / df["CarAge"].replace(0, np.nan)
df["Is_OldCar"]     = (df["CarAge"] > 15).astype(int)
df["Accident_Flag"] = (df["Accidents"] > 0).astype(int)
df["Price_per_Age"] = df["Price"] / df["CarAge"].replace(0, np.nan)
df["Is_FamilyCar"]  = (df["Doors"] >= 4).astype(int)
df["LogPrice"] = np.log1p(df["Price"])



# Print sample
print("Sample engineered features:\n", df[[
    "CarAge","Km_per_year","Accident_Rate","Is_OldCar",
    "LogPrice","Accident_Flag","Price_per_Age","Is_FamilyCar"
]].head())



# 9. Feature Scaling (X only keep targets & dummies unscaled)
dont_scale = {"Price", "LogPrice"}
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()
exclude = [c for c in df.columns if c.startswith("Location_")] + ["Accident_Flag"] + ["Price_per_Age"] + ["Is_FamilyCar"]
num_features_to_scale = [c for c in numeric_cols if c not in dont_scale and c not in exclude]
scaler = StandardScaler()
df[num_features_to_scale] = scaler.fit_transform(df[num_features_to_scale])
print("sample scaled:")
print(df[num_features_to_scale].head())

# 10. Final Checks & Save
print("Final info:")
print(df.info())
print("Final missing values:")
print(df.isnull().sum())
print("Final describe:")
print(df.describe())

OUT_PATH = 'car_l3_clean_ready.csv'
df.to_csv(OUT_PATH, index=False)
print("Cleaned dataset saved to", OUT_PATH)
