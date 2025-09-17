# House Price Prediction Report

## What Did You Implement?
I built two machine learning models to predict house prices: **Linear Regression (LR)** and **Random Forest (RF)**.  
The data included features like location, size, and other housing characteristics.  
The target (what we want to predict) was the **Price** column. I trained the models by splitting the dataset into training and testing sets.  

## Training the Models
- **Linear Regression**: This model tries to fit a straight-line relationship between the features and the house price. It assumes the data follows a linear trend.  
- **Random Forest**: This model is based on many decision trees. Each tree makes its own prediction, and the forest averages the results to give a final prediction.  

## Comparison of Models (Sanity Check)
I tested both models on **three unseen houses (from `X_test`)**.  

| House | Actual Price | LR Prediction | RF Prediction |
|-------|--------------|---------------|---------------|
| 1     | $292,500     | $188,637      | $290,899      |
| 2     | $554,800     | $594,041      | $557,028      |
| 3     | $367,500     | $444,366      | $396,774      |

### Observations
- **Linear Regression** often predicted too high or too low, missing the real values by a large margin.  
- **Random Forest** predictions were much closer to the actual prices in all three cases.  
- This shows Random Forest gave more realistic results because it can capture complex patterns.  

## Understanding Random Forest
- **What it is**: Random Forest is an *ensemble model* that uses many decision trees.  
- **How it works**:  
  1. Each decision tree looks at random parts of the data.  
  2. Each tree gives a prediction.  
  3. The forest averages these predictions (for regression tasks like price prediction).  

This makes Random Forest more stable and accurate compared to a single decision tree.  

## Metrics Discussion
When I compared error metrics (**R², MAE, RMSE**):  
- Random Forest had **better R²** (closer to 1) and **lower errors**.  
- Linear Regression had worse performance, meaning it struggled to capture the data’s complexity.  

**What this tells us**:  
- Linear Regression is simple but too limited for house price data.  
- Random Forest is more powerful and flexible, but also more complex.  

## My Findings
Overall, **Random Forest is the better model** for predicting house prices in this project.  
It gave predictions much closer to the real values, as shown in the sanity check table.  

👉 Therefore, I prefer **Random Forest** because it balances accuracy and flexibility, and it handled the test cases very well.  
