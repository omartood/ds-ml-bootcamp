# 🎓 Assignment – House Price Prediction with Linear Regression & Random Forest
1. **What did you implement?**
- I implemented a house price prediction model using Linear Regression and Random Forest.
- The models predict the price of a house based on various features such as size, location, and number of rooms.

2. **Comparison of Models:**
**How predictions differed:** 
- When testing on a single row from the test set, the Linear Regression prediction and the Random Forest prediction were both close to the actual price, but usually not exactly the same.

Example:

| Actual Price | Linear Regression | Random Forest |
|--------------|-----------------|---------------|
| $535,300|  $609,615      |$538,756    |


**Observation:**

- Linear Regression slightly underestimated the actual price.
- Random Forest slightly overestimated, but was closer to the real value.

This shows that Linear Regression may struggle with non-linear patterns or extreme values in the dataset, while Random Forest adapts better.

## Which model gave more realistic results and why

Random Forest gave more realistic results for this single row.

**Reason:**
- Random Forest averages predictions from multiple decision trees, which helps it capture complex, non-linear relationships in the data.
- Linear Regression assumes a straight-line relationship between features and price, so it can under- or overestimate depending on the feature values.

Therefore, for individual houses, Random Forest predictions tend to be closer to reality.

3. **Understanding Random Forest:**

**Random Forest**: an ensemble learning method that creates multiple decision trees during training.
**How it works:** Each tree predicts a value; the final prediction is the average of all trees. This reduces overfitting and improves accuracy.

4. **Metrics Discussion:**

 **Random Forest**typically has higher R² and lower MAE/RMSE, meaning it predicts house prices more accurately.

**Linear Regression** is simpler but may not capture complex patterns in the data he only applies single linear line data.

5. **Your Findings:**
- Preferred Model: Random Forest, because it better handles non-linear relationships and gives more realistic 
    predictions.
- Linear Regression is faster and easier to interpret but less accurate for complex datasets.
- Random Forest is more robust to outliers and feature interactions, making it more suitable for house price prediction.