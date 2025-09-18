## Introduction to Regression

Regression is a supervised machine learning method used to predict continuous numerical outcomes. It explores the relationship between input features (independent variables) and a target value (dependent variable).

For example, given factors like house size, number of rooms, and neighborhood, a regression model can predict the price of the house.

The key difference from classification is the type of output:

Regression → predicts numbers (e.g., salary amount).

Classification → predicts categories (e.g., employed vs. unemployed).

Example: Predicting a student’s exam score (regression) vs. predicting whether they pass or fail (classification).

## Major Types of Regression


a) Simple Linear Regression

This is the most basic type. It assumes a straight-line relationship between a single input variable and the output.

Use case: Predicting house price based only on square footage.

Advantages: Easy to use and interpret.

Limitations: Limited to linear relationships with just one predictor; sensitive to outliers.

b) Multiple Linear Regression

An extension of simple linear regression where the output depends on several input variables at once.

Use case: Estimating car prices using mileage, age, and brand.

Advantages: More realistic since real-life outcomes depend on multiple factors.

Limitations: Struggles if features are highly correlated (multicollinearity) or irrelevant; assumes linearity between all features and the target.

c) Polynomial Regression

Polynomial regression models curved relationships by adding higher-order terms (e.g., 
𝑥
2
,
𝑥
3
x
2
,x
3
).

Use case: Predicting population growth where the increase is not constant over time.

Advantages: Can capture non-linear patterns more effectively than linear regression.

Limitations: High-degree polynomials can lead to overfitting; harder to interpret.

👉 In short:

Simple Linear = one factor, straight line.

Multiple Linear = many factors, straight line.

Polynomial = can bend into curves for complex patterns.

## Metrics to Evaluate Regression

| Metric   | Definition                             | Units          | Sensitive to Outliers? | Meaning                            |
| -------- | -------------------------------------- | -------------- | ---------------------- | ---------------------------------- |
| **MAE**  | Average absolute error                 | Same as target | No                     | Shows typical size of errors       |
| **MSE**  | Average squared error                  | Squared units  | Yes                    | Penalizes large mistakes heavily   |
| **RMSE** | Square root of MSE                     | Same as target | Yes                    | Indicates overall prediction error |
| **R²**   | Proportion of variance explained (0–1) | None           | No                     | Higher = better model fit          |

## Underfitting vs. Overfitting

Underfitting: Model is too simple, missing important patterns (e.g., using a straight line for curved data).

Overfitting: Model is too complex, fitting noise instead of real patterns (e.g., very high-degree polynomial).

Preventing Overfitting:

Use cross-validation for fair testing.

Apply regularization (Ridge, Lasso).

Reduce irrelevant features or keep polynomial degree low.

## Case Study: Finance Sector

In banking, regression is widely used to predict customer credit scores or loan amounts.

Goal: Estimate how much money a customer is eligible to borrow.

Data Used: Income, employment history, credit history, and age.

Model Applied: Multiple Linear Regression.

Outcome: The model identified income and past credit history as the strongest predictors, helping banks reduce loan risks.

##  Conclusion

Regression is a powerful tool in machine learning for predicting continuous outcomes. Simple linear regression provides a starting point, multiple regression captures several influences, and polynomial regression handles non-linear data. Evaluation metrics (MAE, MSE, RMSE, R²) ensure the model’s accuracy. Understanding underfitting and overfitting is essential for building reliable predictions.

Applications of regression span across industries—finance, healthcare, real estate, and beyond—making it a cornerstone of data-driven decision-making.
