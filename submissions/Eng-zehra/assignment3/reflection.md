# Reflection — Lesson 3 Data Preprocessing

This reflection explains the main decisions I made while cleaning and preparing my dataset.

---

## Step 1 — Load & Inspect

The initial dataset appeared messy with mixed data types, missing values, and typos in categorical columns (e.g., `"YESSS"` instead of `"yes"`). I inspected the data using `head()`, `info()`, `isna().sum()`, and value counts to identify inconsistencies and missing values.

## Step 2 — Fix Categories

Inconsistent entries were present in categorical columns. For example:

- In the `Buyer` column, entries like `"yeS"` were standardized to `"yes"`.  
- Values like `"5-16km"` were cleaned by removing extra symbols (e.g., `"km"`), leaving just the numeric range.

This step ensured categories were consistent and comparable.

## Step 3 — Imputation

Most missing values were in categorical columns, so I imputed using `mode()` to replace missing entries with the most frequent value. This approach is suitable for categorical data and preserves the distribution of values.

After imputation, no missing values remained.

## Step 4 — Final Checks

I performed a final validation to confirm:

- All missing values were addressed.  
- Categories were consistent and standardized.  
- The dataset was clean and ready for analysis.

---

### Conclusion

The preprocessing pipeline successfully prepared the dataset by:

- Handling missing values  
- Correcting typos and inconsistent entries  
- Normalizing categories  

This ensured that the dataset was reliable, consistent, and ready for further analysis or modeling.
