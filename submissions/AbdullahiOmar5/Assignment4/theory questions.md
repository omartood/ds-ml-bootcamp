# Theory Answers

## Introduction Regress
### What is regression in machine learning?
Regression is a type of supervised learning used to predict continues values like price house or weather temperature, by modeling the relationship between input variables (features) and an output variable(target).
### How is it different from classification?
Classification and regression are two primary tasks in supervised machine learning. But there difference lies on nature of the output.classification deals with discrete outcomes (e.g yes/no, categories) while regression deals with continues outcomes (e.g price, temperature). Regression algorithms predicts a continues values, it is used when you want to predict income, height, temperature and weight.
### Give one real-life example of regression and one of classification.
Regression example: Predicting if a patient blood pressure is high or low based on thier age, weight, and exercise habits.
Classification example: Predicting if a tumor has a malignant or benign based on their medical history like chronic illness, age, weight, their family history of cancer, and lifestyle habits.

## 📈 Types of Regression in Machine Learning


| Regression Type             | How It Works (Basic Idea)                                                                 | Real-World Use Case                                                                                   | Main Advantage                                | Limitation                                      |
|----------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|-----------------------------------------------|--------------------------------------------------|
| **Linear Regression**       | Predicts output based on one input feature with a straight-line relationship              | Predicting crop yield based on the amount of fertilizer applied                                        | Simple and easy to interpret                  | Only models straight-line relationships          |
| **Multiple Linear Regression** | Similar to linear regression, but uses several input features to predict the output         | Predicting crop yield based on fertilizer amount, rainfall, and sunlight hours                         | Can analyze multiple factors at once          | Assumes linear relationship between inputs and output |
| **Polynomial Regression**   | Fits a curved line to capture complex, non-linear relationships between inputs and output | Modeling crop yield with diminishing returns or saturation effects from fertilizer application         | Models complex, non-linear trends accurately  | Can overfit data, harder to interpret            |

### 📏 Regression Metrics

Mean Absolute Error (MAE) measures the average size of the errors in a set of predictions, without considering their direction. All errors are given equal weight. It represents how much, on average, the predictions are off from the actual values. MAE is easy to interpret because it uses the same units as the target variable.
Mean Squared Error (MSE) measures the average of the squared differences between predicted and actual values. By squaring the errors, MSE gives more weight to larger errors, making it very sensitive to big mistakes. This can be useful when large errors are particularly undesirable.
Root Mean Squared Error (RMSE) RMSE is the square root of MSE, effectively bringing the error metric back to the original units of the target variable. It is easier to interpret than MSE but still emphasizes larger errors more than MAE
R-squared (R²) or Coefficint of Determination is a statistical measure that shows the proportion of variance in the target variable that is explained by the model. Values closer to 1 mean the model explains the data well, while values near 0 mean it does not perform better than simply predicting the average of the target values.

### Comparison Table 

| Metric                        | Units                    | Sensitivity to Large Errors | Meaning / Interpretation                                                                 |
|------------------------------|--------------------------|-----------------------------|-------------------------------------------------------------------------------------------|
| **MAE (Mean Absolute Error)**| Same as target variable  | Low                         | Average size of errors; all errors weighted equally; easy to interpret.                   |
| **MSE (Mean Squared Error)** | Squared units of target  | High                        | Average squared errors; penalizes larger errors more; sensitive to outliers.              |
| **RMSE (Root Mean Squared Error)** | Same as target variable  | High                  | Square root of MSE; error in same units as target; emphasizes large errors.               |
| **R² (Coefficient of Determination)** | Unitless (proportion)     | N/A               | Fraction of variance explained by the model; closer to 1 means better fit.                |


## Underfitting and Overfitting 
### Explain what underfitting and overfitting mean in regression models.
Overfitting happens when a regression model learns the training data too well — not just the general trend, but also the random noise or small details that don’t really matter for making predictions. This makes the model perform extremely well on the training data but poorly on new or unseen data because it is too tied to the specific quirks of the training set.While Underfitting happens when a model is too simple to capture the real relationship between the inputs and output. It can’t learn the pattern well enough, so it has poor performance on both the training and test data.

In polynomial regression, overfitting happens mainly because the model becomes too complex and starts capturing not just the real pattern in the data but also the random noise and small curve, which are not actually meaningful.
### What causes overfitting, especially in polynomial regression?
These are the causes of overfitting in polynomial regression
1. Too few data points:
When there isn’t enough training data available relative to the complexity of the polynomial, the model essentially “memorizes” the training points instead of learning the general trend.
2. Noisy or messy data:
If the training data has errors, inconsistencies, or random fluctuations, a complex polynomial model will try to fit those areas too closely, leading to poor generalization.
3. High-degree polynomial:
When the polynomial degree is very high (for example, degree 9 or 10), the fitted curve becomes very wiggly and can perfectly pass through every single training data point. This looks like a perfect fit on the training data but behaves poorly when predicting new data. This is because it is capturing noise (random errors) and not just the true relationship.
in summary overfitting in polynomial regression is caused by making the model too complex relative to the data, which causes it to fit noise, not just the true signal.
The model loses its ability to generalize and predict well on new or unseen data.
### Give 2–3 methods to prevent overfitting.
We can prevent overfitting by these follows:
1. More Training Data
The more quality data you have, the harder it is for the model to memorize random noise. More diverse data helps the model learn true underlying patterns, improving generalization.
2. Feature Selection
Reducing the number of input features by keeping only the most relevant ones avoids giving the model too many meaningless details, which can cause overfitting. It simplifies the problem and improves prediction reliability.
3. Cross-Validation
Cross-validation splits the training data into multiple parts, then trains the model multiple times on different subsets, testing on held-out parts each time. This helps detect if the model only performs well on specific data, ensuring it generalizes better to new data.

## 📚 Real-World Case Study

Healthcare Linear Regression Case Study

Goal: Study the relationship between health indicators (like BMI, blood pressure) and labor market performance (income, employment).

Data Used: Health and income data from the China Nutrition Survey (CHNS) microdata with multiple physical and health characteristics.

Regression Model: Linear regression.

Key Results: Found significant impact of health on income and probability of employment, helping understand economic implications of health status.

Reference:
Li, Z. (2023). A linear regression-based study of the relationship between health and labor market performance using CHNS data. Journal of Health and Social Behavior.