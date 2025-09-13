import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load the car dataset from CSV
CSV_PATH = 'dataset/car_l3_dataset.csv'
df = pd.read_csv(CSV_PATH)

# Clean categorical values in 'Location' (fix typos and missing)
df["Location"] = df["Location"].replace({"Subrb": "Suburb" , "??" : pd.NA})

# Clean and convert 'Price' column to float
df["Price"] = df["Price"].replace({"\$": "", ",": ""}, regex=True).astype(float)

# Impute missing values for numeric and categorical columns
df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
df["Location"]  = df["Location"].fillna(df["Location"].mode()[0])

# Remove duplicate rows from the dataset
df = df.drop_duplicates()

# Define IQR capping function and apply to 'Price' and 'Odometer_km'
def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper

low_price, high_price = iqr_fun(df["Price"])
low_size,  high_size  = iqr_fun(df["Odometer_km"])

df["Price"]     = df["Price"].clip(lower=low_price, upper=high_price)
df["Odometer_km"] = df["Odometer_km"].clip(lower=low_size,  upper=high_size)

# One-hot encode the 'Location' column
df = pd.get_dummies(df, columns=["Location"], drop_first=False, dtype="int")

# Feature engineering: create new features
CURRENT_YEAR = 2025
df["CarAge"] = CURRENT_YEAR - df["Year"]
if "Location_City" in df.columns:
    df["Is_City"] = df["Location_City"].astype(int)
df["LogPrice"] = np.log1p(df["Price"])
df["Accidents_per_year"] = df["Accidents"] / df["CarAge"].replace(0, np.nan)

# Feature scaling: scale numeric features except targets and dummies
dont_scale = {"Price", "LogPrice"}
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()
exclude = [c for c in df.columns if c.startswith("Location_")] + ["Is_City"]
num_features_to_scale = [c for c in numeric_cols if c not in dont_scale and c not in exclude]

scaler = StandardScaler()
df[num_features_to_scale] = scaler.fit_transform(df[num_features_to_scale])

# Save the cleaned and processed dataset to CSV
OUTPUT_CSV_PATH = 'Eng-Mohamed-abdirahman/car_l3_dataset_cleaned.csv'
df.to_csv(OUTPUT_CSV_PATH, index=False)