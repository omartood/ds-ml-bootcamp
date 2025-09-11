# Reflection — Lesson 3 Data Preprocessing

This reflection explains the main decisions I made while cleaning and preparing the car dataset.

---

## Step 1 — Load & Inspect

The initial dataset had mixed data types, missing values, typos in categories, and possible duplicates. I inspected with `head()`, `info()`, `isna().sum()`, and value counts to identify problems.

## Step 2 — Clean Price

The `Price` column contained strings with `$` and commas. I removed these symbols and converted all values to float. This ensured the target variable was numeric and ready for analysis. Skewness confirmed it was strongly right-skewed, so I also created a log-transformed version later.

## Step 3 — Fix Categories

The `Location` column had typos (`Subrb`) and placeholders (`??`, empty). I normalized them by replacing typos with the correct label and converting unknowns to missing values. This step avoided treating errors as new categories.

## Step 4 — Imputation

* **Odometer\_km** → median, because mileage can have extreme values, and the median is more robust.
* **Doors** and **Accidents** → mode, since these are discrete categorical counts where the most common value is the most reasonable guess.
* **Location** → mode, as it represents the most common car location.
  After imputation, no missing values remained.

## Step 5 — Duplicates

I dropped exact duplicate rows. This reduced redundancy and prevented the model from being biased toward repeated records.

## Step 6 — Outliers

I used the IQR method to cap extreme values in `Price` and `Odometer_km`. This reduced the influence of extreme outliers (e.g., very high prices like 120,000) while still preserving overall data distribution.

## Step 7 — One-Hot Encoding

I converted `Location` into dummy variables (`Location_City`, `Location_Suburb`, `Location_Rural`). This allowed the categorical data to be used in models without introducing ordinality.

## Step 8 — Feature Engineering

I added three features:

* **CarAge = 2025 - Year**, to capture vehicle age.
* **Km\_per\_year = Odometer\_km / (CarAge+1)**, normalizing mileage by age.
* **Is\_Urban = 1 if City or Suburb, else 0**, to capture urban vs rural market difference.
  I also created **LogPrice = log(Price+1)** to reduce skewness in the target variable.

## Step 9 — Scaling

I standardized continuous features (`Odometer_km`, `CarAge`, `Km_per_year`) using `StandardScaler`. I left binary dummy variables and target variables (`Price`, `LogPrice`) unscaled. This ensured features had mean 0 and standard deviation \~1.

## Step 10 — Final Checks

Final checks confirmed:

* `Price` and `LogPrice` are numeric.
* No missing values remain.
* At least one dummy column exists.
* The scaled features have the expected distribution.

---

### Conclusion

The pipeline ensured the dataset was clean, consistent, and ready for modeling. Each decision (median vs mode, IQR capping, engineered features) was chosen to balance robustness, interpretability, and fairness in downstream machine learning tasks.
