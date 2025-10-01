# Machine Learning: Classification vs Regression

---

## 1. What is Classification in Machine Learning?

**Classification** is a type of **supervised learning** where the goal is to predict a **categorical label (class)** for a given input.

- **Input:** Features (numbers, text, images, etc.)  
- **Output:** Discrete categories (e.g., "spam" or "not spam", "cat" or "dog")  

**Example:**  
Email filtering—predicting if an email is `"Spam"` or `"Not Spam"`.

---

## 2. How is it different from Regression?

| Aspect             | Classification                           | Regression                               |
|-------------------|-----------------------------------------|-----------------------------------------|
| **Output**        | Categorical (discrete)                  | Continuous (numeric)                     |
| **Goal**          | Assign a class/label                     | Predict a number/value                   |
| **Examples of Output** | "Yes"/"No", "Cat"/"Dog", "High"/"Low" | 72°F, $350,000, 3.5 (GPA)               |
| **Algorithms**    | Logistic Regression, Decision Trees, SVM, Random Forest | Linear Regression, Polynomial Regression, SVR |

✅ **Key difference:** Classification predicts **categories**, Regression predicts **quantities**.

---

## 3. Real-life Examples

- **Classification:**  
  Predicting whether a patient has a disease: `"Yes"` or `"No"`.

- **Regression:**  
  Predicting house prices based on size, location, and features: `$250,000`.
# Machine Learning: Classification vs Regression

---

## 1. What is Classification in Machine Learning?

**Classification** is a type of **supervised learning** where the goal is to predict a **categorical label (class)** for a given input.

- **Input:** Features (numbers, text, images, etc.)  
- **Output:** Discrete categories (e.g., "spam" or "not spam", "cat" or "dog")  

**Example:**  
Email filtering—predicting if an email is `"Spam"` or `"Not Spam"`.

---

## 2. How is it different from Regression?

| Aspect             | Classification                           | Regression                               |
|-------------------|-----------------------------------------|-----------------------------------------|
| **Output**        | Categorical (discrete)                  | Continuous (numeric)                     |
| **Goal**          | Assign a class/label                     | Predict a number/value                   |
| **Examples of Output** | "Yes"/"No", "Cat"/"Dog", "High"/"Low" | 72°F, $350,000, 3.5 (GPA)               |
| **Algorithms**    | Logistic Regression, Decision Trees, SVM, Random Forest | Linear Regression, Polynomial Regression, SVR |

✅ **Key difference:** Classification predicts **categories**, Regression predicts **quantities**.

---

## 3. Real-life Examples

- **Classification:**  
  Predicting whether a patient has a disease: `"Yes"` or `"No"`.

- **Regression:**  
  Predicting house prices based on size, location, and features: `$250,000`.



# Classification Algorithms

---

## 1. Logistic Regression

**How it works (basic idea):**  
Logistic Regression is a supervised learning algorithm used for **binary classification**. It predicts the probability that an input belongs to a particular class using the **logistic (sigmoid) function**, which maps any real-valued number to a value between 0 and 1. A threshold (commonly 0.5) is used to assign the final class label.

**Real-world use case:**  
Predicting whether an email is `"Spam"` or `"Not Spam"`.

**Advantages:**  
- Simple, fast, and easy to implement  
- Interpretable (feature coefficients show effect on output)  
- Works well when the relationship between features and the log-odds is linear  

**Limitations:**  
- Not suitable for complex or non-linear relationships  
- Sensitive to highly correlated features  
- Cannot handle multi-class classification without extensions (e.g., one-vs-rest)  

---

## 2. Decision Trees

**How it works (basic idea):**  
Decision Trees split the dataset based on feature values, creating a **tree structure**. Each internal node represents a decision based on a feature, each branch represents an outcome of the decision, and each leaf node assigns a class label. Splits are chosen to **maximize information gain** or **minimize Gini impurity**.

**Real-world use case:**  
Predicting whether a patient has a disease based on symptoms like fever, cough, or age.

**Advantages:**  
- Easy to understand and visualize  
- Handles both numerical and categorical data  
- No need for feature scaling  

**Limitations:**  
- Prone to **overfitting** if the tree is too deep  
- Can be unstable—small changes in data may produce different trees  
- Less accurate alone compared to ensemble methods  

---

## 3. Random Forest

**How it works (basic idea):**  
Random Forest is an **ensemble learning method** that builds **many decision trees** on random subsets of data and features. Each tree predicts a class, and the final prediction is based on **majority voting**. This reduces overfitting and improves accuracy compared to a single tree.

**Real-world use case:**  
Predicting whether a bank transaction is `"Fraudulent"` or `"Not Fraudulent"`.

**Advantages:**  
- Reduces overfitting compared to a single decision tree  
- More accurate and robust  
- Handles large datasets and many features well  

**Limitations:**  
- Less interpretable than a single decision tree  
- Slower to train and predict due to multiple trees  
- Requires more memory and computational resources  
# 2B. Extended Task – K-Nearest Neighbors (KNN)

**What problem is this algorithm good at solving?**  
K-Nearest Neighbors (KNN) is a **supervised learning algorithm** used for **classification** (and regression). It is particularly good at problems where the relationship between features and labels is **non-linear** and where similar data points tend to belong to the same class.

**How does it work (the core idea)?**  
- KNN stores all the training data and makes predictions for new data points based on **similarity to the 'k' nearest neighbors** (usually measured by distance metrics like Euclidean distance).  
- The predicted class is determined by **majority voting** among the k nearest neighbors.

**Real-world application:**  
- **Recommender systems:** Suggesting products or movies to users based on preferences of similar users.  
- **Other examples:** Handwriting recognition, image classification.

**Strengths:**  
- Simple to understand and implement  
- Non-parametric; can model complex, non-linear decision boundaries  
- No training phase required (lazy learning)

**Weaknesses (compared to Logistic Regression, Decision Trees, Random Forest):**  
- Slower to predict for large datasets since it compares a new point to all training data  
- Sensitive to irrelevant or noisy features  
- Requires careful choice of **k** and distance metric  
- Less interpretable than Decision Trees or Logistic Regression
# Classification Metrics

---

## 1. Accuracy
**Definition:** The proportion of correctly predicted instances (both positive and negative) out of all predictions.  
**Formula:**  
`Accuracy = (TP + TN) / (TP + TN + FP + FN)`  
**What it measures:** Overall correctness of the model.  
**Note:** Can be misleading for **imbalanced datasets**.

---

## 2. Precision
**Definition:** The proportion of correctly predicted positive instances out of all instances predicted as positive.  
**Formula:**  
`Precision = TP / (TP + FP)`  
**What it measures:** How many of the predicted positives are actually correct.  
**Use case:** Important when **false positives are costly** (e.g., spam detection, medical tests).

---

## 3. Recall (Sensitivity / True Positive Rate)
**Definition:** The proportion of correctly predicted positive instances out of all actual positives.  
**Formula:**  
`Recall = TP / (TP + FN)`  
**What it measures:** How well the model captures all actual positives.  
**Use case:** Important when **missing a positive is costly** (e.g., disease detection).

---

## 4. F1-Score
**Definition:** The **harmonic mean** of precision and recall.  
**Formula:**  
`F1-Score = 2 * (Precision * Recall) / (Precision + Recall)`  
**What it measures:** A balance between precision and recall.  
**Use case:** Useful for **imbalanced datasets** or when both false positives and false negatives matter.

---

## 5. Confusion Matrix
**Definition:** A table showing **True Positives (TP), True Negatives (TN), False Positives (FP), and False Negatives (FN)**.  
**Purpose:** Provides a complete overview of model performance.  

**Example Table:**

|                 | Predicted Positive | Predicted Negative |
|-----------------|-----------------|-----------------|
| Actual Positive | TP              | FN              |
| Actual Negative | FP              | TN              |

---

## Comparison Table

| Metric       | Focus                             | When to Use                                   | Weakness                                         |
|-------------|----------------------------------|----------------------------------------------|-------------------------------------------------|
| Accuracy     | Overall correctness               | Balanced datasets                             | Misleading for imbalanced datasets             |
| Precision    | Correctness of predicted positives| When **false positives** are costly          | Ignores false negatives                         |
| Recall      | Capturing all actual positives     | When **false negatives** are costly          | Ignores false positives                         |
| F1-Score    | Balance of precision and recall   | Imbalanced datasets, both FP & FN matter     | Harder to interpret than simple accuracy       |
| Confusion Matrix | Complete performance overview | Anytime you want detailed error analysis     | Can be harder to summarize in one number       |

# Imbalanced Data Problem

## 1. What is imbalanced data?
- In classification tasks, **imbalanced data** occurs when the classes are **not equally represented**.  
- **One class (majority)** has many examples, while **the other class (minority)** has few examples.  
- **Example:**  
  - Dataset of 1000 patients:  
    - Healthy = 990  
    - Sick = 10 → minority class  

---

## 2. Why is accuracy misleading?
- Accuracy measures the **overall proportion of correct predictions**:

\[
\text{Accuracy} = \frac{\text{Correct Predictions}}{\text{Total Predictions}}
\]

- In imbalanced datasets:  
  - A model predicting **all patients as healthy** gets 990/1000 = 99% accuracy ✅  
  - But it **misses all sick patients** ❌ → very dangerous in practice  
- **Key point:** Accuracy favors the majority class and ignores the minority class.  

---

## 3. More reliable metrics
For imbalanced datasets, metrics that focus on the **minority class** are more useful:

| Metric      | What it measures                       | Why useful in imbalanced data                           |
|------------|---------------------------------------|--------------------------------------------------------|
| **Recall**  | How many actual positives were detected | Shows if the model finds the minority class (e.g., sick patients) |
| **Precision** | How many predicted positives are correct | Reduces false positives when predicting minority class |
| **F1-Score** | Balance of precision and recall       | Combines both to give a better picture of model performance |

---

## ✅ Key takeaway
- **Imbalanced data** is common in medicine, fraud detection, etc.  
- **Accuracy alone is misleading**.  
- **Recall, precision, and F1-score** are more reliable because they **focus on detecting the minority class**, which is often the most important.



# Customer Churn Prediction Study – Libyan ISP

## Goal of the Study
- Build a predictive model to forecast **customer churn** for an Internet Service Provider (ISP) in Libya.
- Enable the business to **proactively retain customers** at high risk of leaving, improving profitability.

## Dataset
- **Source:** Libyan ISP company in Benghazi  
- **Period:** January 20, 2022 – March 2, 2023  
- **Size:** 3,606 instances after preprocessing  
- **Attributes:** 11 features related to customer behavior and account information  
- **Imbalance:** Only 5% of customers had churned, making it a **highly imbalanced dataset**

## Classification Models Used
- Logistic Regression (LR)  
- Decision Tree (DT)  
- Random Forest (RF)  
- Gradient Boosting Machine (GBM)  
- Extreme Gradient Boosting (XGBoost)  

**Data Split:** 80% training, 20% testing  
**Imbalance Handling:** Applied oversampling techniques: **SMOTE** and **SMOTEENN** to the training set

## Key Results
1. Models trained on the **original imbalanced dataset** performed poorly at predicting churn customers.  
2. After applying **oversampling techniques**, model performance in predicting churn improved significantly.  
3. **Best-performing models:** XGBoost and GBM, achieving an **AUC of 94%** after re-sampling  

**Insight:**  
- Handling **imbalanced data** is critical in churn prediction. Without re-sampling, models tend to predict the majority class (non-churn) and fail to detect churners effectively.
