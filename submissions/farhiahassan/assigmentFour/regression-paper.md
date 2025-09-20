# 📘 Lesson 4 — Regression

**Theory Assignment**

---

## 1. Introduction to Regression

**Regression** is a supervised learning technique in Machine Learning that predicts **continuous values** from input features. While classification deals with assigning inputs to **categories**, regression estimates **numerical outcomes**.

**Example (Regression):** Predicting a student’s exam score based on study hours, sleep, and class attendance.  

**Example (Classification):** Predicting whether a student will **pass** or **fail** an exam.  

📌 **Key Difference:**  
- Regression → answers **“How much?”**  
- Classification → answers **“Which class?”**  

---

## 2. Types of Regression

### a) Linear Regression
- **Idea:** Models the relationship between a single feature (X) and the target (y) using a straight line.  
- **Example:** Predicting a person’s weight based on their height.  
- **Strengths:** Simple, interpretable, quick to train.  
- **Limitations:** Only suitable if the relationship is linear.  

### b) Multiple Linear Regression
- **Idea:** Extends linear regression by using two or more features to predict the target.  
- **Example:** Predicting monthly electricity bills using features like house size, number of residents, and appliances.  
- **Strengths:** Handles real-world problems with many influencing factors.  
- **Limitations:** Can suffer from **multicollinearity** (when features are strongly correlated).  

### c) Polynomial Regression
- **Idea:** Adds polynomial terms (x², x³, …) to capture curved patterns in data.  
- **Example:** Predicting population growth trends where increases accelerate over time.  
- **Strengths:** Models non-linear relationships effectively.  
- **Limitations:** High-degree polynomials can **overfit** the data.  

---

### 📊 Table: Comparison of Regression Types

| Type                       | Shape of Relationship  | Example Features                   | Best for                        |
| -------------------------- | ---------------------- | ---------------------------------- | ------------------------------- |
| Linear Regression          | Straight line          | Height → Weight                    | Simple one-factor predictions   |
| Multiple Linear Regression | Flat plane (multi-dim) | Size, Residents → Electricity Bill | Complex, real-world tasks       |
| Polynomial Regression      | Curved line            | Year, Year² → Population Growth    | Non-linear patterns & trends    |

---

## 3. Regression Metrics

To evaluate regression models, we measure how close predictions are to actual outcomes.  

| Metric                                | Meaning                           | Sensitive to Large Errors? | Units        |
| ------------------------------------- | --------------------------------- | -------------------------- | ------------ |
| **MAE** (Mean Absolute Error)         | Average of absolute errors        | ❌ No                       | Same as data |
| **MSE** (Mean Squared Error)          | Average of squared errors         | ✅ Yes                      | Squared      |
| **RMSE** (Root Mean Squared Error)    | Square root of MSE                | ✅ Yes                      | Same as data |
| **R²** (Coefficient of Determination) | % of variation explained by model | ❌ No                       | 0–1 (or %)   |

**Example:**  
- If RMSE = 2.5 → predictions are off by about **2.5 units** on average.  
- If R² = 0.82 → the model explains **82%** of the variation in the data.  

---

## 4. Underfitting and Overfitting

- **Underfitting:** The model is too simple, misses important patterns, and performs poorly on both training and test data.  
- **Overfitting:** The model learns the training data too well (including noise), leading to poor generalization on unseen data.  

**Causes of Overfitting (common in polynomial regression):**  
- Using a very high polynomial degree  
- Too few data points  
- Too many irrelevant features  

**Prevention Methods:**  
- Use regularization techniques (L1/L2)  
- Apply cross-validation to test model performance  
- Limit model complexity or use simpler models  
- Collect more representative data  

---

## 5. Case Study — Regression in Healthcare

**Title:** “Predicting Diabetes Progression Using Multiple Linear Regression”  
(*Source: Diabetes Dataset, University of California, Irvine – UCI Repository*)  

**Goal:** Estimate disease progression one year after baseline using medical indicators.  

**Data:** 442 patient records with features such as age, body mass index (BMI), blood pressure, and blood test results.  

**Model:** Multiple Linear Regression  

**Results:**  
- R² ≈ 0.52 (explained 52% of disease progression variability)  
- BMI and blood sugar levels were the most significant predictors  
- Model provided insights into which factors most strongly influence diabetes progression  

**Insight:** Regression in healthcare can support **early diagnosis** and **treatment planning**, leading to better patient outcomes.  

---

## References

1. Alpaydin, E. (2020). *Introduction to Machine Learning*. MIT Press.  
2. Géron, A. (2019). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*. O’Reilly.  
3. UCI Machine Learning Repository. “Diabetes Dataset.” University of California, Irvine.  
4. Mitchell, T. M. (1997). *Machine Learning*. McGraw-Hill*.  
