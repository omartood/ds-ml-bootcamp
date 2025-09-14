
## 🔹 Imagine the Problem

We want to predict **house prices**.  

- Actual prices (in $1000s): `[100, 150, 200]`  
- Model predictions: `[110, 140, 195]`  

So errors = difference between actual and predicted.

---

## 1️⃣ **MAE (Mean Absolute Error)**

**Formula:**

$$
MAE = \frac{1}{n} \sum |y_{actual} - y_{predicted}|
$$

**Meaning:** Average of **absolute errors** (ignores +/– sign).  

**Example:**
- Errors = |100–110|, |150–140|, |200–195| = `[10, 10, 5]`  
- MAE = (10 + 10 + 5) / 3 = **8.3**  

👉 **Interpretation:** On average, our predictions are **off by $8.3k**.

---

## 2️⃣ **MSE (Mean Squared Error)**

**Formula:**

$$
MSE = \frac{1}{n} \sum (y_{actual} - y_{predicted})^2
$$

**Meaning:** Average of **squared errors** (penalizes big mistakes more).  

**Example:**
- Errors² = `[100, 100, 25]`  
- MSE = (100 + 100 + 25) / 3 = **75**  

👉 **Interpretation:** Squared error average is 75. Units are not the same as target (less intuitive).

---

## 3️⃣ **RMSE (Root Mean Squared Error)**

**Formula:**

$$
RMSE = \sqrt{MSE}
$$

**Meaning:** Just the square root of MSE → brings it back to original units.  

**Example:**
- RMSE = √75 ≈ **8.66**  

👉 **Interpretation:** On average, predictions are off by about **$8.66k**.

---

## 4️⃣ **R² (R-Squared, Coefficient of Determination)**

**What is R²?**

- **R² (R-squared)** is a metric that shows **how well a regression model fits the data**.  
- In simple terms: it tells you **how much of the variation in the target (y) is explained by the model**.  
- **Range:**  
  - **1** → perfect prediction  
  - **0** → model does no better than predicting the average  
  - **Negative** → model is worse than predicting the average  

**Formula:**

$$
R^2 = 1 - \frac{\text{Sum of Squared Errors (SSE)}}{\text{Total Sum of Squares (SST)}}
$$

Where:  
- SSE = sum of squared differences between **actual and predicted values**  
- SST = sum of squared differences between **actual values and their mean**  

---

### Example of R²

| House | Actual Price | Predicted Price |
| ----- | ------------ | --------------- |
| 1     | 100          | 110             |
| 2     | 150          | 140             |
| 3     | 200          | 195             |

**Step 1: Compute mean of actual prices**

$$
\bar{y} = \frac{100 + 150 + 200}{3} = 150
$$

**Step 2: Compute SSE (Sum of Squared Errors)**

$$
SSE = (100-110)^2 + (150-140)^2 + (200-195)^2 = 100 + 100 + 25 = 225
$$

**Step 3: Compute SST (Total Sum of Squares)**

$$
SST = (100-150)^2 + (150-150)^2 + (200-150)^2 = 2500 + 0 + 2500 = 5000
$$

**Step 4: Compute R²**

$$
R^2 = 1 - \frac{SSE}{SST} = 1 - \frac{225}{5000} = 0.955
$$

**Interpretation:**  
- **R² = 0.955** → The model explains **95.5% of the variation** in house prices.  
- The closer R² is to **1**, the better the model fits the data.

---

## ✅ Summary

| Metric   | What it means        | Example value | Easy Interpretation                          |
| -------- | -------------------- | ------------- | -------------------------------------------- |
| **MAE**  | Avg. absolute error  | 8.3           | On average, predictions are off by $8.3k    |
| **MSE**  | Avg. squared error   | 75            | Squared errors, penalizes large mistakes     |
| **RMSE** | Square root of MSE   | 8.66          | Same as MAE but more sensitive to big errors |
| **R²**   | % variance explained | 0.955         | Model explains 95.5% of variation            |

---

## 👉 In practice:

- **MAE** = simple, easy to understand.  
- **RMSE** = better if you want to penalize big mistakes.  
- **R²** = tells you how “good” the overall fit is.  
