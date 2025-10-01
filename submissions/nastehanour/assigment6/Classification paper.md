---

## 1. Introduction to Classification

Classification is a type of supervised learning in Machine Learning where the target variable is categorical. Instead of predicting a continuous value, the task is to assign an observation to a predefined class. For example, a classification model may determine whether a transaction is fraudulent or legitimate.

Classification differs from regression, which predicts continuous numerical values. Regression estimates how much (e.g., predicting house prices), while classification determines which class (e.g., whether an email is spam or not).

A real-life example of classification is medical diagnosis, where an algorithm predicts whether a patient has diabetes (yes/no). A real-life example of regression is predicting the selling price of a used car based on its mileage, age, and brand.



## Difference from Regression:**  

- Classification → predicts discrete outcomes (catagory,class)  
- Regression → predicts continuous numerical values(numbers)  

**Examples:**  
- **Classification:** Predicting if a patient has diabetes ("Yes"/"No")  
- **Regression:** Estimating the market value of a house based on size and location

---

## 2A. Classification Algorithms

### 1. Logistic Regression

**How it works:**  
Uses the **sigmoid function** to estimate the probability of belonging to a class (0–1). A threshold (usually 0.5) determines the final prediction.

**Use Case:**  
Email spam detection

**Advantages:**  
- Simple and efficient  
- Interpretable coefficients  
- Works well with linearly separable data  

**Limitations:**  
- Not suitable for complex, non-linear data  
- Multi-class requires extensions  
- Sensitive to correlated features

---

### 2. Decision Trees

**How it works:**  
Splits data into subsets based on feature values, forming a tree structure. Each internal node is a decision, branches represent outcomes, leaves assign class labels. Splits aim to **maximize information gain** or **minimize Gini impurity**.

**Use Case:**  
Diagnosing diseases based on patient symptoms

**Advantages:**  
- Easy to visualize and interpret  
- Handles numerical and categorical features  
- No feature scaling needed

**Limitations:**  
- Can overfit  
- Sensitive to small data changes  
- Less accurate alone than ensemble methods

---

### 3. Random Forest

**How it works:**  
Ensemble of decision trees trained on random subsets of data/features. Final prediction is based on **majority voting**.

**Use Case:**  
Detecting fraudulent bank transactions

**Advantages:**  
- Reduces overfitting  
- Robust and accurate  
- Handles large datasets well

**Limitations:**  
- Less interpretable  
- Requires more memory and computation  
- Slower training/prediction

---

## 2B. Extended Task – K-Nearest Neighbors (KNN)

**Problem it solves:**  
Good for non-linear relationships where similar instances belong to the same class.

**Core idea:**  
Predicts a new instance’s class based on the majority class of its **k nearest neighbors** (distance metrics like Euclidean).

**Real-world Application:**  
Movie or product recommendation systems

**Strengths:**  
- Simple and flexible  
- Non-parametric, no explicit training  
- Can model complex boundaries

**Weaknesses:**  
- Slow for large datasets  
- Sensitive to noisy/irrelevant features  
- Requires careful choice of k and distance metric

---

## 3. Classification Metrics

| Metric          | Definition / Focus                 | Best Use Case                     | Limitation                          |
|-----------------|----------------------------------|----------------------------------|------------------------------------|
| Accuracy        | Proportion of correct predictions | Balanced datasets                 | Misleading with imbalanced data    |
| Precision       | Correctness of predicted positives| When false positives are costly   | Ignores false negatives             |
| Recall          | Proportion of actual positives detected | When false negatives are costly | Ignores false positives             |
| F1-Score        | Harmonic mean of precision & recall | Imbalanced datasets              | Harder to interpret than accuracy   |
| Confusion Matrix| TP, TN, FP, FN breakdown          | Detailed error analysis           | Cannot summarize as single value   |


---

## 4. Imbalanced Data Problem

**Definition:**  
Occurs when one class has far fewer instances than another.  
- Example: 1000 patients → 990 healthy, 10 sick

**Why Accuracy is Misleading:**  
Predicting all as healthy gives 99% accuracy but fails to detect sick patients.

**Reliable Metrics:**  
- Precision, Recall, F1-Score  
- Techniques like **SMOTE** or cost-sensitive learning help improve performance

---

## 5. Real-World Case Study – Customer Churn Prediction (Libyan ISP)

**Goal:** Predict which customers are likely to leave the ISP to reduce churn.

**Data:**  
- 3,606 customers, 11 features  
- Only 5% churned → highly imbalanced

**Models Applied:**  
- Logistic Regression, Decision Tree, Random Forest, Gradient Boosting, XGBoost  
- Oversampling (SMOTE / SMOTEENN) applied

**Key Results:**  
- Original data → poor minority detection  
- Oversampling → improved predictions  
- Best models: XGBoost & GBM, AUC = 94%

**Conclusion:** Handling imbalanced data and selecting appropriate models is crucial for effective classification.

