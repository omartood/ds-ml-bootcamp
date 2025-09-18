# House Price Prediction: Linear Regression & Random Forest

## 1. Data Preparation
- Loaded a cleaned dataset with house features and target prices.
- Split the data into **features (X)** and **target (y = Price)**, dropping columns like `LogPrice` to avoid target leakage.
- Divided the data into **training (80%)** and **testing (20%)** sets for evaluation.

## 2. Linear Regression (LR)
- Created a linear model using `LinearRegression()`.
- Fitted it on the training data to learn coefficients that best predict house prices.
- Made predictions on the test set.
- Serves as a simple, interpretable baseline model.

## 3. Random Forest (RF)
- Created an ensemble model using `RandomForestRegressor(n_estimators=100)`.
- Each tree learned patterns from training data via feature splits.
- Predictions were averaged across all trees to capture non-linear relationships and improve accuracy.

## 4. Evaluation
- Measured performance using **R²**, **MAE**, **MSE**, and **RMSE**.
- Conducted a **single-row sanity check** to see predictions for an individual house.

## Summary
- **Linear Regression** captures linear trends in the data.
- **Random Forest** captures complex, non-linear relationships, often leading to better predictive performance.


# Model Comparison: Sanity Check Predictions

| Actual Price | Linear Regression (LR) | Random Forest (RF) |
|-------------:|----------------------:|------------------:|
| $395,900     | $552,711             | $551,299          |
| $571,000     | $486,276             | $551,531          |
| $654,200     | $718,486             | $777,862          |

## Observations
- **Linear Regression** predictions:
  - Overestimates lower-priced houses (e.g., $395,900 → $552,711).
  - Underestimates higher-priced houses (e.g., $571,000 → $486,276).  
  - Tends to “pull” predictions toward the mean due to its linear nature.

- **Random Forest** predictions:
  - More consistent across different price ranges.
  - Captures some non-linear patterns, but sometimes slightly overshoots (e.g., $654,200 → $777,862).  

## Which Model is More Realistic?
- **Random Forest** generally gives more realistic predictions for individual houses.
- Reason:
  - RF can capture **non-linear relationships** between features and price.
  - LR is limited to **linear trends**, causing under- or overestimation at the extremes.

# Random Forest

## What is Random Forest?
Random Forest is a **machine learning model** used for prediction (like house prices).  
- It’s called a “forest” because it is made up of **many decision trees**.  
- Each tree is like a little expert that tries to guess the output.  
- By combining the trees, the model becomes **more accurate and stable** than a single tree.  

## How does it work?

### 1. Build many decision trees
- Each tree is trained on a **random sample of the data**.  
- Each tree decides how to **split the data based on the features** (like size, rooms, location).  

### 2. Make predictions with all trees
- Each tree gives a **prediction** for a given input.  

### 3. Average the predictions
- **Regression** (predicting numbers, like house prices): the final prediction is the **average** of all trees’ predictions.  
- **Classification** (predicting categories): the final prediction is the **majority vote**.  

## Key idea
- Random Forest **reduces errors** by combining many “opinions” (trees) rather than relying on a single model.  
- It can handle **complex, non-linear relationships** in the data.

# Metrics Discussion: Linear Regression vs Random Forest

## Metrics Comparison
- **R² (coefficient of determination):**  
  - Higher R² means the model explains more variance in the data.  
  - Random Forest usually has **higher R²** than Linear Regression because it captures non-linear relationships.  

- **Error metrics (MAE, RMSE):**  
  - Lower values are better.  
  - Random Forest usually has **lower MAE and RMSE**, meaning its predictions are closer to actual house prices.  

## Interpretation

### Linear Regression (LR)
- **Strengths:** Simple, interpretable, fast to train.  
- **Weaknesses:** Limited to **linear trends**; struggles with extreme values → errors higher at very cheap or expensive houses.  

### Random Forest (RF)
- **Strengths:** Captures **complex, non-linear relationships**; more accurate across all price ranges.  
- **Weaknesses:** Less interpretable; slower to train and predict compared to LR.  

## Conclusion
- Random Forest is generally better for predicting house prices due to its flexibility and accuracy.  
- Linear Regression is good as a baseline or when interpretability is important.


## Preferred Model for Price Prediction

For price prediction, I prefer **Random Forest** over Linear Regression. Random Forest generally achieves higher **R² scores** and lower **error metrics** like **MAE** and **RMSE**, meaning it captures complex patterns in the data more accurately. Unlike Linear Regression, which assumes a linear relationship, Random Forest can handle non-linear interactions without extensive feature engineering.

Although Random Forest can be more computationally intensive and less interpretable, its improved accuracy and robustness to outliers make it more reliable for real-world price prediction tasks. Linear Regression may be preferred only for simplicity or interpretability, but overall, **Random Forest** offers the best balance between performance and reliability.
