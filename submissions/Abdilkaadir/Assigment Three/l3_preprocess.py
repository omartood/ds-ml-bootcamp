import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
CSV_PATH= 'car_l3_dataset.csv'
df=pd.read_csv(CSV_PATH)

#print(df.head(10))
#print(df.shape)
#print(df.info())
#print("Missing Values")
#print(df.isnull().sum())
#print("Show counts of location")
#print(df["Location"].value_counts(dropna=False))
df["Price"]=df["Price"].replace(r"[\$,]","",regex=True).astype(float)

#print(df["Price"].skew())

df["Location"]=df["Location"].replace({"Subrb":"Suburb","??":pd.NA})
#print(df.head(10))
#print(df.isnull().sum())

#print(df["Location"].value_counts(dropna=False))

df["Odometer_km"]=df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"]=df["Doors"].fillna(df["Doors"].mode()[0])
df["Accidents"]=df["Accidents"].fillna(df["Accidents"].mode()[0])
df["Location"]=df["Location"].fillna(df["Location"].mode()[0])

#print(df.head(10))
#print(df.isnull().sum())

before=df.shape
df=df.drop_duplicates()
after=df.shape
#print("before",before,"After",after)



def iqr_fun(series, k=1.5):
    q1,q3=series.quantile([0.25,0.75])
    iqr=q3-q1
    lower=q1-k*iqr
    upper=q3+k*iqr
    return lower,upper
low_price,high_price=iqr_fun(df["Price"])
low_Odometer,high_Odemeter=iqr_fun(df["Odometer_km"])

# print("IQR of Price")

# print("low_price: ",low_price,"Hight_price",high_price)

# print("IQR of Odometer")

# print("low_Odometer: ",low_Odometer,"Hight_Odometer",high_Odemeter)

df["Price"]=df["Price"].clip(lower=low_price,upper=high_price)
df["Odometer_km"]=df["Odometer_km"].clip(lower=low_Odometer,upper=high_Odemeter)

# print("price after IQR Clipping ...")
# print(df["Price"].describe())

# print(df.head(10))


df=pd.get_dummies(df,columns=["Location"],drop_first=False)
# print("One Hot Encoded of Location: ")
# print([c for c in df.columns if c.startswith("Location")])

CURRENT_YEAR=2025
df["CarAge"]=CURRENT_YEAR-df["Year"]
df["Km_per_year"] = df["Odometer_km"] / df["CarAge"].replace(0, 1)
df["Is_Urban"]=df["Location_City"].astype(int)

df["LogPrice"] = np.log1p(df["Price"])



dont_scale={"price","LogPrice"}
numeric_cols=df.select_dtypes(include=["int16","float64"]).columns.tolist()

exclude=[c for c in df.columns if c.startswith("Location_")]+["Is_City"]

num_features_to_scale=[c for c in numeric_cols if c not in dont_scale and c not in exclude]
scaler=StandardScaler()
df[num_features_to_scale]=scaler.fit_transform(df[num_features_to_scale])
sample_cols=["Price","LogPrice"]
sample_cols+=[c for c in df.columns if c not in sample_cols]
#print(df[sample_cols].describe())# Do not scale targets


dont_scale = {"Price", "LogPrice"}


exclude = [c for c in df.columns if c.startswith("Location_")] + ["Is_City"]

print(df.head(10))

OUT_PATH="car_l3_clean_ready.csv"
df.to_csv(OUT_PATH)










