Reflection — Lesson 3: Data Preprocessing
Step 1: Load & Inspect

When loading the raw dataset, I checked the first 10 rows, the overall shape, and missing counts. The inspection revealed several issues: inconsistent Price formatting (currency strings vs. floats), missing values in Odometer_km, Doors, and Location, as well as typos such as “Subrb” and placeholders like “??”. Outliers and duplicate rows were also evident.

Step 2: Clean Target Formatting

I standardized Price by removing $ and commas, converting it to float. This was essential for numeric analysis and modeling. I also examined skewness to confirm that a log transform (added later as LogPrice) would be beneficial.

Step 3: Fix Categories before Imputation

I corrected categorical typos before imputing. For example, "Subrb" was mapped to "Suburb", and "??" was treated as missing. This ensures that imputation does not propagate bad categories.

Step 4: Impute Missing Values

I used median imputation for Odometer_km because it is robust against extreme outliers, while mode was chosen for categorical variables (Doors, Accidents, Location) since they represent discrete categories. This kept the data distribution realistic.

Step 5: Remove Duplicates

Duplicates were dropped to avoid over-representing specific vehicles and biasing the dataset. I reported the shape before and after removal to document the rows lost.

Step 6: Outliers (IQR Capping)

For Price and Odometer_km, I applied IQR-based clipping. This retains most natural variation while preventing extreme values from dominating the model. Instead of dropping rows, clipping keeps the dataset size intact.

Step 7: One-Hot Encode

I one-hot encoded Location into dummy variables (Location_City, Location_Suburb, Location_Rural). This makes the categorical variable usable in ML models without assuming an ordinal relationship.

Step 8: Feature Engineering

I added three sensible features:

CarAge = current year – manufacture year (captures depreciation).

Km_per_year = Odometer ÷ age (usage intensity, with safe denominator).

Is_Urban = binary flag for City/Suburb vs. Rural (captures demand differences).
I also added LogPrice as an alternative target to reduce skewness.

Step 9: Feature Scaling

I applied StandardScaler to continuous numeric features only, excluding Price, LogPrice, and 0/1 dummy columns. This ensures comparability of features without distorting binary categories.

Step 10: Final Checks & Save

I confirmed all missing values were handled, all types were consistent, and scaling worked (means ≈ 0, std ≈ 1). Finally, I saved the cleaned dataset to car_l3_clean_ready.csv.