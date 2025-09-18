# Regression  
**Part A — Theory Assignment**  

## 1. Introduction to Regression  

Regression is a supervised learning technique in Machine Learning used to predict **continuous numerical outcomes** based on one or more input features. The model attempts to learn the mathematical relationship between independent variables (predictors) and a dependent variable (target).  

**Difference from Classification:**  
- Regression deals with predicting continuous values such as sales revenue, blood pressure, or energy consumption.  
- Classification, in contrast, deals with discrete categories such as “disease present” or “disease absent,” or “pass” versus “fail.”  

**Examples:**  
- *Regression example*: Forecasting the daily electricity demand of a city based on weather conditions, time of year, and population trends.  
- *Classification example*: Predicting whether a flight will be delayed (yes/no) based on airline, route, and weather information.  

---

## 2. Types of Regression  

### a) Linear Regression  
**How it works:** Linear regression fits a straight line through the data to model the relationship between one independent variable and a dependent variable. The formula is expressed as:  
\[
y = a + bx
\]  
where \(a\) is the intercept and \(b\) is the slope.  

**Use case:** Predicting a patient’s blood pressure from their age.  

**Advantages:** Simple, easy to interpret, computationally efficient.  
**Limitations:** Cannot capture complex or non-linear relationships.  

---

### b) Multiple Linear Regression  
**How it works:** This extends linear regression to include multiple predictors:  
\[
y = a + b_1x_1 + b_2x_2 + ... + b_nx_n
\]  
This allows the model to analyze the combined influence of several variables.  

**Use case:** Predicting the yield of a farm by considering rainfall, fertilizer use, and soil quality.  

**Advantages:** Handles multiple influencing factors, more realistic than simple linear regression.  
**Limitations:** Sensitive to multicollinearity (when predictors are highly correlated).  

---

### c) Polynomial Regression  
**How it works:** Polynomial regression allows for curved relationships by adding polynomial terms:  
\[
y = a + b_1x + b_2x^2 + b_3x^3 + ...
\]  

**Use case:** Modeling the progression of a disease over time, where the pattern is not strictly linear.  

**Advantages:** Can capture non-linear patterns in data.  
**Limitations:** High risk of overfitting if the polynomial degree is too large, making predictions unreliable on new data.  

---

## 3. Regression Metrics  

- **Mean Absolute Error (MAE):** The average of absolute differences between predicted and actual values. It gives a direct sense of the average error in the same unit as the data.  
- **Mean Squared Error (MSE):** The average of squared differences between predicted and actual values. Squaring penalizes larger errors more heavily.  
- **Root Mean Squared Error (RMSE):** The square root of MSE, bringing the error back to the same unit as the data. It is highly sensitive to large errors.  
- **R² (Coefficient of Determination):** Measures how much of the variance in the dependent variable is explained by the model. Ranges from 0 (poor fit) to 1 (perfect fit).  

**Comparison Table:**  

| Metric | Units | Sensitivity to Large Errors | Meaning |  
|--------|-------|-----------------------------|---------|  
| **MAE** | Same as target variable | Moderate | Average size of absolute errors |  
| **MSE** | Squared units | Very high | Penalizes large errors strongly |  
| **RMSE** | Same as target variable | Very high | Interpretable as “typical error size” |  
| **R²** | Percentage / ratio | Not applicable | Proportion of variance explained by model |  

---

## 4. Underfitting and Overfitting  

- **Underfitting:** Occurs when a model is too simple to capture the underlying structure of the data. It performs poorly both on training and test data.  
- **Overfitting:** Occurs when a model learns not only the underlying pattern but also the noise in the training data, leading to poor generalization on new data.  

**Causes of overfitting, especially in polynomial regression:** Using a very high polynomial degree allows the model to follow every small fluctuation in training data, which does not generalize.  

**Ways to prevent overfitting:**  
1. Use cross-validation to test model generalization.  
2. Reduce model complexity (e.g., use lower-degree polynomials).  
3. Apply regularization techniques (such as Lasso or Ridge regression).  

---

## 5. Real-World Case Study  

**Study Example: Predicting Patient Survival in Intensive Care Units**  

- **Goal of the project:** Researchers aimed to predict the survival probability of patients admitted to intensive care based on multiple health indicators.  
- **Data used:** Medical records including vital signs, laboratory results, and demographic information.  
- **Regression model applied:** Multiple linear regression and variations with regularization.  
- **Key results:** The model identified that oxygen levels, age, and blood lactate concentration were significant predictors. The regression analysis provided physicians with quantitative insights that supported early interventions.  

This case demonstrates how regression models are not only statistical tools but also powerful aids in healthcare decision-making.  

---
