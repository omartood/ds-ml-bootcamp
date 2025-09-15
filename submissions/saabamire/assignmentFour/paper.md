# 📘 Lesson 4 — Regression

## Part A — Regression in Machine Learning

---

## 1. What is Regression?

**Regression** is a way in Machine Learning to predict numbers. For example, to predict the price of a car or the temperature tomorrow. Regression tries to find how input data (like size, age, or location) is connected with the result value.

Regression is not same as classification. In classification, the result is a group or label (for example, “spam” or “not spam”). In regression, the result is a number (for example, 500 dollars, 25°C).

**Example of regression:** predict how many cups of tea a café will sell tomorrow, based on weather and day of the week.

**Example of classification:** decide if a student passed or failed a test, based on their score.

**Key Difference:** regression answers “how much”, while classification answers “which group.”

---

## 2. Types of Regression

These are three basic types:

### a) Linear Regression

This is the most simple type. It tries to draw a straight line between input and output and take decision only one factor.

**Example:** predict a student’s exam score based only on the number of hours they studied.

**Advantage:** easy to use and understand.

**Limitation:** too simple, not good when many factors affect the result.

### b) Multiple Linear Regression

Real world is not only one factor. This type uses many inputs together to predict the result.

**Example:** predict a student’s exam score using hours studied, number of practice exercises done, and amount of sleep the night before.

**Advantage:** more real and gives better prediction.

**Limitation:** need more data and more work to explain.

### c) Polynomial Regression

Sometimes the relation is not straight. Polynomial regression draw a curve instead of line. It uses power values like squared (x²).

**Example:** car value goes down fast in first years, then slow later. A curve shows it better.

**Advantage:** It can follow patterns that are not straight, so it works better when data has curves.

**Limitation:** If the curve is too flexible, the model learns noise, and it will not predict new data well.

### 📊 Table: Comparison of Regression Types

| Type                       | Shape of Relationship    | Example Features                                    | Best For                                  |
| -------------------------- | ------------------------ | --------------------------------------------------- | ----------------------------------------- |
| Linear Regression          | Straight line            | Study hours → Exam score                            | Simple cases with one main factor         |
| Multiple Linear Regression | Flat plane (many inputs) | Study hours, Sleep, Practice exercises → Exam score | Problems where many factors affect result |
| Polynomial Regression      | Curved line              | Age, Age² → Child’s height                          | Non-linear patterns that change over time |

---

## 3. Regression Metrics

We need to check if our model is good. Metrics are numbers to measure this.

* **MAE (Mean Absolute Error):** average distance between prediction and real value.
* **MSE (Mean Squared Error):** square the error then take average, big mistakes count more.
* **RMSE (Root Mean Squared Error):** square root of MSE, result in same unit as target.
* **R² (Coefficient of Determination):** shows how much of data pattern is explained by model. 1 is perfect, 0 means very weak and negative very very weak.

### 📊 Comparison Table of Regression Metrics

| Metric                            | Meaning                                                                 | Unit                                  | Sensitive to Big Errors? |
| --------------------------------- | ----------------------------------------------------------------------- | ------------------------------------- | ------------------------ |
| MAE (Mean Absolute Error)         | Average size of mistakes (how far predictions are from real values)     | Same as target (e.g., dollars, hours) | ❌ No                     |
| MSE (Mean Squared Error)          | Average of squared mistakes, big errors count much more                 | Squared units (e.g., dollars²)        | ✅ Yes                    |
| RMSE (Root Mean Squared Error)    | Square root of MSE, easier to read because same unit as target          | Same as target                        | ✅ Yes                    |
| R² (Coefficient of Determination) | How much of the result is explained by the model (0 = bad, 1 = perfect) | No unit (0–1 scale)                   | ❌ No                     |

---

## 4. Underfitting and Overfitting

**Underfitting:** model too simple, cannot learn real pattern. Example: predict price only by size when other features also important.

**Overfitting:** model too complex, tries to learn even the noise. Works good on training but bad on new data. Often happens in high degree polynomial regression.

**Why overfitting happens:**

* Model is too big or too complex.
* Not enough training data.
* Too many unnecessary features.

**Ways to reduce overfitting:**

* Use less features or smaller degree of polynomial.
* Use regularization (L1 or L2).
* Add more training data.

---

## 5. Case Study — Regression in Healthcare

**Title:** “Medical Costs Estimation Using Linear Regression Method” (Source: SciSpace, 2023)

**Goal:** Estimate annual medical expenses for individuals based on demographic and health-related factors.

**Data:** A dataset containing attributes such as age, gender, body mass index (BMI), number of children, smoking habits, region, and medical charges.

**Model:** Multiple Linear Regression

**Results:**

* Achieved an R² value of 0.79.99, indicating that 79.99%  of the variance in medical costs was explained by the model.
* Lower Mean Squared Error (MSE) and Mean Absolute Error (MAE) compared to simple linear regression models.
* Smoking status, BMI, and age were identified as significant predictors of higher medical costs.

**Insight:** This study demonstrates how regression models can effectively estimate healthcare expenses, aiding in resource allocation and financial planning for healthcare providers.

References

Alpaydin, E. (2020). Introduction to Machine Learning (4th ed.). MIT Press.

Géron, A. (2019). Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow (2nd ed.). O’Reilly Media.

James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013). An Introduction to Statistical Learning with Applications in R. Springer.


Dwikasari, N. M. D. (2023). Medical Costs Estimation Using Linear Regression Method. Jurnal Ilmiah Merpati, 11(3), 173–180. Retrieved from https://scispace.com/pdf/medical-costs-estimation-using-linear-regression-method-38k6wo4bri.pdf