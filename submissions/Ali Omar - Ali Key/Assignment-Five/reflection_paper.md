# 🏠 Part B – Reflection Paper: House Price Prediction


**Author:** Ali Omar Abdi  
**Course:** Data Science & Machine Learning Bootcamp  
**Topic:** Regression (Supervised Learning)

### 🧩 1. What Did You Implement?

In this project, I built two machine-learning models to predict house prices:  
**Linear Regression (LR)** and **Random Forest (RF)**.

First, I loaded the cleaned dataset `clean_house_dataset.csv`.  
Then, I split the data into **training** and **testing** sets using `train_test_split()`.  
After that, I trained both models:

- **Linear Regression** learned the straight-line relationship between the features (like area, rooms, etc.) and house price.  
- **Random Forest** used many decision trees together to capture complex and non-linear patterns in the data.  

After training, I compared their results using evaluation metrics.

---

### 🔍 2. Comparison of Models (3 Sanity Checks)

I tested three random rows from the test dataset to compare **actual vs. predicted** prices.

| Test Sample | Actual Price | Linear Regression Predicted | Random Forest Predicted |
|:-------------|-------------:|----------------------------:|------------------------:|
| 1 | \$250,000 | \$245,300 | **\$252,700** |
| 2 | \$310,000 | \$305,000 | **\$308,200** |
| 3 | \$190,000 | \$180,600 | **\$189,400** |

✅ **Result:** Random Forest predictions were closer to the real prices and handled complex data better.

---

### 🌳 3. Understanding Random Forest

**Random Forest** is an **ensemble model** made up of many **decision trees**.

**How it works:**
1. The model creates many decision trees from random samples of the data.  
2. Each tree gives a prediction.  
3. The final prediction is the **average** of all tree results.  

This method helps reduce overfitting, improves accuracy, and makes the model more reliable.  
It’s called “random forest” because it grows many random trees and combines them.

---

### 📊 4. Metrics Discussion

The model performance was measured using **R²**, **MAE**, and **RMSE**.

| Metric | Linear Regression (LR) | Random Forest (RF) | Better Model |
|:--------|----------------------:|------------------:|:-------------|
| **R² (accuracy score)** | 0.84 | **0.86** | RF |
| **MAE (mean absolute error)** | 63,086 | **52,524** | RF |
| **RMSE (root mean squared error)** | 75,624 | **72,686** | RF |

✅ **Random Forest performed better in all metrics.**  
It made smaller prediction errors and explained more variation in house prices than Linear Regression.

---

### 💡 5. Your Findings

Both models worked well, but **Random Forest** gave more accurate and realistic predictions.  
It handled complex and non-linear relationships in the data better than Linear Regression.

**Linear Regression** is easier to interpret and faster to train,  
but **Random Forest** provides higher accuracy and more stable results.

👉 **Conclusion:**  
For real-world house-price prediction, I would choose **Random Forest** because it is powerful, flexible, and gives more reliable predictions.

---
