import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

CSV_PATH = 'car_l3_dataset.csv'
df = pd.read_csv(CSV_PATH)


#1: Load & Inspect — show head(10), shape, info, missing counts, and Location value counts; note key issues.
#== Qiimeynta xogta/dataset ==
print("\n=== INITIAL HEAD, INFO, MISSING VALUES===")
print(df.head(11))  #arag 10 u horeysta dataset kaaga
print(df.shape)     #arag rows iyo samples kaaga dataset 
print(df.info())    #xog yar oo ku saabsan datasetka 
print(df.isnull().sum())  #kuwa maqan ii sheeg iskuna soo dar  
print(df["Location"].value_counts(dropna=False))   #fiiri khaladadka


#2: Clean Target Formatting (Price) — remove currency/commas; ensure numeric; report dtype and skewness.
# Hagaajinta ciladahayga sida (), / \ | % $ ;
df["Price"] = df["Price"].replace(r"[$,]", "", regex=True).astype(float)
print(" dtype:", df["Price"].dtype)
#waa fun pd o cabbiraya qallooc ee qaybinta xogta numeric 0 waa siman yihiin, > 0  waa qallooc midig, < 0 waa qallooc bidix
print("skewness:", df["Price"].skew())  
print(df["Price"].describe())



#3: Fix Category Errors before Imputation — normalize Location text, map typos (e.g., Subrb→Suburb),
#convert unknowns (e.g., ??) to missing; recount including missing.
df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??": pd.NA})


#4: Impute Missing Values (justify choices) — Odometer\_km→median; Doors/Accidents→mode;
# Location→mode; confirm post-imputation missing counts
df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"]  = df["Doors"].fillna(df["Doors"].mode()[0])
df["Accidents"]  = df["Accidents"].fillna(df["Accidents"].mode()[0])
df["Location"]  = df["Location"].fillna(df["Location"].mode()[0])


# 5: Remove Duplicates — report shape before/after and rows removed
before = df.shape
df = df.drop_duplicates()
after = df.shape
print(f"ka_hor: {before}, ka_dib: {after}")


# 6: Outliers (IQR capping) — compute bounds and clip for Price and Odometer\_km; show a short summary after capping
def iqr_fun(series, k=1.5):                          #series ku waa colums ka pd, k stander factor ka
  q1, q3 = series.quantile([0.25, 0.75])
  iqr = q3 - q1
  lower = q1 - k * iqr
  upper = q3 + k * iqr
  return lower, upper

low_price, high_price = iqr_fun(df["Price"])
df["Price"] = df["Price"].clip(lower=low_price, upper=high_price)

low_odo, high_odo = iqr_fun(df["Odometer_km"])
df["Odometer_km"] = df["Odometer_km"].clip(lower=low_odo, upper=high_odo)

print(df[["Price", "Odometer_km"]].describe())


# 7: One-Hot Encode Categorical(s) — encode Location as 0/1 columns; list the new columns created
df = pd.get_dummies(df, columns=["Location"], drop_first=False, dtype="int")
print("columnska cusub waa :", [c for c in df.columns if c.startswith("Location_")])




# 8: Feature Engineering (no leakage) — add at least three sensible features (e.g., CarAge, Km\_per\_year with safe handling, Is\_Urban). Add LogPrice = log(Price+1) as an alternative target (not a feature)
CURRENT_YEAR = 2025
df["CarAge"] = CURRENT_YEAR - df["Year"]
df["Km__per_year"] = df["Odometer_km"] / df["CarAge"].replace(0, np.nan)
df["is_Urban"] = 1 - df["Location_Rural"]
df["log_Price"] = np.log1p(df["Price"])


# 9: Feature Scaling (X only) — standardize continuous features; do not scale Price or LogPrice; prefer leaving 0/1 dummies unscaled; show a small sample of scaled values
dont_scale = {"Price", "log_Price"}
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list() #soo saar kuwa numeric ah
exclude = [c for c in df.columns if c.startswith("Location")]    #ka reeb 0 1 kuwa binary dummies ah
num_features_to_scale = [c for c in numeric_cols if c not in dont_scale and c not in exclude]

scaler = StandardScaler()
df[num_features_to_scale] = scaler.fit_transform(df[num_features_to_scale])


print(df.info())    #xog yar oo ku saabsan datasetka 
print(df.isnull().sum())  #kuwa maqan ii sheeg iskuna soo dar  
print(df.describe())

print("=== Gabagabo my DATA SAMPLE ===")
print(df)

# Save garee file ka aa nadiifiyey
OUT_PATH = "car_l3_clean_ready.csv..csv"
df.to_csv(OUT_PATH, index=False)

print("wan save gareyey:", OUT_PATH)