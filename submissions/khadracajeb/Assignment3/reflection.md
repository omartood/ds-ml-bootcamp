# Reflection on Car Dataset Preprocessing

## 1. Missing Value Imputation
- **Odometer_km**: filled with **median** (robust to outliers).  
- **Doors**: filled with **mode** (discrete feature, preserves common value).  
- **Location**: filled with **mode** (categorical, ensures consistency).  

## 2. Outlier Handling (IQR Capping)
- Applied **IQR capping** to `Price` and `Odometer_km` to limit extreme values.  
- Keeps most data intact while reducing influence of outliers.

## 3. Feature Engineering
- **CarAge** = CURRENT_YEAR - Year → age of the car.  
- **LogPrice** = log(Price+1) → reduces skewness, stabilizes variance.  
- **Accidents_per_Year** = Accidents / CarAge → normalized accident frequency.  
- **Km_per_Year** = Odometer_km / CarAge → average annual usage.  
- **Is_City** → binary indicator for urban location of the car.

## 4. Scaling
- Used **StandardScaler (Z-score)** on numeric features except targets (`Price`, `LogPrice`) and dummies (`Location_*`, `Is_City`).  
- Ensures features are on similar scales, improving model convergence and preventing dominance by large-magnitude values.

## Summary
- Median vs mode chosen based on feature type and distribution.  
- IQR capping used to mitigate outliers.  
- Engineered features enhance predictive power without target leakage.  
- Final dataset is clean, complete, scaled, and ready for modeling.
