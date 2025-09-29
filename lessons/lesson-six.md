# 📘 Lesson 6 – Classification

✅ In **Lesson 4**, we explored **Regression** — predicting continuous values such as house prices.
✅ We saw how models like **Linear Regression** and **Polynomial Regression** work, and how to measure their performance with metrics like MAE, RMSE, and R².
✅ In **Lesson 5**, we built a **House Price Prediction project** — regression in action — where we used **Linear Regression** and **Random Forest** to make real predictions.

👉 **Now in Lesson 6, we focus on Classification — another core supervised learning method.**

---

## 🎯 Learning Objectives

By the end of this lesson, students will be able to:

* Understand what **Classification** is and how it differs from Regression.
* Learn about common **Classification algorithms**:

  * Logistic Regression
  * Decision Trees
  * Random Forest
* Understand how to **evaluate classification models** using metrics:

  * Accuracy
  * Precision
  * Recall
  * F1-Score
  * Confusion Matrix

---

## 1) Introduction

Classification is one of the most widely used areas in Machine Learning.
👉 Instead of predicting a number (like house price), we predict a **category** (spam vs not spam, churn vs not churn, healthy vs sick).

---

## 2) What is Classification?

**Definition:**

* **Classification** is a type of supervised learning where the target variable is **categorical** (e.g., Yes/No, Male/Female, Pass/Fail).
* The model learns from labeled data and predicts which class a new observation belongs to.

---

### Real-World Examples

* 📧 **Spam Detection**: Predict whether an email is spam or not.
* 📱 **Customer Churn**: Predict whether a customer will leave a service or stay.
* 🐶 **Image Recognition**: Predict if a picture is of a cat, dog, or another animal.

---

### Contrast with Regression

* **Regression:** Predicts **continuous values** (e.g., house price = \$350,000).
* **Classification:** Predicts **categories** (e.g., spam vs not spam).

📌 **Key Point:**
Regression = predicting **how much**.
Classification = predicting **which class**.

---

## 3) Classification Algorithms

### a) Logistic Regression

* Despite the name, it’s used for **classification**, not regression.
* Uses the **sigmoid function** to map predictions to probabilities (0–1).
* Example: Predicting whether a student passes an exam (Yes/No).

---

### b) Decision Trees

* Models decisions as a **tree structure** (if/else rules).
* Easy to interpret, but can **overfit** if not pruned.
* Example: Predict whether a loan is approved based on income, credit score, and history.

---

### c) Random Forest

* An **ensemble of many decision trees** working together.
* More accurate and robust than a single tree.
* Example: Predicting customer churn more reliably than a single tree.

📌 **Important Note:**
Classification algorithms are **not limited** to just Logistic Regression, Decision Trees, and Random Forest.
There are many more (like **Naive Bayes, KNN, Support Vector Machines, Neural Networks**).
👉 But the key takeaway is to **understand how classification works in general** — once you know that, you can research and choose the algorithm that fits your problem best.

---

## 4) Classification Metrics

When we build a classification model, we need to evaluate how good it is. ---

---

### 🎯 1) Accuracy

> Of **all predictions made**, how many were **correct** (both positives and negatives)?

* 📌 Focuses on the **overall correctness** of the model.

* 💡 Use when **classes are balanced** (almost equal positives and negatives).
  ⚠️ Not reliable when data is **imbalanced** (e.g. 95% healthy, 5% sick).

**Example**

* Model predicted 100 emails:

  * 90 predictions are correct (either spam correctly or not spam correctly)
* **Accuracy = 90 / 100 = 0.9 (90%)**

---

### 🎯 2) Precision

> Of all the cases the model **predicted as positive**, how many were **actually positive**?

* 📌 Focuses on **quality of positive predictions**.

* 💡 Use when **false positives are dangerous**, e.g.

  * Saying a healthy person has cancer
  * Accusing an innocent email of being spam

**Example**

* Model predicted 10 emails as spam → 7 are really spam
* **Precision = 7 / 10 = 0.7 (70%)**

---

### 🎯 3) Recall (Sensitivity)

> Of all the **actual positive cases**, how many did the model **successfully detect**?

* 📌 Focuses on **catching all positives**.

* 💡 Use when **false negatives are dangerous**, e.g.

  * Missing a real cancer patient
  * Letting real spam into the inbox

**Example**

* There are 10 real spam emails → model caught 7
* **Recall = 7 / 10 = 0.7 (70%)**

---

### ⚖️ 4) F1-Score

> A **balanced measure** of Precision and Recall.

* 📌 Useful when classes are **imbalanced**.

* 💡 High F1 means the model is **both accurate and thorough** at finding positives.

**Example**

* Precision = 0.7, Recall = 0.7
* **F1 = 0.7**
* If one is very low, F1 will also be low.

---

### 📋 5) Confusion Matrix

> A table that shows **the complete picture** of predictions

|                     | **Predicted Positive** | **Predicted Negative** |
| ------------------- | ---------------------- | ---------------------- |
| **Actual Positive** | True Positive (TP) ✅   | False Negative (FN) ❌  |
| **Actual Negative** | False Positive (FP) ❌  | True Negative (TN) ✅   |

* Shows **exactly what errors** the model makes
* Lets you calculate **all other metrics** from it

---

### 🧠 Quick Summary Table

| Metric           | Question it answers                                     | Focus                    |
| ---------------- | ------------------------------------------------------- | ------------------------ |
| Accuracy         | How many predictions are correct overall?               | Overall correctness      |
| Precision        | Of predicted positives, how many are actually positive? | Avoiding false positives |
| Recall           | Of actual positives, how many are caught?               | Avoiding false negatives |
| F1-Score         | How well balance precision & recall?                    | Balanced performance     |
| Confusion Matrix | What are the counts of TP, FP, FN, TN?                  | Complete error breakdown |

---

## ✅ Lesson Summary

* **Classification** is a supervised ML task where the goal is to predict **categories**.
* Common algorithms: **Logistic Regression, Decision Trees, Random Forest**.
* But remember: there are **many more algorithms** (KNN, Naive Bayes, SVM, Neural Networks) — the most important skill is knowing **how classification works** and learning how to select the best algorithm for your problem.
* Evaluation metrics: **Accuracy, Precision, Recall, F1-Score, Confusion Matrix**.
* Key difference:

  * Regression → predicts **numbers**.
  * Classification → predicts **classes**.

---

## 🔚 End of Lesson 6

🎉 Congratulations! You’ve completed **Classification – your second core supervised learning method in Machine Learning.**

---
