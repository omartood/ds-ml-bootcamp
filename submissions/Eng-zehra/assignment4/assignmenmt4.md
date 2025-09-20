## Assignment Four Regration
**Solving assignment Four**
---
## 1.introduction of Regration
**Regression** is a machine learning method used to predict number and the output is countinious number
**Example of regration** if i want to know the age of students under grade 8 of schools
**Classification** is a machine learning method used to predict when the output is categorical like 
*yes/no pass/fail* 
**Example of regression is predicting housing price**
**Example of classification if the students pass their exames or fail**

## Types of Regression
1) Linear regression : is the simplet regression that uses straightline and has one input and one output
   **Real example of linear regression**  predicting exam scores using hous of study
   **Strengths**The speed of linear regrassion is fast*
   **Limitations:** if the relationship is curve or not linear prediction will fail and too simples
2) multipleLinear regration :can have multiple input and one output
   **Strengths** more accurency and not limited inputes
   **Limitations:* can cause overfitting since it need lots of dataset*
3) polynomial regression is same as linear regression but have curve 
**curved** shape
**Example:*predicting profit/loss by month i can go profit up or lost*
**Strengths:*Better fit when there is curve*
**Limitations:* takes only one input*

**Regression Metrics** 
| Metric                                | What it Measures                                                                                                                   | Units           | Sensitivity                                     |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | --------------- | ----------------------------------------------- |
| **MAE (Mean Absolute Error)**         | Adding up all differences or errors and dividing by the length of the dataset; difference between predicted value and actual value | Same as dataset | Less sensitive                                  |
| **MSE (Mean Squared Error)**          | Instead of adding errors, the errors are **squared** and then divided by the number of data points                                 | Squared unit    | Can be affected by outliers because of squaring |
| **RMSE (Root Mean Squared Error)**    | Same as MSE but square root is taken so result is comparable to original data                                                      | Same as dataset | Sensitive to large errors                       |
| **R² (Coefficient of Determination)** | How much of the variation in the data is explained by the model compared to the baseline model                                     | Unitless        | Shows model fit; sensitive to outliers          |

## Underfitting and Overfitting
*underfitting*is when the model cant learn enought from dataset 
*overfitting* is when model can learn old dataset but cant predict new 
*in polynomial regression* hight degree can cause overfitting

* To avoid overfiiting use less degree
* and giving more examples
**Title** Relationship among Advertising Expenditure, Sales and Profit using linear regression 
**Goal**To test whether Advertisement Expenditure has a significant effect on Sales Revenue and Net Profit (after tax)
**Data They Used** 70 months of company financial records.
*Independent Variable (X): Advertisement Expenditure.
* Dependent Variables (Y):
* Sales Revenue
* Net Profit after tax
 **Type of Regression Model Applied**Simple Linear Regression (straight-line relationship tested using SPSS).
**Key Results / Insights**Advertisement Expenditure had a positive and significant effect
on both Sales Revenue and Net Profit Meaning: increasing advertising spending led to higher sales and profits.
   