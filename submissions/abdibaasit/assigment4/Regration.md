Assignment Part A — Theory Questions
1. Introduction to Regression

Regression is a technique in machine learning that focuses on predicting numerical values. Instead of assigning data into categories, as in classification, regression produces a continuous output. For example, if a company wants to estimate next month’s sales based on advertising spending, regression is the suitable approach.

The difference between regression and classification lies mainly in the output. Classification predicts discrete labels such as “spam” vs. “not spam”, while regression predicts continuous numbers such as house prices, rainfall, or exam scores. For instance, a real-life example of regression is predicting the cost of a taxi ride based on distance and time. A common example of classification is detecting whether an email is spam or genuine.

2. Types of Regression
Linear Regression

Linear regression is the simplest form, where the model tries to draw a straight line that best fits the relationship between input and output. For example, predicting someone’s weight based on height can often be modeled linearly.

Advantage: Easy to understand and implement.

Limitation: Cannot capture complex, non-linear relationships.

Multiple Linear Regression

This method extends simple linear regression by using more than one input variable. For example, predicting house prices may depend not only on size but also on location and number of rooms.

Advantage: Uses several factors, making predictions more accurate.

Limitation: Becomes less reliable when independent variables are highly correlated (multicollinearity).

Polynomial Regression

Polynomial regression models the relationship using powers of the input variable, which allows it to capture curves. For example, predicting the speed of a car based on engine power may require a curved line rather than a straight one.

Advantage: Flexible, handles non-linear patterns.

Limitation: Can easily overfit the data if the polynomial degree is too high.

3. Regression Metrics

To evaluate regression models, several metrics are commonly used:

MAE (Mean Absolute Error): Average of absolute differences between predicted and actual values. It shows the typical size of an error.

MSE (Mean Squared Error): Squares the errors before averaging. This gives more weight to larger errors.

RMSE (Root Mean Squared Error): The square root of MSE. It has the same unit as the predicted variable, making it easier to interpret.

R² (Coefficient of Determination): Measures how much of the variation in the data is explained by the model. A higher R² means better fit.

| Metric | Units | Sensitivity to Large Errors | Meaning |
|--------|-------|-----------------------------|---------|
| MAE    | Same as target | Low  | Average absolute error |
| MSE    | Squared units  | High | Penalizes big errors   |
| RMSE   | Same as target | High | Typical error size     |
| R²     | None           | N/A  | % variance explained   |

4. Underfitting and Overfitting

Underfitting happens when the model is too simple and cannot capture the trend in the data. For example, using a straight line to fit curved data.

Overfitting happens when the model becomes too complex and starts memorizing noise instead of learning patterns. This is common in polynomial regression when the degree is too high.

Causes of Overfitting

Too many features in the model.

Using a very high-degree polynomial.

Insufficient training data.

Ways to Prevent Overfitting

Use cross-validation to test model performance on unseen data.

Apply regularization (such as Lasso or Ridge regression) to penalize large coefficients.

Simplify the model or collect more training data.

5. Real-World Case Study

A practical example of regression can be found in healthcare. In one study, researchers aimed to predict the risk of developing diabetes based on factors such as age, body mass index (BMI), and blood pressure.

Goal: To identify patients at high risk of diabetes early.

Data: Medical records including BMI, glucose levels, age, and lifestyle factors.

Model Used: Multiple linear regression, since more than one factor influenced the outcome.

Results: The model helped doctors estimate a patient’s likelihood of developing diabetes. By knowing this risk, hospitals could recommend lifestyle changes and preventive treatments.

This case study shows that regression is not just a mathematical tool but a valuable method that can guide real-world decision-making, especially in areas like public health.

References

James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). An Introduction to Statistical Learning. Springer.

Kuhn, M., & Johnson, K. (2019). Applied Predictive Modeling. Springer.