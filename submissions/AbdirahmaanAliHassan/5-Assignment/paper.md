Part B – Reflection Paper

## What I Implemented

I implemented a **house price prediction system** using two models: **Linear Regression** and **Random Forest Regressor**.

- **Linear Regression** fitted a straight-line relationship between features and price.
- **Random Forest Regressor** (100 trees, random_state=42) aggregated predictions from multiple decision trees to capture complex, non-linear relationships.

The target variable was **Price**, while all other features (except `Price` and `LogPrice`) were used as predictors.

---

## Comparison of Models (Sanity Checks)

I tested the models on **3 rows** from the test set:


| Index | Actual Price | Linear Predicted | RF Predicted | Closer Model      |
| ----- | ------------ | ---------------- | ------------ | ----------------- |
| 9     | 812,100      | 825,316          | 832,261      | Linear Regression |
| 5     | 419,200      | 411,139          | 297,368      | Linear Regression |
| 11    | 571,000      | 486,276          | 551,531      | Random Forest     |

**Observation:**

- At Index 9, both models were close, but Linear Regression was slightly more accurate.
- At Index 5, Linear Regression was clearly better.
- At Index 11, Random Forest produced the closest prediction.

This shows that **Random Forest can adapt better to non-linear patterns**, while **Linear Regression gives more stable but sometimes less flexible predictions**.

---

## Understanding Random Forest

Random Forest is an **ensemble algorithm** built from many **decision trees**.

- Each tree is trained on random samples of the data and features.
- For regression, predictions are averaged across all trees.
- This reduces overfitting and improves generalization compared to a single decision tree.

---

## Metrics Discussion

- **Random Forest** had a higher **R²** and lower error metrics (**MAE, RMSE**) when evaluated on the full test dataset.
- **Linear Regression** is simple, fast, and interpretable, but struggles with complex feature interactions.
- **Random Forest** handles complexity better but may sometimes make larger mistakes on individual predictions (like Index 5).

---

## Findings
Although **Linear Regression** performed better in two out of the three sanity checks, overall I prefer the **Random Forest Regressor**. The reasons are:  
- Random Forest achieved a **higher R² and lower error metrics (MAE, RMSE)** when evaluated on the entire test set, showing stronger overall accuracy compared to Linear Regression.  
- House prices usually follow **complex, non-linear patterns**, which Random Forest can capture more effectively, while Linear Regression is limited to straight-line relationships.  
- Random Forest is more **robust to diverse data** and can model feature interactions, leading to more reliable predictions in practical use cases.  

**Conclusion:** Random Forest is the better choice when accuracy and capturing complex relationships are the priority, while Linear Regression remains a fast and interpretable baseline.  

**Conclusion:**

- Use **Random Forest** when accuracy is the priority.
- Use **Linear Regression** as a simple, explainable benchmark.
