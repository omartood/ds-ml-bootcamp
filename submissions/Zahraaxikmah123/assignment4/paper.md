# ✅ Part A — Theory Questions

## 1. Introduction to Regression

Regression is one of the main methods in supervised machine learning, and it's used for predicting numbers that can change, like prices or scores. Unlike classification, which just puts things into categories, regression tries to find out how input features (independent variables) are related to a target variable that keeps changing (dependent variable). The goal is to get a mathematical function—like a line or curve—that fits the data well, by making the difference between predicted and actual values as small as possible. This helps us answer questions like "how much" or "how many," which is really useful in real life.

This is actually pretty different from classification. For example, a classification model might predict if a customer will "buy" or "not buy" a product, which is just yes or no. But regression would estimate how much money the customer will spend, which is a number. One common use of regression is predicting a student's exam score based on how many hours they studied, their attendance, and quiz results. On the other hand, classification would be used to predict if the student will pass or fail.

---

## 2. Types of Regression

All regression models try to predict continuous outcomes, but they are not all the same in how they show relationships between variables. Here are some popular types.

### a) Simple and Multiple Linear Regression

**Mechanism:**  
Linear regression assumes there is a straight-line relationship between the input features and the target variable. The model finds the best-fitting line by reducing the total squared difference between the predicted and actual values.

- *Simple linear regression* uses just one input variable—for example, predicting a car’s fuel efficiency based only on its weight.
- *Multiple linear regression* uses two or more variables, like weight, engine size, and etc.

**Use Case:**  
In retail, multiple linear regression can help forecast weekly sales by looking at advertising budgets, promotions, and the day of the week.

**Strengths & Limitations:**  
The main advantage of linear regression is that it’s easy to interpret—the model's coefficients show how each input affects the prediction. But it assumes all relationships are linear, which sometimes isn't true for real-world data.

### b) Polynomial Regression

**Mechanism:**  
Polynomial regression is like linear regression but includes powers of the input variables (like x², x³, etc.). This lets the model catch curved, non-linear relationships in the data.

**Use Case:**  
In public health, polynomial regression can be used to model how an epidemic spreads over time, especially if the infection rate follows an S-shaped curve that a straight-line model can't show.

**Strengths & Limitations:**  
Its main strength is flexibility in modeling complex patterns. But if you use too many polynomial terms, it can lead to overfitting—where the model gets too sensitive to the training data and doesn't work well on new data.

---

## 3. Regression Metrics

Checking how well a regression model works is important. These metrics measure how close the model’s predictions are to the actual values:

| Metric | Meaning | Sensitive to Large Errors? | Units |
|--------|---------|----------------------------|-------|
| MAE (Mean Absolute Error) | Average size of the errors (ignores direction) | No | Same as target |
| MSE (Mean Squared Error)  | Average of squared errors | Yes | Squared units |
| RMSE (Root Mean Squared Error) | Square root of MSE; easier to interpret | Yes | Same as target |
| R² (R-squared) | Percentage of variation explained by the model | No | 0 to 1 (or 0% to 100%) |

### Key Distinctions:

- MAE and RMSE give the average error in the same units as the target variable, which makes them easy to understand.
- RMSE gives more weight to big errors, so it's better when you want to avoid large mistakes.
- R² tells us how much of the variation in the target variable is explained by the model.  
  For example, an R² of 0.85 means the model explains 85% of the variation in the data.

---

## 4. Underfitting and Overfitting

Making a good regression model means finding the right balance between being simple and being complex.

### Underfitting:
This happens when the model is too simple to learn the real patterns in the data.  
For example, using a linear model to fit data that clearly follows a curve.  
Underfitting usually results in poor accuracy on both training and test datasets.

### Overfitting:
Overfitting happens when the model gets too complex, learning not just the actual pattern but also the random noise in the training data.  
For example, a high-degree polynomial model might match every data point in the training set, but it would probably do badly on new data.

### Causes of Overfitting in Polynomial Regression:
The main reason is using a very high-degree polynomial, which makes the model too flexible and sensitive to the training data, including the noise.

### How to Prevent Overfitting:

- **Regularization:**  
  Techniques like (L1) and (L2) add penalties to the model's complexity, helping it stay simple.

- **Cross-Validation:**  
  Splitting the data into several parts for training and validation helps test how well the model works on unseen data.

- **More Data & Better Features:**  
  Having more and better data can help the model generalize better.  
  Picking only the most relevant features also helps avoid unnecessary complexity.

---

## 5. Real-World Case Study: Regression in Healthcare

**Title:** Predicting Patient Response to Chemotherapy Using Multiple Linear Regression  
**Source:** *International Journal of Medical Informatics, 2022*

### Goal:
The study wanted to build a model that predicts how much a cancer patient’s tumor will shrink after chemotherapy.  
Accurate predictions can help doctors customize treatment plans, adjust drug dosages, and set more realistic recovery goals.

### Data Used:
The researchers used patient medical records that included:

- Initial tumor size (cm)
- Patient age and weight (kg)
- Chemotherapy drug dosage (mg)
- Length of treatment (weeks)
- Blood test results (like white blood cell count)

### Model Chosen:
They used a multiple linear regression model to study how these factors work together to influence treatment outcomes.  
One of the main reasons for choosing this model was its interpretability, so doctors can clearly see the role of each factor.

### Key Results & Insights:

- The model got an **R² score of 0.81**, meaning it explained **81%** of the variation in tumor shrinkage.
- **Higher chemotherapy dosages** and **longer treatment periods** were strong positive indicators of better outcomes.
- **Larger initial tumor sizes** and **older patient age** were linked to less effective treatment responses.
- Overall, the study showed that multiple regression can be a useful decision-support tool in oncology, helping personalize and improve patient care.

---

## References:

1. Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow*. O’Reilly Media.  
2. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning: with Applications in R*. Springer.  
3. Myers, R. H., Montgomery, D. C., & Vining, G. G. (2012). *Generalized Linear Models: With Applications in Engineering and the Sciences*. Wiley.  
4. Wang, L., Zhang, Y., & Li, J. (2022). "Predicting Patient Response to Chemotherapy Using Multiple Regression." *International Journal of Medical Informatics*, 165, 104868.