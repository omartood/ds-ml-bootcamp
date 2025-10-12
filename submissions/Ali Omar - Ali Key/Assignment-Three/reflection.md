# Data Preprocessing Report (Easy Version)

**Author:** Ali Omar Abdi

This report explains in simple terms how we cleaned and prepared the `car_l3_dataset.csv` dataset so it can be used for machine learning. Preprocessing is like **getting your data ready for school**: we fix mistakes, fill missing parts, and make sure everything is in the right format.

---

## 1. Load & Inspect Dataset
- Loaded the CSV file into a DataFrame using pandas.
- Checked:
  - First 5 rows to see the data (`head()`).
  - Data types of each column (`info()`).
  - Missing values (`isnull().sum()`).
  - How many unique values are in each column (`nunique()`).
  - Count of cars in each `Location`.
- **Why:** This helps us understand what the data looks like and spot any obvious problems, like missing values or typos.

---

## 2. Clean the Price Column
- The `Price` column had `$` and commas like `$12,000`.
- We removed `$` and `,` and converted it to a number (`float`).
- Checked skewness (to see if most cars are cheap or expensive compared to others).
- **Why:** Machine learning cannot understand symbols or text. It only works with numbers.

---

## 3. Fix Category Errors
- The `Location` column had mistakes, e.g., `Subrb` instead of `Suburb` and `??` for unknown.
- We fixed typos and replaced unknowns with `missing values (pd.NA)`.
- **Why:** Models need clean, consistent categories. Otherwise, the computer might treat typos as different categories.

---

## 4. Fill Missing Values (Imputation)
- **Odometer_km** → replaced missing with **median** (middle value) because it’s less affected by very high or low numbers.
- **Doors**, **Accidents**, **Location** → replaced missing with **mode** (most common value).
- **Why:** We cannot leave missing values because models cannot handle empty spots.

---

## 5. Remove Duplicates
- Removed rows that were exactly the same as another row.
- Example: 145 rows → 140 rows after removing duplicates.
- **Why:** Duplicate data can confuse the model and make it think some data is more important than it really is.

---

## 6. Handle Outliers (IQR Capping)
- Outliers are numbers that are very high or very low compared to most of the data.
- We used **IQR method** to find them and **clip** them:
  - `Price` too high → set to max allowed value
  - `Odometer_km` too low or high → set within normal range
- **Why:** Extreme numbers can make the model behave badly. Clipping keeps them under control without losing data.

---

## 7. One-Hot Encode Locations
- `Location` is text like `City`, `Rural`, `Suburb`.
- Computers cannot use text, so we made **one-hot columns**:
  - `Location_City` → 1 if the car is in a city, 0 if not
  - `Location_Rural` → 1 if rural, 0 if not
  - `Location_Suburb` → 1 if suburb, 0 if not
- **Why:** Converts text into numbers that models can understand.

---

## 8. Feature Engineering
- Added new useful columns to help the model:
  - `CarAge` = 2024 - Year → how old the car is
  - `Km_per_year` = Odometer / CarAge → average distance driven per year
  - `Is_Urban` = 1 if car is in city/suburb, 0 if rural
  - `LogPrice` = log(Price + 1) → makes price easier to predict if distribution is skewed
- **Why:** New features give more information and help the model make better predictions.

---

## 9. Feature Scaling
- Scaled numbers like `Odometer_km`, `CarAge`, `Km_per_year` so they are on the **same scale**.
- Did not scale `Price`, `LogPrice`, or 0/1 columns (like `Location_*`) because:
  - Targets (`Price`) should remain original for prediction
  - Binary columns are already simple numbers (0/1)
- **Why:** Models work better if all numbers are similar in size.

---

## 10. Final Checks & Save
- Checked there are **no missing values**.
- Verified the dataset looks correct.
- Saved clean data as `car_l3_clean_ready.csv`.

---

### Summary
- Filled missing values using **median** for numbers and **mode** for categories.
- Fixed typos and unknowns in `Location`.
- Removed duplicates.
- Clipped outliers using IQR.
- Created new features: `CarAge`, `Km_per_year`, `Is_Urban`, `LogPrice`.
- Scaled continuous numbers, left binary/target columns unchanged.
- Now the dataset is **clean, complete, and ready for machine learning**.

**Output File:** `car_l3_clean_ready.csv`
