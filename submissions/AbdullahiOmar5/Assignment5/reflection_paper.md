# 🛠️ 1. What Did You Implement?

- First, I imported the necessary libraries: `pandas`, `numpy`, and `sklearn`.
- Then, I loaded the CSV file into a pandas DataFrame and displayed the first few rows and the shape of the dataset.
- I separated the DataFrame into features (`X`) and the target variable (`y`).
- I split the data into training and testing sets using `train_test_split` from `sklearn`.
- I created two models: **Linear Regression** and **Random Forest Regressor**.

### Model Explanation:
- **Linear Regression** assumes a linear relationship between features and the target variable.
- **Random Forest Regressor** is an ensemble model that combines multiple decision trees to improve prediction accuracy.

- I trained both models on the training dataset.
- I made predictions on the test dataset using both models.
- I evaluated model performance using metrics: **R²**, **MAE**, **MSE**, and **RMSE**.
- Finally, I printed the evaluation metrics to compare both models.

---

# 🔍 2. Comparison of Models

### Sanity Check Results:
- **Row 1**: Actual = \$642,500  
  - Linear Regression = \$656,755  
  - Random Forest = \$789,031  
  → RF overestimated significantly.

- **Row 2**: Actual = \$948,600  
  - Linear Regression = \$822,635  
  - Random Forest = \$821,977  
  → Both underestimated, LR slightly closer.

- **Row 3**: Actual = \$292,500  
  - Linear Regression = \$188,637  
  - Random Forest = \$290,899  
  → RF was very close, LR underestimated.

- **Row 4**: Actual = \$554,800  
  - Linear Regression = \$594,041  
  - Random Forest = \$557,028  
  → RF was very close, LR overestimated.

### Which Model Gave More Realistic Results?
- **Random Forest** gave more realistic predictions overall.
- It captured complex relationships better due to its ensemble nature.
- Linear Regression had larger deviations and struggled with non-linear patterns.

---

# 🌲 3. Understanding Random Forest

### What Is Random Forest?
- Random Forest is an **ensemble learning method** used for regression and classification.
- It builds multiple decision trees and combines their predictions.

### How Does It Work?
- Each tree makes predictions based on random subsets of data.
- For classification: majority vote.
- For regression: average of all tree predictions.
- This ensemble approach improves accuracy and reduces overfitting.

---

# 📊 Metrics Discussion

### Which Model Had Better Metrics?
- **Random Forest** had better:
  - R² score: **0.86** vs. **0.84** (Linear Regression)
  - Lower MAE and RMSE values

### What Does That Tell Us?
- RF is more robust and accurate for this dataset.
- It handles non-linear relationships and feature interactions well.
- LR is simpler and interpretable but limited in complex scenarios.

---

# ✅ Your Findings

Based on the evaluation metrics and sanity checks, I prefer the **Random Forest model** for price prediction. It consistently produced predictions closer to actual values and had better performance across all metrics.

Its ability to model complex, non-linear relationships and reduce overfitting makes it a stronger choice for datasets with many features and interactions. While Linear Regression is simpler and easier to interpret, it lacks the flexibility needed for more nuanced data patterns.
