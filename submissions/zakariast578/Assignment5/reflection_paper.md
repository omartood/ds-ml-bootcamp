# Reflection Paper – House Price Prediction

## What I Implemented
In this assignment, I designed and implemented two machine learning models to predict house prices using a cleaned housing dataset. The two models I worked with were **Linear Regression (LR)** and **Random Forest Regressor (RF)**.  

The process began with preparing the dataset. I set **Price** as the target variable (the value I wanted to predict) and used all the other available features as predictors, excluding `LogPrice` to avoid data leakage. After preprocessing, I split the dataset into **80% training** and **20% testing**, with `random_state=42` to ensure reproducibility of results.  

The **Linear Regression model** was trained first. It assumes a straight-line relationship between predictors and the target variable. This makes it easy to interpret, but it struggles with complex, non-linear data.  

Next, I trained a **Random Forest model** with 100 decision trees. This model uses an ensemble approach to capture more complicated relationships between the features and house prices. It often performs better than a single linear model in real-world datasets, especially when interactions between variables are non-linear.


## Comparison of Models
To directly evaluate the predictions, I conducted **sanity checks** by testing four individual rows from the test set and comparing actual values with the predicted ones:

- **Row i=3:**  
  Actual: $554,800 | Linear Regression: $594,041 | Random Forest: $557,028  
- **Row i=6:**  
  Actual: $367,500 | Linear Regression: $444,366 | Random Forest: $396,774  
- **Row i=9:**  
  Actual: $812,100 | Linear Regression: $825,316 | Random Forest: $832,261  
- **Row i=12:**  
  Actual: $345,900 | Linear Regression: $420,031 | Random Forest: $393,837  

From these results, it is clear that **Random Forest predictions were consistently closer to the actual prices**. Linear Regression tended to overestimate the values (for example, at rows i=6 and i=12), while Random Forest provided outputs that tracked the true values more closely. This highlighted the difference between a simple linear model and an ensemble model that can capture complex relationships.


## Understanding Random Forest
Random Forest is an **ensemble machine learning method** that combines the predictions of many decision trees. Each decision tree in the forest is trained on a random subset of the data (bootstrapping) and a random subset of features. This randomness ensures that each tree is different, reducing the risk of overfitting.  

For regression problems, like predicting house prices, Random Forest works by **averaging the predictions** of all the trees. This averaging smooths out extreme predictions from any single tree and leads to more stable, accurate results.  

In simple terms:  
- **Decision Tree:** A single flowchart-like structure that predicts outcomes by splitting features into rules.  
- **Random Forest:** Dozens or hundreds of these trees trained on different perspectives of the data, whose predictions are averaged together.  

This ensemble strategy makes Random Forest both **powerful** and **robust**, especially for datasets with many features and non-linear patterns.


## Metrics Discussion
Beyond the sanity checks, I also evaluated the models with standard regression metrics: **R², Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE)**.  

- **Linear Regression:**  
  Provided reasonable results but often left larger errors in cases where the relationship between features and price was not purely linear.  

- **Random Forest:**  
  Consistently achieved a higher **R² score**, showing it explained more of the variance in house prices. It also had lower **MAE** and **RMSE**, meaning its predictions were closer to the actual prices on average and more reliable overall.  

These results tell me that Linear Regression is limited when features interact in complicated, non-linear ways, while Random Forest is more flexible and adapts better to real-world housing data.


## Findings
From this assignment, I learned that while **Linear Regression** is simple, fast, and interpretable, it does not always capture the true complexity of housing markets. It can serve as a good **baseline model** to start with, but it should not be the final choice for accuracy-critical applications.  

**Random Forest**, on the other hand, proved to be the stronger model for this task. Its ensemble approach handled non-linearities, reduced errors, and produced predictions that were much closer to actual values in both the sanity checks and the overall performance metrics.  

In summary, if I had to choose one model for predicting house prices, I would select **Random Forest** because of its higher accuracy and robustness. However, I would still use Linear Regression as a complementary model for its interpretability and to quickly establish a baseline before moving on to more advanced techniques.
