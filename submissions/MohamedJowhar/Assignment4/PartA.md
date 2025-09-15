# 📘 Introduction to Regression in Machine Learning  

## 📌 What is Regression?  
Regression is a **supervised learning technique** used to **predict continuous values (numbers)**.  

The algorithm learns from input data (**features**) and outputs a **numerical value**.  

**Example**: Predicting someone’s **salary** based on their **age, education, and experience**.  

---

## 📌 How is Regression Different from Classification?  

| **Aspect**       | **Regression** | **Classification** |
|------------------|----------------|---------------------|
| **Output type**  | Continuous (numbers) | Categorical (labels/classes) |
| **Examples of output** | Price, age, temperature, height | Spam/Not Spam, Male/Female, Yes/No |

---

## 📌 Real-Life Examples  

- **Regression Example** 🏠: Predicting the **house price** in Mogadishu based on location, size, and number of rooms.  
  - Output: a number (e.g., **$25,000**)  

- **Classification Example** 📧: Predicting whether an **email is spam or not spam**.  
  - Output: a label (e.g., **"Spam"** or **"Not Spam"**)  



# 📊 Types of Regression in Machine Learning

Regression is used to predict continuous outcomes. There are several types, each suited for different scenarios.

---

## 1️⃣ Linear Regression

**How it works:**  
Predicts a continuous outcome using a straight-line relationship between the input (independent variable) and output (dependent variable).

**Equation:**  
y = mx + b

**Where:**  
- `y` = predicted value  
- `x` = input variable  
- `m` = slope (how much y changes when x changes)  
- `b` = intercept (value of y when x = 0)  

**Example real-world use case:**  
Predicting a person’s weight based on height.

**Advantages:**  
- Simple and easy to understand  
- Fast to compute  
- Works well when the relationship is close to linear  

**Limitations:**  
- Can’t capture complex relationships  
- Sensitive to outliers  
- Assumes the relationship between x and y is linear  

---

## 2️⃣ Multiple Linear Regression

**How it works:**  
Like linear regression but uses more than one input variable to predict the output.

**Equation:**  
y = b0 + b1x1 + b2x2 + ... + bn*xn

**Where:**  
- `x1, x2, ..., xn` = different features  
- `b0` = intercept  
- `b1, b2, ..., bn` = coefficients  

**Example real-world use case:**  
Predicting house prices using size, number of bedrooms, location, and age of the house.

**Advantages:**  
- Can handle multiple factors affecting the outcome  
- More flexible than simple linear regression  

**Limitations:**  
- Harder to interpret if many variables  
- Can overfit if too many features  
- Assumes linear relationships between each feature and the output  

---

## 3️⃣ Polynomial Regression

**How it works:**  
Fits a curved line to the data instead of a straight line.

**Equation example (degree 2):**  
y = b0 + b1x + b2x^2

**Example real-world use case:**  
Predicting sales over time, where sales increase, peak, and then decline.

**Advantages:**  
- Can model complex, non-linear relationships  
- More accurate for certain datasets  

**Limitations:**  
- Risk of overfitting if degree is too high  
- Harder to interpret than linear regression  
- Sensitive to outliers  

---

## ✅ Comparison Table

| Type                       | Relationship | Inputs | Use Case                   | Pros                       | Cons                               |
|-----------------------------|-------------|--------|----------------------------|----------------------------|-----------------------------------|
| Linear Regression           | Straight line | 1      | Weight vs height          | Simple, fast               | Only linear, sensitive to outliers |
| Multiple Linear Regression  | Straight line | Many   | House price prediction    | Handles multiple factors   | Complex, can overfit               |
| Polynomial Regression       | Curve        | 1+     | Sales trends over time    | Can model non-linear       | Overfitting risk, complex          |


# Regression Metrics

Regression metrics are used to evaluate the performance of regression models, which predict continuous values (e.g., house prices, temperatures, stock prices).

---

## 1️⃣ MAE – Mean Absolute Error

**Definition:**  
The average of the absolute differences between predicted values and actual values.

**Formula:**  
\[
MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|
\]

- \(y_i\) = actual value  
- \(\hat{y}_i\) = predicted value  
- \(n\) = number of observations  

**Meaning:**  
- Measures the **average magnitude of errors**, ignoring direction.  
- Lower MAE → better predictions.

**Example:**  
Actual: `[10, 20, 30]`  
Predicted: `[12, 18, 33]`  
Errors: `|10–12|=2, |20–18|=2, |30–33|=3`  
MAE = `(2+2+3)/3 = 2.33`  

✅ Interpretation: On average, predictions are off by **2.33 units**.

---

## 2️⃣ MSE – Mean Squared Error

**Definition:**  
The average of the squared differences between predicted and actual values.

**Formula:**  
\[
MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
\]

**Meaning:**  
- Penalizes **larger errors more** than MAE because of squaring.  
- Useful when large errors are especially undesirable.

**Example:**  
Errors: `2, 2, 3`  
Squared: `4, 4, 9`  
MSE = `(4+4+9)/3 = 5.67`

✅ Interpretation: MSE emphasizes **big mistakes** more than MAE.

---

## 3️⃣ RMSE – Root Mean Squared Error

**Definition:**  
The square root of MSE.

**Formula:**  
\[
RMSE = \sqrt{MSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}
\]

**Meaning:**  
- Expressed in the **same units as the target variable**.  
- Sensitive to large errors (like MSE).

**Example:**  
MSE = `5.67` → RMSE = `√5.67 ≈ 2.38`

✅ Interpretation: On average, prediction errors are around **2.38 units**.

---

## 4️⃣ R² – Coefficient of Determination

**Definition:**  
Measures how well the model explains the variance in the target variable.

**Formula:**  
\[
R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}
\]

- \(\bar{y}\) = mean of actual values  

**Meaning:**  
- R² = 1 → perfect prediction  
- R² = 0 → model is no better than predicting the mean  
- R² < 0 → model is worse than predicting the mean

✅ Interpretation: If R² = 0.8, the model explains **80% of the variance** in the target variable.

---

## Comparison Table

| Metric | Unit | Sensitivity to Large Errors | Meaning / Use |
|--------|------|----------------------------|---------------|
| **MAE** | Same as target | Low (all errors treated equally) | Average error magnitude. Easy to interpret. |
| **MSE** | Squared units of target | High (large errors penalized more) | Highlights large errors. Good for optimization. |
| **RMSE** | Same as target | High | Like MSE but in original units. Standard way to report error. |
| **R²** | Unitless | Medium | Percentage of variance explained by model. Good for overall fit. |

---

### Key Notes
- **MAE** is simple and intuitive.  
- **MSE/RMSE** are better if you care about **big errors**.  
- **R²** shows **how well the model fits the data**, not the size of errors.


# Regression Metrics

Regression metrics are used to evaluate the performance of regression models, which predict continuous values (e.g., house prices, temperatures, stock prices).

---

## 1️⃣ MAE – Mean Absolute Error

**Definition:**  
The average of the absolute differences between predicted values and actual values.

**Formula:**  
\[
MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|
\]

- \(y_i\) = actual value  
- \(\hat{y}_i\) = predicted value  
- \(n\) = number of observations  

**Meaning:**  
- Measures the **average magnitude of errors**, ignoring direction.  
- Lower MAE → better predictions.

**Example:**  
Actual: `[10, 20, 30]`  
Predicted: `[12, 18, 33]`  
Errors: `|10–12|=2, |20–18|=2, |30–33|=3`  
MAE = `(2+2+3)/3 = 2.33`  

✅ Interpretation: On average, predictions are off by **2.33 units**.

---

## 2️⃣ MSE – Mean Squared Error

**Definition:**  
The average of the squared differences between predicted and actual values.

**Formula:**  
\[
MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
\]

**Meaning:**  
- Penalizes **larger errors more** than MAE because of squaring.  
- Useful when large errors are especially undesirable.

**Example:**  
Errors: `2, 2, 3`  
Squared: `4, 4, 9`  
MSE = `(4+4+9)/3 = 5.67`

✅ Interpretation: MSE emphasizes **big mistakes** more than MAE.

---

## 3️⃣ RMSE – Root Mean Squared Error

**Definition:**  
The square root of MSE.

**Formula:**  
\[
RMSE = \sqrt{MSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}
\]

**Meaning:**  
- Expressed in the **same units as the target variable**.  
- Sensitive to large errors (like MSE).

**Example:**  
MSE = `5.67` → RMSE = `√5.67 ≈ 2.38`

✅ Interpretation: On average, prediction errors are around **2.38 units**.

---

## 4️⃣ R² – Coefficient of Determination

**Definition:**  
Measures how well the model explains the variance in the target variable.

**Formula:**  
\[
R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}
\]

- \(\bar{y}\) = mean of actual values  

**Meaning:**  
- R² = 1 → perfect prediction  
- R² = 0 → model is no better than predicting the mean  
- R² < 0 → model is worse than predicting the mean

✅ Interpretation: If R² = 0.8, the model explains **80% of the variance** in the target variable.

---

## Comparison Table

| Metric | Unit | Sensitivity to Large Errors | Meaning / Use |
|--------|------|----------------------------|---------------|
| **MAE** | Same as target | Low (all errors treated equally) | Average error magnitude. Easy to interpret. |
| **MSE** | Squared units of target | High (large errors penalized more) | Highlights large errors. Good for optimization. |
| **RMSE** | Same as target | High | Like MSE but in original units. Standard way to report error. |
| **R²** | Unitless | Medium | Percentage of variance explained by model. Good for overall fit. |

---

### Key Notes
- **MAE** is simple and intuitive.  
- **MSE/RMSE** are better if you care about **big errors**.  
- **R²** shows **how well the model fits the data**, not the size of errors.

# 🔹 Underfitting vs Overfitting in Regression Models

## 1. Underfitting
**Definition:** When a model is too simple to capture the underlying trend in the data.  

**Cause:** The model ignores important patterns because it doesn’t have enough complexity.  

**Example:**  
Using a straight line (**linear regression**) to fit data that is actually curved.  

**Effect:**  
- High bias (wrong assumptions).  
- Both training error and testing error are high.  

---

## 2. Overfitting
**Definition:** When a model is too complex and learns not just the patterns, but also the noise (random fluctuations) in the training data.  

**Cause:** Model tries too hard to perfectly fit the training data.  

**Example:**  
Using a **high-degree polynomial** that twists and turns to pass through almost every data point.  

**Effect:**  
- Low training error (fits training data very well).  
- High testing error (fails on new data).  
- High variance (model changes a lot if training data changes slightly).  

---

# 🔹 What Causes Overfitting in Polynomial Regression?
- **High-degree polynomial:** The curve bends excessively to fit all data points.  
- **Too many features (variables):** Model has too much freedom.  
- **Small dataset:** Easier for the model to memorize noise instead of learning the real pattern.  

---

# 🔹 Methods to Prevent Overfitting
### 1. Reduce model complexity
- Use a lower-degree polynomial.  
- Use fewer features if they don’t add real value.  

### 2. Regularization
- Add penalty terms like **Ridge Regression (L2)** or **Lasso Regression (L1)** to control large coefficients.  

### 3. Cross-validation
- Split data into **training and validation sets**.  
- Ensure the model generalizes well, not just memorizes training data.  

**Other helpful methods:**  
- Get more data  
- Use early stopping in iterative training  
- Apply feature selection  

---

# ✅ In Short
- **Underfitting = too simple → misses the trend.**  
- **Overfitting = too complex → memorizes noise.**  




# 🎓 Case Study: Predicting Student Performance with Multiple Linear Regression  

## 🎯 Goal of the Project  
Researchers wanted to **predict students’ final exam scores** based on their study habits, attendance, and other factors.  

---

## 📊 Data Used  
- Hours studied per week  
- Attendance rate (%)  
- Previous test scores  
- Family background factors  

---

## 🔎 Regression Model Applied  
They used **Multiple Linear Regression** (because there are many features, not just one).  

---

## 📌 Key Results / Insights  
- **Hours studied** had the **biggest positive effect** → every extra study hour added about **5 points**.  
- **Attendance** also mattered → each **1% increase** added about **0.3 points**.  
- **Previous scores** helped predict future performance.  
- The model could explain about **80% of the variation** in student exam results.  

---

## ✅ In short  
Multiple linear regression helped schools see which factors matter most.  
They learned that **studying regularly + good attendance** are the strongest predictors of success.  

