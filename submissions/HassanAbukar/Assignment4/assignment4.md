# 📘 Lesson 4 — Regression

## 📌 Definition:
- A supervised learning method used when the target (Y) is a **continuous numeric value**.
- The model predicts a number within a range.

### 🔍 Examples:
- Predicting house prices: $150,000 → $200,000  
- Predicting car value: $5,000 → $20,000  
- Predicting temperature: 27.5°C  

### 🛠️ Use Cases:
- Car Price Prediction (your dataset)  
- Sales forecasting  
- Weather prediction  

---

## 🆚 Classification

### 📌 Definition:
- A supervised learning method used when the target (Y) is a **category (class)**.
- The model predicts **discrete labels**, like Yes/No or multiple classes.

### 🔍 Examples:
- Does this person have a disease? → Yes (1) / No (0)  
- Is this email spam? → Spam / Not Spam  
- Animal type → Cat / Dog / Bird  

### 🛠️ Use Cases:
- Love recommender → Is this person a match? Yes/No  
- Sentiment analysis → Positive/Negative  
- Fraud detection → Fraud / Legit  

---

## 🎯 Key Difference

| Task           | Output Type        | Example                        |
|----------------|--------------------|--------------------------------|
| Regression     | Continuous Value   | Car price = $180,000          |
| Classification | Discrete Category  | This email is Spam            |

---

## 📊 Main Types of Regression

### 1. **Simple Linear Regression**
- **Definition:** Predicts the target using one independent variable with a straight-line relationship.
- **Example:** Predict car price based only on CarAge.
- **Strength:** Easy to understand, quick to implement.
- **Limitation:** Only works when the relationship is roughly linear and based on one feature.

### 2. **Multiple Linear Regression**
- **Definition:** Predicts the target using two or more independent variables.
- **Example:** Predict car price using CarAge + Km_per_year + Is_FamilyCar.
- **Strength:** Considers many factors at once.
- **Limitation:** Assumes linearity; sensitive to multicollinearity (when features are highly correlated).

### 3. **Polynomial Regression**
- **Definition:** Extends linear regression by adding polynomial terms (squared, cubic) to capture curves.
- **Example:** Predict housing price based on square footage when the relationship curves upward.
- **Strength:** Captures non-linear trends.
- **Limitation:** Can overfit if degree is too high; harder to interpret.

| **Regression Type** | **Definition**                       | **Example**                             | **Strengths**                        | **Limitations**                                              |
|---------------------|--------------------------------------|-----------------------------------------|-------------------------------------|---------------------------------------------------------------|
| Simple Linear        | One feature with a straight line     | Car price vs CarAge                     | Very easy, interpretable            | Too simple, only one factor, assumes linearity                |
| Multiple Linear      | Many features, still straight line   | Car price vs CarAge + Km_per_year       | Considers multiple factors          | Assumes linearity, sensitive to correlated features           |
| Polynomial           | Adds squared/cubic terms for curves  | House price vs size (curved trend)      | Captures non-linear patterns        | Risk of overfitting, less interpretable                       |


---

## 📏 Regression Metrics

### 1. **MAE – Mean Absolute Error**
- **Definition:** Average of the absolute differences between predicted values and actual values.
- ✅ Easy to understand (real units)  
- ❌ Treats all errors equally; doesn’t punish big mistakes extra.

### 2. **MSE – Mean Squared Error**
- **Definition:** Average of squared differences.
- ✅ Penalizes large mistakes  
- ❌ Units are squared → harder to interpret

### 3. **RMSE – Root Mean Squared Error**
- **Definition:** Square root of MSE.
- ✅ Punishes large errors, keeps units  
- ❌ Still sensitive to outliers

### 4. **R² – Coefficient of Determination**
- **Definition:** How much of the variance in the target is explained by the model.
- ✅ Easy to compare models (higher = better)  
- ❌ Can be misleading if data is non-linear or has outliers

| **Metric** | **Measures**                | **Strength**                        | **Limitation**                            |
|------------|-----------------------------|-------------------------------------|-------------------------------------------|
| **MAE**    | Average absolute error      | Simple, interpretable               | Doesn’t punish big errors                 |
| **MSE**    | Average squared error       | Punishes large errors               | Units squared, hard to read               |
| **RMSE**   | Root of MSE                 | Same units, punishes big errors     | Sensitive to outliers                     |
| **R²**     | % variance explained        | Intuitive, easy to compare          | Misleading with bad models                |

---

## 📉 Underfitting

- **Definition:** Model is too simple; fails to capture patterns in the data  
- **Performance:** Poor on both training and test data  
- **Example:** Linear regression on curved data  
- **Causes:**
  - Too simple model
  - Too few features
  - Too much regularization  
- **Prevention:**
  - Use more complex models (Polynomial, Random Forest)
  - Add more features
  - Reduce regularization

---

## 📈 Overfitting

- **Definition:** Model is too complex; memorizes training data instead of generalizing  
- **Performance:** Great on training, bad on test  
- **Example:** Polynomial regression (degree 15) perfectly fitting all points  
- **Causes:**
  - Too complex model
  - Too little training data
  - Noisy data  
- **Prevention:**
  - Simplify model
  - Use regularization (Ridge, Lasso)
  - Use more data
  - Cross-validation or Early Stopping (for neural nets)

---

## 😎 Good Fit

- **Definition:** Model captures the true patterns without being too simple or too complex  
- **Example:** Predicting house prices with features like size, location, rooms  
- **Signs:**
  - Low training error
  - Validation/test error is also low
  - Generalizes well  
- **Causes of Good Fit:**
  - Right model complexity
  - Good features & preprocessing
  - Enough data  
- **Strategy:**
  - Use train/test split
  - Use cross-validation
  - Regularize appropriately
  - Collect more data if needed

> **In short:**
> - Underfit = Dumb model 🤦  
> - Overfit = Overly clever, memorizing model 🤯  
> - Good Fit = Smart model that generalizes 😎

---

## 🌍 Case Study: Predicting Air Pollution (PM2.5)

### 🎯 Title:  
**Predicting daily PM2.5 air pollution levels in Beijing**

### 🥅 Goal:
- Build a regression model to predict PM2.5 concentration (µg/m³) using weather & seasonal features.
- Support policymakers with early warnings on hazardous air days.

### 📊 Data:
- ~43,800 rows (hourly data, 2010–2014)
- Features:
  - year, month, day, hour  
  - DEWP → Dew point temperature (°C)  
  - TEMP → Temperature (°C)  
  - PRES → Atmospheric pressure (hPa)  
  - WSPM → Wind speed (m/s)  
  - cbwd → Combined wind direction (categorical)  
  - **Target:** PM2.5  

### 🤖 Models Used:
| Model                     | RMSE (µg/m³) | R²     |
|--------------------------|--------------|--------|
| Multiple Linear Regression | ~38         | 0.65   |
| Random Forest Regression   | ~25         | 0.82   |
| XGBoost Regression         | ~21         | 0.89   |

> 🏆 **Best Model:** XGBoost Regression

### 💡 Key Insights:
1. Multiple Linear Regression was too simple → underfitting seasonal effects  
2. Random Forest improved results by capturing non-linearities  
3. XGBoost combined many weak models → strongest generalization  
4. Pollution spikes are influenced by weather & seasonality (esp. winter heating)

---

## 📚 References

- **Dataset:** Beijing PM2.5 Data Set  
- **Source:** Beijing Municipal Environmental Monitoring Center  
- **Hosted at:** UCI Machine Learning Repository  
- **Link:** [UCI – Beijing PM2.5 Data Set](https://archive.ics.uci.edu/ml/datasets/Beijing+PM2.5+Data)

