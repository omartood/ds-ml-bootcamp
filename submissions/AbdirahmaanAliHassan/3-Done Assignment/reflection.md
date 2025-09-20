**Name:** Abdirahmaan Ali Hassan
**Course:** Data Science & Machine Learning Bootcamp
**Date:** September 10, 2025 

**Dataset & Goal**
The dataset contained car listings with columns: `Price`, `Odometer_km`, `Doors`, `Accidents`, `Location`, and `Year`. It included missing values, typos, outliers, and duplicates. The goal was to build a clean, reproducible preprocessing pipeline suitable for modeling.

---

**Key Decisions**

* **Target cleaning (Price):** Removed currency symbols/commas and cast to float to allow numeric analysis. Skewness was checked to understand distribution.
* **Category fixing before impute:** Normalized and corrected `Location` text (typos like *Subrb* → *Suburb*; `??` → missing) before imputation to avoid bias.
* **Imputation:**
  * `Odometer_km` → median (robust to outliers).
  * `Doors`, `Accidents`, `Location` → mode (categorical/low-cardinality).
* **Duplicates:** Dropped duplicate rows to prevent leakage and over-counting.
* **Outliers (IQR capping):** Applied IQR bounds on `Price` and `Odometer_km` to reduce the effect of extreme values.
* **Encoding:** One-hot encoded `Location` for compatibility with ML models and easier interpretation.
* **Feature engineering:** Added
  * `CarAge` = Current year – Year,
  * `Km_per_year` = usage rate with safe divide,
  * `Is_Urban` = indicator for City/Suburb.
* **Alternative target:** Created `LogPrice = log(Price+1)` to reduce skew and stabilize modeling.
* **Scaling:** Standardized only continuous predictors (`Odometer_km`, `CarAge`, `Km_per_year`, `Year`). Left `Price`, `LogPrice`, and dummy columns unscaled.

---

**Sanity Checks & Reproducibility**
Assertions confirmed: `Price` is float, `LogPrice` exists and numeric, no missing values remain, dummy columns are present, and scaled features have mean ≈ 0 and std ≈ 1. A clean virtual environment was used and exact package versions recorded in `requirements.txt`.

---

**AI Usage**
I used AI for **concept clarification and planning only**. All implementation was written and tested by me.
