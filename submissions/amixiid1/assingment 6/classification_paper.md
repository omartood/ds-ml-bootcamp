# 📝 Classification Assignment  

**Due:** Saturday, September 20, 2025 — 12:00 PM (Africa/Mogadishu / EAT)  
**Goal:** Understand the key concepts, algorithms, and evaluation metrics of Classification in Machine Learning.  

---

## 1. Introduction to Classification  

Classification is a fundamental task in Machine Learning where the goal is to assign input data into predefined categories or labels. For example, given an email, a classification model predicts whether it is *spam* or *not spam*. This process involves learning patterns from training data and applying them to new, unseen data.  

**Difference from Regression:**  
- **Classification** predicts *discrete categories* (e.g., “yes” or “no,” “disease” or “no disease”).  
- **Regression** predicts *continuous values* (e.g., predicting house prices or temperature).  

**Examples:**  
- **Classification:** Predicting whether a transaction is *fraudulent* or *legitimate*.  
- **Regression:** Estimating the *price* of a car based on mileage and age.  

---

## 2A. Classification Algorithms  

### Logistic Regression  
- **How it works:** Uses a logistic (sigmoid) function to map inputs to probabilities between 0 and 1, then classifies based on a threshold (e.g., 0.5).  
- **Use case:** Email spam detection.  
- **Advantages:** Simple, interpretable, works well on linearly separable data.  
- **Limitations:** Struggles with complex, nonlinear relationships.  

### Decision Trees  
- **How it works:** Splits the dataset into branches based on feature values, forming a tree structure where leaves represent decisions.  
- **Use case:** Predicting loan approval in banking.  
- **Advantages:** Easy to interpret, handles both numerical and categorical data.  
- **Limitations:** Prone to overfitting, sensitive to small data changes.  

### Random Forest  
- **How it works:** Combines many decision trees (ensemble method) and averages their results to improve accuracy and reduce overfitting.  
- **Use case:** Customer churn prediction in telecom.  
- **Advantages:** High accuracy, robust against overfitting, works well on large datasets.  
- **Limitations:** Less interpretable, computationally expensive.  

---

## 2B. Extended Task – Support Vector Machines (SVM)  

- **Problem suitability:** Excellent for binary classification tasks with clear margins of separation.  
- **How it works:** Finds the optimal hyperplane that maximizes the margin between two classes. Can use kernel functions to handle non-linear boundaries.  
- **Use case:** Face recognition systems.  
- **Strengths:** Effective in high-dimensional spaces, robust to overfitting when properly tuned.  
- **Weaknesses:** Training can be slow on large datasets, less effective when classes overlap heavily compared to Random Forest or Neural Networks.  

---

## 3. Classification Metrics  

- **Accuracy:** Proportion of correct predictions over total predictions. Works well when classes are balanced.  
- **Precision:** Of all predicted positives, how many were actually positive. Important when false positives are costly (e.g., fraud alerts).  
- **Recall:** Of all actual positives, how many were correctly predicted. Important when missing a positive is costly (e.g., cancer diagnosis).  
- **F1-Score:** Harmonic mean of precision and recall; balances both in one metric.  
- **Confusion Matrix:** A table summarizing true positives, false positives, true negatives, and false negatives.  

**Comparison Table:**  

| Metric            | Focus                          | Best Use Case                           | Weakness                   |  
|-------------------|--------------------------------|------------------------------------------|----------------------------|  
| Accuracy          | Overall correctness            | Balanced datasets                        | Misleading on imbalance    |  
| Precision         | Avoiding false positives       | Fraud detection, spam filters            | Ignores false negatives    |  
| Recall            | Capturing true positives       | Medical diagnosis, safety-critical tasks | Ignores false positives    |  
| F1-Score          | Balance of precision & recall  | When trade-off is needed                 | Harder to interpret        |  
| Confusion Matrix  | Full error breakdown           | Model evaluation & debugging             | Hard to summarize in one value |  

---

## 4. Imbalanced Data Problem  

Imbalanced data occurs when one class significantly outnumbers the other(s). For example, in fraud detection, 99% of transactions are normal while only 1% are fraudulent.  

- **Why accuracy is misleading:** A model that predicts *“always normal”* could achieve 99% accuracy but completely fail to detect fraud.  
- **Better metrics:** Precision, Recall, F1-Score, and the Confusion Matrix are more reliable since they reveal performance on minority classes.  

---

## 5. Real-World Case Study – Medical Diagnosis (Breast Cancer Detection)  

- **Goal:** Predict whether a tumor is malignant (cancerous) or benign (non-cancerous).  
- **Data:** The Wisconsin Breast Cancer Dataset, containing features such as cell size, texture, and shape.  
- **Model used:** Support Vector Machine (SVM) and Random Forest classifiers.  
- **Key results:** Both models achieved high accuracy (over 95%), with SVM excelling in precision and Random Forest providing higher recall. The study showed that machine learning can effectively assist doctors in early cancer detection, improving patient outcomes.  

---


