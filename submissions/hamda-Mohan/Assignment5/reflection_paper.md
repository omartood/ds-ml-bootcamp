# Reflection Paper – House Price Prediction

## What did you implement?  
In this assignment, I trained two regression models — **Linear Regression (LR)** and **Random Forest (RF)** — to predict house prices using a cleaned housing dataset. The target variable was *Price*, and all other columns except *Price* and *LogPrice* were used as features. **The dataset was manually cleaned by me**, ensuring that missing values, outliers, and inconsistencies were handled appropriately. The dataset was then split into training (80%) and testing (20%) sets for fair evaluation. Both models were trained on the training data, and their performance was evaluated on the test set using metrics such as **R²**, **Mean Absolute Error (MAE)**, **Mean Squared Error (MSE)**, and **Root Mean Squared Error (RMSE)**.

---

## Comparison of Models (Sanity Check)  
To see how the models perform on individual examples, I conducted a sanity check using three samples from the test set. The table below summarizes the results:

| Sample | Actual Price | LR Prediction | RF Prediction | Closer Model |
|--------|--------------|---------------|---------------|--------------|
| 2      | 292,500      | 188,637       | 291,111       | RF           |
| 4      | 535,300      | 609,615       | 536,285       | RF           |
| 6      | 367,500      | 444,366       | 395,333       | RF           |

From these sanity checks, it is clear that **Random Forest predictions are generally closer to the actual prices**, while Linear Regression sometimes overestimates or underestimates. This indicates that although LR can work for simple trends, RF handles variability and complex patterns in the data better.

---

## Understanding Random Forest  
Random Forest is an **ensemble learning method** that builds many decision trees during training. Each tree is trained on a random subset of the data and features. During prediction, the model takes the average of all tree predictions to produce the final result. This approach reduces overfitting, improves accuracy, and is particularly useful when the data contains non-linear relationships or outliers.  

In contrast, Linear Regression assumes a straight-line relationship between the features and the target, which may not always be accurate in real-world datasets.

---

## Metrics Discussion  
The overall performance of the two models on the test set is summarized below:

| Metric | Linear Regression | Random Forest |
|--------|------------------|---------------|
| R²     | 0.848            | 0.859         |
| MAE    | 63,086           | 52,524        |
| MSE    | 5,718,940,941    | 5,283,317,455 |
| RMSE   | 75,624           | 72,686        |

Random Forest achieved a higher **R²** and lower error metrics (MAE, RMSE) than Linear Regression. This demonstrates that RF can better capture complex relationships in the data, whereas LR may underperform when the features and target are not strictly linearly related.

---

## Your Findings  
Based on both the sanity check and the overall metrics, **Random Forest is the preferred model** for predicting house prices. It provides more accurate and reliable predictions across different scenarios. Linear Regression, while simple and interpretable, does not always capture the complexity of housing data and can produce larger errors.  

Overall, for tasks like house price prediction where relationships between features are not strictly linear and outliers exist, **Random Forest offers a strong balance between accuracy and robustness**, making it the better choice.  

