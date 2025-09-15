# Regression

**Assignment**

---

## 1. Introduction to Regression

Regression is a supervised learning approach that estimates **numeric outcomes** by analyzing the relationship between one or more input variables and a continuous target variable. It is useful whenever the task involves predicting a measurable quantity.

- **Regression Example:** Estimating a car’s resale price using mileage, model year, and engine size.  
- **Classification Example:** Deciding whether a car belongs to the category **“affordable”** or **“luxury.”**

📌 **Essential Difference:**
- Regression → predicts a **numeric values**
- Classification → predicts a **categories**

---

## 2. Types of Regression

### **a Linear Regression**
- **Concept:** Describes the link between a single predictor and an outcome using a straight line.  
- **Application:** Forecasting crop yield based only on rainfall amount.  
- **Strengths:** Easy to compute and interpret.  
- **Drawbacks:** Not suitable when patterns are curved or complex.

---

### **b Multiple Linear Regression**
- **Concept:** Extends the linear method to include two or more predictors influencing one continuous outcome.  
- **Application:** Estimating the selling price of a house using area, number of rooms, and neighborhood quality.  
- **Strengths:** Captures the effect of multiple variables.  
- **Drawbacks:** Can become unreliable if predictors are strongly correlated with each other.

---

### **c Polynomial Regression**
- **Concept:** Enhances linear regression by adding polynomial terms (x², x³, etc.) to capture curved relationships.  
- **Application:** Modeling the growth of a startup company’s revenue over several years, where the trend accelerates rather than staying straight.  
- **Strengths:** Able to fit data with non-linear patterns.  
- **Drawbacks:** May overfit if the polynomial degree is chosen too high.

---

### 📊 Comparison of Regression Types

| Type                       | Pattern Captured         | Example Scenario                      | Best Use Case                 |
| -------------------------- | ------------------------ | ------------------------------------- | ----------------------------- |
| Linear Regression          | Straight line            | Rainfall → Crop Yield                 | Simple one-variable problems  |
| Multiple Linear Regression | Flat surface (multi-dim) | Rooms, Size, Location → House Price   | Complex multi-factor settings |
| Polynomial Regression      | Curved line              | Year, Year² → Company Revenue Growth  | Non-linear behaviors          |

---

## 3. Regression Metrics

To judge the accuracy of regression models, several evaluation tools are used:

| Metric                                | What It Measures                    | Sensitive to Large Errors | Unit of Measurement |
| ------------------------------------- | ----------------------------------- | ------------------------- | ------------------ |
| **MAE** (Mean Absolute Error)         | Average distance between predictions and true values | ❌ No | Same as target variable |
| **MSE** (Mean Squared Error)          | Mean of squared prediction errors   | ✅ Yes | Squared units |
| **RMSE** (Root Mean Squared Error)    | Square root of MSE, easier to interpret | ✅ Yes | Same as target variable |
| **R²** (Coefficient of Determination) | Portion of variance explained by model | ❌ No | 0 to 1 (or %) |

**Illustration:**  
- If RMSE = 3 → predictions deviate by about 3 units on average.  
- If R² = 0.70 → the model accounts for 70% of the variability in the outcome.  

---

## 4. Underfitting and Overfitting

- **Underfitting:** Happens when the model is too limited to detect meaningful patterns, resulting in weak results on both training and unseen data.  
- **Overfitting:** Occurs when the model becomes too tailored to the training data, capturing noise rather than general trends, leading to poor test performance.  

**Common reasons for overfitting in polynomial regression:**
- Very high polynomial degree  
- Too few observations  
- Irrelevant or noisy predictors  

**Ways to reduce overfitting:**
1. Limit model complexity  
2. Use regularization techniques (L1/L2)  
3. Validate with cross-validation strategies  
4. Increase dataset size if possible  

---

## 5. Case Study — Regression in Business

**Topic:** Predicting Monthly Sales for Retail Stores  
(*Based on a retail analytics study, 2023*)  

- **Objective:** Estimate the monthly sales revenue of retail shops.  
- **Dataset:** Historical sales figures from 1,200 stores including variables like advertising budget, store size, and number of employees.  
- **Model Used:** Multiple Linear Regression  
- **Findings:**  
  - Advertising spend and store size were the most significant predictors.  
  - Achieved R² ≈ 0.82 and RMSE ≈ \$4,500.  
  - Insights allowed managers to adjust marketing budgets effectively.  




