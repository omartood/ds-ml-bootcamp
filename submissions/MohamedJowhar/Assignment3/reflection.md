# Data Preprocessing and Feature Engineering – Detailed Explanation

## 1. Missing Value Imputation

### Continuous Variable: Odometer_km
- **Purpose:** Fill in missing values in car mileage data.  
- **Method:** Median  
- **Reason:** Continuous variables like mileage can have extremely high or low values. Using the median ensures that missing values are replaced with a “typical” car mileage without being skewed by extreme values. This preserves the natural distribution of the dataset and keeps models from being biased.

### Categorical/Discrete Variables: Doors, Accidents, Location
- **Purpose:** Fill in missing values in categories like the number of doors, accidents, or location.  
- **Method:** Mode (most frequent value)  
- **Reason:** Replacing missing values with the most common category preserves the natural distribution of data. It avoids introducing unrealistic or rare values and maintains consistency across the dataset.

---

## 2. Outlier Handling

### Method: Interquartile Range (IQR) Capping
- **Purpose:** Handle extreme values in continuous variables like Price and Odometer_km.  
- **Process:**  
  1. Identify the 25th percentile (Q1) and 75th percentile (Q3).  
  2. Compute the interquartile range (IQR) as Q3 - Q1.  
  3. Define boundaries for normal data:  
     - Lower bound = Q1 - 1.5 × IQR  
     - Upper bound = Q3 + 1.5 × IQR  
  4. Values outside these boundaries are capped to the nearest bound.  
- **Reason:** Extreme values can distort averages and model predictions. Capping rather than removing outliers keeps most of the data intact, reduces the influence of anomalies, and ensures models remain accurate and robust.

---

## 3. Feature Engineering

Feature engineering is creating new variables from existing data to capture meaningful patterns. This improves model performance and interpretability.

### Key Features

**Car Age**  
- Measures how old the car is.  
- Older cars tend to have lower prices due to depreciation.  
- Captures the relationship between age and price.

**Kilometers per Year (Km_per_Year)**  
- Average distance driven annually.  
- High yearly mileage may indicate heavy usage, reducing value.  
- Low yearly mileage suggests careful usage, often associated with higher resale value.

**Price per Age (Price_per_Age)**  
- Shows how much value remains relative to car age.  
- Helps compare cars of different ages fairly.  
- Useful for understanding which older cars maintain higher value.

**Price per Kilometer (Price_per_km)**  
- Indicates price relative to total distance traveled.  
- Highlights cars that are overpriced or underpriced for their usage.  
- Useful for identifying cars with unusual price-to-usage ratios.

**Logarithmic Price (LogPrice)**  
- Applies a log transformation to the price distribution.  
- Reduces skewness caused by very high-priced cars.  
- Makes statistical analysis and regression models more stable and reliable.

**High Price / Low Price Flags**  
- Binary indicators for whether a car is above or below the median price.  
- Useful for classification tasks or exploratory analysis.  
- Simplifies the dataset for understanding patterns in pricing.

---

## 4. Summary of Benefits

- **Handling Missing Values:** Ensures dataset completeness without introducing unrealistic data.  
- **Outlier Handling:** Reduces distortion from extreme values while keeping most data intact.  
- **Feature Engineering:** Creates meaningful metrics that capture car age, usage intensity, and pricing relationships.  
- **Overall Impact:** Improves model accuracy, helps compare cars more fairly, and makes patterns in the data easier to understand.
