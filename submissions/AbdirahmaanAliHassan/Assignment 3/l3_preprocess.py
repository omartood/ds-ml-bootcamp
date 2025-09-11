# (Optional) from statistics import mode   # not used; kept for parity
from statistics import mode
from sklearn.preprocessing import StandardScaler
import pandas as pd, numpy as np

# 1) Load & Initial Exploration
# -------------------------------
df = pd.read_csv("car_l3_dataset.csv")
print("\n=== [1A] HEAD(10) ===")
print(df.head(10))

print("\n=== [1] INITIAL INSPECTION ===")
print("Shape:", df.shape)
print("\nInfo:")
print(df.info())
print("\nMissing counts:\n", df.isna().sum())
print("\nLocation value counts (incl. NaN):")
print(df['Location'].value_counts(dropna=False))
print("\nDuplicates:", df.duplicated().sum())
print("Price examples:", df['Price'].unique()[:10])

# ------------------------------------
# 2) Clean Target (Price → float)
# ------------------------------------
# Remove non-numeric chars (currency, commas), cast to float
df['Price'] = (
    df['Price'].astype(str)
    .str.replace(r'[^0-9.]', '', regex=True)
    .replace('', np.nan)
).astype(float)

print("\n=== [2] PRICE CLEANED ===")
print("Price dtype:", df['Price'].dtype)
print("Price skew:", df['Price'].skew())

# ------------------------------------
# 3) Fix Categorical (Location)
# ------------------------------------
# Normalize case/whitespace, map typos, mark unknowns as NaN
loc = df['Location'].astype(str).str.strip().str.lower()
typo_map = {
    'subrb': 'suburb', 'subrb.': 'suburb', 'citty': 'city', 'rual': 'rural',
    '??': np.nan, 'unknown': np.nan, 'na': np.nan
}
loc = loc.replace(typo_map)
valid = {'city', 'suburb', 'rural'}
loc = loc.where(loc.isin(valid), np.nan)
df['Location'] = loc.map({'city': 'city', 'suburb': 'suburb', 'rural': 'rural'})

print("\n=== [3] LOCATION CLEANED ===")
print(df['Location'].value_counts(dropna=False))

# ------------------------------------
# 4) Impute Missing Values
# ------------------------------------
# Odometer_km → median; Doors/Accidents/Location → mode
df['Odometer_km'] = df['Odometer_km'].fillna(df['Odometer_km'].median())
for col in ['Doors', 'Accidents', 'Location']:
    df[col] = df[col].fillna(df[col].mode().iloc[0])

print("\n=== [4] AFTER IMPUTATION ===")
print(df.isna().sum())

# ------------------------------------
# 5) Remove Duplicates
# ------------------------------------
before = df.shape[0]
df = df.drop_duplicates()
after = df.shape[0]

print("\n=== [5] DEDUPLICATION ===")
print(f"Duplicates removed: {before - after} (shape {before} -> {after})")

# ------------------------------------
# 6) Outliers (IQR capping)
# ------------------------------------
def iqr_clip(s, k=1.5):
    q1, q3 = s.quantile([0.25, 0.75])
    iqr = q3 - q1
    low, high = q1 - k * iqr, q3 + k * iqr
    return s.clip(lower=low, upper=high), (low, high)

# Cap Price and Odometer_km
df['Price'], price_bounds = iqr_clip(df['Price'])
df['Odometer_km'], odo_bounds = iqr_clip(df['Odometer_km'])

print("\n=== [6] IQR CAPPING SUMMARY ===")
print("Price bounds:", price_bounds, "| Odometer bounds:", odo_bounds)
print(df[['Price', 'Odometer_km']].describe().T[['min','25%','50%','75%','max']])

# ------------------------------------
# 7) One-Hot Encode Location
# ------------------------------------
dummies = pd.get_dummies(df['Location'], prefix='Location', dtype=int)
df = pd.concat([df.drop(columns=['Location']), dummies], axis=1)

print("\n=== [7] DUMMIES CREATED ===")
print("New dummy cols:", list(dummies.columns))

# ------------------------------------
# 8) Feature Engineering (no leakage)
# ------------------------------------
CURRENT_YEAR = 2025  # or use df['Year'].max() if preferred
df['CarAge'] = (CURRENT_YEAR - df['Year']).clip(lower=0)
df['Km_per_year'] = df['Odometer_km'] / df['CarAge'].replace(0, 1)
df['Is_Urban'] = ((df.get('Location_city', 0) + df.get('Location_suburb', 0)) > 0).astype(int)

print("\n=== [8] ENGINEERED FEATURES (HEAD) ===")
print(df[['Year', 'CarAge', 'Km_per_year', 'Is_Urban']].head())

# ------------------------------------
# 9) Alternative Target (LogPrice)
# ------------------------------------
df['LogPrice'] = np.log1p(df['Price'])
print("\n=== [9] LOGPRICE ===")
print("LogPrice skew:", df['LogPrice'].skew())

# ------------------------------------
# 10) Feature Scaling (X only)
# ------------------------------------
# Do not scale targets (Price, LogPrice) or 0/1 dummies
num_cols = ['Odometer_km', 'CarAge', 'Km_per_year', 'Year']
scaler = StandardScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])

print("\n=== [10] SCALED SAMPLE ===")
print(df[num_cols].head())

# ------------------------------------
# Final Checks & Save
# ------------------------------------
print("\n=== [FINAL] INFO ===")
print(df.info())
print("\n=== [FINAL] MISSING (expect zeros) ===")
print(df.isna().sum())
print("\n=== [FINAL] QUICK DESCRIBE ===")
print(df[['Price', 'LogPrice', 'Odometer_km', 'CarAge', 'Km_per_year']].describe())

df.to_csv("car_l3_clean_ready.csv", index=False)
print("\nSaved -> car_l3_clean_ready.csv")