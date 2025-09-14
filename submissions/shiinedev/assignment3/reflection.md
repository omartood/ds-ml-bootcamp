# Reflection

In this project, I prepared and engineered features from a used car dataset to build a cleaner and more informative dataset for price prediction.

## Handling Missing Values
- **Odometer_km:** Imputed with the **median**, because mileage is typically skewed. The median is more robust against outliers than the mean.  
- **Doors & Location:** Imputed with the **mode** (most frequent value) since these are categorical. Mode preserves the most common category without distorting the distribution.

## Cleaning & Deduplication
- Removed duplicates to avoid bias from repeated entries.  
- Standardized categorical entries (e.g., fixing `"Subrb"` → `"Suburb"`) and replaced invalid tokens (`"??"`) with missing values before imputation.

## Outlier Treatment
- Applied **IQR capping** to `Price` and `Odometer_km`.  
- IQR (Interquartile Range) clipping reduces the effect of extreme values beyond `1.5 × IQR` while keeping most natural variation.  
- Chose capping instead of dropping rows to retain dataset size.

## Feature Engineering
- **CarAge = CurrentYear – Year** → captures depreciation with age.  
- **Had_Accident (binary)** → distinguishes cars with accident history.  
- **Accidents_per_year** → normalizes accident count by car age (converted to integer for interpretability).  
- **Odometer_per_Year** → captures intensity of use (km driven per year).  
- **LogPrice (log of Odometer_per_Year)** → reduces skewness and stabilizes variance.  

These engineered features better reflect how wear, usage, and history affect price.

## Encoding
- Applied **one-hot encoding** to `Location` so models can handle categories without assuming an order.

## Scaling
- Used **StandardScaler** on continuous numeric features (excluding `Price`, `LogPrice`, and binary flags).  
- This puts mileage, accidents, and other numerical features on comparable scales for machine learning.

---

✅ **Summary of Decisions:**  
- **Median vs Mode** → chosen based on variable type (numeric vs categorical).  
- **IQR capping** → robust outlier handling without data loss.  
- **Feature engineering** → designed to capture realistic car depreciation, usage, and accident effects.  
- **Encoding & scaling** → ensure features are model-ready, unbiased, and consistent.
