import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

CSV_PATH = 'car_l3_dataset.csv'

df = pd.read_csv(CSV_PATH)

# print("Checking my data")
# print(df.head())
# print(df.shape)
# print(df.isnull().sum())
# print(df)

# print(df.info())
# print("Clerning")
df["Price"] = df["Price"].replace(r"[\$,]","", regex=True).astype(float)

# print("Checking the location if their is an issue")
# print(df['Location'].value_counts())

# print("fixing some issues like Subrb this issue is spelling also ?? this issue is unknow it will change to null")
df["Location"] = df["Location"].replace({"Subrb":"Suburb"})
df["Location"] = df["Location"].replace({"??":pd.NA})

# print("also you can make it one line")
# df["Location"] = df["Location"].replace({"Subrb":"Suburb","??":pd.NA})
# print(df['Location'].value_counts(dropna=False))


# print(df['Doors'].value_counts(dropna=False)) 
# print(df['Accidents'].value_counts(dropna=False))
# print(df['Year'].value_counts(dropna=False))

# print("filling the empty value in doors using mode() because their is no Out layers instead there is a repetation doors actually doors are 4,5,3,2 the null places will fill the repeated doors. also filling the Location like this doors but Odometer_km we will use median becuase it has outliers ")
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])
df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
# print(df['Doors'].value_counts(dropna=False))
# print(df['Location'].value_counts(dropna=False))


# print("Removing duplicats ")
before = df.shape
df = df.drop_duplicates()

# print("before:",before,"After:",df.shape)
# print(df.info())



# print("checking if my data has out layer before IQR")
# print(df["Odometer_km"].max())
# print(df["Odometer_km"].min())

def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper

low_Odometer_km, high_Odometer_km = iqr_fun(df["Odometer_km"])
# print("for IQR")
# print(f"low: {low_Odometer_km} > high: {high_Odometer_km}")

df["Odometer_km"] = df["Odometer_km"].clip(lower=low_Odometer_km, upper=high_Odometer_km)

# print("checking if my data has out layer after IQR")
# print(df["Odometer_km"].max())
# print(df["Odometer_km"].min())

df = pd.get_dummies(df, columns=["Location"], drop_first=False, dtype="int")


#knowing the age of the car whether is old, middle or new to do this we need to add carAge column that comes from current year minus the year of the car also this method called feature engineering.

CURRENT_YEAR = 2025 # THIS IS THE CURRENT YEAR 
df["Car_Age"] = CURRENT_YEAR - df["Year"] 
#adding kilometer per year that we can show using to divide Odometer_km and age
df["Km_Per_Year"] = df["Odometer_km"] / df["Car_Age"] 
# print(df.head(20))

#also we can add if the car is old, normal or new
#now we create a function that returns old if the car age is over 15 or normal if the car is b/w 6 - 15 or new if the car less than or equal 5

def StatusOfCar_fun(age):
    if(age <= 5):
        return 'New'
    elif(age > 5 and age <= 15):
        return 'Normal'
    else:
        return 'Old'
    

df["Car_Status"] =  [StatusOfCar_fun(c) for c in df["Car_Age"]]
# df["Car_Status"] = df["Car_Age"].apply(StatusOfCar_fun) # you can also use this


# also we can add if the car is a high mileage that can the buyer consider if this car fit i mean if the car new but the odometer km obove 200,000 is not fit because of odometer mk 

df["Is_High_Mileage"] = df["Odometer_km"] > 200000
#let's convert into int because now it's a true or false
df["Is_High_Mileage"] = df["Is_High_Mileage"].astype(int)
#also adding is get accidents
df["Is_Accident"] = (df["Accidents" ]> 0).astype(int)

#also let's make one-hot encoding for the car status since now is old, normal and new

df = pd.get_dummies(df, columns=["Car_Status"], drop_first=False, dtype="int")

# print(df.head(20))

# 9) Feature scaling (X only; keep targets & dummies unscaled) # this part i sed chatGPT since i didn't get it but now i understand it well and i will review it I.a
dont_scale = {"Price"}  # target
exclude = ["Is_High_Mileage", "Car_Status_New", "Car_Status_Normal", "Car_Status_Old", 
           "Location_City", "Location_Rural", "Location_Suburb","Is_Accident"]

numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()
num_features_to_scale = [c for c in numeric_cols if c not in dont_scale and c not in exclude]
# print("Columns to scale:", num_features_to_scale)


# 4. Apply StandardScaler
scaler = StandardScaler()
df[num_features_to_scale] = scaler.fit_transform(df[num_features_to_scale])



# === FINAL SNAPSHOT ===
# print("\n=== FINAL HEAD ===")
# print(df.head())

# print("\n=== FINAL INFO ===")
# print(df.info())

# print("\n=== FINAL MISSING VALUES ===")
# print(df.isnull().sum())
OUTPUT_CSV = 'cleaned_car_dataset.csv'

df.to_csv(OUTPUT_CSV, index=False)

# print(df.info())


