# Regression in Machine Learning

## 1. Introduction to Regression

**Regression** is a supervised machine learning technique used to predict continuous values. It finds relationships between input variables (features) and an output variable (target).

**Difference from Classification:**

- Regression → predicts numbers (e.g., price, temperature).
- Classification → predicts categories (e.g., spam/not spam).

**Examples:**

- Regression: Predicting house prices based on size and location.
- Classification: Predicting if an email is spam or not.

---

## 2. Types of Regression

### Linear Regression

- **How it works:** Fits a straight line between one input and output.
- **Use case:** Predicting salary from years of experience.
- **Advantages:** Simple, interpretable.
- **Limitations:** Only models linear relationships.

### Multiple Linear Regression

- **How it works:** Uses two or more inputs to predict the output.
- **Use case:** Predicting student performance from study hours, attendance, and sleep.
- **Advantages:** Captures multiple factors.
- **Limitations:** Sensitive to multicollinearity.

### Polynomial Regression

- **How it works:** Uses polynomial terms (x², x³, …) to fit curves.
- **Use case:** Predicting car price depreciation over time.
- **Advantages:** Models complex, non-linear trends.
- **Limitations:** High risk of overfitting with large degrees.

---

## 3. Regression Metrics

- **MAE:** Average of absolute errors; shows typical error size.
- **MSE:** Average of squared errors; penalizes large errors more.
- **RMSE:** Square root of MSE; error in same units as target.
- **R²:** Proportion of variance explained by the model.

**Comparison Table**


| Metric | Units          | Sensitive to Large Errors? | Meaning                |
| ------ | -------------- | -------------------------- | ---------------------- |
| MAE    | Same as target | No                         | Average absolute error |
| MSE    | Squared units  | Yes                        | Penalizes large errors |
| RMSE   | Same as target | Yes                        | Typical error size     |
| R²    | None           | No                         | Variance explained     |

---

## 4. Underfitting and Overfitting

- **Underfitting:** Model too simple, fails to capture data patterns.
- **Overfitting:** Model too complex, memorizes training data instead of generalizing.
- **Cause in polynomial regression:** Using very high-degree polynomials.

**Prevention methods:**

1. Regularization (Lasso, Ridge).
2. Cross-validation.
3. Simpler models (lower-degree polynomials).

---

## 5. Real-World Case Study: Diabetes Progression

- **Goal:** Predict progression of diabetes disease.
- **Data:** Age, sex, BMI, blood pressure, and blood test results of 442 patients.
- **Model:** Multiple Linear Regression.
- **Results:** BMI and blood sugar were strong predictors. The model helped identify health factors linked to disease progression.

---

## References

- James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning*. Springer.
- UCI Machine Learning Repository: Diabetes Dataset.
