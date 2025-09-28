# 1. Introduction to Classification

## What is Classification in Machine Learning?
Classification is a type of **supervised learning** where a computer learns to **assign a label or category** to an input based on its features.  
The computer studies **past data** where each example already has a correct label, finds patterns, and then can predict the label for **new, unseen data**.

Unlike regression, which predicts a **continuous value**, classification predicts **discrete outputs**, meaning the result belongs to a set of predefined categories.

For example, a company may want to decide if a **job applicant should be shortlisted or rejected** based on their resume details like education, experience, and skills. The output is **shortlisted** or **not shortlisted**, not a number.

---

## How is it Different from Regression?

| Aspect            | Classification                     | Regression                          |
|------------------|-----------------------------------|------------------------------------|
| Output Type       | Discrete categories (e.g., Yes/No) | Continuous numeric values          |
| Goal              | Predict a **class/label**          | Predict a **quantity/value**       |
| Examples          | Shortlisting job applicants, Online product recommendation | Delivery time prediction, Monthly electricity bill |

**Key point:** Regression tells us **how much** or **how many**, while classification tells us **which category** something belongs to.

---

## Real-Life Examples

- **Classification:** An online marketplace predicts if a **user will buy a recommended product** or not based on their browsing history and past purchases.  
- **Regression:** A logistics company predicts **how long a delivery will take** in hours based on distance, traffic, and delivery type.

**Explanation:** In the classification example, the output is **binary (buy / not buy)**. In regression, the output is **numerical (hours)**.

---

## Why Classification is Important

- Helps **make decisions automatically** in real-world problems.  
- Widely used in **healthcare, finance, e-commerce, and education**.  
- Allows organizations to **reduce errors, save time, and improve accuracy**.

---

# 2A. Classification Algorithms

## 1. Logistic Regression

**How it works (basic idea):**  
- Logistic regression predicts **two possible outcomes** (yes/no, success/failure) by creating a **linear combination of input features**.  
- Then it applies the **sigmoid function** to convert the result into a probability between 0 and 1.  
- A cutoff (usually 0.5) is used: if the probability is ≥0.5 → Class 1, otherwise → Class 0.

**Real-world example:**  
- A streaming service predicts whether a user will **watch a recommended movie** based on their past viewing habits and preferences.  
- The model calculates a probability (e.g., 0.72) that the user will watch it.  
- If ≥0.5 → predict “Will watch”; else → “Will not watch.”

**Advantages:**  
- Easy to understand and implement.  
- Outputs probabilities, useful for decision-making.

**Limitations:**  
- Assumes a **linear relationship** between features and the log-odds, so it struggles with complex patterns.  
- Sensitive to **outliers** and irrelevant features.

---

## 2. Decision Trees

**How it works (basic idea):**  
- Decision trees ask a series of **yes/no questions** about the input features.  
- Each split creates branches separating data into groups with similar labels.  
- Leaf nodes provide the final prediction for the class.

**Real-world example:**  
- A city council uses a decision tree to decide whether a **parking ticket should be issued**.  
  - Question 1: “Is the car parked in a no-parking zone?”  
  - Question 2: “Is the parking time over 2 hours?”  
  - Outcome: “Issue ticket” or “Do not issue ticket.”

**Advantages:**  
- Easy to interpret and visualize.  
- Handles both numeric and categorical data.

**Limitations:**  
- Can **overfit** training data if not pruned.  
- Small changes in input data can produce a very different tree.

---

## 3. Random Forest

**How it works (basic idea):**  
- Random forest creates **many decision trees** using random subsets of data and features.  
- Each tree gives a prediction, and the **majority vote** determines the final class.  
- This reduces the risk of overfitting compared to a single tree.

**Real-world example:**  
- A supermarket predicts which **items customers are likely to buy together** during a sale based on past transactions.  
- Each tree makes its prediction (“Buy together” or “Not together”), and the majority vote decides the final recommendation.

**Advantages:**  
- More accurate and robust than a single decision tree.  
- Works well with **complex and noisy data**.

**Limitations:**  
- Slower to train and predict.  
- Harder to interpret than a single tree (“black box” model).

---

## Summary Table: Core Algorithms

| Algorithm           | How it Works                        | Real-World Example                                | Advantages                         | Limitations                    |
|---------------------|------------------------------------|-------------------------------------------------|-----------------------------------|--------------------------------|
| Logistic Regression | Linear equation + Sigmoid → Class   | Streaming service: Predict movie choice        | Easy to understand, probability output | Struggles with non-linear patterns |
| Decision Tree       | Yes/No questions → branches → leaf | City parking ticket decisions                   | Easy to interpret, numeric & categorical data | Can overfit, sensitive to small changes |
| Random Forest       | Many trees + majority voting        | Supermarket: Items likely bought together      | High accuracy, reduces overfitting | Slower, harder to interpret    |

---


# 2B. Extended Task – Support Vector Machines (SVM)

**How it works (basic idea):**  
Support Vector Machines (SVM) are supervised learning algorithms that aim to find the **best decision boundary (hyperplane)** to separate classes. Instead of just any line, SVM chooses the one with the **largest margin** between the closest points of each class (called *support vectors*). This makes SVM highly effective for both linearly separable and non-linear problems (using kernels).  

**Problem it solves well:**  
SVM works especially well with **high-dimensional data** where the number of features is large compared to the number of samples, such as text classification and bioinformatics.  

**Real-world application:**  
In healthcare, SVMs have been used to classify **cancer cells as malignant or benign** using medical imaging data. For example, the Wisconsin Breast Cancer Dataset is a common benchmark where SVM achieved high accuracy in tumor classification (Cortes & Vapnik, 1995; Noble, 2006).  

**Strengths:**  
- Performs well in high-dimensional spaces.  
- Can model complex boundaries using kernel functions.  
- Robust against overfitting, especially with a good choice of regularization.  

**Weaknesses:**  
- Computationally expensive on very large datasets.  
- Model interpretability is limited compared to decision trees.  
- Requires careful parameter tuning (choice of kernel, regularization).  
 

---

# 3. Classification Metrics

When evaluating classification models, different metrics are used depending on the problem:  

- **Accuracy:** The proportion of correctly predicted labels over total predictions. Best when classes are balanced.  
- **Precision:** The percentage of predicted positives that are truly positive. Important when false positives are costly.  
- **Recall (Sensitivity):** The percentage of actual positives that are correctly identified. Important when missing positives is risky.  
- **F1-Score:** Harmonic mean of precision and recall, providing a balance between them.  
- **Confusion Matrix:** A 2x2 (or larger) table summarizing true positives, true negatives, false positives, and false negatives.  

### Comparison Table

| **Metric**               | **Definition**                                  | **Focus**                    | **Best When to Use**                                                                               | **Weakness**                              |
| ------------------------ | ----------------------------------------------- | ---------------------------- | -------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| **Accuracy**             | (TP+TN) / (Total predictions)                   | Overall correctness          | Datasets with balanced classes and equal misclassification cost                                    | Misleading in imbalanced datasets         |
| **Precision**            | TP / (TP+FP)                                    | Avoiding false positives     | Applications where false alarms are costly (e.g., spam detection, fraud alerts)                    | Ignores false negatives                   |
| **Recall (Sensitivity)** | TP / (TP+FN)                                    | Avoiding false negatives     | Critical scenarios where missing a positive is costly (e.g., medical diagnosis, safety monitoring) | Ignores false positives                   |
| **F1-Score**             | 2 × (Precision × Recall) / (Precision + Recall) | Balancing precision & recall | Imbalanced datasets where both false positives & false negatives matter                            | Less intuitive to interpret               |
| **Confusion Matrix**     | Table of TP, TN, FP, FN                         | Full error breakdown         | Any dataset (to analyze model behavior in detail)                                                  | Not a single metric, needs interpretation |

---

# 4. Imbalanced Data Problem

**What it means:**  
Imbalanced data occurs when one class dominates the dataset. For example, in **fraud detection**, 99% of transactions are legitimate while only 1% are fraudulent.  

**Why accuracy is misleading:**  
If a model predicts *every transaction as legitimate*, it will achieve **99% accuracy**, yet it completely fails at detecting fraud (0% recall for fraud class).  

**Better metrics:**  
- **Recall**: Ensures that fraudulent cases are detected.  
- **Precision**: Avoids overwhelming investigators with too many false alarms.  
- **F1-score**: Balances both, making it suitable for imbalanced datasets.  
- **Confusion Matrix**: Provides detailed insight into errors made.  

In fraud detection, **recall is especially critical**, since missing fraudulent cases is far more dangerous than flagging a few legitimate ones by mistake.  

---

# 5. Real-World Case Study – Spam Detection

**Goal of the project:**  
The project aimed to classify incoming emails into **spam** or **not spam** categories to protect users from phishing, scams, and irrelevant messages.  

**Data used:**  
A popular dataset used is the **Enron Email Dataset**, containing hundreds of thousands of emails labeled as spam or ham (legitimate). Features include word frequency, presence of suspicious keywords, sender information, and metadata.  

**Classification model applied:**  
Naive Bayes and Logistic Regression were widely applied due to their effectiveness in text classification. Naive Bayes, in particular, performs well because spam detection relies heavily on the frequency of certain words.  

**Key results/insights:**  
Studies show that Naive Bayes can achieve over **95% accuracy** on benchmark datasets (Metsis et al., 2006). The approach significantly reduced the amount of spam reaching users, while Logistic Regression provided probability-based predictions that allowed fine-tuning of spam filters.  

**References:**  
- Cortes, C., & Vapnik, V. (1995). Support-vector networks. *Machine Learning, 20*(3), 273–297. https://doi.org/10.1007/BF00994018  
- Noble, W. S. (2006). What is a support vector machine? *Nature Biotechnology, 24*(12), 1565–1567. https://doi.org/10.1038/nbt1206-1565 
- Metsis, V., Androutsopoulos, I., & Paliouras, G. (2006). Spam filtering with Naive Bayes – Which Naive Bayes? *CEAS 2006 – Third Conference on Email and Anti-Spam.*  
- Androutsopoulos, I., Koutsias, J., Chandrinos, K. V., & Spyropoulos, C. D. (2000). An experimental comparison of naive Bayesian and keyword-based anti-spam filtering with personal e-mail messages. *SIGIR Forum, 33*(1), 160–167. https://doi.org/10.1145/345508.345579  

---

