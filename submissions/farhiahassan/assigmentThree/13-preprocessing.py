# # import pandas as pd
# # import numpy as np
# # from sklearn.preprocessing import StandardScaler

# CSV_PATH= 'car_13-dataset(1).csv'

# df = pd.read_csv(CSV_PATH)

# # initial snapshot
# print("INITIAL HEAD ")
# print(df.head())
# print(df.head(10))
# print("information")
# print(df.info())
# print("MISSING VALUES")
# print(df.isnull().sum())

# # 2 cleaning format
# print("clean formt")
# df["Price"] = df["Price"].replace(r"[\$,]", "", regex=True).astype(float)

# # 3fixing categoricaly
# df['Location'] = df['Location'].replace({'Subrb':'Suburb', '??': np.nan, '':'Unknown'})
# print("Location counts after fix:")
# print(df["Location"].value_counts(dropna=False))

# # 4 misiing values
# print("Impute missing values")
# df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
# df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
# df["Accidents"] = df["Accidents"].fillna(df["Accidents"].mode()[0])
# df["Location"] = df["Location"].fillna(df["Location"].mode()[0])

# print(df.head(20))
# print("\MISSING VALUES")
# print(df.isnull().sum())

# # 5 remove duplicate
# print("removing duplicate")
# before = df.shape
# df = df.drop_duplicates()
# after = df.shape
# print(f" dropedd duplicate: {before} {after}")

# # 6 Outliers (IQR capping)
# def iqr_arounds(series, k=1.5):
#     q1, q3 = series.quantile([0.25, 0.75])
#     iqr = q3 - q1
#     lower = q1 - k * iqr
#     upper = q3 + k * iqr
#     return lower, upper

# low_price, high_price = iqr_arounds(df["Price"])
# low_odometer, high_odometer = iqr_arounds(df["Odometer_km"])
# df["Price"] = df["Price"].clip(lower=low_price, upper=high_price)
# df["Odometer_km"] = df["Odometer_km"].clip(lower=low_odometer, upper=high_odometer)
# print("Price and Odometer summary after capping:")
# print(df[["Price", "Odometer_km"]].describe()) 
# df["LogPrice"] = np.log1p(df["Price"])

# # step 7: One-Hot Encode Categorical
# df = pd.get_dummies(df, columns=["Location"], drop_first=False, dtype="int")

# # step 8:Feature engineering
# CURRENT_YEAR = 2025
# df["CarAge"] = CURRENT_YEAR - df["Year"]
# df["Price_per_km"] = df["Price"] / df["Odometer_km"].replace(0, np.nan)
# df["Price_per_km"] = df["Price_per_km"].fillna(0)
# df["High_Mileage"] = (df["Odometer_km"] > 150000).astype(int)
# df["Age_Group"] = pd.cut(
#     df["CarAge"],
#     bins=[0, 5, 10, 15, 25, 100],
#     labels=["0-5", "6-10", "11-15", "16-25", "25+"]
# )
# df["Had_Accident"] = (df["Accidents"] > 0).astype(int)
# df["Log_Odometer"] = np.log1p(df["Odometer_km"])

# # step 9: feature scaling
# print("Before Feature Scaling --")
# print(df.isnull().sum())
# print("Shape:", df.shape)
# dont_scale = {"Price", "LogPrice"}
# numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()

# exclude = [
#     "High_Mileage",
#     "Had_Accident",
#     "Age_Group"
# ]
# features_to_scale = [c for c in numeric_cols if c not in dont_scale and c not in exclude]
# scaler = StandardScaler()
# df[features_to_scale] = scaler.fit_transform(df[features_to_scale])

# # 10 final checks
# print("Final Checks & Save -- ")
# print(df.head(10))
# print(df.info())
# print(df.isnull().sum())
# print(df.shape)

# OUT_PATH = "car_13_clean_ready.csv"
# df.to_csv(OUT_PATH, index=False)
