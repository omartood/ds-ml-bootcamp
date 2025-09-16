# Data Preprocessing Summary

## 1. Initial Data Exploration
I began by loading the dataset and displaying the first five rows to get an initial understanding of the data. I then checked the shape and information of the dataset to identify data types and the count of non-null values.

## 2. Data Cleaning
I checked for missing values and found that the target column **'Price'** had formatting issues. I cleaned it by removing dollar signs and commas, then converted the column to a `float` data type. Next, I addressed categorical issues in the **'Location'** column by replacing incorrect values with correct ones.


## 3. Handling Missing Values
I imputed missing values in the dataset using the **median** and **mode**. I chose the median for **'Odometer_km'** because it's less affected by outliers than the mean. For **'Doors'** and **'Location'**, which are categorical columns, I used the mode as it represents the most frequent value.

## 4. Duplicate Removal
I removed duplicate rows from the dataset to ensure there was no redundancy or inconsistency.

## 5. Outlier Treatment
I applied the **IQR Capping** technique to the **'Odometer_km'** and **'Price'** columns. This method limits extreme values without deleting them, making the data more reliable. IQR capping is robust to outliers because it's based on the interquartile range, a measure of statistical dispersion.

## 6. Categorical Encoding
I performed **one-hot encoding** on the **'Location'** column to convert its categorical data into a numerical format suitable for machine learning algorithms. This method creates binary columns for each category, avoiding the creation of an artificial ordinal relationship that can occur with label encoding.

## 7. Feature Engineering
I created several new features to provide more information to the model:
* **'Car_Age'**
* **'Km_per_Year'**
* **'Accident_Rate'**
* **'Log_Price'**
* **'Is_OldCar'**
* **'Is_FamilyCar'**
* **'Is_UrbanCar'**
These new features can help the model better understand the data and improve prediction accuracy.

## 8. Feature Scaling
I used **Standard Scaling** on the numerical columns to bring them to a common scale and prevent bias. This step is crucial for improving model performance. I excluded the target columns **'Price'** and **'Log_Price'** from scaling, as well as the one-hot encoded columns, which are already in a binary format.

## 9. Final Checks and Saving
After completing the preprocessing steps, I displayed the first five rows, dataset info, and checked for any remaining missing values to ensure the data was clean and ready for modeling. Finally, I saved the preprocessed dataset to a new CSV file for future use.