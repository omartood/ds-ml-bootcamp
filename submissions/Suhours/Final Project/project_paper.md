# 🧠 Sales Price Prediction — Machine Learning Project Report

**Author:** Suhuur Abdikarim Idle  
**Date:** October 2025    
**Project Type:** Machine Learning + Web Deployment  
**Tools Used:** Python, Flask, Scikit-learn, Pandas, NumPy, Next.js, TypeScript  

---

## 1️⃣ Problem Statement & Motivation

In today’s business and retail environments, predicting sales performance accurately is a crucial factor in decision-making, pricing strategy, and revenue management.  
Organizations generate vast amounts of transactional data — including product details, pricing, regions, and sales channels. However, much of this data remains underutilized.  

The core **problem** addressed by this project is:
> *How can we accurately predict the total revenue (sales price) of a product based on various transactional and categorical features?*

This project aims to build a robust **machine learning model** capable of predicting total sales revenue from multiple influencing factors.  
Beyond model accuracy, a key motivation is to **bridge the gap between data science and real-world usability** by integrating the trained model into a **Flask REST API** and **Next.js frontend** — allowing non-technical users to make predictions easily through a web interface.

---

## 2️⃣ Dataset & Preprocessing

### 📊 Dataset Overview

The dataset used is a curated sales dataset named **`clean_sales.csv`**, containing approximately **10,000+ records**. Each record represents a product sale with numerical and categorical attributes.

| Feature | Description |
|----------|--------------|
| `Units Sold` | Number of product units sold |
| `Unit Price` | Selling price per unit |
| `Unit Cost` | Cost per unit incurred by the company |
| `Order Priority` | Level of urgency (Low, Medium, High, Critical) |
| `Sales Channel` | Online or Offline transaction medium |
| `Region` | Geographic region (e.g., Africa, Asia, Europe, etc.) |
| `Country` | Specific country name |
| `Item Type` | Category of the item sold (e.g., Shoes, Clothing, Electronics, etc.) |
| `Order Weekday` | Day of the week when the order was made |
| `Total Profit` | Profit from the sale |
| `Total Revenue` | Target variable to be predicted |

---

### 🧹 Data Cleaning Steps

Before model training, the dataset underwent multiple cleaning and feature engineering stages to ensure high-quality inputs:

1. **Missing Value Handling:**  
   - Numerical columns were filled with 0 or median values.  
   - Categorical columns were filled with `"Other"` or most frequent category.

2. **Outlier Treatment:**  
   - Outliers were capped using **IQR-based capping** to prevent extreme values from skewing model training.  
   - For features like `Units Sold`, `Unit Price`, and `Unit Cost`, values outside the 1.5×IQR range were clipped to the upper or lower bounds.

3. **Feature Engineering:**  
   Several new features were added to enhance model learning and capture non-linear relationships:
   - `Profit_per_Unit = Total Profit / Units Sold`
   - `Total_Revenue = Units Sold * Unit Price`
   - `Log_Profit = log1p(Total Profit)`  
   These engineered features improved model interpretability and helped the Random Forest model achieve better results.

4. **Encoding Categorical Variables:**  
   - One-hot encoding was applied for categorical features like `Region`, `Country`, `Item Type`, `Sales Channel`, and `Order Priority`.
   - This created over 200 feature columns after encoding, improving model expressiveness.

5. **Feature Scaling:**  
   - Numeric features were standardized using `StandardScaler`.  
   - Target variables (`Total Profit`, `Log_Profit`) and dummy variables were excluded from scaling to preserve their interpretability.

---

## 3️⃣ Model Building and Algorithms

Two regression models were trained, compared, and evaluated:

### 🧩 1. Linear Regression
- Acts as the **baseline model**.
- Assumes a linear relationship between features and target.
- Fast to train and interpret, but less capable of handling complex patterns.

### 🌲 2. Random Forest Regressor
- An **ensemble model** that combines multiple decision trees.
- Captures non-linear patterns and handles outliers more robustly.
- Performs feature bagging and averaging to reduce variance.

---

### ⚙️ Model Training Process

1. **Train-Test Split:**  
   - Dataset was split into **80% training** and **20% testing**.
2. **Evaluation Metrics:**  
   - `R² (Coefficient of Determination)`  
   - `MAE (Mean Absolute Error)`  
   - `MSE (Mean Squared Error)`  
   - `RMSE (Root Mean Squared Error)`
3. **Model Saving:**  
   - Trained models were serialized using `joblib`:
     - `lr_model.joblib`
     - `rf_model.joblib`
   - Scaling information and feature columns were stored in:
     - `Sales_scaler.pkl`
     - `train_columns.json`

---

## 4️⃣ Model Evaluation & Results

| Metric | Linear Regression | Random Forest |
|---------|-------------------|----------------|
| **R²** | 0.916 | **0.998** |
| **MAE** | 71,160 | **9,263** |
| **MSE** | 8,922,708,287 | **227,135,063** |
| **RMSE** | 94,460 | **15,071** |

The Random Forest model significantly outperformed Linear Regression across all metrics.  
It provided highly accurate predictions while maintaining low error values.

---

### 📈 Example Predictions

| Units Sold | Unit Price | Unit Cost | Prediction (LR) | Prediction (RF) |
|-------------|-------------|------------|------------------|------------------|
| 12,000 | 30 | 25 | 18,050.89 | **22,375.32** |

---

## 5️⃣ Deployment & System Integration

The project was deployed as a **Flask REST API** integrated with a **Next.js frontend**.  
This setup allows users to input their sales data and instantly receive predictions via a modern web interface.

### ⚙️ Flask API
- Endpoints:
  - `/` → Returns API info and usage details  
  - `/predict?model=lr|rf` → Returns prediction results based on chosen model
- Handles JSON input and outputs formatted JSON response.

### 🌐 Next.js Frontend
- Built using **React + TypeScript + TailwindCSS**
- Features:
  - User-friendly form for entering prediction parameters
  - Dropdown menus for categorical variables (Country, Region, Item Type)
  - Real-time result display
  - Toggle between Linear Regression and Random Forest

---

### 🔄 Example API Call

```bash
curl -X POST "http://127.0.0.1:8000/predict?model=rf" \
  -H "Content-Type: application/json" \
  -d '{
    "Units Sold": 12000,
    "Unit Price": 30,
    "Unit Cost": 25,
    "Order Priority": "High",
    "Sales Channel": "Online",
    "Region": "Sool",
    "Country": "Somalia",
    "Item Type": "Shoes",
    "Order Weekday": "Thursday"
  }'

```
# 🧠 Discussion & Lessons Learned

---

## 🔍 Key Findings

- **Feature Engineering Matters**  
  Derived variables such as `Profit_per_Unit` and `Log_Profit` significantly enhanced predictive accuracy.  
  These transformations helped the models better understand non-linear relationships and reduce bias, proving how crucial domain-informed feature engineering is in applied machine learning.

- **Random Forest Superiority**  
  Compared to Linear Regression, the Random Forest model showed stronger resilience to outliers and captured complex non-linear dependencies between sales variables.  
  This demonstrates the power of ensemble learning when dealing with real-world, noisy business data.

- **Data Preprocessing Impact**  
  Every stage of preprocessing — scaling, encoding categorical variables, and removing outliers — had a measurable influence on model stability and generalization.  
  Without normalization and encoding, model predictions fluctuated drastically.

- **Integration Challenges**  
  Bridging the trained model with the frontend (Next.js) via a Flask API revealed key software engineering lessons.  
  Proper JSON field mapping and consistent naming conventions were essential for smooth request–response flow and for ensuring the frontend form communicated correctly with the backend model.

---

## 💡 Lessons Learned

1. **Machine Learning is Only as Good as the Data**  
   Data quality determines model quality. Even the most sophisticated algorithms fail without careful cleaning, balancing, and preprocessing of raw datasets.

2. **Practical Deployment via Flask + Next.js**  
   Deploying the trained model as a Flask API and linking it with a Next.js frontend offered hands-on experience with production workflows — from serialization using `joblib` to RESTful endpoint handling.

3. **CORS Configuration is Critical**  
   While developing locally, CORS setup was vital to allow communication between the backend (`localhost:8000`) and frontend (`localhost:3000`).  
   This experience emphasized the importance of web security and cross-origin policies in real deployments.

4. **Comprehensive Technical Growth**  
   This project deepened understanding across multiple layers of the ML lifecycle:
   - How APIs transmit model inputs and outputs.
   - The structure of web deployment pipelines.
   - Model versioning, serialization, and prediction handling.
   - Debugging end-to-end integration between Python and JavaScript environments.

---

# 🚀 Future Work

The current implementation operates locally with static models. Potential improvements include:

- 🌍 **Cloud Deployment**  
  Hosting the Flask API on platforms like **Render**, **Railway**, or **AWS Lambda** to enable public access and scalability.

- 💾 **Database Integration**  
  Storing user predictions, request logs, and model statistics in a SQL database (PostgreSQL or SQLite) for deeper performance tracking and analytics.

- 📊 **Interactive Dashboards**  
  Integrating visualization tools such as **Plotly**, **Power BI**, or **Tableau** to provide business insights from prediction history and data trends.

- ⚡ **Model Optimization**  
  Expanding experimentation with **Gradient Boosting**, **XGBoost**, or **LightGBM** for improved accuracy and reduced overfitting.

- 🧩 **Automated Feature Updates**  
  Building a pipeline that automatically updates categorical encodings and scaler parameters whenever new training data arrives.

---

# 🏁 Conclusion

This project showcases the **end-to-end process of designing, building, and deploying a predictive analytics system**.  
From **data preprocessing** and **feature engineering** to **model training**, **evaluation**, and **frontend integration**, each component contributes to a cohesive, real-world machine learning workflow.

The final system delivers accurate sales revenue predictions using a **Random Forest Regressor** while providing a seamless user interface for interaction through the web.  

Ultimately, this project bridges the gap between **data science and practical business decision-making**, highlighting how technical ML systems can transform into functional, user-facing applications ready for deployment.

---

## 🧭 GitHub Repository

Explore the project and full source code here:  
👉 [https://github.com/Suhours/Sales-price-prediction](https://github.com/Suhours/Sales-price-prediction)
