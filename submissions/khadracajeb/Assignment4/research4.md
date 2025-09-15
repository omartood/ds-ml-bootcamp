# 📋 Part A — Theory Questions

## 1. Introduction to Regression  

### What is Regression in Machine Learning?  
Regression is a **supervised learning technique** used to predict continuous numerical values. It models the relationship between one or more independent variables (features) and a dependent variable (target). By learning from historical data, regression can estimate future outcomes.  

For example, regression can be applied to predict a house price based on its size, location, and number of rooms.  

### Difference from Classification  
The main difference lies in the **output**:  
- **Regression** predicts **continuous values** (e.g., salary, temperature).  
- **Classification** predicts **discrete categories** (e.g., spam vs. not spam, disease vs. no disease).  

### Real-Life Examples  
- **Regression Examples**:  
  1. Predicting the amount of rainfall in a region based on humidity, temperature, and wind speed.  
  2. Estimating a company’s future revenue from past sales data and market trends.  

- **Classification Examples**:  
  1. Determining whether an email is spam or not.  
  2. Predicting whether a patient has a disease (positive/negative).  

---

## 2. Types of Regression  

### 2.1 Linear Regression  
- **How it works**: Models the relationship between a dependent variable and one independent variable using a straight line.  
- **Use case**: Predicting house prices from square footage.  
- **Advantages**: Simple, easy to interpret.  
- **Limitations**: Assumes linearity; not suitable for complex relationships.  

### 2.2 Multiple Linear Regression  
- **How it works**: Extends linear regression by using multiple independent variables.  
- **Use case**: Predicting sales based on advertising budget, product price, and location.  
- **Advantages**: Handles multiple factors; more realistic.  
- **Limitations**: Requires careful feature selection; sensitive to multicollinearity.  

### 2.3 Polynomial Regression  
- **How it works**: Models non-linear relationships by adding polynomial terms (e.g., x², x³).  
- **Use case**: Predicting population growth over time.  
- **Advantages**: Captures complex, curved relationships.  
- **Limitations**: High risk of overfitting; computationally expensive.  

---

## 3. Regression Metrics  

### 3.1 MAE (Mean Absolute Error)  
Measures the average absolute difference between predicted and actual values. Easy to interpret but less sensitive to large errors.  

### 3.2 MSE (Mean Squared Error)  
Calculates the average squared difference. Penalizes large errors more heavily.  

### 3.3 RMSE (Root Mean Squared Error)  
Square root of MSE. Same interpretation as MSE but keeps the units consistent with the target variable.  

### 3.4 R² (Coefficient of Determination)  
Indicates how much variance in the target is explained by the model. Ranges from 0 to 1 (higher is better).  

### Comparison Table  

| **Metric** | **Units**        | **Sensitivity to Large Errors** | **Meaning**                               |
|------------|------------------|---------------------------------|-------------------------------------------|
| **MAE**    | Same as target   | Low                             | Average absolute deviation                 |
| **MSE**    | Squared units    | High                            | Penalizes large errors                     |
| **RMSE**   | Same as target   | High                            | Standard deviation of prediction errors    |
| **R²**     | None (0–1)       | N/A                             | Proportion of variance explained           |

---

## 4. Underfitting and Overfitting  

### Underfitting  
Occurs when a model is too simple to capture patterns in the data (e.g., fitting a straight line to curved data). This results in **poor performance** on both training and test datasets. 
**like**  Predicting house prices using only the size of the house while ignoring other important factors like location and number of rooms. The model will miss key relationships and give inaccurate predictions.  

### Overfitting  
Happens when the model learns **noise** instead of the underlying pattern, performing well on training data but poorly on unseen data.
**like** A student memorizing past exam answers instead of understanding the concepts. They may perform perfectly on practice questions but fail in the real exam with new questions.    

- **Causes in Polynomial Regression**: Adding too many polynomial terms makes the model overly flexible, fitting random fluctuations instead of true trends.  

### Methods to Prevent Overfitting  
1. **Regularization** .  
2. **Cross-validation** to choose optimal complexity.  
3. **Early stopping** or limiting polynomial degree.  

---

## 5. Real-World Case Study  

### Healthcare Example: Predicting Hospital Stay Duration  
- **Goal**: Estimate the length of hospital stay for patients based on health records, age, and diagnosis.  
- **Data**: Patient demographics, medical test results, and treatment details.  
- **Model Applied**: Multiple Linear Regression.  
- **Results/Insights**:  
  - Found strong correlations between patient age, severity of illness, and hospital stay.  
  - Helped hospitals optimize resource allocation and reduce overcrowding.  

---

## References  
- James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013). *An Introduction to Statistical Learning*. Springer.  
- Kuhn, M., & Johnson, K. (2013). *Applied Predictive Modeling*. Springer.  
- Scikit-learn Documentation: [https://scikit-learn.org](https://scikit-learn.org)  
