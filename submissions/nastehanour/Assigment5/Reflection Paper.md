## House Price Prediction with Linear Regression & Random Forest
 
## What Did You Implement?

In this project, I implemented two supervised machine learning models—**Linear Regression (LR)** and **Random Forest (RF)**—to predict house prices. The dataset contained 99 records with 13 features, including size, number of bedrooms, age of the house, and location indicators. After preprocessing, the data was split into training (80%) and testing (20%) sets. Linear Regression was trained as a baseline model to capture linear relationships, while Random Forest was trained to model more complex, nonlinear interactions.

## Comparison of Models

During the **sanity check on three test samples**, the predictions differed noticeably:

* Linear Regression often **underestimated prices**, deviating significantly from actual values.
* Random Forest predictions were **much closer to the true prices**, capturing patterns missed by Linear Regression.

For example, when the actual price was **$292,500**, Linear Regression predicted **$188,637**, while Random Forest predicted **$290,899**. This shows that RF gave more realistic results because it considers nonlinear relationships and interactions among features.

## Understanding Random Forest

**Random Forest** is an **ensemble learning method** based on decision trees. Instead of relying on a single tree, it builds many trees using bootstrapped samples of the training data. Each tree makes a prediction, and the final result is obtained by averaging the predictions (for regression tasks). This process reduces overfitting and increases accuracy, making Random Forest more robust than individual trees.

## Metrics Discussion

The evaluation metrics showed that **Random Forest performed better** than Linear Regression:

| Model             | R²    | MAE ($) | RMSE ($) |
| ----------------- | ----- | ------- | -------- |
| Linear Regression | 0.848 | 63,086  | 75,624   |
| Random Forest     | 0.859 | 52,524  | 72,686   |

Random Forest achieved a slightly higher R² and significantly lower error values (MAE, RMSE). This indicates that while Linear Regression is interpretable and provides a solid baseline, Random Forest is more effective for capturing complex housing price patterns.

## my Findings

From this practice, I conclude that **Random Forest is the stronger model for house price prediction**. It consistently produced more realistic results in sanity checks and achieved lower prediction errors across evaluation metrics. Although Linear Regression is simple and interpretable, it struggled to model the nonlinear relationships in the dataset.

Therefore, for practical applications where accuracy is critical, Random Forest should be preferred. However, Linear Regression still has value as a quick, interpretable baseline model to understand general trends and feature importance.

---
