 Lesson 4 — Regression
Theory Assignment + Jupyter Setup Task
Due: Sunday, September 14, 2025 — 12:00 PM (EAT)
Goal: Understand the key concepts, types, and evaluation metrics of Regression in Machine Learning — and
successfully set up Jupyter Notebook using Anaconda.
 Part A — Theory Questions
1. Introduction to Regression
Regression is a type of supervised machine learning used to predict continuous numerical values. Unlike
classification, which predicts categories (e.g., spam or not spam, sick or healthy), regression predicts
quantities that can vary along a continuous scale.
Example of regression: Predicting the score difference between two football teams. Example of
classification: Determining whether an email is spam or not, or if a patient has a disease based on age and
symptoms.
2. Types of Regression
Linear Regression - How it works: Fits a straight line through the data points to predict outcomes. -
Example: Predicting house prices based on size in square feet — as size increases, price usually increases. -
Advantages: Simple, interpretable. - Limitations: Cannot capture non-linear relationships.
Multiple Linear Regression - How it works: Uses more than one feature to predict the target. - Example:
Predicting house prices using size, number of bedrooms, and location. - Advantages: Handles multiple
influencing factors. - Limitations: Assumes linear relationships; can overfit with many features.
Polynomial Regression - How it works: Uses powers of features (e.g., X², X³) to capture non-linear trends. -
Example: Modeling the trajectory of a ball in sports analytics. - Advantages: Captures non-linear patterns. -
Limitations: High-degree polynomials can overfit the data.
3. Regression Metrics
Metric What it measures Sensitivity to large
errors
Units
MAE (Mean Absolute
Error)
Average absolute prediction error Low
Same as
target
1
Metric What it measures Sensitivity to large
errors
Units
MSE (Mean Squared Error) Average squared prediction error High Squared
units
RMSE (Root Mean Squared
Error)
Square root of MSE High Same as
target
R² (Coefficient of
Determination)
Proportion of variance explained
by the model N/A 0–1
MAE: Measures average error magnitude.
MSE: Penalizes large errors more heavily.
RMSE: Provides error in the same units as the target.
R²: Indicates how much variation in the data the model can explain (e.g., 0.88 = 88%).
4. Underfitting and Overfitting
Underfitting: - Occurs when a model is too simple to capture the true data patterns. - Example: Using
linear regression on a clearly non-linear dataset.
Overfitting: - Happens when a model learns the training data too well but fails on new data. - Causes: Too
many features, small training dataset. - Prevention: Split data into training/test sets, stop training early,
remove irrelevant features.
5. Real-World Case Study
Goal: Predict goals scored by two Premier League teams (e.g., Manchester City vs Tottenham).
Features: Home team, away team, home goals scored, away goals scored, last 5 match goals (home
and away), team positions, head-to-head results.
Target: Goals scored in the match.
Insights: Regression models can help forecast match outcomes and support betting or strategic
planning.
 Part B — Practical Jupyter Setup Task
Install Anaconda.
Open Jupyter Notebook from Anaconda Navigator.
Create a new Python notebook.
Enter the following code:
print("Hello, World!")
arr = [1,2,3,4,5,6,7]
print(arr)
•
•
•
•
•
•
•
•
1.
2.
3.
4.
2
Run the cells. Output should display:
Hello, World!
[1, 2, 3, 4, 5, 6, 7]
5.
3