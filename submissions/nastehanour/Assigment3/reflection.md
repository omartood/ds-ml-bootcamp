 🔎 Reflection on Data Preprocessing & Feature Engineering

1. Dataset Inspection

Loaded the dataset and checked its shape, first rows, data types, missing values, and category distributions.

This gave an overview and helped detect issues early.

2. Target Variable Cleaning (Price)

Removed $ and , from the Price column and converted it to numeric.

Ensured the target variable was ready for modeling.

3. Fixing Category Errors

Corrected invalid Location entries (e.g., “Subrb” → “Suburb”, “??” → missing).

Prevented one category from splitting into multiple variations.

4. Handling Missing Values

Numeric features → filled with median.

Categorical features → filled with mode.

Preserved data consistency and avoided distortion from outliers.

5. Removing Duplicates

Dropped duplicate rows.

Ensured each record contained unique information.

6. Outlier Treatment (IQR Capping)

Capped extreme values in Price and Odometer_km using the IQR method.

Reduced the effect of extreme outliers while keeping all rows.

7. Encoding Categorical Variables

Applied one-hot encoding on Location.

Converted categorical values into machine-readable format.

8. Feature Engineering

Created new features to improve predictive power:

CarAge → Age of the car.

Km_per_year → Average yearly usage.

Accident_Rate → Impact of accidents relative to age.

Is_OldCar → Binary flag for older cars.

Accident_Flag → Binary flag showing if the car had accidents.

Price_per_Age → Price trend relative to age.

Is_FamilyCar → Binary indicator for family cars.

LogPrice → Log-transformed price to reduce skewness.

9. Feature Scaling

Standardized continuous features using StandardScaler.

Excluded: target variables (Price, LogPrice), dummy variables (Location_*), and binary/ratio features.

Ensured fair weighting among continuous features.

10. Final Checks & Saving

✅ Conclusion

The preprocessing and feature engineering steps successfully converted the raw dataset into a structured and reliable form, ready for machine learning. Each stage—cleaning, imputing missing values, handling outliers, encoding categories, scaling features, and creating new variables—improved data quality and interpretability. The engineered features added real-world insights such as depreciation, accident influence, and usage patterns, making the dataset more powerful and meaningful for predictive modeling.



Checked feature distributions and summary statistics.

Saved the cleaned dataset as car_l3_clean_ready.csv.
