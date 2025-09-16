# 📝 Assignment 4 — Regression

**Theory Assignment**

---
## 1. Introduction to Regression

In machine learning, **regression** is a type of supervised learning used to predict a **continuous numeric value** based on input data. It's a way to answer questions like **How much? or How many?**.

The key difference between **regression** and **classification** is the type of **output**. While regression predicts **a quantity**, classification predicts **a category**. A classification model would sort something into a specific group, such as deciding if a loan application is **low-risk, medium-risk, or high-risk**.

* **Regression Example:** A model that predicts a student's final score (a number) based on how much time they studied.
* **Classification Example:** A model that predicts if a customer will either "buy" or "not buy" a product.
---

## 2. Types of Regression

### **a) Linear Regression**

Linear regression is a simple model that identifies a straight-line relationship between a single input feature and a target variable. It is the most basic form of regression.

* **How It Works:** It finds a straight line that best fits the data points to make predictions.
* **Real-World Use Case:** Predicting a person's weight based only on their height.
* **Advantages:** It's easy to understand and quick to train.
* **Limitations:** It can only model linear relationships and won't work well if the data has a curved pattern.

### **b) Multiple Linear Regression**

This type of regression builds on linear regression by using two or more features to predict a single outcome.

* **How It Works:** Instead of a single line, it fits a flat plane in a multi-dimensional space to the data.
* **Real-World Use Case:** Forecasting a company's sales by considering advertising spending, the number of employees, and the time of year.
* **Advantages:** It is more realistic for real-world problems that involve many influencing factors.
* **Limitations:** It can be unreliable if some of the input features are too similar to each other (a condition known as multicollinearity).

### **c) Polynomial Regression**

Polynomial regression is a flexible model that can capture non-linear, or curved, relationships between features and the target variable.

* **How It Works:** It extends the linear model by including features raised to different powers (e.g., $x^2$, $x^3$), allowing it to fit a curve to the data.
* **Real-World Use Case:** Modeling the growth of a bacterial colony over time, which often follows a non-linear, S-shaped curve.
* **Advantages:** It is very good at identifying and fitting curved patterns in the data.
* **Limitations:** It can easily become too complex and overfit the training data if the polynomial degree is too high.
----

### 📊 Table: Comparison of Regression Types

| Type                       | Shape of Relationship  | Example Features                 | Best for                      |
| -------------------------- | ---------------------- | -------------------------------- | ----------------------------- |
| **Linear Regression** | A straight line | A house's size to predict its price | Simple predictions with a single factor |
| **Multiple Linear Regression** | A flat plane in multiple dimensions | Size, bedrooms, and location to predict price | Complex, multi-factor problems |
| **Polynomial Regression** | A curved line | A house's size and size squared to predict price | Capturing non-linear patterns in the data |

---

## 3. Regression Metrics

When we evaluate a regression model, we use different metrics to measure how accurate its predictions are.

| Metric                                | What It Measures                         | Sensitive to Large Errors? | Units        |
| ------------------------------------- | --------------------------------- | -------------------------- | ------------ |
| **MAE** (Mean Absolute Error) | The average of all prediction errors, ignoring their direction. | ❌ No | Same as the data (e.g., dollars). |
| **MSE** (Mean Squared Error) | The average of the squared errors, which heavily penalizes bigger mistakes. | ✅ Yes | Squared units (e.g., $dollars^2$). |
| **RMSE** (Root Mean Squared Error) | The square root of the MSE, returning the error to the original data's units. | ✅ Yes | Same as the data (e.g., dollars). |
| **R²** (Coefficient of Determination) | The percentage of the target variable's variation that the model can explain. | ❌ No | A score from 0 to 1 (or %). |

---

## 4. Underfitting and Overfitting

**Underfitting:** occurs when a model is too simple to learn the basic patterns in the data, resulting in poor performance on both the data it was trained on and new data. Think of it like a student who doesn't study at all for a test; they will perform poorly because they haven't learned the material.

**Overfitting:** happens when a model is overly complex and learns the training data, including its random noise, too well. This model performs perfectly on the training data but fails on new data because it has memorized the answers instead of learning the general rules. This is like a student who memorizes a practice test but then can't answer different questions on the actual exam. Polynomial regression, especially with a high degree, can easily overfit the data.

### Causes of Underfitting:

* Using a model that is too simple for the complexity of the data.
* Having too few features in the dataset.
* Not training the model for a long enough period.

### Causes of Overfitting:

* Using an overly complex model.
* A dataset that is too small or does not have enough variety.
* Including too many features that are not relevant to the prediction.

### How to Prevent:

* **Underfitting:** Use a more complex model, add more relevant features, or train the model for a longer duration.
* **Overfitting:** Use a simpler model, collect more data, or use regularization to penalize complexity.

---

## 5. Real-World Case Study: Regression in Agriculture

**Title:** “Predicting Crop Yield with Multiple Linear Regression” (*Source: ResearchGate, 2021*)

**Goal:** The main objective was to predict crop yield by analyzing the effects of various weather variables and other factors. This kind of prediction can help farmers and agricultural businesses plan for the upcoming season and optimize resource allocation.

**Data:** The researchers used real agricultural data, including weather variables like rainfall, temperature, and humidity, along with the area of land for cultivation. The dependent variable was the crop yield itself.

**Model:** The study used a **Multiple Linear Regression** model to study how these different variables influenced the crop yield. This model was chosen because it allows for the analysis of how multiple factors simultaneously affect a single outcome, providing a more comprehensive understanding than a simple regression model.

**Results:**

* The results showed that the yield of crops was significantly dependent on climatic variables.
* For instance, rainfall was found to have a significant influence on the yield of crops like rice and maize.
* The model's accuracy was confirmed by its ability to predict crop yield effectively.
* One study was able to predict crop yield 6-8 weeks before harvest with an R² of 0.75 and RMSE of 0.281 (t/ha).

**Insight:** This case study highlights how multiple linear regression is a valuable tool in agriculture. It helps farmers understand the complex relationships between weather, land, and crop production, allowing them to make informed decisions to increase yields and avoid financial loss.

---