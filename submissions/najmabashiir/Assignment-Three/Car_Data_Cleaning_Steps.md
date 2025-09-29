# 🚗 Car Dataset Cleaning & Feature Engineering Steps

This document explains the **steps followed** for cleaning,
preprocessing, and feature engineering of the car dataset.

------------------------------------------------------------------------

## 1. Load Dataset & Explore

-   Load the dataset using Pandas.
-   Display the **first few rows** (`head()`).
-   Use `info()` to understand column data types and non-null counts.
-   Check **missing values** using `isnull().sum()`.

------------------------------------------------------------------------

## 2. Clean Target Variable (Price)

-   Remove special characters like `$` and `,` from **Price**.
-   Convert **Price** column to numeric type (`float`).

------------------------------------------------------------------------

## 3. Clean Location Column

-   Some categories in `Location` were **misspelled** (e.g., `Subrb` →
    `Suburb`).
-   Missing values (`??`) were replaced with `NaN`.
-   Filled missing values with the **most frequent value (mode)**.

✅ **Why Mode?**\
Because `Location` is a **categorical variable**, the most common
category makes sense to fill missing values.

------------------------------------------------------------------------

## 4. Handle Missing Values

-   `Odometer_km`: Filled with **median**.\
-   `Doors`: Filled with **mode**.

✅ **Why Median?**\
Median is more **robust to outliers** compared to mean, so it prevents
extreme values from skewing the imputation.

✅ **Why Mode for Doors?**\
Since `Doors` is a discrete/categorical-like variable, mode (most common
value) is the best choice.

------------------------------------------------------------------------

## 5. Remove Duplicates

-   Checked dataset shape **before and after** removing duplicates.
-   Dropped duplicate rows to avoid repeated data.

------------------------------------------------------------------------

## 6. Handle Outliers (IQR Method)

-   Used **Interquartile Range (IQR)** to detect outliers for `Price`
    and `Odometer_km`.\
-   Formula:
    -   IQR = Q3 - Q1\
    -   Lower Bound = Q1 - 1.5 × IQR\
    -   Upper Bound = Q3 + 1.5 × IQR\
-   Values outside bounds were **clipped** to avoid extreme distortions.

✅ **Why IQR?**\
IQR is a **robust method** that focuses on the middle 50% of data and
ignores extreme outliers.

------------------------------------------------------------------------

## 7. One-Hot Encoding (Categorical Features)

-   Applied **One-Hot Encoding** to the `Location` column.\
-   Created new columns: `Location_City`, `Location_Rural`,
    `Location_Suburb`.

------------------------------------------------------------------------

## 8. Feature Engineering

-   **Car_Age** = Current Year (2025) - Car's Year.\
-   **Km_per_Year** = Odometer / Car Age → shows average usage.\
-   **Is_Suburb** = Binary column indicating if the car is from Suburb.\
-   **Log_Price** = Log transformation of Price to reduce skewness.

------------------------------------------------------------------------

## 9. Feature Scaling

-   Used **StandardScaler** to normalize numeric features (mean=0,
    std=1).\
-   Excluded:
    -   Target (`Price`)
    -   `Log_Price` (already transformed)
    -   One-hot encoded location columns
    -   Derived boolean columns like `Is_Suburb`

------------------------------------------------------------------------

## 10. Save Final Dataset

-   Exported the cleaned and engineered dataset as **Car_Clean.csv**.

------------------------------------------------------------------------

# ✅ Summary

We successfully: 1. Cleaned missing values (using mode & median).\
2. Corrected categorical inconsistencies.\
3. Handled outliers (IQR clipping).\
4. Encoded categorical variables (One-Hot).\
5. Engineered new useful features.\
6. Scaled numeric features for ML readiness.\
7. Saved the processed dataset.
