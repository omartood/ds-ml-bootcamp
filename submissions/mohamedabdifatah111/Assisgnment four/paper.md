1. Introduction to Regression

Regression is a supervised learning technique in machine learning that focuses on predicting continuous numerical values. The main idea is to model the relationship between input variables (features) and an output variable (target). By finding patterns in data, regression allows us to estimate future outcomes or unknown values.

Regression differs from classification because classification predicts discrete labels or categories, while regression predicts continuous outcomes. For example, predicting the price of a house is regression, whereas predicting whether an email is spam or not spam is classification.

2. Types of Regression
Linear Regression

Linear regression models the relationship between one independent variable and one dependent variable using a straight line. It assumes a linear relationship of the form y = mx + c.
Use case: Predicting student exam scores based on study hours.
Advantages: Simple to implement and interpret.
Limitations: Cannot model complex, non-linear relationships.

Multiple Linear Regression

Multiple linear regression extends linear regression to include two or more independent variables. The model takes the form y = b0 + b1x1 + b2x2 + ... + bnxn.
Use case: Predicting house prices based on size, location, and number of rooms.
Advantages: Can account for multiple factors influencing the outcome.
Limitations: Assumes linearity and independence of variables, which may not hold true.

Polynomial Regression

Polynomial regression fits a curved line by including higher-order terms of the independent variable, e.g., y = b0 + b1x + b2x² + ... + bnx^n.
Use case: Modeling the growth of populations over time.
Advantages: Captures non-linear relationships effectively.
Limitations: Prone to overfitting if the polynomial degree is too high.

3. Regression Metrics
Mean Absolute Error (MAE)

MAE measures the average absolute difference between predicted and actual values. It shows how far predictions are, on average, from the true values.

Mean Squared Error (MSE)

MSE calculates the average of squared differences between predicted and actual values. Squaring emphasizes larger errors more strongly.

Root Mean Squared Error (RMSE)

RMSE is the square root of MSE. It gives error values in the same unit as the target variable, making interpretation easier.

Coefficient of Determination (R²)

R² measures how well the regression model explains the variability of the target variable. A value close to 1 indicates a good fit.

Comparison Table

Metric	Units	Sensitivity to Large Errors	Meaning
MAE	Same as target variable	Less sensitive	Average magnitude of errors
MSE	Squared units	More sensitive	Penalizes large errors heavily
RMSE	Same as target variable	More sensitive	Standard deviation of prediction errors
R²	Unitless (0–1)	Not sensitive	Proportion of variance explained
4. Underfitting and Overfitting

Underfitting occurs when a model is too simple to capture the underlying trend in the data. It leads to poor performance on both training and test sets.

Overfitting happens when a model learns not only the trend but also the noise in the training data. As a result, it performs well on training data but poorly on unseen data. In polynomial regression, overfitting is common when the degree of the polynomial is unnecessarily high.

Methods to Prevent Overfitting:

Use cross-validation to select the right model complexity.

Apply regularization methods such as Ridge or Lasso regression.

Reduce the number of features or simplify the model.

5. Real-World Case Study

One notable example of regression in practice is in healthcare cost prediction. A study used multiple linear regression to estimate patient hospital costs based on variables such as age, diagnosis, length of stay, and treatment type.

Goal: To predict and manage healthcare expenses more effectively.
Data Used: Patient demographics, medical history, and treatment records.
Model Applied: Multiple Linear Regression.
Key Results: The model highlighted that length of stay and type of treatment were strong predictors of hospital costs. Hospitals could use this insight for budgeting and policy planning.
