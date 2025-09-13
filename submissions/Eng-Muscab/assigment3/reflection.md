explaining your decisions for each major step (why median vs mode, why IQR capping, which features you engineered and why).
Reflection on Data Preprocessing Steps

1.  Initial Snapshot: I began by loading the dataset and taking an initial snapshot to understand its structure, data types, and the presence of missing values. This step is crucial for planning subsequent preprocessing tasks.
2.  Price Cleaning: The 'Price' column contained formatting issues with commas and dollar signs, which I removed to convert the values to a numeric type. This is essential for any numerical analysis or modeling.
3.  Fixing Category Errors: I normalized the 'Location' text by correcting typos (e.g., 'Subrb' to 'Suburb') and converting unknowns (e.g., '??', 'N/A') to NaN. This ensures consistency in categorical data, which is important for accurate analysis and modeling.
4.  Imputation of Missing Values: For imputation, I used the mode for 'Accidents' and 'Doors' to fill in missing values. This is a common approach for handling missing data in categorical features. For 'Odometer_km' and 'Year', I used the median to mitigate the impact of outliers, which can skew the mean.
5.  Removing Duplicates: I removed duplicate rows to ensure that each record in the dataset is unique, which is important for analysis and modeling.
6.  Outliers (IQR capping): I computed bounds and capped the 'Price' and 'Odometer_km' features to remove outliers. This is a common approach to handle outliers in numerical features.
7.  One-hot Encoding: I applied one-hot encoding to the 'Location' feature to convert categorical data into a format suitable for machine learning algorithms. This allows the model to interpret categorical variables effectively.
8.  Feature Engineering: I engineered several new features:

    - 'CarAge': This feature represents the age of the car, which is likely to be a significant factor in determining its price.
    - 'Km_per_year': This feature indicates the average kilometers driven per year, providing
      insight into the car's usage and wear.
    - 'Is_Urban': This binary feature indicates whether the car is located in an urban area, which could influence its price due to demand and availability.
    - 'LogPrice': I created this feature as an alternative target variable to address potential skewness in the 'Price' distribution.
    - 'NewAccidents': This binary feature indicates whether the car has had any accidents, which is important for assessing its condition and value.

    9. Feature Scaling: I standardized continuous features (excluding 'Price' and 'LogPrice') to ensure that they have a mean of 0 and a standard deviation of 1. This is important for many machine learning algorithms that are sensitive to the scale of input features. I left binary features unscaled to preserve their interpretability.
    10. Final Checks & Save I performed final checks to ensure there were no missing values and that the dataset was ready for modeling. I saved the cleaned dataset to a new CSV file for future use. valuable information about the car's condition.

        - 'Is_Urban': This binary feature indicates whether the car is located in an urban area, which could influence its price due to demand and availability.

        - 'LogPrice': I created this feature as an alternative target variable to address potential skewness in the 'Price' distribution.
        - 'NewAccidents': This binary feature indicates whether the car has had any accidents , which is important for assessing its condition and value.

    11. Feature Scaling: I standardized continuous features (excluding 'Price' and 'LogPrice') to ensure that they have a mean of 0 and a standard deviation of 1. This is important for many machine learning algorithms that are sensitive to the scale of input features. I left binary features unscaled to preserve their interpretability.
    12. Final Checks & Save: I performed final checks to ensure there were no missing values and that the dataset was ready for modeling. I saved the cleaned dataset to a new CSV file for future use.

        - 'NewAccidents': This binary feature indicates whether the car has had any accidents, which is important for assessing its condition and value.
