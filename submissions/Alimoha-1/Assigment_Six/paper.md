# Research Classification

## 1. Introduction to Classification
Classification is a supervised machine learning task where the goal is to predict a categorical label or class for new data points. The model learns from a dataset containing both input features and their corresponding class labels, identifying patterns and relationships that allow it to categorize unseen data.  

**Examples:**  
- Sorting emails into *"spam"* or *"not spam"*  
- Determining if a customer will *"churn"* or *"stay"*  
- Identifying a disease as *"present"* or *"absent"*  

The key difference between **classification** and **regression** lies in the nature of the output:  
- **Classification** predicts *discrete categories*.  
- **Regression** predicts *continuous values*.  

**Real-life examples:**  
- Classification: Predicting whether a loan application will be *approved* or *rejected*.  
- Regression: Predicting the future *temperature* in a city.  

---

## 2A. Classification Algorithms

### Logistic Regression
- **How it works:** Uses the logistic (sigmoid) function to model probabilities between 0 and 1. A threshold (e.g., 0.5) determines the predicted class. For multi-class problems, extensions like one-vs-rest are used.  
- **Use case:** Predicting customer purchase behavior (e.g., will a customer click an ad?).  
- **Advantages:** Efficient, interpretable, provides probability scores, good baseline.  
- **Limitations:** Assumes linear relationship, sensitive to outliers and multicollinearity.  

---

### Decision Trees
- **How it works:** Builds a tree where nodes test features, branches represent outcomes, and leaves give class labels. Splits are chosen to maximize information gain or minimize impurity (e.g., Gini, entropy).  
- **Use case:** Medical diagnosis (classifying flu vs. cold using symptoms).  
- **Advantages:** Easy to interpret, handles numerical & categorical data, minimal preprocessing.  
- **Limitations:** Prone to overfitting, unstable (small data changes → different tree).  

---

### Random Forest
- **How it works:** An ensemble of many decision trees. Each tree votes, and the majority class is chosen. Reduces overfitting of single trees.  
- **Use case:** Fraud detection (analyzing transaction features: amount, location, time).  
- **Advantages:** High accuracy, robust, can handle many features, shows feature importance.  
- **Limitations:** Less interpretable, slower training, computationally expensive.  

---

## 2B. Extended Task – K-Nearest Neighbors (KNN)
- **How it works:** Classifies new points based on the majority class of their *K nearest neighbors* (distance often measured by Euclidean distance).  
- **Application:** Recommendation systems (e.g., suggesting movies based on similar users).  
- **Strengths:** No linear assumptions, flexible.  
- **Weaknesses:** Slow predictions on large datasets, depends on *K* and distance metric.  

---

## 3. Classification Metrics

- **Accuracy:** Correct predictions ÷ Total predictions.  
- **Precision:** True Positives ÷ (True Positives + False Positives). Focus: *quality of positive predictions*.  
- **Recall:** True Positives ÷ (True Positives + False Negatives). Focus: *finding all positives*.  
- **F1-Score:** Harmonic mean of Precision & Recall. Useful for imbalanced data.  
- **Confusion Matrix:** Table of TP, TN, FP, FN counts.  

### Comparison Table

| Metric       | When to Use                           | Focus                               | Weaknesses                         |
|--------------|---------------------------------------|-------------------------------------|-------------------------------------|
| Accuracy     | Balanced datasets                     | Overall correctness                 | Misleading on imbalanced data       |
| Precision    | High cost of false positives          | Purity of positive predictions      | Ignores false negatives             |
| Recall       | High cost of false negatives          | Completeness of positive predictions| Ignores false positives             |
| F1-Score     | Need balance between precision/recall | Balance of purity & completeness    | Less intuitive than single metrics  |

---

## 4. Imbalanced Data Problem
- **Definition:** One class has far more examples than another (e.g., fraud detection: 99% legitimate vs. 1% fraud).  
- **Problem:** Accuracy can be misleading. A model predicting only the majority class may achieve 99% accuracy but detect 0% fraud.  
- **Better metrics:** Precision, Recall, and F1-Score—because they evaluate the minority (important) class more effectively.  

---



## 5. Real-World Case Study: Breast Cancer Diagnosis

- **Goal:** The main goal was to accurately classify whether a tumor is *benign* (non-cancerous) or *malignant* (cancerous) based on patient medical data. Early and correct diagnosis is critical for improving treatment outcomes.  

- **Data:** The dataset widely used in research is the **Wisconsin Breast Cancer Dataset (WBCD)**, which contains features extracted from digitized images of fine-needle aspirates of breast masses. These features include cell size, texture, smoothness, and nucleus characteristics.  

- **Model:** Various classification models have been applied, including Logistic Regression, Support Vector Machines (SVM), Random Forest, and Neural Networks. Many studies found that ensemble methods and SVM often achieve very high accuracy in distinguishing between benign and malignant tumors.  

- **Results:**  
  - High classification accuracy (often >95%) achieved with modern algorithms.  
  - SVM and ensemble methods reduced false negatives, which is critical in medical diagnosis.  
  - The study highlights that classification models can significantly assist doctors in decision-making, but they should complement—not replace—medical expertise.  


---
