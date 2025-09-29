# 📘 Assignment 6 — Classification

## 1. Introduction to Classification

Classification is a supervised learning approach where the aim is to assign each input to a specific group or category based on its characteristics. The model is trained using data that already has known categories, and it learns to recognize patterns that distinguish one class from another.

Unlike regression, which is concerned with predicting a continuous outcome, classification focuses on predicting discrete labels. For instance, regression might estimate the temperature tomorrow, while classification would decide if tomorrow will be "hot" or "cold".

**Example of Classification:**  
- Predicting whether a bank transaction is fraudulent or legitimate.

**Example of Regression:**  
- Estimating the number of sales for a new product next month.

---

## 2A. Classification Algorithms

### Logistic Regression

**How it works:**  
Logistic Regression estimates the probability that an input belongs to a particular category by applying a logistic function to a linear combination of the input features. The output is a value between 0 and 1, which can be interpreted as the likelihood of belonging to the positive class.

**Use case:**  
- Determining if a patient is at risk for a certain disease (risk/no risk).

**Advantages:**  
- Straightforward to implement and interpret.
- Provides probability scores for predictions.
- Works well when the relationship between features and the outcome is approximately linear.

**Limitations:**  
- Struggles with complex, non-linear relationships.
- Sensitive to outliers and irrelevant features.

---

### Decision Trees

**How it works:**  
Decision Trees use a series of binary decisions to split the data into subsets based on feature values. Each split is chosen to best separate the classes, and the process continues until the data is divided into pure groups or a stopping rule is met.

**Use case:**  
- Classifying types of plants based on their physical characteristics.

**Advantages:**  
- Easy to visualize and explain.
- Can handle both numerical and categorical data.
- No need for feature scaling or normalization.

**Limitations:**  
- Can easily overfit, especially with deep trees.
- May be unstable; small changes in data can lead to different splits.

---

### Random Forest

**How it works:**  
Random Forest builds multiple decision trees using different random samples of the data and features. Each tree votes for a class, and the class with the most votes is chosen as the final prediction. This ensemble approach reduces the risk of overfitting and increases robustness.

**Use case:**  
- Predicting whether a customer will default on a loan.

**Advantages:**  
- Handles large datasets and many features well.
- Less likely to overfit than a single decision tree.
- Can capture complex interactions between features.

**Limitations:**  
- Less transparent than a single tree; harder to interpret.
- Requires more computational resources.

---

## 2B. Extended Task – Research Another Algorithm

### Naive Bayes

**Problem it solves:**  
Naive Bayes is especially effective for text-related tasks, such as document classification or sentiment analysis, where features are word counts or frequencies.

**How it works:**  
It applies Bayes’ Theorem, assuming all features are independent given the class label. The algorithm calculates the probability of each class for a given input and selects the class with the highest probability.

**Real-world application:**  
- Filtering spam emails from legitimate messages.

**Strengths:**  
- Extremely fast and efficient, even with large or high-dimensional datasets.
- Simple to implement and works well with limited training data.

**Weaknesses:**  
- The independence assumption is rarely true, which can reduce accuracy.
- Not ideal when features are highly correlated.

**Comparison with Other Algorithms:**  
Naive Bayes is much faster than Logistic Regression, Decision Trees, and Random Forest, and excels with high-dimensional data like text. However, it can struggle when features are correlated, where tree-based models (Decision Trees, Random Forest) or Logistic Regression may perform better. Naive Bayes and Logistic Regression are both easy to interpret, while Random Forest is more complex but handles non-linear relationships and feature interactions better.

| Algorithm           | Non-Linearity | High-Dimensional Data | Fast Training | Interpretable | Sensitive to Feature Correlation |
|---------------------|---------------|----------------------|---------------|---------------|-------------------------------|
| Naive Bayes         | No            | Yes                  | Yes           | Yes           | Yes                          |
| Logistic Regression | No            | Yes                  | Yes           | Yes           | No                           |
| Decision Trees      | Yes           | Yes                  | Yes           | Yes           | No                           |
| Random Forest       | Yes           | Yes                  | No            | Less          | No                           |

In summary, Naive Bayes is a strong, simple choice for text and high-dimensional data, but for complex or correlated features, tree-based models or Logistic Regression may be more reliable. **Choosing the right algorithm depends on the data and problem: Naive Bayes is best for text and speed, while Random Forest is better for complex, non-linear data.**

---

## 3. Classification Metrics

| Metric           | What it Measures                                                      | When to Use                        | Weaknesses                        |
|------------------|-----------------------------------------------------------------------|-------------------------------------|------------------------------------|
| Accuracy         | Fraction of total predictions that are correct                        | When classes are balanced           | Can be misleading with imbalance   |
| Precision        | Proportion of positive predictions that are actually correct          | When false positives are costly     | Does not consider false negatives  |
| Recall           | Proportion of actual positives that are correctly identified          | When missing positives is costly    | Does not consider false positives  |
| F1-Score         | Balance between precision and recall                                  | When classes are imbalanced         | Less intuitive than accuracy       |
| Confusion Matrix | Counts of true/false positives/negatives for all predictions          | For detailed error analysis         | Can be complex for many classes    |

**Definitions:**

- **Accuracy:** Measures how often the model is correct overall.
- **Precision:** Focuses on how many selected items are relevant.
- **Recall:** Focuses on how many relevant items are selected.
- **F1-Score:** Combines precision and recall into a single score.
- **Confusion Matrix:** Shows the breakdown of correct and incorrect predictions for each class.

---

## 4. Imbalanced Data Problem

Imbalanced data refers to situations where some classes are much more common than others in the dataset. For example, in fraud detection, fraudulent transactions are much rarer than legitimate ones.

**Why accuracy can be misleading:**  
If 98% of transactions are legitimate, a model that always predicts "legitimate" will have 98% accuracy but will never catch any fraud. This gives a false sense of good performance.

**More reliable metrics:**  
- **Precision** and **Recall** are more informative in these cases, as they focus on the model’s ability to correctly identify the minority class.
- **F1-Score** is also useful because it balances the trade-off between precision and recall.

---

## 5. Real-World Case Study: Spam Detection

**Goal:**  
To automatically identify and filter out unwanted or harmful emails (spam) from users’ inboxes.

**Data Used:**  
- Large datasets of emails labeled as spam or not spam.
- Features include word frequencies, sender reputation, presence of links, and more.

**Classification Model Applied:**  
- Naive Bayes is widely used for spam detection due to its effectiveness with text data and speed.
- Other models like Support Vector Machines and ensemble methods are also used for improved performance.

**Key Results or Insights:**  
- Spam filters using Naive Bayes can achieve high recall, catching most spam emails.
- Precision is also important to avoid blocking legitimate emails.
- The use of machine learning for spam detection has significantly improved email security and user satisfaction.

---

**References:**
- Raschka, S. (2015). Python Machine Learning. Packt Publishing.
- scikit-learn documentation: https://scikit-learn.org/stable/modules/naive_bayes.html
- Wikipedia: [Naive Bayes spam filtering](https://en.wikipedia.org/wiki/Naive_Bayes_spam_filtering)
- Towards Data Science: [Understanding Naive Bayes Classifier](https://towardsdatascience.com/understanding-naive-bayes-classifier-7e2c2a51d2fc)