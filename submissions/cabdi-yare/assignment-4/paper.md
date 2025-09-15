# Regression in Machine Learning

Definition:  
Regression is a supervised learning approach in machine learning that focuses on finding the relationship between a set of independent variables (features) and a continuous dependent variable (target).  

The main objective is to build a model that can predict continuous outcomes for new, unseen data by learning patterns from the training dataset.

Example:  
In finance, a regression model could be trained using historical data to predict future sales revenue based on factors such as advertising expenditure and economic conditions.  
The output would be a numerical value (e.g., \$1,000,000 or \$1,250,000).

---

# Regression vs Classification

| Aspect       | Regression | Classification |
|--------------|------------|----------------|
| Output Type | Continuous numerical values (e.g., tomorrow’s temperature = 28.5°C) | Discrete categories/labels (e.g., tomorrow’s weather = “rainy” or “sunny”) |
| Goal       | Estimate a numerical quantity (e.g., predict a student’s exam score) | Assign data into predefined groups (e.g., classify a plant as “healthy” or “diseased”) |
| Focus      | Answers questions like “How much?”, “How high?”, or “How many?” | Answers questions like “Which class?”, “Yes or No?”, or “Is it A or B?” |

---

# Types of Regression

Regression techniques vary depending on the complexity of relationships they can capture.


## 1. Linear Regression

How it works:  
- Examines the relationship between one independent variable (predictor) and one dependent variable (outcome).  
- Draws a straight line that best represents the data.  

Example:  
Predicting a company’s stock price change based on daily trading volume.

Advantages:
- Easy to understand, implement, and interpret.  

Limitations:
- Assumes a perfectly linear relationship, which may not hold true for real-world data.  


## 2. Multiple Linear Regression

How it works:  
- Extends simple linear regression by using two or more independent variables to predict a single outcome.  
- Finds the best-fitting line that combines all predictors to explain the dependent variable.  

Example:  
Predicting house prices based on size, number of bedrooms, and location.  

Advantages:
- Captures more complex relationships.  
- Improves prediction accuracy compared to simple linear regression.  

Limitations:
- Harder to interpret.  
- Requires larger datasets to accurately estimate relationships.  


## 3. Polynomial Regression

How it works:  
- Models non-linear relationships by fitting a curve instead of a straight line.  
- Uses higher-degree terms of independent variables to capture curvature.  

Example:  
Modeling crop yield based on fertilizer usage, where yield increases at first but then levels off or decreases.  

Advantages:
- Very flexible, can represent complex curved patterns.  

Limitations:
- High-degree polynomials risk overfitting (capturing noise instead of general trends).  

---

# Regression Metrics

When building a regression model, we need to check how well its predictions match the real values. Several common metrics are used to measure this accuracy.


## 1. MAE (Mean Absolute Error)

Definition:  
MAE is the average of the absolute differences between predicted values and actual values.

Formula:

\[
MAE = \frac{1}{n}\sum_{i=1}^{n} |y_i - \hat{y}_i|
\]

Interpretation:  
MAE tells us, on average, how far the model’s predictions are from the real values, without worrying about whether the error is positive or negative.

Key Points:
- Very easy to understand because it uses the same units as the target variable.  
- Treats all errors equally (does not punish big mistakes more than small ones).  


## 2. MSE (Mean Squared Error)

Definition:  
MSE is the average of the squared differences between predictions and actual values.

Formula:

\[
MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2
\]

Interpretation:  
Like MAE, it measures how far predictions are from actual values, but by squaring the errors, it gives more weight to large mistakes.

Key Points:
- Very sensitive to outliers because big errors are squared and become much larger.  
- Measured in squared units of the target variable, which makes it harder to interpret directly.  


## 3. RMSE (Root Mean Squared Error)

Definition:  
RMSE is simply the square root of the MSE.

Formula:

\[
RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}
\]

Interpretation:  
RMSE tells us how far the predictions are from the actual values, on average, but it does so in the same units as the target variable (making it easier to understand than MSE).

Key Points:
- Like MSE, it penalizes large errors more strongly.  
- Easier to read because the result is in the same scale as the original data.  


## 4. R² (Coefficient of Determination)

Definition:  
R² shows how much of the variation in the target variable is explained by the model.

Formula:

\[
R^2 = 1 - \frac{SS_{res}}{SS_{tot}}
\]

Where:  
- \(SS_{res}\) = sum of squared residuals (errors)  
- \(SS_{tot}\) = total sum of squares (variation in the data)  

Interpretation:  
- \(R^2 = 0\) → Model explains none of the variation.  
- \(R^2 = 1\) → Model explains all the variation perfectly.  
- \(R^2 < 0\) → Model performs worse than simply predicting the mean.  

Key Points:
- A good measure of overall model fit.  
- Does not tell you how big the errors actually are.  


---

##  Comparison 

| Metric | Units                  | Sensitivity to Large Errors | Main Purpose                           | Easy to Interpret? |
|--------|------------------------|-----------------------------|----------------------------------------|--------------------|
| MAE    | Same as target variable | Low (treats all equally)   | Shows average size of errors           |  Yes             |
| MSE    | Squared units           | High (squares errors)      | Emphasizes large errors during training|  No              |
| RMSE   | Same as target variable | High (but intuitive)       | Shows error magnitude with outlier weight|  Yes          |
| R²     | Unitless (0–1, or negative) | N/A                    | Shows overall model fit                |  Yes (conceptually harder) |

---

# Underfitting and Overfitting in Regression Models

### Underfitting
- Happens when a model is too simple to capture the patterns in the data.  
- Performs poorly on both training and test data.  
- Example: fitting a straight line to data that clearly follows a curve.  

### Overfitting
- Happens when a model is too complex and memorizes training data (including noise).  
- Performs very well on training data but fails on unseen test data.  


# Why Overfitting Happens in Polynomial Regression
Polynomial regression uses higher-degree polynomials to fit the data.  
- With low-degree polynomials, the model may underfit (too simple).  
- With very high-degree polynomials, the model can pass through almost every training point, leading to overfitting.  

This happens because the polynomial becomes too flexible, capturing random noise instead of just the true underlying trend.

----

# 5. Case Study — Multiple Linear Regression in Agriculture and Economic Growth

## Title  
Predicting Somalia’s GDP Using Multiple Economic Indicators  

Source: Simulated Example Based on World Bank and FAOSTAT Data  


## Goal  
- To predict Somalia’s GDP using several economic indicators:  
  - Agricultural output  
  - Agricultural employment  
  - Gross capital formation  
  - Industry  
  - Services  
- To identify which predictors most influence economic growth.  


## Data  

- Type: Time-series (1970–2020)  
- Observations: 11 (aggregated decades/periods)  
- Features:  
  - Agricultural Output (% of GDP)  
  - Agricultural Employment (% of labor force)  
  - Gross Capital Formation (% of GDP)  
  - Industry (% of GDP)  
  - Services (% of GDP)  


## Model Applied  
Multiple Linear Regression  
\[
GDP = \beta_0 + \beta_1 \times \text{Agricultural Output} + \beta_2 \times \text{Agricultural Employment} + \beta_3 \times \text{Gross Capital Formation} + \beta_4 \times \text{Industry} + \beta_5 \times \text{Services} + \epsilon
\]  

- GDP predicted using all features simultaneously.  


## Results  
- Achieved R² ≈ 0.97 (very strong explanatory power).  
- Key predictors:  
  - Agricultural output  
  - Agricultural employment  
  - Gross capital formation  
- Including multiple indicators significantly improves prediction accuracy compared to using agriculture alone.  


## Insight  
- Agriculture remains a key driver of Somalia’s economic growth.  
- However, the combined effect of multiple economic indicators provides the most accurate GDP prediction.  

---

## References  
- Samatar, E. H. (2022). *The Impact of Agricultural Output on Economic Growth in Somalia (1970–2020).* Master’s Thesis, University of Nairobi.  
- World Bank. World Development Indicators.  
- FAOSTAT. Agricultural Data for Somalia.