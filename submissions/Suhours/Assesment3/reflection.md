# Reflection on Data Preprocessing (Lesson 3)

This document summarizes the reasoning behind each preprocessing step.

## Step 1 — Load & Inspect
We inspected the dataset and identified issues: mixed formatting in `Price`, inconsistent `Location` categories, missing values in `Odometer_km`, `Doors`, and `Location`, and possible duplicates/outliers.

## Step 2 — Clean Target (Price)
Removed currency symbols and commas, then converted to numeric. Price was stored as float and its skewness checked, showing strong right skew. This justified using `LogPrice` later.

## Step 3 — Fix Categories
Normalized `Location` text with `.title()`, corrected typos (e.g., `Subrb → Suburb`), and converted placeholders like `??` into missing values.

## Step 4 — Imputation
- `Odometer_km` → median (robust to skew).
- `Doors` and `Accidents` → mode (categorical/discrete values).
- `Location` → mode (most common location).
This ensured no missing values remained.

## Step 5 — Duplicates
Removed duplicate rows, reducing dataset size slightly and improving data integrity.

## Step 6 — Outliers (IQR Capping)
Applied IQR clipping to `Price` and `Odometer_km` to cap extreme outliers while preserving the majority of the data distribution.

## Step 7 — One-Hot Encoding
Encoded `Location` into dummy variables (`Location_City`, `Location_Rural`, `Location_Suburb`), enabling machine learning models to use categorical data properly.

## Step 8 — Feature Engineering
Added:
- **CarAge** = 2025 - Year (vehicle age).
- **Km_per_year** = Odometer / CarAge (intensity of use).
- **Price_per_km** = measures how much the car costs per kilometer driven.
- **LogPrice** = log-transformed price to handle skewed distribution (used as target, not a feature).

## Step 9 — Scaling
Standardized continuous features (`Odometer_km`, `Doors`, `Accidents`, `CarAge`, `Km_per_year`) with StandardScaler. Excluded `Price` and `LogPrice` (targets) and dummy variables (already 0/1).

## Step 10 — Final Checks & Save
Confirmed no missing values, all columns had proper data types, and exported the cleaned dataset as `car_l3_clean_ready.csv`.

---

This preprocessing pipeline ensures the dataset is consistent, clean, and ready for modeling, while minimizing data leakage and preserving interpretability.
