# Reflection Paper – House_Price_Prediction

## 1. What I Did
For this assignment, I trained two machine learning models — *Linear Regression* and *Random Forest Regressor* — to predict house prices.  
I started by loading the cleaned dataset, then I separated the target column (Price) from the other features.  
After splitting the data into 80% training and 20% testing sets, I trained both models.

The Linear Regression model acted as my baseline since it is simple and easy to interpret.  
The Random Forest model was chosen because it can capture more complex patterns in the data.  
Finally, I compared their performance using R², MAE, MSE, and RMSE, and ran a sanity check on a single row to see which model was closer to the real price.

---

## 2. Model Comparison
Both models were able to predict house prices fairly well.  
However, *Random Forest consistently performed better*, especially when I compared predictions to the actual prices.  
Linear Regression sometimes under-predicted or over-predicted in cases where the data was not perfectly linear, while Random Forest handled those cases better.

In the single-row sanity check, Random Forest’s predicted price was closer to the actual value, which gave me more confidence in its reliability.

---

## 3. What Random Forest Is
Random Forest is basically a *group of decision trees* working together.  
Each tree gives its own prediction, and then the model averages them.  
This makes the predictions more stable and accurate because one single tree cannot dominate the result.  
It also reduces overfitting compared to using just one tree.

---

## 4. Metrics and Results
When I compared the metrics, Random Forest had:
- *Higher R²* (closer to 1, meaning it explained more variance in the data)
- *Lower MAE and RMSE* (meaning its errors were smaller)

This clearly showed that Random Forest was more accurate for this dataset.

---

## 5. My Takeaways
From this assignment, I learned that while Linear Regression is a great starting point, it struggles with data that has non-linear relationships.  
Random Forest, on the other hand, adapts better to such situations and gives more realistic predictions.  

If I were to use one model in a real-world house price prediction project, I would choose *Random Forest* because of its better accuracy and reliability.