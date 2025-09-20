# 🔧 Data Preprocessing and Feature Engineering -- Detailed Explanation

## 1. Missing Value Imputation

**Continuous Variable: `Odometer_km`**\
- **Purpose:** Fill in missing values for car mileage.\
- **Method:** **Median**\
- **Reason:** Continuous variables like mileage often contain extreme
values. Using the median ensures missing values are replaced with a
"typical" value that isn't distorted by outliers, keeping the
distribution natural and the models unbiased.

**Categorical/Discrete Variables: `Doors`, `Accidents`, `Location`**\
- **Purpose:** Fill in missing values for categorical features.\
- **Method:** **Mode (most frequent value)**\
- **Reason:** Replacing missing values with the most frequent category
preserves the natural data distribution and avoids unrealistic values.

------------------------------------------------------------------------

## 2. Outlier Handling

**Method:** **Interquartile Range (IQR) Capping**\
- **Purpose:** Handle extreme values in continuous variables like
`Price` and `Odometer_km`.\
- **Process:**\
1. Find Q1 (25th percentile) and Q3 (75th percentile).\
2. Compute IQR = Q3 -- Q1.\
3. Define limits:\
- **Lower bound** = Q1 -- 1.5 × IQR\
- **Upper bound** = Q3 + 1.5 × IQR\
4. Cap values outside the range to the nearest bound.

-   **Reason:** Extreme values can distort averages and predictions.
    Capping keeps most data intact while minimizing the influence of
    anomalies.

------------------------------------------------------------------------

## 3. Feature Engineering

Feature engineering creates new variables from existing ones to capture
meaningful relationships and improve model performance.

### Key Features

-   **Car Age**
    -   Measures how old the car is.\
    -   Older cars generally lose value due to depreciation.
-   **Kilometers per Year (`Km_per_Year`)**
    -   Average yearly mileage.\
    -   High yearly mileage → heavy usage, lower value.\
    -   Low yearly mileage → careful usage, higher value.
-   **Price per Age (`Price_per_Age`)**
    -   Represents the car's value relative to its age.\
    -   Helps compare cars of different ages fairly.
-   **Price per Kilometer (`Price_per_km`)**
    -   Indicates value relative to total distance traveled.\
    -   Identifies cars that may be overpriced or underpriced for their
        usage.
-   **Logarithmic Price (`LogPrice`)**
    -   Reduces skewness in price distribution.\
    -   Stabilizes regression models and analysis.
-   **High/Low Price Flags**
    -   Binary indicators (0/1) showing whether a car is above or below
        the median price.\
    -   Useful for classification and pattern recognition.

------------------------------------------------------------------------

## 4. Summary of Benefits

-   **Missing Value Handling:** Ensures completeness without adding
    unrealistic data.\
-   **Outlier Capping:** Minimizes distortion from extreme values while
    retaining most data.\
-   **Feature Engineering:** Creates meaningful new variables that
    capture car age, usage intensity, and price relationships.

👉 **Overall Impact:** Produces a more balanced dataset, easier
analysis, and improved model accuracy.
