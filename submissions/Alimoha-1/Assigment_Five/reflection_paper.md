#  Reflection Paper – House Price Prediction

## 1. Project Implementation  
In this project, I built and evaluated two machine learning models — **Linear Regression** and **Random Forest Regressor** — to predict house prices.  

The dataset had already been cleaned and prepared during Lesson 3 (`clean_house_dataset.csv`). I defined the **features (X)** by removing the `Price` and `LogPrice` columns to prevent data leakage, and selected `Price` as the **target (y)**.  

I then split the dataset into training and testing subsets (80% / 20%), ensuring that the evaluation remained fair and reproducible by fixing `random_state=42`.  
After that, I trained both models, generated predictions, and compared their performance using four standard regression metrics: **R², MAE, MSE, and RMSE**.  

This pipeline represents a typical supervised learning workflow: **data preparation → model training → evaluation → interpretation**.

---

## 2. Comparison Between the Models  
### Linear Regression  
- Works by fitting a straight line (or hyperplane) to minimize errors.  
- Provides coefficients that are easy to interpret.  
- Tends to underfit when relationships between features and price are non-linear.  

### Random Forest Regressor  
- An **ensemble model** that combines predictions from multiple decision trees.  
- Captures complex, non-linear relationships in the dataset.  
- Reduces the risk of overfitting compared to a single decision tree by averaging predictions.  

### Observations  
During the **sanity check** (testing row `i=3`):  
- **Linear Regression** gave a baseline estimate but missed some details.  
- **Random Forest** prediction was much closer to the actual house price, confirming its ability to adapt to feature interactions.  

Overall, Random Forest consistently outperformed Linear Regression.

---

## 3. Deep Dive into Random Forest  
Random Forest is powerful because:  
1. **Random Sampling (Bagging):** Each tree is trained on a bootstrapped sample of the dataset.  
2. **Random Feature Selection:** Each tree considers a random subset of features when splitting.  
3. **Aggregation:** Predictions from all trees are averaged (for regression).  

These properties make the model:  
- More robust to noise in the data.  
- Better at capturing non-linear relationships.  
- Less prone to overfitting compared to a single tree.  

This explains why Random Forest gave stronger performance than Linear Regression.

---

## 4. Metrics Interpretation  
To fairly evaluate the models, I analyzed four metrics:  

- **R² (Coefficient of Determination):** Measures how much variance in the target is explained by the model. Higher is better.  
- **MAE (Mean Absolute Error):** Average magnitude of errors in predictions, without considering direction.  
- **MSE (Mean Squared Error):** Like MAE but squares errors, penalizing larger mistakes more heavily.  
- **RMSE (Root Mean Squared Error):** Square root of MSE, expressed in the same units as the target (Price).  

### Results  
- **Random Forest:** Higher R², lower MAE/MSE/RMSE → better accuracy.  
- **Linear Regression:** Lower R², higher errors → weaker fit.  

This showed that Random Forest explained more variance in house prices and produced fewer large mistakes.

---

## 5. Findings and Reflections  
From the experiments, my key findings are:  
- **Random Forest** was the superior model for this dataset due to its ability to handle non-linearity and diverse feature interactions.  
- **Linear Regression**, although weaker in predictive power, was useful as a baseline. It is interpretable and fast, which is valuable in scenarios where transparency is required.  
- Performance metrics confirmed my expectations: Random Forest achieved better generalization, while Linear Regression was limited by its linear assumptions.  

### Personal Reflection  
Working on this project helped me understand the importance of comparing models with different complexities.  
- A simple model like Linear Regression provides interpretability but may miss subtle relationships.  
- A more advanced ensemble like Random Forest improves accuracy but sacrifices interpretability.  

In real-world applications such as real estate, where accurate predictions can influence financial decisions, I would choose **Random Forest** because it balances **accuracy, robustness, and generalization**. However, I recognize the importance of still including a simple baseline model to benchmark against.  

---

✅ **Conclusion:** Random Forest is better suited for house price prediction in this dataset. Linear Regression still plays an important role as a baseline model, but for deployment, Random Forest is the stronger choice.  
