# 📘 Assignment 4 — Regression  

Part A: Theory Questions

**Author:** Ali Omar Abdi  
**Course:** Data Science & Machine Learning Bootcamp  
**Topic:** Regression (Supervised Learning)

## **1. Introduction to Regression**  

Regression is a **supervised learning technique** used in Machine Learning to predict a **continuous numeric value** based on one or more input features. It helps us understand how changes in one or more independent variables affect a dependent variable.  

In simpler terms, regression answers questions like:  
- *“How much will something increase or decrease?”*  
- *“What will be the future value based on past trends?”*  

### **Difference Between Regression and Classification**
| Aspect | Regression | Classification |
|--------|-------------|----------------|
| Output Type | Continuous numeric value | Discrete category or label |
| Example Questions | How much will the temperature rise tomorrow? | Will it rain tomorrow — yes or no? |
| Learning Goal | Estimate a quantity | Assign data to a class |

### **Real-Life Examples**
- **Regression Example:** Predicting the **daily electricity consumption** in a city based on temperature, humidity, and time of day.  
- **Classification Example:** Determining whether an **email is spam or not spam** based on its content.  

---

## **2. Types of Regression**

Regression models come in various forms depending on the number of features and the shape of the relationship between variables.

---

### **a) Linear Regression**

**How It Works:**  
Linear regression fits a straight line that best represents the relationship between a single independent variable (x) and the dependent variable (y).  

**Real-World Example:**  
Predicting a **student’s test score** based on **hours of study**.  

**Advantages:**  
- Simple to implement and interpret.  
- Works well when variables have a linear relationship.  

**Limitations:**  
- Cannot handle curved relationships.  
- Sensitive to outliers.

---

### **b) Multiple Linear Regression**

**How It Works:**  
Multiple linear regression extends the simple linear model by using **two or more independent variables** to predict a target variable.  

**Real-World Example:**  
Predicting the **number of hospital patients** each day based on **weather conditions, flu season, and public holidays**.  

**Advantages:**  
- Captures complex relationships involving multiple factors.  
- Useful for real-world problems where outcomes depend on many variables.  

**Limitations:**  
- Struggles with multicollinearity (when variables are highly correlated).  
- Harder to interpret compared to simple regression.

---

### **c) Polynomial Regression**

**How It Works:**  
Polynomial regression models curved relationships by including powers of the independent variable (e.g., x², x³).  

**Real-World Example:**  
Predicting **the growth of a tree** over time, where growth slows after reaching maturity — a curved relationship.  

**Advantages:**  
- Models non-linear patterns effectively.  
- More flexible than linear regression.  

**Limitations:**  
- High-degree polynomials can **overfit** the data.  
- Harder to interpret visually and mathematically.  

---

### 📊 **Comparison of Regression Types**

| Type | Shape of Relationship | Example Use Case | Advantages | Limitations |
|------|-----------------------|------------------|-------------|-------------|
| Linear Regression | Straight line | Predicting student score from study hours | Simple, fast | Only linear patterns |
| Multiple Linear Regression | Plane in multiple dimensions | Forecasting hospital patient count | Handles many features | Multicollinearity issues |
| Polynomial Regression | Curved line | Modeling tree growth over years | Fits curves | Risk of overfitting |

---

## **3. Regression Metrics**

Regression models are evaluated using metrics that measure how close the predicted values are to the actual values.

| **Metric** | **Definition** | **Measures** | **Sensitive to Large Errors** | **Units** |
|-------------|----------------|---------------|-------------------------------|------------|
| **MAE (Mean Absolute Error)** | Average of absolute prediction errors | Average magnitude of error | ❌ No | Same as data |
| **MSE (Mean Squared Error)** | Average of squared prediction errors | Penalizes large errors more | ✅ Yes | Squared units |
| **RMSE (Root Mean Squared Error)** | Square root of MSE | Easy to interpret; same units as data | ✅ Yes | Same as data |
| **R² (Coefficient of Determination)** | Percentage of variance in target explained by model | Model’s overall accuracy | ❌ No | Score (0–1 or %) |

### **Example Interpretation**
- **MAE = 5** → On average, predictions are off by 5 units.  
- **RMSE = 7** → Larger mistakes have more impact on the score.  
- **R² = 0.90** → 90% of the target variation is explained by the model.  

---

## **4. Underfitting and Overfitting**

### **Underfitting**
Occurs when a model is **too simple** to capture patterns in the data.  
It performs poorly on both training and testing sets.  
**Example:** Using a straight line to model curved temperature changes over a year.  

### **Overfitting**
Occurs when a model is **too complex** and starts memorizing the training data, including noise.  
It performs well on training data but poorly on new data.  
**Example:** Polynomial regression of degree 10 used on a small dataset of only 20 samples.  

### **Causes**
- Too many features or polynomial terms.  
- Small or unbalanced dataset.  
- Noise or irrelevant data included.  

### **Prevention Methods**
1. **Simplify the model:** Use fewer parameters or reduce polynomial degree.  
2. **Regularization:** Apply penalties for complexity (e.g., Ridge or Lasso Regression).  
3. **Cross-validation:** Train and test on different data splits to ensure generalization.  
4. **Gather more data:** Helps the model learn broader patterns.  

---

## **5. Real-World Case Study: Regression in Agriculture**

**Title:** *Predicting Crop Yield Using Multiple Linear Regression (FAO Research, 2021)*  

**Goal:**  
To estimate **crop yield per hectare** based on environmental and management factors to help farmers optimize production.  

**Data Used:**  
- Rainfall (mm)  
- Temperature (°C)  
- Soil moisture (%)  
- Fertilizer amount (kg/acre)  
- Pesticide usage  

**Regression Type:**  
**Multiple Linear Regression**  

**Methodology:**  
1. Collected 5 years of agricultural data from regional farms.  
2. Cleaned and standardized the dataset.  
3. Selected relevant variables (e.g., rainfall, soil moisture).  
4. Trained a regression model using these features.  
5. Evaluated performance using MAE and RMSE metrics.  

**Results:**  
- The model achieved an **R² score of 0.89**, showing high accuracy.  
- **Rainfall** and **soil moisture** were found to be the strongest predictors of crop yield.  
- The research helped farmers **reduce waste** and **improve harvest planning**.  

**Key Insights:**  
- Regression models can effectively support decision-making in agriculture.  
- Environmental variables have measurable and predictable impacts on production.  
- Similar models can be applied to forecast food supply and plan resource allocation.  

---

### ✅ **Summary**
This assignment explored the concept of regression in Machine Learning — from linear to polynomial models, including evaluation metrics and the risks of overfitting. The real-world case study demonstrated how regression can be applied to improve agricultural efficiency and sustainability.
