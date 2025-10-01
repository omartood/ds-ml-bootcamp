# 1. Introduction to Classification

## What is Classification in Machine Learning?
- **Classification** is a type of supervised learning where the goal is to **predict the category or class** of a given input based on its features.  
- The output is **discrete**, meaning it belongs to a set of predefined labels (e.g., Yes/No, Spam/Not Spam, Disease/No Disease).

---

## How is it Different from Regression?
| Aspect            | Classification                     | Regression                          |
|------------------|-----------------------------------|------------------------------------|
| Output Type       | Discrete (categories/classes)      | Continuous (numeric values)        |
| Goal              | Predict a **class/label**          | Predict a **quantity/value**       |
| Examples          | Credit card fraud detection, Disease diagnosis | Stock price prediction, Temperature forecast |

---

## Real-Life Examples
- **Classification:** Predict whether a bank transaction is **fraudulent** or **legitimate** based on transaction amount, location, and time.  
- **Regression:** Predict the **monthly electricity bill** for a household based on usage, number of appliances, and household size.


# 🔹 Classification Algorithms 

## 1. Logistic Regression  

**How it works (basic idea):**  
- Creates a **linear equation** with input features.  
- Applies the **sigmoid function** to map results into probabilities (0–1).  
- Predicts a class using a cutoff (e.g., ≥0.5 = Class 1, <0.5 = Class 0).  

**Real-world example:**  
**Hospital predicting heart disease**  
- Features: Age, cholesterol, blood pressure, exercise habits.  
- Logistic regression calculates a probability (e.g., 0.78).  
- If >0.5 → “Patient likely has heart disease,” else “No disease.”  

**Advantages:**  
- Simple and interpretable.  
- Provides probability of outcome.  

**Limitations:**  
- Performs poorly with **non-linear relationships**.  
- Sensitive to **outliers**.  

---

## 2. Decision Trees  

**How it works (basic idea):**  
- Splits the data using **yes/no questions** about features.  
- Each step separates data into groups with mostly one label.  
- Ends with a **leaf node** predicting the class.  

**Real-world example:**  
**Retail store predicting if a customer will buy a product**  
- Split 1: “Is income > $40,000?”  
- Split 2: “Is age between 25–40?”  
- Outcome: “Will buy” or “Won’t buy.”  

**Advantages:**  
- Easy to visualize and explain.  
- Works with both numerical and categorical data.  

**Limitations:**  
- Can **overfit** easily.  
- Sensitive to small changes in data.  

---

## 3. Random Forest  

**How it works (basic idea):**  
- Builds **many decision trees** using random subsets of data and features.  
- Each tree gives a prediction.  
- Final decision = **majority vote** (classification) or average (regression).  

**Real-world example:**  
**Bank detecting fraudulent transactions**  
- Features: Transaction amount, location, time, customer history.  
- Trees vote: “Fraud” or “Not Fraud.”  
- Majority vote → Bank flags transaction.  

**Advantages:**  
- High accuracy.  
- Reduces overfitting compared to a single tree.  
- Works well with complex data.  

**Limitations:**  
- Slower than a single tree.  
- Harder to interpret (“black box”).  

---

## Summary Table: Core Algorithms

| Algorithm           | How it Works                        | Real-World Example                     | Advantages                         | Limitations                    |
|---------------------|------------------------------------|---------------------------------------|-----------------------------------|--------------------------------|
| Logistic Regression | Linear equation + Sigmoid → Class   | Predicting heart disease               | Simple, interpretable, probabilistic | Struggles with non-linear data |
| Decision Tree       | Splits data using yes/no questions  | Retail: Will a customer buy a product?| Easy to interpret, no scaling needed | Overfitting, unstable          |
| Random Forest       | Many trees + majority voting        | Bank: Fraud detection                  | High accuracy, reduces overfitting | Slower, harder to interpret    |

---

# Extended Task – Additional Algorithms

## 1. Naive Bayes  

**Problem it solves:**  
- Text classification, spam detection, sentiment analysis.  
- Works well for **large, high-dimensional datasets**.  

**How it works:**  
- Uses **Bayes’ Theorem** to calculate probability of a class.  
- Assumes **feature independence** (“naive”).  
- Predicts class with **highest probability**.  

**Real-world application:**  
- **Email spam detection** – classifies emails as spam or not spam.  

**Strengths:**  
- Fast, simple, handles large datasets.  
- Requires less training data.  

**Weaknesses:**  
- Assumes feature independence, rarely true in reality.  
- Less flexible than Decision Trees or Random Forest for complex patterns.  

---

## 2. K-Nearest Neighbors (KNN)  

**Problem it solves:**  
- Works well for classification with **non-linear decision boundaries**.  
- Suitable when **similar points have similar labels**.  

**How it works:**  
- Stores all training data.  
- Classifies new points based on **k nearest neighbors** (e.g., Euclidean distance).  
- Assigns the most common class among neighbors.  

**Real-world application:**  
- **Handwriting recognition** – predicts digits by comparing to similar digits in the dataset.  

**Strengths:**  
- Simple and intuitive.  
- Non-parametric; no assumption about data distribution.  
- Handles multi-class problems easily.  

**Weaknesses:**  
- Slow for large datasets.  
- Sensitive to irrelevant features and feature scaling.  
- Performance drops if data is noisy.  

---

## Comparison Table: All 5 Algorithms

| Algorithm       | Strengths                                    | Weaknesses                                           |
|-----------------|---------------------------------------------|-----------------------------------------------------|
| Naive Bayes     | Fast, simple, works with high-dimensional data | Assumes feature independence, less accurate on complex patterns |
| KNN             | Non-parametric, flexible with non-linear boundaries | Slow on large datasets, sensitive to noise & scaling |
| Logistic Regression | Provides probabilities, interpretable       | Struggles with non-linear data                     |
| Decision Tree   | Easy to interpret, handles numeric & categorical data | Can overfit, sensitive to small changes           |
| Random Forest   | High accuracy, reduces overfitting           | Harder to interpret, slower than a single tree    |

---

# 🔹 Classification Metrics

## 1. Accuracy  
Measures **overall correctness** of predictions:  
Accuracy = (TP + TN) / (TP + TN + FP + FN)  
- Best for **balanced datasets**.  

## 2. Precision  
Measures **correctness of positive predictions**:  
Precision = TP / (TP + FP)  
- Important when **false positives are costly**.  

## 3. Recall (Sensitivity)  
Measures **ability to detect actual positives**:  
Recall = TP / (TP + FN)  
- Important when **false negatives are costly**.  

## 4. F1-Score  
Harmonic mean of Precision and Recall:  
F1 = 2 × (Precision × Recall) / (Precision + Recall)  
- Best when **classes are imbalanced**.  

## 5. Confusion Matrix  

|                     | Predicted Positive | Predicted Negative |
|---------------------|-----------------|-----------------|
| Actual Positive     | TP              | FN              |
| Actual Negative     | FP              | TN              |

---

## Metrics Comparison Table

| Metric          | Focus                              | Best Use Case                                   | Weakness                           |
|-----------------|-----------------------------------|------------------------------------------------|-----------------------------------|
| Accuracy        | Overall correctness               | Balanced datasets                               | Misleading on imbalanced data     |
| Precision       | Correctness of predicted positives | False positives are costly (spam, alerts)      | Ignores false negatives           |
| Recall          | Detecting all positives           | False negatives are costly (disease, fraud)   | Ignores false positives           |
| F1-Score        | Balance between Precision & Recall | Imbalanced datasets                             | Harder to interpret               |
| Confusion Matrix| Full breakdown                     | Understanding all model errors                  | No single performance number      |

---

# Imbalanced Data Problem

**What it means:**  
- Classes are **unequally represented**.  
- Example: Fraud detection – 2% fraud, 98% legitimate.  

**Why accuracy is misleading:**  
- A model predicting all as majority class can achieve **high accuracy** but fail to detect the minority class.  

**Better metrics for imbalanced data:**  
- **Precision, Recall, F1-Score, Confusion Matrix** – focus on **minority class detection**.  

**Metrics Table for Imbalanced Data**

| Metric          | Usefulness                                    |
|-----------------|----------------------------------------------|
| Precision       | Correctness of predicted positives           |
| Recall          | Detect all actual positives                  |
| F1-Score        | Balances Precision & Recall                  |
| Confusion Matrix| Detailed view of TP, FP, TN, FN              |

---

# Case Study: Real-World Classification Projects

## 1. Spam Detection  
**Goal:** Classify emails as spam or not.  
**Data:** Enron Email Dataset – emails labeled spam/ham.  
**Model:** Naive Bayes classifier.  
**Key Insights:** ~95% accuracy, strong precision, reduced false positives.  

## 2. Fraud Detection  
**Goal:** Detect fraudulent credit card transactions.  
**Data:** Transaction amount, time, location, merchant, customer history.  
**Model:** Random Forest classifier.  
**Key Insights:** High recall for fraud detection, F1-score important due to imbalance, enabled real-time fraud alerts.  

**Summary Table**

| Case Study       | Goal                                  | Data Features                          | Model Used      | Key Metric / Insight                       |
|-----------------|---------------------------------------|---------------------------------------|----------------|-------------------------------------------|
| Spam Detection  | Classify emails as spam or not spam   | Email subject, body, sender, keywords | Naive Bayes    | High accuracy (~95%), strong precision    |
| Fraud Detection | Detect fraudulent transactions        | Amount, time, location, merchant      | Random Forest  | High recall, F1-score important           |
