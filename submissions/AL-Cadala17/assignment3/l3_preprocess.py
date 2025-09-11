import pandas as pd
import numpy as np  
from sklearn.preprocessing import StandardScaler

CSV_FILE_PATH = "car_l3_dataset.csv"
df = pd.read_csv(CSV_FILE_PATH)

# 1. Load & Inspect Data
# === INITIAL SNAPSHOT ===
print("\n=== INITIAL HEAD ===")
print(df.head())

print("\n=== INITIAL SHAPE ===")
print(df.shape)

print("\n=== INITIAL INFO ===")
print(df.info())

print("\n=== INITIAL MISSING VALUES ===")
print(df.isnull().sum())

print("\n === INITIAL LOCATION COUNTS ===")
print(df["Location"].value_counts(dropna=False))

# 2. Cleaning Target formatting
# Remove $ and , from Price and convert to float    
df["Price"] = df["Price"].replace(r"[\$,]", "", regex=True).astype(float)
print("\n=== PRICE DATATYPE AND SKEWNESS===")
print("Price Datatype:", df["Price"].dtype)  
print("Price Skewness:" ,df['Price'].skew())  # Check skewness

# 3. Fix Category Errors before Imputation
df["Location"] = df["Location"].replace({"Subrb":"Suburb", "??": pd.NA})
print("\n === LOCATION COUNTS AFTER FIXING ===")
print(df["Location"].value_counts(dropna=False))

# 4 Impute Missing Values
df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"]       = df["Doors"].fillna(df["Doors"].mode()[0])
df["Location"]    = df["Location"].fillna(df["Location"].mode()[0])
print("\n=== MISSING VALUES AFTER IMPUTATION ===")
print(df.isnull().sum())

# 5 Removing Duplicates
before = df.shape
df = df.drop_duplicates()
after = df.shape
print("\n=== DUPLICATE REMOVAL SUMMARY ===")
print(f"Duplicates Before: {before} → Duplicates After:{after}")
print(f"Dropped duplicates : {before[0] - after[0]}")

# 6 Outlier Detection
def detect_outliers_iqr(series):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return lower_bound, upper_bound

lower_price, upper_price = detect_outliers_iqr(df["Price"])             # output: Price outlier bounds: -2984.625 to 8974.375
lower_odometer, upper_odometer = detect_outliers_iqr(df["Odometer_km"]) # output: Odometer_km outlier bounds: -6642.25 to 271987.75

# print("\n=== OUTLIER BOUNDS ===")
# print(f"Price outlier bounds: {lower_price} to {upper_price}") 
# print(f"Odometer_km outlier bounds: {lower_odometer} to {upper_odometer}") 

df["Price"] = df["Price"].clip(lower=lower_price, upper=upper_price)
df["Odometer_km"] = df["Odometer_km"].clip(lower=lower_odometer, upper=upper_odometer)

# === SHORT SUMMARY STATISTICS AFTER THE IQR CLIPPING ===
print("\n=== SHORT SUMMARY STATISTICS AFTER CAPPING ===")
print("Price Summary after the capping: ", df["Price"].describe())
print("Odometer_km Summary after te capping: ", df["Odometer_km"].describe())

# 7 One-Hot Encodeing for Location
df = pd.get_dummies(df,columns=["Location"], dtype="int")
# Check new columns created
print("\n=== NEW COLUMNS CREATED AFTER ONE-HOT ENCODING ===")
print([i for i in df.columns if i.startswith("Location")]) # Output: ['Location_City', 'Location_Rural', 'Location_Suburb']
# print(df.head())

# 8 Feature Engineering
df["Is_City"]  = df["Location_City"]
df["Car_Age"] = 2024 - df["Year"]
df["Accidents_per_Year"] = df["Accidents"] / df["Car_Age"].replace(0, np.nan) # Avoid division by zero
df["had_accidents"] = (df["Accidents"] > 0).astype(int)
df["km per_Year"] = df["Odometer_km"] / df["Car_Age"].replace(0, np.nan) # Avoid division by zero
df["log_Price"] = np.log1p(df["Price"]) 
# Check new features
print("\n=== FEATURE ENGINEERING SAMPLE ===")
print(df[["Is_City", "Car_Age", "Accidents_per_Year", "had_accidents", "km per_Year", "log_Price"]].head())

# 9 Feature Scaling
do_not_scale = ["Price", "log_Price"]
numiric_col = df.select_dtypes(include = ("int64", "float64")).columns.to_list()
excluded_features = [col for col in df.columns if col.startswith("Location_")] + ["Is_City", "had_accidents"]
features_to_scale = [col for col in numiric_col if col not in do_not_scale + excluded_features]
# print("Features to scale:", features_to_scale) 

scaler = StandardScaler()
df[features_to_scale] = scaler.fit_transform(df[features_to_scale])
# Check scaled features
print("\n=== SCALED FEATURES SAMPLE ===")
print(df[features_to_scale].head())

# === FINAL SNAPSHOT ===
print("\n=== FINAL HEAD ===")
print(df.head())

print("\n=== FINAL INFO ===")
print(df.info())

print("\n=== FINAL MISSING VALUES ===")
print(df.isnull().sum())

# 10) Save
OUT_PATH = "car_l3_clean_ready.csv"
df.to_csv(OUT_PATH, index=False)
