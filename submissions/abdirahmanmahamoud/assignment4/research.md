## 1. Introduction to Regression

Regression in Machine Learning is a **supervised learning technique** used to predict **continuous numerical values**. It aims to establish a relationship between input features (independent variables) and a target variable (dependent variable). For instance, a regression model may use features such as house size, location, and the number of bedrooms to predict the **price of a house**.

Regression differs from classification in terms of output. **Classification** predicts **categories** (e.g., spam vs. not spam emails), while **regression** predicts **numbers** (e.g., house prices in dollars).

A real-life regression example is predicting a person’s annual income based on education, age, and years of work experience. In contrast, a classification example is predicting whether a loan applicant will **default or not**.

---

## 2. Types of Regression

### a) Linear Regression

Linear regression is the simplest regression technique. It assumes a **straight-line relationship** between one feature and the target variable. The model fits the best line through the data points by minimizing the error between predicted and actual values.

- **Use case:** Predicting house prices based on size alone.
- **Advantages:** Easy to interpret and implement.
- **Limitations:** Only works when the relationship is linear and depends on a single factor.

### b) Multiple Linear Regression

Multiple linear regression extends linear regression by considering **two or more features** simultaneously. It predicts the target variable as a weighted combination of several factors.

- **Use case:** Predicting house prices using multiple features such as size, number of rooms, and location.
- **Advantages:** Captures more realistic relationships.
- **Limitations:** Assumes linearity among all features; performance decreases if irrelevant or correlated features are included.

### c) Polynomial Regression

Polynomial regression is a form of regression where the model fits a **curved relationship** between features and the target by adding polynomial terms (e.g., x², x³). This approach is useful when the relationship is not strictly linear.

- **Use case:** Predicting housing prices where prices rise quickly for smaller houses but plateau for larger ones.
- **Advantages:** Handles non-linear relationships better than simple linear regression.
- **Limitations:** Susceptible to overfitting if the polynomial degree is too high.

---

## 3. Regression Metrics

To evaluate regression models, we use error metrics that measure how close predictions are to actual values.

- **Mean Absolute Error (MAE):** The average of absolute differences between predicted and actual values. It tells us the **average error** in the same units as the target.
- **Mean Squared Error (MSE):** The average of squared differences. It penalizes large errors more than MAE.
- **Root Mean Squared Error (RMSE):** The square root of MSE, bringing the error back to the same units as the target variable.
- **R² (Coefficient of Determination):** Explains how much of the variance in the target variable is captured by the model (ranges from 0 to 1).

### Comparison Table

| Metric | Meaning                | Units          | Sensitive to Large Errors? | Interpretation       |
| ------ | ---------------------- | -------------- | -------------------------- | -------------------- |
| MAE    | Average absolute error | Same as target | No                         | Average deviation    |
| MSE    | Average squared error  | Squared units  | Yes                        | Penalizes big errors |
| RMSE   | Square root of MSE     | Same as target | Yes                        | Typical error size   |
| R²     | Variation explained    | None (0–1)     | No                         | Model fit quality    |

---

## 4. Underfitting and Overfitting

**Underfitting** occurs when a regression model is too simple to capture patterns in the data. For example, fitting a straight line to data that follows a curve results in poor accuracy.

**Overfitting** occurs when the model is too complex and fits noise in the training data rather than general trends. Polynomial regression with a high degree is especially prone to overfitting because the curve bends too much to fit every data point.

### Causes of Overfitting

- Too many polynomial terms.
- Small training dataset.
- Lack of regularization.

### Methods to Prevent Overfitting

1. Use **cross-validation** to check performance on unseen data.
2. Apply **regularization techniques** such as Ridge or Lasso regression.
3. Limit the degree of polynomial terms and remove irrelevant features.

---

## 5. Real-World Case Study

A practical example of regression in the real world comes from the **healthcare sector**. Researchers have applied **multiple linear regression** to predict patients’ blood pressure levels based on factors such as age, body mass index (BMI), diet, and physical activity.

- **Goal:** Estimate blood pressure to identify at-risk patients early.
- **Data Used:** Patient demographic data, lifestyle factors, and clinical history.
- **Model Applied:** Multiple Linear Regression.
- **Results:** The study found that age and BMI were strong predictors, explaining over 70% of the variance in blood pressure readings. This helped healthcare providers prioritize preventive measures.

---

## ✅ Conclusion

Regression is a foundational concept in Machine Learning that enables us to predict continuous outcomes. Linear regression is straightforward but limited, multiple regression accounts for several variables, and polynomial regression captures non-linear trends. Evaluation metrics such as MAE, MSE, RMSE, and R² help assess model performance. Finally, understanding underfitting and overfitting is crucial to avoid building unreliable models.

Regression is widely applied across industries — from predicting housing prices in real estate to forecasting patient health outcomes in healthcare.
