# Reflection Paper – House Price Prediction  

## 1. What did you implement?  
In this assignment, I trained two models to predict the price of houses.  
- The first model was **Linear Regression**, which tries to find a straight-line relationship between the features of a house (like size, rooms, location) and the price.  
- The second model was **Random Forest Regressor**, which uses many decision trees and then averages their results.  

I prepared the dataset, split it into training and testing, trained both models, and checked their performance using R², MAE, MSE, and RMSE. I also tested one row from the test set to see the predictions compared with the real price.  

---

## 2. Comparison of Models  
When I did the single-row sanity check, I saw that the predictions were different:  
- **Linear Regression** sometimes gave a value that was far from the real price.  
- **Random Forest** gave a value closer to the actual price.  

Random Forest looked more realistic because it could understand the complex patterns better. Linear Regression was simple but not always correct.  

---

## 3. Understanding Random Forest  
Random Forest is an algorithm that uses many **decision trees** together.  
- Each tree is trained on a random part of the data.  
- For regression, the final prediction is the **average** of all tree predictions.  

It works like asking many people the same question and then taking the average answer. This makes the result more accurate and reduces mistakes compared to using just one tree.  

---

## 4. Metrics Discussion  
From my results:  
- **Random Forest had better R² and smaller errors (MAE, RMSE)** than Linear Regression.  
- This means Random Forest explained the variation in house prices better and predicted more accurately.  

Linear Regression was easier to understand, but it could not capture the complex, non-linear patterns in the dataset.  

---

## 5. My Findings  
From this project, I learned that both models have their strengths.  
- **Linear Regression** is simple and good as a starting point.  
- **Random Forest** is stronger, more flexible, and gives more accurate results.  

For price prediction, I prefer **Random Forest** because it gave me better performance and more realistic predictions in the sanity check so that I can relay on.  
