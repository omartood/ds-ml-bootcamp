# 🏡 Reflection Paper — House Price Prediction

## What I Implemented  
In this project, I implemented two regression models — **Linear Regression** and **Random Forest Regressor** — to predict house prices using a cleaned dataset. I split the data into training and testing sets (80/20), trained both models on the training data, and then evaluated them on the unseen test set. The models were assessed using **R², MAE, MSE, and RMSE**. I also performed a single-row “sanity check” prediction to compare actual vs. predicted prices.

---

## Comparison of Models (Sanity Check)  
When I ran the **single-row predictions**, Linear Regression and Random Forest produced slightly different results.  

- **Linear Regression** gave a reasonable estimate but sometimes under/over-shot when features had non-linear relationships.  
- **Random Forest** was often closer to the actual price because it captures complex interactions between features.  

In my test, **Random Forest predictions were more realistic** since housing prices usually depend on non-linear factors (like neighborhood, condition, and square footage interacting together).

---

## Understanding Random Forest  
A **Random Forest** is an ensemble model made up of many decision trees.  

- Each tree learns slightly different patterns by training on random subsets of data and features.  
- For regression tasks, the forest combines predictions by taking the **average** of all trees.  

This ensemble approach reduces overfitting (compared to a single tree) and makes Random Forests more robust for real-world data.

---

## Metrics Discussion  
Based on evaluation metrics:  

- **Random Forest** achieved a higher **R²** score, meaning it explained more variance in the test data.  
- It also had **lower MAE and RMSE** values, showing smaller prediction errors compared to Linear Regression.  

This suggests that **Random Forest is stronger at capturing complex, non-linear relationships**, while Linear Regression is simpler and more interpretable but limited when data patterns aren’t linear.

---

## Findings  
Overall, I found that **Random Forest is the better model for house price prediction** in this project. Its higher accuracy and better error metrics show that it adapts well to the complex nature of housing markets.  

However, **Linear Regression is still useful** as a baseline model. It is quick to train, easy to interpret, and helps highlight feature importance in a straightforward way.  

For real-world deployment, I would prefer **Random Forest** because of its **robustness, higher accuracy, and ability to generalize** better across diverse housing data.
