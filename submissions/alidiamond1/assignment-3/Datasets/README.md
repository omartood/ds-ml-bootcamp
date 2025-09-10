# Car Dataset Preprocessing Pipeline

**Dataset:** `car_l3_dataset.csv`  
**Output:** `Car_Clean.csv`  
**Script:** `app.py`  
**Goal:** Build a clean, reproducible preprocessing pipeline on dataset.

---

## **Dataset Overview**

### **Original Dataset Structure**
- **Rows:** 146 records
- **Columns:** 6 features
- **Features:** `Price`, `Odometer_km`, `Doors`, `Accidents`, `Location`, `Year`

### **Data Quality Issues Identified**
- Price values with formatting (dollar signs, commas)
- Missing values in multiple columns
- Inconsistent location naming
- Potential outliers in numeric fields
- Unknown location markers ("??")

---

## **Data Preprocessing Questions & Answers**

### **Step 1 — Data Inspection**

**Q1:** How many rows and columns are in the dataset before preprocessing?  
**A1:** The dataset has **146 rows** and **6 columns**: `Price`, `Odometer_km`, `Doors`, `Accidents`, `Location`, `Year`.

**Q2:** Which columns contain missing values?  
**A2:** `Odometer_km`, `Doors`, and `Location` contain missing values in the original dataset.

**Q3:** What data quality issues were identified?  
**A3:** 
- Price formatting inconsistencies ("$1,500" vs 1500.0)
- Location inconsistencies ("Suburb" vs "Subrb", "??" markers)
- Missing values across multiple columns
- Potential outliers in numeric fields

---

### **Step 2 — Data Cleaning**

**Q4:** How were inconsistent values in `Price` handled?  
**A4:** 
- Dollar signs and commas (e.g., `"$1,500"`) were removed using regex pattern `r"[\$,]"`
- Values were converted to numeric (`float`) data type

**Q5:** How were location inconsistencies handled?  
**A5:** 
- "Suburb" was standardized to "Subrb" for consistency
- Unknown markers ("??") were replaced with `pd.NA` for proper missing value handling

---

### **Step 3 — Missing Value Imputation**

**Q6:** How were missing values in `Odometer_km` handled?  
**A6:** Missing `Odometer_km` values were imputed with the **median** of the column to handle potential skewness.

**Q7:** How were missing `Doors` values handled?  
**A7:** Imputed using the **mode** (most frequent number of doors) as it's a categorical-like numeric variable.

**Q8:** How were missing `Location` values handled?  
**A8:** Missing locations were filled with the **mode** (most frequent location category).

---

### **Step 4 — Duplicate Removal**

**Q9:** Were there any duplicate records?  
**A9:** The script tracks duplicate removal with `before_dedup_shape` and `after_dedup_shape` variables to report any changes.

---

### **Step 5 — Outlier Handling**

**Q10:** How were outliers handled?  
**A10:** 
- Used **IQR method** with k=1.5 multiplier
- Applied to `Price` and `Odometer_km` columns
- Values capped at Q1 - 1.5×IQR (lower bound) and Q3 + 1.5×IQR (upper bound)

**Q11:** Why use IQR capping instead of removal?  
**A11:** Capping preserves data points while reducing extreme outlier impact, maintaining dataset size for modeling.

---

### **Step 6 — Categorical Encoding**

**Q12:** How were categorical variables encoded?  
**A12:** 
- `Location` → one-hot encoding: `Location_City`, `Location_Rural`, `Location_Subrb`
- Used `drop_first=False` to keep all categories for interpretability
- Set `dtype="int"` for consistent binary encoding

---

### **Step 7 — Feature Engineering**

**Q13:** What new features were created?  
**A13:** 
1. **`Year`** → Converted to car age (2025 - Year)
2. **`Price_per_km`** → Normalized price relative to odometer reading
3. **`Had_Accident`** → Binary flag (1 if accidents > 0, else 0)
4. **`Small_Car`** → Binary flag for cars with ≤3 doors
5. **`Medium_Car`** → Binary flag for cars with exactly 4 doors
6. **`Large_Car`** → Binary flag for cars with ≥5 doors
7. **`Is_City`** → Binary flag derived from `Location_City`
8. **`LogPrice`** → Log transformation of price using `np.log1p()`

**Q14:** How is car size categorization determined?  
**A14:** Based on number of doors:
- `Small_Car`: ≤3 doors
- `Medium_Car`: exactly 4 doors  
- `Large_Car`: ≥5 doors

**Q15:** Why use `np.log1p()` for price transformation?  
**A15:** `log1p()` handles zero values gracefully and reduces price distribution skewness for better modeling performance.

---

### **Step 8 — Feature Scaling**

**Q16:** Which features were scaled?  
**A16:** 
- **Scaled:** Numeric features excluding price and binary encodings
- **Excluded from scaling:** `Price`, `LogPrice`, location dummy variables (`Location_*`), `Is_City`
- **Method:** StandardScaler (z-score normalization)

**Q17:** Why exclude certain features from scaling?  
**A17:** 
- `Price` & `LogPrice`: Target variables often kept in original scale
- Binary variables: Already in 0-1 range, scaling unnecessary
- One-hot encoded features: Standardized binary format

---

### **Step 9 — Final Dataset Validation**

**Q18:** How many features are in the final dataset?  
**A18:** The final dataset contains **15+ features** (original 6 + engineered features + one-hot encoded location variables).

**Q19:** Are there any remaining missing values?  
**A19:** No. All missing values were imputed during the preprocessing pipeline.

**Q20:** What validation checks were performed?  
**A20:** 
- Initial and final dataset snapshots (`.head()`, `.info()`, `.isnull().sum()`)
- Shape tracking for duplicate removal
- Missing value verification

---

### **Step 10 — Pipeline Summary**

**Q21:** List all major preprocessing steps applied.  
**A21:** 
1. **Data Loading** → Load `car_l3_dataset.csv`
2. **Price Cleaning** → Remove formatting, convert to numeric
3. **Location Standardization** → Fix inconsistencies, handle unknown values
4. **Missing Value Imputation** → Median for odometer, mode for doors/location
5. **Duplicate Removal** → Drop exact duplicate records
6. **Outlier Capping** → IQR method for price and odometer
7. **Categorical Encoding** → One-hot encode location
8. **Feature Engineering** → Create 8 new derived features
9. **Feature Scaling** → StandardScaler for numeric features
10. **Final Export** → Save cleaned dataset as `Car_Clean.csv`

---

## **Technical Implementation Details**

### **Dependencies**
```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
```

### **Key Functions**
- **`iqr_fun(series, k=1.5)`**: Custom IQR outlier detection and capping
- **Regex cleaning**: `r"[\$,]"` pattern for price formatting
- **Feature engineering**: Multiple binary flag creation

### **File Structure**
```
├── car_l3_dataset.csv    # Original messy dataset
├── app.py               # Complete preprocessing pipeline
├── Car_Clean.csv        # Final cleaned dataset (output)
└── README.md           # This documentation
```

---

## **Usage Instructions**

1. **Ensure all files are in the same directory**
2. **Install required packages:**
   ```bash
   pip install pandas numpy scikit-learn
   ```
3. **Run the preprocessing pipeline:**
   ```bash
   python app.py
   ```
4. **Output:** Clean dataset saved as `Car_Clean.csv`

---

## **Data Quality Improvements**

| **Issue** | **Solution** | **Impact** |
|-----------|--------------|------------|
| Price formatting | Regex cleaning + type conversion | Consistent numeric data |
| Missing values | Statistical imputation (median/mode) | Complete dataset |
| Location inconsistency | Standardization + NA handling | Clean categories |
| Outliers | IQR capping | Reduced extreme value impact |
| Limited features | Engineering 8 new features | Enhanced modeling potential |
| Mixed scales | StandardScaler normalization | Algorithm-ready features |

---

**Pipeline Result:** A robust, feature-rich dataset ready for machine learning applications with comprehensive data quality improvements and engineered features for enhanced predictive modeling.