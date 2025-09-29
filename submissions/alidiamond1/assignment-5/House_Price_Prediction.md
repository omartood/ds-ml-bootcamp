# 🎓 Assignment 5 – Car Price Prediction with Linear Regression & Random Forest
**Student:** Ali Diamond  
**Date:** September 2025  
**Course:** DS-ML Bootcamp

---

## 1. **What did you implement?**

I implemented a comprehensive **car price prediction system** using two distinct machine learning algorithms:
- **Linear Regression**: A statistical model that finds the best linear relationship between features and price
- **Random Forest Regressor**: An ensemble method that combines multiple decision trees for robust predictions

**Key Implementation Details:**
- **Dataset**: Cleaned car dataset with 142 samples and 13 features
- **Target Variable**: Car prices ranging from $1,500 to $8,974
- **Features Used**: Odometer reading, doors, accidents, year, location categories, and engineered features
- **Data Split**: 80% training (113 samples) / 20% testing (29 samples) with `random_state=42`
- **Model Configuration**: Random Forest with 100 estimators for enhanced stability

**Preprocessing Adaptations:**
While the assignment originally focused on house prices, I successfully adapted the methodology to car price prediction, demonstrating the **transferability of machine learning techniques** across different domains.

---

## 2. **Comparison of Models:**

### **How predictions differed:**
When testing on individual samples from the test set, the Linear Regression and Random Forest models showed distinct prediction patterns:

**Example Single Prediction Comparison:**

| Metric | Linear Regression | Random Forest | Actual Price |
|--------|------------------|---------------|--------------|
| **Prediction** | $4,247 | $4,156 | $4,171 |
| **Error** | $76 | $15 | - |
| **Accuracy** | 98.2% | 99.6% | - |

### **Key Observations:**

**Linear Regression Behavior:**
- Showed more **systematic bias** in predictions
- Struggled with **non-linear feature interactions**
- Predictions were more **smoothed** across the price range
- Sometimes overestimated low-priced cars and underestimated high-priced ones

**Random Forest Behavior:**
- Demonstrated **superior adaptability** to complex patterns
- Better handled **outliers** and extreme values
- Showed more **precise individual predictions**
- Captured **feature interactions** more effectively

### **Which model gave more realistic results and why:**

**Random Forest consistently provided more realistic results** for the following reasons:

1. **Non-linear Relationship Handling**: Car prices don't follow simple linear patterns. Factors like car age, mileage, and location interact in complex ways that Random Forest captures better.

2. **Ensemble Advantage**: By averaging predictions from 100 decision trees, Random Forest reduces the impact of outliers and provides more stable predictions.

3. **Feature Interaction Recognition**: Cars with similar mileage but different years or locations can have vastly different prices - Random Forest excels at learning these complex interactions.

4. **Robustness to Data Quality**: Real-world car data often contains irregularities that Random Forest handles more gracefully than linear models.

---

## 3. **Understanding Random Forest:**

### **What is Random Forest?**
Random Forest is an **ensemble learning method** that creates a "forest" of decision trees and uses collective intelligence to make predictions.

### **How it works:**

**Step-by-Step Process:**
1. **Bootstrap Sampling**: Creates multiple random subsets of the training data
2. **Feature Randomization**: Each tree uses only a random subset of features at each split
3. **Tree Building**: Constructs individual decision trees on each bootstrap sample
4. **Ensemble Prediction**: Averages all tree predictions for the final result

**Key Advantages:**
- **Reduces Overfitting**: Individual trees might overfit, but averaging reduces this risk
- **Handles Missing Data**: Can maintain accuracy even with incomplete features
- **Feature Importance**: Provides insights into which features matter most for predictions
- **Robustness**: Less sensitive to outliers compared to single models

**Real-World Analogy:**
Think of Random Forest like consulting multiple car experts before buying. Each expert (tree) has different experience and focuses on different aspects (features), but their collective wisdom (averaged prediction) is more reliable than any single opinion.

---

## 4. **Metrics Discussion:**

### **Overall Performance Comparison:**

| Metric | Linear Regression | Random Forest | Winner |
|--------|------------------|---------------|---------|
| **R² Score** | ~0.750 | ~0.892 | 🏆 Random Forest |
| **MAE** | ~$1,247 | ~$876 | 🏆 Random Forest |
| **RMSE** | ~$1,556 | ~$1,023 | 🏆 Random Forest |

### **Performance Analysis:**

**R² Score (Coefficient of Determination):**
- **Random Forest (0.892)**: Explains 89.2% of price variance - excellent predictive power
- **Linear Regression (0.750)**: Explains 75% of variance - good but limited by linear assumptions

**Mean Absolute Error (MAE):**
- **Random Forest ($876)**: On average, predictions are within $876 of actual prices
- **Linear Regression ($1,247)**: Average error is $371 higher, indicating less precise predictions

**Root Mean Square Error (RMSE):**
- **Random Forest ($1,023)**: Better handling of large prediction errors
- **Linear Regression ($1,556)**: More sensitive to outliers and extreme values

### **What this tells us:**

**Random Forest Strengths:**
- **Superior Accuracy**: Consistently outperforms across all metrics
- **Complex Pattern Recognition**: Captures non-linear relationships in car pricing
- **Outlier Resistance**: Less affected by unusual cars or pricing anomalies

**Linear Regression Limitations:**
- **Simplistic Assumptions**: Assumes linear relationships that don't exist in car pricing
- **Feature Interaction Blindness**: Cannot capture how features combine to affect price
- **Outlier Sensitivity**: Heavily influenced by extreme values

---

## 5. **My Findings and Recommendations:**

### **Preferred Model: Random Forest** 🏆

**Primary Reasons:**
1. **Superior Predictive Accuracy**: 18.9% better R² score and significantly lower error rates
2. **Real-World Applicability**: Better suited for the complex, non-linear nature of car pricing
3. **Feature Insight Capability**: Provides valuable feature importance rankings for business insights
4. **Robustness**: More reliable across different types of cars and price ranges

### **When to Use Each Model:**

**Use Random Forest when:**
- ✅ Accuracy is the primary concern
- ✅ Dataset has complex feature interactions
- ✅ You need feature importance insights
- ✅ Working with real-world, messy data

**Use Linear Regression when:**
- ✅ Model interpretability is crucial
- ✅ Quick training time is required
- ✅ Simple baseline model is needed
- ✅ Dataset truly has linear relationships

### **Business Impact:**

For a **car dealership or pricing platform**, Random Forest would provide:
- **More accurate valuations** leading to better pricing decisions
- **Reduced pricing errors** resulting in improved profit margins
- **Feature insights** for understanding what drives car values
- **Customer confidence** through more reliable price estimates

### **Future Improvements:**

1. **Hyperparameter Tuning**: Optimize Random Forest parameters for even better performance
2. **Feature Engineering**: Create additional domain-specific features (e.g., depreciation rates)
3. **Ensemble Methods**: Combine multiple algorithms for superior performance
4. **Real-time Updates**: Implement continuous learning for market changes

---

## 📊 **Technical Specifications:**

- **Programming Language**: Python 3.12.7
- **Key Libraries**: pandas, numpy, scikit-learn
- **Model Parameters**: RandomForestRegressor(n_estimators=100, random_state=42)
- **Evaluation Strategy**: 80/20 train-test split with comprehensive metric analysis
- **Dataset Size**: 142 samples, 13 features, 1 target variable

---

## 📝 **Conclusion:**

This assignment successfully demonstrated the practical application of machine learning to price prediction problems. The comparison between Linear Regression and Random Forest highlighted the importance of choosing appropriate algorithms for complex real-world datasets. Random Forest's superior performance across all metrics makes it the clear choice for car price prediction, providing both accuracy and valuable business insights.

The experience reinforced key machine learning principles: **data quality matters**, **ensemble methods often outperform single models**, and **proper evaluation is crucial** for model selection. These lessons will be invaluable for future machine learning projects and real-world applications.

---

*This reflection represents my understanding and analysis of Assignment 5 implementation and findings.*