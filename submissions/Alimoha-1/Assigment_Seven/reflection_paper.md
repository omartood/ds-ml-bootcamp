# 🎓 Reflection Paper – House Price Prediction

## 1. What I Implemented
In this project, I trained two machine learning models — **Linear Regression** and **Random Forest Regressor** — to predict house prices.  
The dataset used was already cleaned in Lesson 3 (`clean_house_dataset.csv`). I prepared features (X) by dropping the `Price` and `LogPrice` columns, and set `Price` as the target (y).  
I then split the data (80% training, 20% testing), trained both models, and compared their performance using metrics: **R², MAE, MSE, RMSE**.

---

## 2. Comparison of Models
For the **sanity check (row i=3)**, I compared the actual house price with predictions from both models.  
- **Linear Regression** gave a more basic estimate.  
- **Random Forest** predictions were usually closer to the true value because it captures non-linear relationships.  

Overall, Random Forest gave more realistic predictions.

---

## 3. Understanding Random Forest
Random Forest is an **ensemble learning method** made up of many decision trees.  
- Each tree learns patterns from a random sample of the dataset and a random subset of features.  
- The model’s final prediction is the **average of predictions** from all the trees (for regression).  

This reduces overfitting and makes Random Forest more robust than a single decision tree.

---

## 4. Metrics Discussion
When comparing results:
- **Random Forest** had **higher R²** and **lower MAE/RMSE** than Linear Regression.  
- This means Random Forest explained more variance in the target and made smaller errors.  

Linear Regression is simple and interpretable, but it assumes linear relationships. Random Forest handles complex, non-linear patterns better.

---

## 5. Findings
Based on the results, **Random Forest** performed better for predicting house prices in this dataset.  
It gave more accurate predictions and adapted well to different features without strict assumptions.  

However, I also see value in **Linear Regression** as a baseline: it is fast, easy to interpret, and provides a benchmark to compare against.  

**Conclusion:** For practical price prediction, I prefer **Random Forest** because it balances accuracy and robustness. Linear Regression is useful for understanding overall trends, but Random Forest is better suited for real-world deployment.
