# Lesson 3 - Data Preprocessing

## Dataset Name  
`car_13_dataset`

## Objective  
Gain cleaned and processed data ready for modeling.

---

## Overview

### Before Cleaning  
- Original dataset contained **145 entries** and **6 features**.  
- **19 entries** had null values.  
- Data issues included:  
  - Misspelling (e.g., "subrb" instead of "suburb").  
  - Inconsistencies (unclear/missing data marked as "??").  
- The target/output column had formatting errors (e.g., `$` and commas).  
- The output column contained a positive outlier at **7.87**.

### After Cleaning and Feature Engineering  
- Dataset was reduced to **140 entries** and expanded to **12 features**.  
- Missing values were handled as follows:  
  - Categorical columns (`Location` and `Doors`) filled with their **mode**.  
  - Numerical column (`Odometer_km`) filled with its **mean**.  
- Outliers were handled using the **IQR method** and the output column and `Odometer_km` were clipped accordingly.  
- Applied **one-hot encoding** to the `Location` column.  
- Scaled all numerical features to prepare the data for modeling.  
- The final cleaned and processed dataset was saved as **`car_13_clean_ready.csv`**.

---

## Notes  
This preprocessing step is crucial to ensure high-quality input for the prediction model.
