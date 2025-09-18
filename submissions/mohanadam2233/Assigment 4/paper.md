
# 📘 Lesson 4 — Regression

**Part A — Theory Assignment**



## 1. Introduction to Regression

**Regression** in Machine Learning is a type of supervised learning used to predict **continuous numerical values** based on input data. The model learns patterns from historical data and uses them to estimate unknown outcomes.

**Difference from Classification:**

* **Regression:** Predicts continuous values (e.g., temperature, price).
* **Classification:** Predicts discrete categories or labels (e.g., spam vs. not spam).

**Real-life examples:**

1. **Regression:** Predicting house prices based on size, location, and number of rooms.
2. **Classification:** Email spam detection (spam or not spam).
3. **Regression:** Forecasting monthly sales revenue for a company.
4. **Classification:** Diagnosing whether a patient has a disease (yes/no).
5. **Regression:** Estimating the age of a person based on lifestyle and genetic data.



## 2. Types of Regression

### 2.1 Linear Regression

* **How it works:** Linear regression predicts a continuous outcome using a **linear relationship** between the independent variable $x$ and dependent variable $y$, modeled as $y = b_0 + b_1x$.
* **Real-world use case:** Predicting salary based on years of experience.
* **Advantages:** Simple, interpretable, fast to train.
* **Limitations:** Assumes linearity; cannot capture complex relationships.

### 2.2 Multiple Linear Regression

* **How it works:** Extends linear regression to include **multiple independent variables**. Formula: $y = b_0 + b_1x_1 + b_2x_2 + ... + b_nx_n$.
* **Real-world use case:** Predicting house prices using size, number of bedrooms, age of house, and neighborhood rating.
* **Advantages:** Can model multiple factors at once.
* **Limitations:** Sensitive to multicollinearity; still assumes linearity.

### 2.3 Polynomial Regression

* **How it works:** Models **non-linear relationships** by including polynomial terms (e.g., $x^2, x^3$) in the regression equation.
* **Real-world use case:** Predicting growth of a plant over time where growth accelerates non-linearly.
* **Advantages:** Can fit curved data patterns.
* **Limitations:** Prone to overfitting with high-degree polynomials; harder to interpret.


## 3. Regression Metrics

### 3.1 Mean Absolute Error (MAE)

* Measures the **average absolute difference** between predicted and actual values.
* **Unit:** Same as the target variable.
* **Example:** Average error in predicting house prices is \$5,000.

### 3.2 Mean Squared Error (MSE)

* Measures **average squared difference** between predicted and actual values.
* **Unit:** Square of target variable.
* **Example:** Penalizes larger errors more strongly; used in model optimization.

### 3.3 Root Mean Squared Error (RMSE)

* Square root of MSE; returns **error in the same units** as the target variable.
* **Example:** RMSE of predicted temperatures is 2°C.

### 3.4 R² (Coefficient of Determination)

* Measures **proportion of variance explained** by the model (0 to 1).
* **Example:** R² = 0.85 means 85% of the variation in house prices is explained by the model.

**Comparison Table:**

| Metric | Units          | Sensitivity to Large Errors | Meaning                                    |
| ------ | -------------- | --------------------------- | ------------------------------------------ |
| MAE    | Same as target | Low                         | Average magnitude of errors                |
| MSE    | Squared        | High                        | Penalizes large errors strongly            |
| RMSE   | Same as target | High                        | Root of MSE, interpretable in target units |
| R²     | None (0–1)     | N/A                         | Proportion of variance explained           |



## 4. Underfitting and Overfitting

* **Underfitting:** Model is too simple to capture data patterns; poor performance on both training and test data.
* **Overfitting:** Model fits training data too closely, capturing noise; poor generalization to new data.

**Causes of Overfitting (especially in polynomial regression):**

* High-degree polynomials.
* Too few data points.
* Noise in data.

**Methods to prevent overfitting:**

1. **Use simpler models** (lower polynomial degree).
2. **Regularization** (e.g., Ridge, Lasso).
3. **Cross-validation** to test generalization.




## 5. Real-World Case Study: Walmart Sales Prediction

### 🎯 Goal of the Project
The objective of this study was to predict Walmart's sales using regression models. Accurate sales forecasting helps with inventory management, staffing, and strategic planning in retail operations.

### 📊 Data Used
The dataset includes historical sales data from Walmart with variables such as:
- **Sales Volume**: Number of units sold
- **Price**: Selling price of products
- **Promotions**: Discounts or special offers applied
- **Store Traffic**: Number of customers visiting the store
- **Seasonality Factors**: Time of year, holidays, and events

### 🧠 Type of Regression Model Applied
- **Multiple Linear Regression (MLR)**: Models the relationship between the dependent variable (sales volume) and multiple independent variables (price, promotions, store traffic, etc.).

**Model Equation:**

\[
\text{Sales Volume} = \beta_0 + \beta_1 (\text{Price}) + \beta_2 (\text{Promotions}) + \beta_3 (\text{Store Traffic}) + \dots + \epsilon
\]

Where:
- \( \beta_0 \) = intercept  
- \( \beta_1, \beta_2, \dots \) = coefficients of independent variables  
- \( \epsilon \) = error term  

### 📈 Key Results and Insights
- **Model Performance**: MLR effectively predicted sales with a high R² value.  
- **Significant Predictors**: Promotions and store traffic had the most impact on sales.  
- **Business Implications**:
  - Optimize pricing strategies  
  - Plan promotions effectively  
  - Improve inventory management  

### 🔗 Reference
Zhang, J. (2023). *Sales Prediction of Walmart Based on Regression Models*. Atlantis Press. [Link](https://www.atlantis-press.com/article/125994715.pdf)

