# Lesson 3 — Data Preprocessing Assignment

**Dataset:** `car_l3_dataset.csv`  
**Goal:** Build a clean, reproducible preprocessing pipeline on a messy tabular dataset.

---

## **Data Preprocessing Questions & Answers**

### **Step 1 — Data Inspection**

**Q1:** How many rows and columns are in the dataset before preprocessing?  
**A1:** The dataset has **140+ rows** (exact depends on the file) and **6 columns**: `Price`, `Odometer_km`, `Doors`, `Accidents`, `Location`, `Year`.

**Q2:** Which columns contain missing values?  
**A2:**`Odometer_km`, `Doors`, and `Location` contain missing values in the original dataset.

---

### **Step 2 — Data Cleaning**

**Q3:** How were inconsistent values in `Price` handled?  
**A3:**  
- Dollar signs and commas (e.g., `"$1,500"`) were removed.  
- Values were converted to numeric (`float`).  

**Q4:** How were missing values in `Odometer_km` handled?  
**A4:** Missing `Odometer_km` values were imputed with the **median** of the column.

**Q5:** How were missing or unknown values in `Location` handled?  
**A5:** Unknown or missing locations (`??` or empty) were:  
- Replaced with a default category (e.g., `Unknown`)  


---

### **Step 3 — Feature Engineering**

**Q6:** What new columns were created?  
**A6:**  
1. `Location_City`, `Location_Rural`, `Location_Subrb` — one-hot encoded location.  
2. `Price_per_km` — normalized `Price` relative to `Odometer_km`.  
3. `Had_Accident` — binary (1 if accidents > 0, else 0).  
4. `Small_Car`, `Medium_Car`, `Large_Car` — based on number of doors.  
5. `Is_City` — binary flag for city location.  
6. `LogPrice` — log transformation of `Price`.

---

### **Step 4 — Scaling and Normalization**

**Q7:** Which columns were scaled?  
**A7:** Continuous numeric columns were scaled:  
- `Odometer_km`, `Doors`, `Accidents`, `Year`, `Price_per_km`  

**Q8:** Why was log transformation applied to `Price`?  
**A8:** To reduce skewness in the `Price` distribution and make it more suitable for modeling.

---

### **Step 5 — Encoding Categorical Variables**

**Q9:** How were categorical variables handled?  
**A9:**  
- `Location` → one-hot encoding: `Location_City`, `Location_Rural`, `Location_Subrb`  
- Car size → `Small_Car`, `Medium_Car`, `Large_Car`  
- City flag → `Is_City` (1 if city, else 0)

---

### **Step 6 — Handling Missing Values**

**Q10:** How were missing `Doors` values handled?  
**A10:** Imputed using the **mode** (most frequent number of doors).  

**Q11:** How were missing `Accidents` values handled?  
**A11:** Filled with **0**, assuming no accidents.

---

### **Step 7 — Creating Binary Features**

**Q12:** How is `Had_Accident` calculated?  
**A12:**  
- `1` if `Accidents > 0`  
- `0` if `Accidents = 0`  

**Q13:** How are `Small_Car`, `Medium_Car`, `Large_Car` determined?  
**A13:** Based on number of doors:  
- `Small_Car`: 2–3 doors  
- `Medium_Car`: 4 doors  
- `Large_Car`: 5+ doors  

---

### **Step 8 — Feature Transformation**

**Q14:** How was `Price_per_km` calculated?  
**A14:**  
- Formula: `Price_per_km = Price / Odometer_km`  
- Then scaled/normalized for uniform distribution.  

**Q15:** Why is `Price_per_km` useful?  
**A15:** Standardizes car value across different mileage.

---

### **Step 9 — Final Dataset Check**

**Q16:** How many rows and columns are in the after dataset?  
**A16:** Same number of rows; **columns increased to ~15** with engineered features.

**Q17:** Are there any remaining missing values?  
**A17:** No. All missing values were imputed or transformed.

---

### **Step 10 — Summary of Transformations**

**Q18:** List all major preprocessing steps applied.  
**A18:**  
1. Remove formatting from `Price` → convert to numeric  
2. Handle missing values (`Odometer_km`, `Doors`, `Location`) → imputation  
3. One-hot encode `Location`  
4. Create binary features: `Had_Accident`, `Is_City`, car size flags  
5. Normalize/scale numeric features (`Odometer_km`, `Doors`, `Accidents`, `Year`, `Price_per_km`)  
6. Compute `Price_per_km`  
7. Apply log transformation to `Price` → `LogPrice`  
8. Final dataset ready for machine learning

---

### **Step-to-Q&A Mapping Table**

| Assignment Step                       | Related Q&A                                      |
| ------------------------------------- | ------------------------------------------------- |
| **1. Load & Inspect**                 | Q1, Q2                                            |
| **2. Clean Target (Price)**           | Q3, Q8, Q15                                       |
| **3. Fix Category Errors (Location)** | Q5, Q9                                            |
| **4. Impute Missing Values**          | Q4, Q10, Q11                                      |
| **5. Remove Duplicates**              | Q16 (report shape change if any duplicates)      |
| **6. Outliers (IQR capping)**         | Q14, Q8                                          |
| **7. One-Hot Encode**                 | Q9                                                |
| **8. Feature Engineering**            | Q6, Q12, Q13, Q14, Q15                            |
| **9. Feature Scaling**                | Q7, Q8                                            |
| **10. Final Checks & Save**           | Q16, Q17, Q18                                     |
