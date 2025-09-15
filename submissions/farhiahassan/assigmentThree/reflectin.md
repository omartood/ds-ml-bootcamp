# Reflection — Data Preprocessing (Lesson 3)

**Dataset:** `car_l3_dataset.csv`  

## 1. Load & Inspect  
I first examined the dataset with `.head()`, `.info()`, and `.value_counts()` for `Location`.  
**Key issues identified:** mixed numeric/currency in `Price`, missing values, typos in `Location`, duplicates, and outliers in `Price` and `Odometer_km`.  

## 2. Clean Target Formatting (Price)  
Removed currency symbols and commas, then converted to float.  
- Ensured numeric type.  
- Checked skewness: `Price` is right-skewed, motivating the creation of `LogPrice`.  

## 3. Fix Category Errors (Location)  
Normalized typos (e.g., `Subrb → Suburb`) and replaced unknowns (`??`) with `NaN`.  
- Ensured consistent categories before imputation.  

## 4. Impute Missing Values  
- `Odometer_km` → median (robust to outliers)  
- `Doors`, `Accidents`, `Location` → mode (most frequent/representative value)  
- Verified no missing values remain.  

## 5. Remove Duplicates  
- Removed exact duplicates to prevent bias in modeling.  
- Reported shape before and after removal.  

## 6. Outliers (IQR Capping)  
- Applied IQR method to `Price` and `Odometer_km` to cap extreme values.  
- Avoids skewing models and reduces influence of rare extreme observations.  

## 7. One-Hot Encoding  
- Encoded `Location` into dummy variables (e.g., `Location_Suburb`).  
- This avoids assuming ordinal relationships in categorical data.  

## 8. Feature Engineering  
Created three new features:  
1. `CarAge = CurrentYear - Year`  
2. `Km_per_year = Odometer_km / CarAge` (handled division by zero)  
3. `Is_Urban = 1 if Location in ['City', 'Suburb'] else 0`  

- Also created `LogPrice = log(Price + 1)` as alternative target to reduce skewness.  

## 9. Feature Scaling  
- Standardized continuous features (e.g., `Odometer_km`, `CarAge`, `Km_per_year`) for model readiness.  
- Left dummy variables and target (`Price`, `LogPrice`) unscaled.  

## 10. Final Checks & Save  
- Confirmed all missing values filled.  
- Ensured numeric types and dummy columns exist.  
- Saved cleaned dataset as `car_l3_clean_ready.csv`.  

**Overall reasoning:**  
- Chose median/mode for robustness and representativeness.  
- Used IQR capping to reduce skew influence.  
- Engineered features to provide meaningful signals without leaking target information.  
- Standardized features to improve algorithm convergence.
