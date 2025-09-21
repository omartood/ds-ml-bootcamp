# 🚗 Car Price Prediction — Linear Regression vs. Random Forest

## 1) What did you implement?
I trained two models on the car dataset to predict **car prices**:

- **Linear Regression (LR):** assumes car price is a weighted sum of the features (odometer, accidents, age, location, etc.).  
- **Random Forest (RF):** builds many decision trees on random subsets of data and averages their outputs to capture non-linear effects.

The dataset was split into **80% training** and **20% testing**, and both models were evaluated on the held-out set.

---

## 2) Comparison of Models — Sanity Check

I performed three single-row sanity checks to see if predictions made sense compared to actual prices:

- **Sanity Check 1**  
  - Actual Price: **$1,500**  
  - LR Pred: **$433** (severely underestimated)  
  - RF Pred: **$1,500** (almost exact)  
  👉 **RF was much more realistic.**

- **Sanity Check 2**  
  - Actual Price: **$7,009**  
  - LR Pred: **$5,694** (underestimated by about $1,300)  
  - RF Pred: **$6,888** (very close to actual)  
  👉 **RF was closer to reality.**

- **Sanity Check 3**  
  - Actual Price: **$1,500**  
  - LR Pred: **$2,547** (overestimated by about $1,000)  
  - RF Pred: **$1,634** (almost correct)  
  👉 **RF again gave the more realistic estimate.**

📌 **Overall:** Random Forest consistently produced **more realistic predictions** than Linear Regression in these sanity checks.

---

## 3) Understanding Random Forest

- **What is Random Forest?**  
  A Random Forest is an **ensemble** of decision trees. Each tree is trained on a random sample of the data and features.

- **How does it work?**  
  1. Each decision tree makes a prediction.  
  2. For regression tasks, the forest averages the predictions.  
  3. This reduces overfitting and captures **non-linear patterns** (e.g., sudden price drops for old or accident-heavy cars).

---

## 4) Metrics Discussion

On the test set, the results were:

**Linear Regression Performance**  
- R²   : **0.435**  
- MAE  : **$1,427**  
- RMSE : **$1,939**  

**Random Forest Performance**  
- R²   : **0.269**  
- MAE  : **$1,213**  
- RMSE : **$2,206**  

**Interpretation:**  
- LR had **higher R²** (explained more of the variance).  
- RF had **slightly lower MAE**, but its RMSE was worse (more large errors).  
- This means LR was better at capturing the **overall price trend**, while RF was better at predicting **individual cases** (as shown in sanity checks).

---

## 5) Findings

For this dataset:  
- **Random Forest** gave more **realistic single predictions** in the sanity checks.  
- **Linear Regression** explained the overall variance better and had more stable trend-following performance.

👉 My preference would be to **use Random Forest when predicting individual car prices** (because it is closer to actuals), but keep **Linear Regression as a benchmark** since it is simpler and explains general relationships better.
