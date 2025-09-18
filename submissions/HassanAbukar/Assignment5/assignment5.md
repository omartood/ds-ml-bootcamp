## 🏠 House Price Prediction – Regression (LR vs RF)
🎯 Goal

Predict the price of a house (Price) using various features.

## 📊 Sample Output – Single Row Sanity Check

Single Row Sanity Check
	•	Actual Price (Target): $948
	•	LR Prediction: $822,635
	•	RF Prediction: $821,977

## 👉 Why we use this?
A single row sanity check ensures the model outputs predictions in the expected range and format for an individual example. It’s a quick way to confirm that the model is not producing absurd results (e.g., negative prices) and helps compare actual vs predicted values directly.

⸻

## Model Metrics

Prediction of LR
	•	R²: 0.848
	•	MAE: 63,086
	•	MSE: 5,718,940,941
	•	RMSE: 75,624

Prediction of RF
	•	R²: 0.859
	•	MAE: 52,524
	•	MSE: 5,283,317,455
	•	RMSE: 72,686

## 📊 Model Comparison: LR vs RF
| Aspect                   | Linear Regression (LR) | Random Forest (RF) |
|---------------------------|-------------------------|---------------------|
| *Why used*             | Baseline model: simple, interpretable, shows feature impact directly | Advanced model: captures non-linear patterns, interactions, and handles complex data |
| *Strengths*            | - Easy to explain<br>- Very fast<br>- Coefficients show feature importance | - High accuracy<br>- Handles non-linear data<br>- Robust to outliers<br>- Works well with mixed features |
| *Limitations*          | - Assumes linear relationships<br>- Sensitive to outliers<br>- Weak with complex data | - Harder to interpret (black-box)<br>- Slower and more resource-heavy |
| *Best for*             | Understanding relationships, quick baseline checks | Production-ready predictions, when accuracy is more important than interpretability |
| *Which performed better here?* | R² = 0.848, MAE ≈ 63K | R² = 0.859, MAE ≈ 52K (*better fit*) |

## 📊 Metrics Comparison: LR vs RF

| Metric   | Linear Regression (LR) | Random Forest (RF) |
|----------|-------------------------|---------------------|
| *R²*   | 0.848                   | 0.859               |
| *MAE*  | 63,086                  | 52,524              |
| *MSE*  | 5,718,940,941           | 5,283,317,455       |
| *RMSE* | 75,624                  | 72,686              |

## ✅ Final Note:

	•	Both models work well, but Random Forest achieved higher accuracy (better R², lower MAE & RMSE).
	•	Linear Regression is still useful for interpretation and baseline comparison.