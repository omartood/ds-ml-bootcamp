# 📘 Lesson 4 — Regression  

**Theory Assignment**  

---

## 1. Introduction to Regression  

In Machine Learning, **regression** is a supervised learning approach used to predict **continuous values**. Instead of classifying inputs into groups, regression estimates a **numerical outcome**.  

**Example (Regression):** Predicting the amount of electricity a household will consume next month based on historical usage, number of residents, and appliances.  

**Example (Classification):** Predicting whether a household is a **low**, **medium**, or **high** energy consumer.  

📌 **Key Difference:**  
* Regression → answers **“how much”**  
* Classification → answers **“which group”**  

---

## 2. Types of Regression  

### **a) Linear Regression**  
* **Idea:** Models a straight-line relationship between one independent variable (X) and one target variable (y).  
* **Example:** Predicting student exam score based only on study hours.  
* **Strengths:** Easy to implement and interpret.  
* **Limitations:** Fails if the relationship is not linear.  

### **b) Multiple Linear Regression**  
* **Idea:** Uses several input factors to estimate one outcome.  
* **Example:** Predicting crop yield using rainfall, soil quality, fertilizer usage, and temperature.  
* **Strengths:** Can handle realistic, multi-factor predictions.  
* **Limitations:** Sensitive to correlation between variables (multicollinearity).  

### **c) Polynomial Regression**  
* **Idea:** Extends linear regression by including higher-order powers (x², x³…) to model curved patterns.  
* **Example:** Predicting population growth where growth accelerates at first and then slows over time.  
* **Strengths:** Good at capturing non-linear relationships.  
* **Limitations:** High-degree polynomials can overfit and become unstable.  

---

### 📊 Table: Comparison of Regression Types  

| Type                       | Shape of Relationship  | Example Features                 | Best for                      |  
| -------------------------- | ---------------------- | -------------------------------- | ----------------------------- |  
| Linear Regression          | Straight line          | Study Hours → Exam Score          | Simple, one-factor prediction |  
| Multiple Linear Regression | Flat plane (multi-dim) | Rainfall, Fertilizer → Crop Yield | Complex, real-world problems  |  
| Polynomial Regression      | Curved line            | Time, Time² → Population Growth   | Non-linear patterns           |  

---

## 3. Regression Metrics  

To evaluate regression models, we use error metrics that compare predictions with actual values.  

| Metric                                | Meaning                                | Sensitive to Large Errors? | Units        |  
| ------------------------------------- | -------------------------------------- | -------------------------- | ------------ |  
| **MAE** (Mean Absolute Error)         | Average of absolute errors              | ❌ No                       | Same as data |  
| **MSE** (Mean Squared Error)          | Average of squared errors               | ✅ Yes                      | Squared      |  
| **RMSE** (Root Mean Squared Error)    | Square root of MSE                      | ✅ Yes                      | Same as data |  
| **R²** (Coefficient of Determination) | % of variation explained by the model   | ❌ No                       | 0–1 (or %)   |  

**Example:**  
If RMSE = 5 kg → predictions are off by about **5 kg** on average.  
If R² = 0.82 → the model explains **82%** of the variation in crop yield.  

---

## 4. Underfitting and Overfitting  

* **Underfitting:** The model is too basic, missing key relationships (e.g., predicting grades using only study hours, ignoring attendance or prior knowledge).  
* **Overfitting:** The model becomes too complex, memorizing training data but failing on new data. This often happens with polynomial regression of very high degree.  

**Causes of Overfitting:**  
* Complex models with too many parameters  
* Limited training data  
* Too many irrelevant variables  

**Prevention:**  
* Simplify the model  
* Use **regularization techniques** (L1, L2)  
* Apply **cross-validation**  
* Collect more training samples  
* Early stopping during training  

---

## 5. Case Study — Regression in Healthcare  

**Title:** “Predicting Patient Recovery Time Using Multiple Linear Regression”  
(*Source: Healthcare Informatics Journal, 2020*)  

**Goal:** Estimate hospital recovery time for patients after surgery based on age, type of surgery, pre-existing conditions, and length of hospital stay.  

**Data:** 20,000 patient records, including demographics, medical history, and treatment details.  

**Model:** Multiple Linear Regression  

**Results:**  
* Achieved R² ≈ 0.70 and RMSE ≈ 3.2 days  
* Age and surgery type were the strongest predictors  
* Helped hospitals improve **resource allocation** and **bed management**  

**Insight:** Regression in healthcare can enhance decision-making and improve patient care by predicting recovery patterns more accurately.  

---

## References  

1. Alpaydin, E. (2020). *Introduction to Machine Learning*. MIT Press.  
2. Géron, A. (2019). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*. O’Reilly.  
3. “Predicting Patient Recovery Time Using Multiple Linear Regression.” *Healthcare Informatics Journal*, 2020.  
4. Mitchell, T. M. (1997). *Machine Learning*. McGraw-Hill.*  
