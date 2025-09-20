# 📝 Reflection Paper -- House Price Prediction

## 1. What did you implement?

In this project, I implemented a house price prediction model using
**Linear Regression** and **Random Forest Regressor**.\
The target variable was **Price**, and the input features were all other
columns (excluding `Price` and `LogPrice`).\
I trained both models on 80% of the dataset and evaluated them on the
remaining 20%.

------------------------------------------------------------------------

## 2. Comparison of Models

In the single-row sanity check (index = 3):

-   **Linear Regression** predicted \$594,041\
-   **Random Forest** predicted \$557,028\
-   **Actual Price** was \$554,800

Random Forest gave a prediction much closer to the actual price, while
Linear Regression overestimated.

------------------------------------------------------------------------

## 3. Understanding Random Forest

Random Forest is an **ensemble learning algorithm** that builds many
decision trees during training.\
Each tree makes a prediction, and the final output is the **average** of
all tree predictions (for regression tasks).\
This approach reduces overfitting, improves generalization, and captures
complex non-linear relationships that simple models may miss.

------------------------------------------------------------------------

## 4. Metrics Discussion

-   **Linear Regression:**\
    R² = 0.848, MAE = 63,086, RMSE = 75,624

-   **Random Forest:**\
    R² = 0.859, MAE = 52,524, RMSE = 72,686

Random Forest achieved slightly higher R² and lower error metrics.\
This shows that it fits the data better and makes more accurate
predictions.

------------------------------------------------------------------------

## 5. Your Findings

Both models performed well, but **Random Forest** was the stronger
choice.\
It captured non-linear patterns in the housing dataset and produced
predictions closer to actual values.

I would prefer **Random Forest** for future house price prediction tasks
because it balances accuracy and robustness.\
However, Linear Regression still provides a simple, interpretable
baseline that helps us understand feature importance and the general
trend of the data.
