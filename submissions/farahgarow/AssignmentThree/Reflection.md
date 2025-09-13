# Reflection on Data Cleaning and Feature Engineering

## Initial Inspection

    I started by exploring the dataset using head(), info(), and missing value counts. This helped identify:

    Missing values in key columns (Odometer_km, Doors, Location)

    Formatting issues in Price (strings with $ and ,)

    Typos in categorical variables (Subrb → Suburb, ?? → missing)

## Handling Missing Values and why i choose mode and median 

    - **Numerical columns:**  
  - `Odometer_km` → filled with **median** because it is robust to outliers.  

- **Categorical columns:**  
  - `Doors` and `Accidents` → filled with **mode** since the most frequent category is most representative.  
  - `Location` → filled with mode after correcting typos to maintain consistency.

## Outliers -IQR = Interquartile Rang
- `Q1` = 25th percentile (lower quartile)

-`Q3` = 75th percentile (upper quartile)
**Applied IQR capping on Price and Odometer_km:**

-Ensures extreme values do not disproportionately affect scaling or modeling.

-Preferred over removal to retain as much data as possible while reducing skew impact.

## Feature Engineering
**Created new features to enhance predictive power**
-`CarAge = CurrentYear - Year`

    - Captures depreciation; older cars are generally cheaper.

-`Km_per_year = Odometer_km / CarAge`

    - Measures usage intensity; better than raw mileage for estimating wear.

-`Is_Urban`

 -Binary feature indicating urban vs rural location (City or Suburb = 1).

 -Helps models account for location-based price differences.

-`LogPrice`

  -Transform target to reduce skew for regression models.

## Encoding and Scaling

- One-hot encoding for Location enables categorical variables for ML models.

- Feature scaling (StandardScaler) applied only to continuous numeric features (Odometer_km, CarAge, Km_per_year) while keeping:

 -Targets (Price, LogPrice) unscaled.

 -Binary/dummy variables unscaled.