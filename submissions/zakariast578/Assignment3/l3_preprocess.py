import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


#load dataset in csv
CSV_PATH = 'dataset/AssignmentDataSet/car_l3_dataset.csv'
df = pd.read_csv(CSV_PATH)

# step 1: Load & Inspect

print(df.head(10))
# print(df.info())
# print(df.describe(include='all'))
print(df.isnull().sum())
print(df.shape)

# step 2: Clean Target Formatting (Price)
print("Before Cleaning The Target Col Price -- ")
df["Price"] = df["Price"].replace(r'\$', "", regex=True).replace(",", "", regex=True).astype(float)

# step 3: Fix Category Errors before Imputation
print("Before Cleaning Category Errors -- ")
print(df.isnull().sum())
# marka hore ogoow values-ka Location col
# print(df['Location'].value_counts())
df["Location"] = df["Location"].replace("Subrb", "Suburb").replace("??", np.nan)
# print(df['Location'].value_counts())
# print(df.head(10))

# **step 4: Impute Missing Values (justify choices)**
print("Before Imputation -- ")
print(df.isnull().sum())
df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])
# print(df.head(10))
# print(df.isnull().sum())

# step 5: Remove Duplicates
# before  remove duplicate
before = df.shape
df = df.drop_duplicates()
after = df.shape
print(f"Dropped duplicates before: {before} → {after}")

# step 6: Outliers (IQR capping)
print("Before Outlier Treatment -- ")
print(df.isnull().sum())

def Iqr_Func(series,  k=1.5):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - k * IQR
    upper = Q3 + k * IQR
    
    return lower, upper

lower_price, upper_price = Iqr_Func(df["Price"])
lower_odometer, upper_odometer = Iqr_Func(df["Odometer_km"])

# print("Original lower_price:", lower_price, "Original upper_price:", upper_price)
# print("Original lower_odometer:", lower_odometer, "Original upper_odometer:", upper_odometer)

df["Price"] = df["Price"].clip(lower=lower_price, upper=upper_price)
df["Odometer_km"] = df["Odometer_km"].clip(lower=lower_odometer, upper=upper_odometer)

# print("------=========-------")
# print("Capped lower_price:", df["Price"].min(), "Capped upper_price:", df["Price"].max())
# print("Capped lower_odometer:", df["Odometer_km"].min(), "Capped upper_odometer:", df["Odometer_km"].max())

# step 7: One-Hot Encode Categorical(s)
print("Before One-Hot Encoding --  ")
print(df.isnull().sum())
df = pd.get_dummies(df, columns=["Location"], drop_first=False, dtype="int")

# print(df.shape)
# print(df.head())

# step 8: Feature Engineering (no leakage)
print(" Before Feature Engineering -- ")
print(df.isnull().sum())
print(df.shape)
df["Car_Age"]  = 2025 - df["Year"]
df["News_with_No_Accident"] = np.where((df["Car_Age"] < 8) & (df["Accidents"] <= 1), 1, 0)
df["Super_Car"] = np.where((df["News_with_No_Accident"] == 1) & (df["Doors"] < 4 ), 1, 0)
df["Best_Seller"] = np.where((df["Car_Age"] >= 5) &  (df["Odometer_km"] < 50000), 1, 0)
df["Log_Price"] = np.log1p(df["Price"])
# df["Log_Odometer_km"] = np.log1p(df["Odometer_km"])

# step 9: Feature Scaling (X only)
print("Before Feature Scaling -- ")
print(df.isnull().sum())
print(df.shape)
dont_scale = {"Price", "Log_Price"}
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()
exclude = [ c for c in df.columns if c.startswith("Location_") or c in ["News_with_No_Accident", "Super_Car", "Best_Seller"]]

feature_to_scale = [c for c in numeric_cols if c not in dont_scale and c not in exclude]

scaler = StandardScaler()
df[feature_to_scale] = scaler.fit_transform(df[feature_to_scale])


# step 10: Final Checks & Save
print("Final Checks & Save -- ")
print(df.head(10))
# print(df.info())
print(df.isnull().sum())
print(df.shape)

OUT_PATH = "./dataset/AssignmentDataSet/car_l3_clean_ready.csv"
df.to_csv(OUT_PATH, index=False)
print("Cleaned & Ready Dataset Saved. for in csv format", OUT_PATH)
