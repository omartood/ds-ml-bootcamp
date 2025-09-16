# Assignment: Data Cleaning & Feature Engineering

## Dataset
This assignment uses the dataset found at:
- `dataset/house_l3_dataset.csv`

## Steps Performed

### 1. Initial Data Inspection
- Loaded the dataset using pandas.
- Displayed the first few rows, data types, and missing value counts for initial understanding.

### 2. Target Cleaning
- Cleaned the `Price` column by removing `$` and `,` symbols.
- Converted `Price` to a numeric (float) type.

### 3. Categorical Fixes
- Corrected typos in the `Location` column (e.g., "Subrb" → "Suburb").
- Replaced ambiguous values (e.g., "??") with missing values (`pd.NA`).

### 4. Missing Value Imputation
- Filled missing values in `Odometer_km` with the median.
- Filled missing values in `Doors` and `Location` with their respective mode (most common value).

### 5. Duplicate Removal
- Removed duplicate rows to ensure data quality.

### 6. Outlier Handling (IQR Capping)
- Applied Interquartile Range (IQR) capping to `Price` and `Odometer_km` to limit extreme outliers.

### 7. One-Hot Encoding
- Converted the `Location` column into dummy/indicator variables for modeling.

### 8. Feature Engineering
- Created new features:
  - `HouseAge`: Age of the house (2025 - YearBuilt).
- `Accidents_per_year`: Calculated the average number of accidents per year for each house, based on available accident history and age. 
  - `Is_City`: Indicator if the house is in the city.
  - `LogPrice`: Log-transformed price for normalization.

### 9. Feature Scaling
- Scaled numeric features (except target variables and dummy columns) using `StandardScaler`.

### 10. Final Output
- Saved the cleaned and processed dataset to `car_l3_dataset_cleaned.csv`.

## Notes
- All steps were performed to ensure the dataset is ready for machine learning modeling.
- No data leakage was introduced during feature engineering.
- Outliers and missing values were handled appropriately.

---
