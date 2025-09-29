# Import libraries
import pandas as pd
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

# Path to the dataset
PATH = "car_l3_clean.dataset.csv"

# Load CSV into a DataFrame
df = pd.read_csv(PATH)

# Initial inspection (commented out)
# print(df.head())
# print(df.info())
# print(df.isnull().sum())

# -------------------------------
# Step 1: Clean Price column
# Remove $ and commas, convert to float
df["Price"] = df["Price"].replace(r"[\$,]", "", regex=True).astype(float)

# -------------------------------
# Step 2: Handle missing values in categorical columns
# Replace 'Unknown' locations with mode
mode_location = df["Location"].mode()[0]
df["Location"] = df["Location"].replace("Unknown", mode_location)

# Fill missing Doors with the mode (most frequent value)
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])

# Fill missing Odometer_km with the median
median_odometer = df['Odometer_km'].median()
df['Odometer_km'] = df['Odometer_km'].fillna(median_odometer)

# -------------------------------
# Step 3: Remove duplicate rows
before = df.shape
df = df.drop_duplicates()
after = df.shape
# print("Before ", before, "after ", after)

# -------------------------------
# Step 4: Outlier handling using IQR capping
def iqr_fun(series, k=1.5):
    """
    Returns lower and upper bounds for outlier capping
    using the IQR method.
    """
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper

# Compute IQR bounds
low_price, high_price = iqr_fun(df["Price"])
low_Odometer_km, high_Odometer_km = iqr_fun(df["Odometer_km"])

# Clip values outside IQR bounds
df["Price"] = df["Price"].clip(lower=low_price, upper=high_price)
df["Odometer_km"] = df["Odometer_km"].clip(lower=low_Odometer_km, upper=high_Odometer_km)

# -------------------------------
# Step 5: One-hot encode categorical Location
# Remove leading/trailing spaces
df['Location'] = df['Location'].astype(str).str.strip()

# Create dummy columns for each Location category
df = pd.get_dummies(df, columns=['Location'], drop_first=False).astype(int)

# -------------------------------
# Step 6: Feature Engineering (no leakage)
CURRENT_YEAR = 2025

# Car age in years
df['Car_Age'] = CURRENT_YEAR - df['Year']

# Price per km
df['Price_per_km'] = df['Price'] / df['Odometer_km']

# Log transformation of Price (alternative target)
df["LogPrice"] = np.log1p(df["Price"])

# Binary flags for high/low price
df["High_Price"] = (df["Price"] > df["Price"].median()).astype(int)
df["Low_Price"] = (df["Price"] < df["Price"].median()).astype(int)

# Kilometers driven per year
df["Km_per_Year"] = df["Odometer_km"] / df["Car_Age"]

# Price relative to car age
df["Price_per_Age"] = df["Price"] / df["Car_Age"]

# -------------------------------
# Step 7: Feature Scaling (X only)
dont_scale = {"Price", "LogPrice"}  # Exclude targets
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()
exclude = [c for c in df.columns if c.startswith("Location_")]  # Exclude dummy columns
num_features_to_scale = [c for c in numeric_cols if c not in dont_scale and c not in exclude]

# Standardize numeric features
scaler = StandardScaler()
df[num_features_to_scale] = scaler.fit_transform(df[num_features_to_scale])

# -------------------------------
# Step 8: Final inspection
print("\n=== FINAL HEAD ===")
print(df.head())

print("\n=== FINAL INFO ===")
print(df.info())

print("\n=== FINAL MISSING VALUES ===")
print(df.isnull().sum())

# -------------------------------
# Step 9: Save cleaned dataset
OUT_PATH = "car_l3_clean_ready.csv"
df.to_csv(OUT_PATH, index=False)
