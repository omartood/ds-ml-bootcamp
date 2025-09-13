# Reflection on Data Preprocessing — Lesson 3

## Step 1–3: Load, Inspect & Fix Categories
I started by loading the dataset and inspecting it to understand its structure, missing values, duplicates, and any obvious errors. The `Location` column had typos like "Subrb" and unknown values like "??", so I normalized the text and corrected these issues to ensure consistency. This step was crucial for reliable imputation and encoding later.

## Step 4: Imputation
Missing values were handled based on the type of data. For `Odometer_km`, I used the median because it is continuous and could contain extreme values. For categorical columns like `Doors` and `Location`, I used the mode to fill in the most common value. This approach ensures that imputed values are realistic and do not distort the data distribution.

## Step 5: Removing Duplicates
Duplicates were identified and removed. This cleaned the dataset and prevented the same vehicle from influencing the model multiple times. In this dataset, 5 duplicate rows were removed.

## Step 6: Outlier Handling
I applied IQR capping to `Price` and `Odometer_km` to limit extreme values while keeping most of the data intact. This reduced the effect of outliers that could skew model training and performance.

## Step 7: One-Hot Encoding
Categorical data in `Location` was converted into dummy columns (`Location_City`, `Location_Suburb`, `Location_Rural`). This allows the model to process location information numerically without assuming any order among categories.

## Step 8: Feature Engineering
I created several new features to help the model better understand the data:
- `CarAge` – shows how old the vehicle is.
- `Km_per_year` – measures annual usage; handled zero-age vehicles to avoid errors.
- `Is_Urban` – binary feature indicating if the car is from an urban area (`City` or `Suburb`).
- `Accident_flag` – binary feature showing whether the car had any accidents.
- `LogPrice` – an alternative target to reduce skewness in `Price`.

These features are meaningful, avoid leaking future information, and help the model capture patterns that affect car price.

## Step 9: Feature Scaling
Continuous numeric features (`CarAge`, `Km_per_year`, `Odometer_km`, `Accidents`) were standardized using StandardScaler to have mean ≈ 0 and std ≈ 1. Binary features (`Is_Urban`, `Accident_flag`, and all `Location` dummy columns`) and target columns (`Price`, `LogPrice`) were left unscaled to preserve interpretability.

## Step 10: Final Checks & Saving
Finally, all missing values were handled, duplicates removed, scaled features verified, and the clean dataset saved as `Car_l3_Clean.csv`. This pipeline ensures a consistent, reproducible, and model-ready dataset.
