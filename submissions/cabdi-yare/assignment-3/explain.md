# Reflection on Car Dataset Cleaning (L3 Preprocessing)

## Step 1: Initial Dataset Inspection
First, I examined the dataset to understand its structure, data types, and locations of missing or inconsistent values. This step helped identify which columns needed cleaning, such as Price, Odometer, and Location. Understanding the raw data is crucial for planning preprocessing steps.

## Step 2: Cleaning Price Column
The Price column contained non-numeric characters like "$" and ",". I removed these characters and converted the values to float. Missing or invalid entries were coerced to NaN. The *median* was used to fill missing values because outliers in Price could heavily skew the mean, while the median provides a more robust central value.

## Step 3: Cleaning Numeric Columns
The Odometer_km column was converted to numeric, and errors were coerced to NaN. Missing values in Doors and Odometer_km were filled with the *median* rather than the mean, minimizing the influence of extreme values and preserving the typical range of values.

## Step 4: Cleaning Categorical Columns
For Location, typos like "Subrb" were corrected to "Suburb," and unknown values "??" were replaced with "Unknown." This ensures consistent categorical entries while retaining all rows, avoiding data loss.

## Step 5: Year Column
The Year column was converted to numeric, and missing values were filled with the *median*. Using the median prevents extreme old or new years from skewing derived features such as CarAge.

## Step 6: Feature Engineering
I created the following features:
- CarAge: Measures the vehicle’s age.
- Accidents_per_km: Indicates the accident frequency relative to distance driven.
- Doors_per_km: Shows the relationship between the number of doors and distance.
These features add meaningful information that could improve model performance.

## Step 7: Outlier Handling (IQR Capping)
I used *IQR capping* to limit extreme numeric values. This reduces the influence of outliers while preserving the overall distribution, which is important for robust modeling.

## Step 8: Scaling Numeric Features
Numeric features were scaled using StandardScaler (mean=0, std=1). Scaling ensures that algorithms like regression or distance-based models treat all numeric features equally and converge more effectively.

## Step 9: Encoding Categorical Features
The Location column was one-hot encoded, converting it into numeric form so machine learning algorithms can interpret it correctly.

## Step 10: Saving Cleaned Dataset
Finally, the cleaned, feature-engineered, and scaled dataset was saved as car_l3_clean.csv for future modeling.

