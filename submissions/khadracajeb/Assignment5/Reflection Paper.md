# Part B – Reflection Paper: House Price Prediction with Linear Regression & Random Forest

## What Did I Implement?

In this project, I implemented two machine learning models—**Linear Regression** and **Random Forest Regressor**—to predict house prices using a cleaned dataset.  

- **Data Preparation:** I selected all columns except `Price` and `LogPrice` as features (X) and used `Price` as the target variable (y).  
- **Train-Test Split:** I divided the dataset into 80% training and 20% testing sets to ensure fair evaluation.  
- **Model Training:** Both Linear Regression and Random Forest models were trained on the training set.  
- **Evaluation:** Performance was assessed on the test set using standard regression metrics: **R², MAE, MSE, and RMSE**.  
- **Sanity Checks:** Single-row predictions were performed to compare model outputs with actual prices.

---

## Comparison of Models

I selected three different rows from the test set to perform sanity checks and compare model predictions:

| Row (i) | Actual Price | Linear Regression Prediction | Random Forest Prediction |
|---------|--------------|----------------------------|-------------------------|
| 5       | $419,200     | $411,139                   | $297,368                |
| 12      | $345,900     | $420,031                   | $393,837                |
| 7       | $743,700     | $727,107                   | $724,944                |

**Observations:**  
- For **row 5**, Linear Regression was closer to the actual price, while Random Forest underestimated.  
- For **row 12**, Random Forest provided a better estimate than Linear Regression.  
- For **row 7**, both models were close to the actual price, with Linear Regression slightly underestimating.  

Overall, **Random Forest often gives more realistic predictions**, especially when the relationship between features and price is not strictly linear.

---

## Understanding Random Forest

**Random Forest** is an ensemble learning algorithm that builds **many decision trees** and combines their predictions.  

- Each tree is trained on a **random subset of the data** and features, which reduces overfitting.  
- For regression tasks, Random Forest **averages the predictions** from all trees.  
- This approach allows it to capture **complex, non-linear relationships** in the data, making it more flexible than a single decision tree or Linear Regression.

---

## Metrics Discussion

When evaluating the models with **R², MAE, and RMSE**:  

- Random Forest generally achieved **higher R²** and **lower error metrics** compared to Linear Regression, indicating more accurate predictions and better variance explanation.  
- Linear Regression is simpler and more interpretable but may struggle with **non-linear relationships** between features and price.  

These results highlight that Linear Regression is a good **baseline**, while Random Forest is stronger for datasets with **complex patterns**.

---

## My Findings

Based on my experiments of this lesson:  

- I prefer **Random Forest** for house price prediction because it handles complexity, reduces overfitting, and provides **more realistic predictions**, especially when feature relationships are non-linear.  
- Linear Regression remains useful for its **simplicity and interpretability**, but for real-world scenarios where accuracy matters, **Random Forest is the better choice**.  
