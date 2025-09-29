# 📘 Lesson 6 — Classification

## 1. Introduction to Classification

**Classification** is a supervised learning task in Machine Learning where the goal is to assign inputs into **categories (classes)**.

- **How it differs from regression:**  
  - Classification predicts **labels** (e.g., spam / not spam).  
  - Regression predicts **numbers** (e.g., house price = $350,000).  

**Examples:**  
- **Classification:** Detecting if an email is **spam or not spam**.  
- **Regression:** Predicting the **sale price** of a car based on mileage and age.  

---

## 2. Classification Algorithms

### 🔹 Logistic Regression
- **How it works:** Calculates a weighted sum of features and applies a **sigmoid function** to produce a probability between 0 and 1. If probability > threshold, predict class 1 (spam), otherwise class 0 (not spam).  
- **Real-world use case:** **Spam filtering** (word frequency → spam probability).  
- **Advantages:** Simple, interpretable, outputs probabilities.  
- **Limitations:** Only models **linear relationships** between features and outcome.  

### 🔹 Decision Trees
- **How it works:** Splits data into branches using feature thresholds (e.g., *Does the email contain the word “lottery”?*). Each branch ends in a prediction (spam/not spam).  
- **Real-world use case:** **Medical diagnosis** (symptoms → disease or no disease).  
- **Advantages:** Easy to visualize and explain. Handles both numeric and categorical data.  
- **Limitations:** Can **overfit** easily; small changes in data may change the tree.  

### 🔹 Random Forest
- **How it works:** Builds many decision trees on random subsets of the data and features, then combines them (majority vote).  
- **Real-world use case:** **Credit card fraud detection**.  
- **Advantages:** Higher accuracy, robust to overfitting, shows feature importance.  
- **Limitations:** Less interpretable; slower than a single decision tree.  

---

## 2. Extended Algorithm — Support Vector Machine (SVM)

- **Problem it solves:** Separates classes with a **maximum-margin boundary** (hyperplane).  
- **How it works:** Finds the line or surface that best separates spam from not spam. With **kernels**, it can handle non-linear boundaries.  
- **Real-world application:** **Handwritten digit recognition** (classify digits 0–9).  
- **Strengths:** High accuracy, works well with high-dimensional data (e.g., text).  
- **Weaknesses:** Training can be slow on large datasets; less interpretable than logistic regression.  

---

## 3. Classification Metrics (with Spam Example)

- **Accuracy:** Overall correctness.  
  - Formula: (TP+TN)/(TP+FP+FN+TN)  
  - *Spam example:* If 95 out of 100 emails are correctly classified, Accuracy = 95%.  

- **Precision:** “Of all emails predicted as spam, how many were truly spam?”  
  - Formula: TP / (TP+FP)  
  - *Spam example:* If 100 emails are marked spam, but 20 are actually good, Precision = 80%.  

- **Recall (Sensitivity):** “Of all actual spam emails, how many did the filter catch?”  
  - Formula: TP / (TP+FN)  
  - *Spam example:* If there are 100 spam emails and the filter caught 90, Recall = 90%.  

- **F1-Score:** Balance of Precision and Recall (harmonic mean). Useful for imbalanced data.  

- **Confusion Matrix:** Shows the breakdown:  
  - **TP:** Spam correctly marked spam  
  - **FP:** Good email wrongly marked spam  
  - **FN:** Spam email missed as “not spam”  
  - **TN:** Good email correctly passed through  

### 📊 Comparison Table

| Metric     | Focus |         When to Use | Weakness |
|--------|------|-------------|----------|
| Accuracy | Overall correctness | Balanced datasets | Misleading on imbalanced data |
| Precision | Quality of positive predictions | When **false positives** are costly (don’t block real emails) | Ignores missed spam |
| Recall | Coverage of positives | When **false negatives** are costly (don’t miss spam) | Ignores false alarms |
| F1-Score | Balance of Precision & Recall | Imbalanced datasets | Harder to interpret |
| Confusion Matrix | Error breakdown | To see which type of errors dominate | Not a single score |

---

## 4. Imbalanced Data Problem

- **What it means:** When one class is much rarer. Example: 99% normal emails, 1% spam.  
- **Why accuracy misleads:** A model that predicts **“not spam” for every email** will be 99% accurate but will **miss all spam**.  
- **Better metrics:** Precision, Recall, F1-Score, and PR-AUC are more reliable because they focus on performance for the **minority class (spam)**.  

---

## 5. Real-World Case Study — Spam Detection

- **Goal:** Build an email filter that automatically classifies emails as **spam** or **not spam**.  
- **Data:** Millions of labeled emails with features like sender address, keywords, frequency of suspicious terms, and metadata.  
- **Model applied:** Logistic Regression, Decision Trees, and later Random Forest and Deep Learning models.  
- **Key results:**  
  - Logistic Regression provided a strong **baseline**.  
  - Random Forest improved accuracy and reduced false negatives (higher Recall).  
  - Deep learning (RNNs on email text) gave the best balance of Precision and Recall.  
- **Insights:** High Recall was important so users don’t receive spam, but Precision also mattered to avoid losing important business emails. The best model balanced both using the **F1-score**.  

---

# ✅ Summary
- **Classification predicts categories** (spam/not spam), unlike regression which predicts numbers.  
- **Algorithms:** Logistic Regression, Decision Trees, Random Forest, plus SVM as an extension.  
- **Metrics:** Accuracy, Precision, Recall, F1, and Confusion Matrix each show different aspects of performance.  
- **Imbalanced data:** Accuracy is misleading; better to use Precision/Recall/F1.  
- **Case study:** Spam detection demonstrates how models are applied and why Recall & Precision trade-offs matter.  
