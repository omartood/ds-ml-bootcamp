# Paper – House Price Prediction

## What did I implement?
In this project, I worked on predicting house prices using two machine learning models: **Linear Regression** and **Random Forest**.  
I trained both models on a dataset of house prices. The data was split into training and testing sets (80% train, 20% test). I dropped the target column "Price" from the features and used it as the prediction target. Then, I fit the two models:
- Linear Regression
- Random Forest Regressor (with 100 trees)

## Comparison of Models
For a **sanity check**, I tested the models three different times by picking rows from the test set. The results were:

1. **Row 2**  
   - Actual Price: $292,500  
   - LR Prediction: $188,637  
   - RF Prediction: $290,899  

2. **Row 3**  
   - Actual Price: $554,800  
   - LR Prediction: $594,041  
   - RF Prediction: $557,028  

3. **Row 4**  
   - Actual Price: $535,300  
   - LR Prediction: $609,615  
   - RF Prediction: $538,756  

From these results, I noticed:  
- **Linear Regression** predictions could be quite far from the true price (especially Row 2 and Row 4).  
- **Random Forest** predictions were always very close to the actual prices, showing more stability.  

This showed me that Random Forest gave more realistic and reliable results compared to Linear Regression.

## Understanding Random Forest
Random Forest is an **ensemble learning method**.  
- It builds many **decision trees** during training.  
- Each tree makes a prediction, and the final prediction is the **average** (for regression) of all the trees.  
This way, Random Forest reduces overfitting and usually gives more stable and accurate results than a single model like Linear Regression.

## Metrics Discussion
I evaluated both models with metrics: **MAE, MSE, RMSE, and R²**.  
From my results:
- Linear Regression had higher error values (MAE and RMSE).  
- Random Forest had lower errors and a higher R² score (~0.86 vs ~0.84).  

This tells me that Random Forest fits the data better and makes more accurate predictions.

## My Findings
Based on my work, I prefer **Random Forest** for house price prediction.  
It gave better accuracy, lower error, and much more realistic predictions in the **sanity checks** I performed. Linear Regression is simple and easy to understand, but it struggles with complex data patterns. Random Forest, being an ensemble method, captures more details and works better for this type of problem.
