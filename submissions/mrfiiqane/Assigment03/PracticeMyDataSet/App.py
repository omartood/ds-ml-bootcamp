import pandas as pd 
import numpy as np 
from sklearn.preprocessing import StandardScaler


#file ka so akhri
CSV_PATH = 'Countries.csv'
df = pd.read_csv(CSV_PATH)  

#Qiimeynta xogta/dataset
print(df.head(4))  #arag 4 u horeysta dataset kaaga
print(df.shape)     #arag rows iyo samples kaaga dataset 
print(df.info())    #xog yar oo ku saabsan datasetka 
print(df.isnull().sum())  #kuwa maqan ii sheeg iskuna soo dar  


#dropna=false  Waxaa lagu darayaa NaN count-kiisa. 
print(df["future_status"].value_counts(dropna=False))   #labelkeyga egayey, tirinayey khaldaadkiisa
# print(df["unemployment_rate"].value_counts(dropna=False))   #unemployment egayey, tirinayey khaldaadkiisa


# magaca column ka sax
df.rename(columns={"%%unemployment_rate": "unemployment_rate"}, inplace=True)

# Hagaajinta ciladahayga sida (), / \ | % $ ;
df["unemployment_rate"] = df["unemployment_rate"].replace(r"[/%,]", "", regex=True).astype(float)
# r" waa Row String, Python wuxuu u qaataa string-ka si raw ah
# regex=True  waxaad isticmaali kartaa pattern-ka si aad u nadiifiso
print(df["unemployment_rate"].head(12))


#cilada meshe ka jirto sax
df["future_status"] = df["future_status"].replace({"normall": "normal", "??": pd.NA})
df["future_status"] = df["future_status"].replace({"normalst": "normal", "??": pd.NA})
df["future_status"] = df["future_status"].replace({"gooder": "good", "??": pd.NA})
print(df["future_status"].value_counts(dropna=True))   
print(df["future_status"].value_counts(dropna=False))   


#Missing Values Hagaajinta meelaha maqan NAN values kuna buuxi   Mean,Median,Mode
df["future_status"] = df["future_status"].fillna(df["future_status"].mode()[0])  #sort samee 0 ka bilow
df["population"] = df["population"].fillna(df["population"].mean())
df["gdp"] = df["gdp"].fillna(df["gdp"].mode()[0])
# fillna buuxinta meelaha bannaan NaN values ah
print(df.isnull().sum())


#Remove Duplicates - Ka saar wixii 2 jeer iyo wax ka badan soo laabtay
before = df.shape
df = df.drop_duplicates()     #ka saar waxyaabaha soo noqnoqda, kan kaliya wacaadi ka tag before & after
after = df.shape
print(f"Ka_Hor: {before}, Ka_Dib: {after}")


#heer ka data ay kala fogtahay haddi outliersku ku badan yihiin + 
# haddi kalena - ku badan yahay data badan keed waa low 
print(df["unemployment_rate"].skew()) 
print(df["population"].skew()) 
print(df["gdp"].skew()) 


# IQR hagajinta autliers ka 
def iqr_fun(series, k=1.5):                          #series ku waa colums ka 
  q1, q3 = series.quantile([0.25, 0.75])
  iqr = q3 - q1
  lower = q1 - k * iqr
  upper = q3 + k * iqr
  return lower, upper

Low_inflation, hight_inflation = iqr_fun(df["inflation"])
print(f"Hoos_Udhac: {Low_inflation}, kor_Ukac: {hight_inflation}")

Low_population, hight_population = iqr_fun(df["population"]) 
print(f"Hoos_Udhac: {Low_population}, kor_Ukac: {hight_population}")

#clip clip() waxaa loo isticmaalaa in lagu xaddido limit qiimaha ugu yar ugu na badan
#kawan waa manual ah gaaar ah adiga sheegaya lower & upper
df["birth"] = df["birth"].clip(lower=1, upper=110)  
df["inflation"] = df["inflation"].clip(lower=0, upper=6) 
# df["population"] = df["population"].clip(lower=50000, upper=1000000) 


# One Hot Encoding get_dummies in lagu beddelo column-ka categorical text to numeric columns
print("One Hot Encoding for future_status")
df = pd.get_dummies(df, columns = ["future_status"], drop_first= False, dtype="int")
print([c for c in df.columns if c.startswith("future_status")])


# Future engineering
df["gdp_per_capita"] = df["gdp"] / df["population"].replace(0, np.nan)
df["birth_death_ratio"] = df["birth"] / df["death"].replace(0, np.nan)
df["log_population"] = np.log1p(df["population"])


# Future scalling   X only keep target dummies unscalled
# ka reeb scalling ka,marmar features-kaas waxay leeyihiin macne asalka ah oo aan rabin in la beddelo
dont_scale = {"inflation", "unemployment_rate"}
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list() #soo saar kuwa numeric ah
exclude = [c for c in df.columns if c.startswith("future_status_")]    #ka reeb 0 1 kuwa binary dummies ah
num_features_to_scale = [c for c in numeric_cols if c not in dont_scale and c not in exclude]

scaler = StandardScaler()
df[num_features_to_scale] = scaler.fit_transform(df[num_features_to_scale])

print(df.head())
# Save garee file ka aa nadiifiyey
OUT_PATH = "Countries_Clean.csv"
df.to_csv(OUT_PATH, index=False)

print("wan save gareyey:", OUT_PATH)