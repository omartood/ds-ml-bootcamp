# House Price Prediction Report

## What Did I Implement?
In this assignment, I implemented a house price prediction system using two machine learning models: **Linear Regression** and **Random Forest Regressor**. I trained both models on a cleaned housing dataset.  
- The **target variable** was `Price`.  
- The **features** included all other columns except `Price` and `LogPrice`.  
- The dataset was split into training (80%) and testing (20%) using `random_state=42`.  

## Training the Models
- **Linear Regression**: This model was trained by fitting a straight line through the data, minimizing the difference between actual and predicted prices.  
- **Random Forest Regressor**: This model was trained by creating an **ensemble of decision trees** (100 trees in this case). Each tree made its own prediction, and the final prediction was the average of all tree outputs.  

## Comparison of Models
For the **sanity check**, I selected three rows from the test set and compared actual prices with predictions.  
- Linear Regression sometimes **underestimated** or **overestimated** prices, especially when the data was not well aligned with a straight line.  
- Random Forest predictions were **closer to the actual prices**, showing more realistic performance because it can capture non-linear patterns.  

Overall, **Random Forest gave more reliable results** since it handled complex relationships better than a simple linear model.

## Understanding Random Forest
Random Forest is an **ensemble learning method** that builds many decision trees on random subsets of the data and features. Each tree makes a prediction, and the model averages those predictions to produce the final output.  
- This reduces the risk of overfitting compared to a single decision tree.  
- It is flexible and works well when the relationship between features and the target is non-linear.  

## Metrics Discussion
When evaluating performance:  
- **Random Forest had higher R²** and lower error values (MAE, RMSE) compared to Linear Regression.  
- This means Random Forest explained more variance in the data and made smaller prediction errors.  

Linear Regression was simpler but struggled when the relationship between features and price was not strictly linear.

## Findings
From my experiments, **Random Forest performed better** for predicting house prices. Its ability to capture non-linear patterns and interactions between features gave it an advantage.  

While Linear Regression is easy to interpret and train, Random Forest provided **higher accuracy and lower error** on the test set. For real-world house price prediction, I would prefer Random Forest because it is more robust and gives results closer to actual values.  
