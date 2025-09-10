# Data Preprocessing Report
This document outlines the steps taken to preprocess the `car_l3_dataset.csv` file, transforming it from a raw state into a clean, machine-learning-ready format.

## Step-by-Step Implementation
### 1. Load & Inspect
I began by loading the `car_l3_dataset.csv` file into a DataFrame and performing initial inspections. This involved displaying the first 5 rows (`head()`), shape, data types (`info()`), and counts of missing values. This step is crucial for understanding the raw state of the data and identifying issues like missing values and inconsistent text.

### 2. Clean Target Formatting (Price)
The `Price` column contained currency symbols (`$`) and commas, which are non-numeric. The code removed these characters and converted the column to a float data type. It then calculated the skewness to understand the distribution of the target variable.

### 3. Fix Category Errors
The `Location` column had inconsistencies like `Subrb` and `??`. The code normalized these entries by mapping `Subrb` to `Suburb` and converting `??` to a missing value (`pd.NA`). This was done before imputation to ensure the missing value count is accurate and the categories are consistent.

### 4. Impute Missing Values
* **`Odometer_km`**: Missing values were filled with the **median**. The median is a good choice for numerical data with a skewed distribution or outliers, as it is less sensitive to extreme values than the mean.
* **`Doors`/`Location`**: Missing values were filled with the **mode**. The mode is the most suitable imputation method for categorical or discrete data, as it uses the most frequent value, which is often the most logical and realistic replacement.

### 5. Remove Duplicates
I removed duplicate rows from the DataFrame. This step is essential to ensure each data point is unique, preventing a machine learning model from being biased by repeated entries. The number of rows was reduced from `(145, 6)` to `(140, 6)`, indicating 5 duplicates were successfully dropped.

### 6. Outliers (IQR Capping)
I handled outliers in the `Price` and `Odometer_km` columns using the **IQR capping method**. This method calculates a statistical range based on the Interquartile Range and clips any values that fall outside of this range. I chose this approach to prevent data loss, which would occur if the outlier rows were simply dropped from the dataset. The IQR method is a robust choice because it is less affected by extreme values than other methods like using the mean. For skewed data like `Price` and `Odometer_km`, it provides a more reliable measure of what a typical value range is.

### 7. One-Hot Encode Categorical(s)
I converted the cleaned `Location` column into one-hot encoded binary columns (`Location_City`, `Location_Rural`, `Location_Suburb`). This is necessary because machine learning models require numerical input and cannot directly interpret string data.

### 8. Feature Engineering
New features were created to provide more context to the model:
* **`Car_Age`**: Represents how old the car is, a strong predictor of price.
* **`km_per_Year`**: Calculates the average annual mileage, providing more context on car usage.
* **`Accidents_per_Year`**: Normalizes accident counts by car age.
* **`had_accidents`**: A simple yes/no flag for accident history.
* **`log_Price`**: A log-transformed version of `Price` to normalize its skewed distribution.

### 9. Feature Scaling
I applied **`StandardScaler`** to the continuous features. I specifically excluded the target variables (`Price`, `log_Price`) as well as the binary features (`Location_*`, `Is_City`, `had_accidents`). This is crucial to prevent data leakage and maintain the interpretability of the target and binary features, which don't require scaling.

### 10. Final Checks & Save
The final state of the DataFrame is inspected to confirm all missing values are handled. The clean, preprocessed data is then saved to a new CSV file (`car_l3_clean_ready.csv`).

## Summary of Key Decisions
* **Imputation**: The **median** was used for `Odometer_km` to handle numerical skew, and the **mode** was used for discrete/categorical features (`Doors`, `Accidents`, `Location`).
* **Outlier Handling**: The **IQR capping** method was chosen to manage extreme values in `Price` and `Odometer_km` without losing data points.
* **Feature Engineering**: New features like `Car_Age` and `km_per_Year` were created to provide the model with more direct and meaningful information about the cars.
* **Scaling**: **`StandardScaler`** was applied to normalize continuous features. Target variables (`Price`, `log_Price`) and binary features (`Location_*`, `Is_City`, `had_accidents`) were deliberately excluded to prevent data leakage and maintain their interpretability.