# Reflection Paper: House Price Prediction with Linear Regression & Random Forest

## What Did I Implement?

In this project, I implemented two machine learning models—**Linear Regression** and **Random Forest Regressor**—to predict house prices using a cleaned dataset. I started by preparing the data: I selected all columns except `Price` and `LogPrice` as features (`X`), and used `Price` as the target variable (`y`). I split the data into training and testing sets (80% train, 20% test) to ensure fair evaluation. Then, I trained both models on the training data and evaluated their performance on the test set using standard regression metrics: R², MAE, MSE, and RMSE. Finally, I performed single-row sanity checks by predicting the price of individual houses and comparing the predictions to the actual prices.

## Comparison of Models

To compare the models, I tested three different rows from the test set:

- **i = 2**
  - Actual Price: $292,500
  - LR Predicted: $188,637
  - RF Predicted: $290,899

- **i = 5**
  - Actual Price: $419,200
  - LR Predicted: $411,139
  - RF Predicted: $297,368

- **i = 9**
  - Actual Price: $812,100
  - LR Predicted: $825,316
  - RF Predicted: $832,261

From these results, I observed that the predictions from both models can be close to the actual price, but sometimes one model is much more accurate than the other. For example, for row 2, Random Forest was almost exactly correct, while Linear Regression was much lower. For row 5, Linear Regression was closer to the actual price, while Random Forest underestimated. For row 9, both models were very close to the actual price.

Overall, **Random Forest** often gave more realistic results, especially when the relationship between features and price was not strictly linear. This is because Random Forest can capture more complex patterns in the data.

## Understanding Random Forest

**Random Forest** is an ensemble machine learning algorithm that builds many decision trees and combines their predictions. Each tree is trained on a random subset of the data and features, which helps reduce overfitting and increases robustness. When making a prediction, Random Forest averages the predictions from all its trees (for regression tasks like this one). This approach allows it to model complex, non-linear relationships in the data, making it more flexible than a single decision tree or a linear model.

## Metrics Discussion

When comparing the models using R², MAE, and RMSE, I found that Random Forest generally had slightly better (higher) R² and lower error metrics than Linear Regression. This means Random Forest explained more of the variance in house prices and made more accurate predictions on average. Linear Regression, while simple and interpretable, struggled when the relationship between features and price was not perfectly linear.

These results show that **Linear Regression** is a good baseline and easy to interpret, but **Random Forest** is stronger when the data has complex patterns or non-linear relationships.

## My Findings

Based on my experiments, I prefer **Random Forest** for house price prediction. It consistently provided more accurate and realistic predictions, especially for rows where the relationship between features and price was not straightforward. While Linear Regression is useful for its simplicity and interpretability, Random Forest's ability to handle complexity and reduce overfitting makes it a better choice for this type of problem. In real-world scenarios where accuracy is important, Random Forest is likely to perform better and provide more reliable estimates for house prices.