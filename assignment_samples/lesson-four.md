# 📘 Lesson 4 — Regression

**Theory Assignment**

---

## 1. Introduction to Regression

**Regression** is a supervised learning method in Machine Learning used to predict **continuous numeric values** based on input features. Unlike classification, which predicts **categories**, regression predicts **quantities**.

**Example (Regression):** Predicting the price of a house based on its size, number of bedrooms, and location.

**Example (Classification):** Predicting if a house is **luxury** or **standard** based on the same features.

📌 **Key Difference:**

* Regression → answers “**how much**”
* Classification → answers “**which class**”

---

## 2. Types of Regression

### **a) Linear Regression**

* **Idea:** Finds a straight-line relationship between one feature (X) and one target (y).
* **Example:** Predicting house price using only size.
* **Strengths:** Simple, easy to understand.
* **Limitations:** Only works well if the relationship is linear.

### **b) Multiple Linear Regression**

* **Idea:** Uses two or more features to predict a single numeric target.
* **Example:** Predicting house price using size, bedrooms, location, and year built.
* **Strengths:** Handles real-world situations with many factors.
* **Limitations:** Sensitive to multicollinearity (when features are highly correlated).

### **c) Polynomial Regression**

* **Idea:** Extends linear regression by adding powers of a feature (x², x³…) to fit **curved** patterns.
* **Example:** Predicting house price using size and size² to capture non-linear price growth.
* **Strengths:** Captures non-linear trends.
* **Limitations:** Can easily overfit if the degree is too high.

---

### 📊 Table: Comparison of Regression Types

| Type                       | Shape of Relationship  | Example Features                 | Best for                      |
| -------------------------- | ---------------------- | -------------------------------- | ----------------------------- |
| Linear Regression          | Straight line          | Size → Price                     | Simple, one-factor prediction |
| Multiple Linear Regression | Flat plane (multi-dim) | Size, Bedrooms, Location → Price | Realistic multi-factor tasks  |
| Polynomial Regression      | Curved line            | Size, Size² → Price              | Non-linear trends             |

---

## 3. Regression Metrics

When we build regression models, we must measure how close predictions are to actual values.

| Metric                                | Meaning                           | Sensitive to Large Errors? | Units        |
| ------------------------------------- | --------------------------------- | -------------------------- | ------------ |
| **MAE** (Mean Absolute Error)         | Average of absolute errors        | ❌ No                       | Same as data |
| **MSE** (Mean Squared Error)          | Average of squared errors         | ✅ Yes                      | Squared      |
| **RMSE** (Root Mean Squared Error)    | Square root of MSE                | ✅ Yes                      | Same as data |
| **R²** (Coefficient of Determination) | % of variation explained by model | ❌ No                       | 0–1 (or %)   |

**Example:**
If RMSE = 12,000 → predictions are off by about \$12,000 on average.
If R² = 0.85 → the model explains **85%** of the variation in house prices.

---

## 4. Underfitting and Overfitting

* **Underfitting:** The model is too simple and fails to learn patterns (low accuracy on both training and test data).
* **Overfitting:** The model memorizes the training data, performs well on it but poorly on new data (especially with high-degree polynomials).

**Causes of Overfitting:**

* Very complex models
* Too few data points
* Too many irrelevant features

**Prevention:**

* Use simpler models
* Use regularization (L1/L2)
* Use cross-validation
* Collect more data
* Stop training early if performance drops on validation set

---

## 5. Case Study — Regression in Transportation

**Title:** “Predicting Taxi Trip Duration Using Multiple Linear Regression”
(*Source: Journal of Big Data, 2021*)

**Goal:** Predict the duration of taxi rides in New York City based on trip distance, pickup time, and weather.

**Data:** 55,000 taxi trips with features including distance, pickup hour, day of week, and weather conditions.

**Model:** Multiple Linear Regression

**Results:**

* Achieved R² ≈ 0.76 and RMSE ≈ 4.8 minutes
* Distance and pickup hour were the strongest predictors
* Model helped taxi companies estimate trip times more accurately

**Insight:** This shows how regression can support **operational planning** and **customer satisfaction** in transportation services.

---

## References

1. Alpaydin, E. (2020). *Introduction to Machine Learning*. MIT Press.
2. Géron, A. (2019). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*. O’Reilly.
3. “Predicting Taxi Trip Duration Using Multiple Linear Regression.” *Journal of Big Data*, 2021.
4. Mitchell, T. M. (1997). *Machine Learning*. McGraw-Hill.

---
