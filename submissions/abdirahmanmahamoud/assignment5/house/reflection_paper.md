# Reflection Paper – House Price Prediction

## 1. What did you implement?

In this assignment, I implemented **house price prediction** using two models: **Linear Regression** and **Random Forest Regressor**.  
I prepared the features (`X`) by dropping the `Price` and `LogPrice` columns, and used `Price` as the target (`y`).  
The dataset was split into 80% training and 20% testing with `random_state=42` for reproducibility.

Both models were trained on the training set and evaluated on the test set using standard regression metrics: **R², MAE, MSE, and RMSE**.

---

## 2. Comparison of Models

When testing with the metrics, both models performed well, but **Random Forest consistently outperformed Linear Regression**:

- **Linear Regression** had an R² of **0.848**, MAE ≈ 63,086, and RMSE ≈ 75,624.
- **Random Forest** had an R² of **0.859**, MAE ≈ 52,524, and RMSE ≈ 72,686.

In the **single-row sanity check** (Actual Price: \$535,300):

- Linear Regression predicted \$609,615 (overestimated).
- Random Forest predicted \$538,756 (very close to the actual price).

This shows Random Forest is more **realistic and reliable** for this dataset.

---

## 3. Understanding Random Forest

**Random Forest** is an **ensemble learning method** that builds multiple decision trees and combines their predictions.

- For regression, it averages the results of many trees.
- This reduces overfitting (compared to a single decision tree) and captures **non-linear relationships** better than a linear model.

In simple terms, Random Forest is like asking **many experts** for their opinion and then taking the average — leading to more stable and accurate predictions.

---

## 4. Metrics Discussion

The comparison of metrics showed:

- **Random Forest** achieved higher **R²** and lower **MAE/RMSE**.
- **Linear Regression** was slightly worse, likely because it assumes a strict linear relationship between features and target.

This indicates:

- Linear Regression is a good **baseline** and easy to interpret.
- Random Forest is more powerful for **complex, real-world data** where relationships are not purely linear.

---

## 5. Findings

From this project, I found that:

- **Linear Regression** is simple and interpretable, but can struggle with complex datasets.
- **Random Forest** provides better accuracy and more realistic predictions for house price prediction.

I would prefer **Random Forest** for practical applications because it produced results closer to actual prices and achieved stronger metrics. However, Linear Regression is still valuable as a quick baseline and for interpretability in cases where understanding feature impact is more important than raw accuracy.
