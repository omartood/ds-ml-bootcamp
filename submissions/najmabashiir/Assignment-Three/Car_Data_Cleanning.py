import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

CSV_FILE_PATH = 'car_l3_dataset.csv'
df = pd.read_csv(CSV_FILE_PATH)

# first i want to know data frame header
print(df.head())

# second we want to know data frame info
print(df.info())

# and step3 i want to know data null values and we sum all null values in each column
print(df.isnull().sum())

# step4 i want to clean target formatting
df['Price']=df['Price'].replace(r"[\$,]",'', regex=True).astype(float)
print(df['Price'].value_counts(dropna=False))
# so loaction some categories incoorect and i fic and i see ?? we change nun
print(df['Location'].value_counts(dropna=False))
df["Location"]=df["Location"].replace({"Subrb":"Suburb" ,"??":pd.NA})
print(df['Location'].value_counts(dropna=False))

# step5 i want to fill null values columns
# first i want to fill null values in location column with mode
df["Location"]=df["Location"].fillna(df["Location"].mode()[0])
# second i want to fill null values in odometer column with median
df["Odometer_km"]=df["Odometer_km"].fillna(df["Odometer_km"].median())

# third i want to fill null values in Doors column with mode
df["Doors"]=df["Doors"].fillna(df["Doors"].mode()[0])
print(df.info())

# step5 i want to remove duplicates
before=df.shape
df = df.drop_duplicates()
after=df.shape
print(f"before removing duplicates {before} and after removing duplicates {after}")

# step6 i want to remove outliers
def iqr_outliers(series, k=1.5):
    q1,q3=series.quantile([0.25 , 0.75])
    iqr=q3-q1
    lower=q1 - k *  iqr
    upper=q3 + k * iqr
    return lower, upper
lower_Price, upper_Price = iqr_outliers(df["Price"])
lower_Odometer, upper_Odometer=iqr_outliers(df["Odometer_km"])

df["Price"]= df["Price"].clip(lower=lower_Price, upper=upper_Price)
df["Odometer_km"]= df["Odometer_km"].clip(lower=lower_Odometer, upper=upper_Odometer)

# step7 i want use oneHot encoding for categorical columns i have only one categorical column that is location
df= pd.get_dummies(df, columns=["Location"], drop_first=False,dtype="int")
# print([col for col in df.columns if col.startswith("Location")]) this line to see new columns that created

# step8 future engineering 
#  w i want to know how old the car
Current_year=2025
df["Car_Age"]=Current_year-df["Year"]
# i want to know how many km the car run in each year
df["Km_per_Year"]=df["Odometer_km"]/df["Car_Age"]
# i want to know is location is suburb or
df["Is_Suburb"]=df["Location_Suburb"].astype(int)
df["Log_Price"]=np.log1p(df["Price"])
print(df.columns)

# step9 feature Scallling
Dont_scale=["Price","Log_Price"]
Numeric_cols=df.select_dtypes(include=["int64","float64"]).columns.tolist()
exclude_cols=[col for col in df.columns if col.startswith("Location_")] +["Is_Suburb"]
num_features_to_scale = [c for c in Numeric_cols if c not in Dont_scale and c not in exclude_cols]

scaler=StandardScaler()
df[num_features_to_scale]=scaler.fit_transform(df[num_features_to_scale])
              

# === FINAL SNAPSHOT ===
print("FINAL HEAD")
print(df.head())

print("FINAL INFO")
print(df.info())

print("FINAL MISSING VALUES")
print(df.isnull().sum())

# 10) Save
OUT_PATH = "Car_Clean.csv"
df.to_csv(OUT_PATH, index=False)
