# **📘 Assignment 6 – Classification:**

### **1\. Introduction to Classification**

Classification is a fundamental task in supervised machine learning where the primary goal is to predict a categorical label for a given input. This process involves training a model on a labeled dataset, enabling it to recognize patterns and relationships between input features and their corresponding classes. The model then uses this learned knowledge to assign a new, unlabeled data point to one of the predetermined categories.

The core difference between classification and regression lies in the nature of their output. Regression models predict a continuous, numerical value from an infinite range, such as predicting the exact price of a house or the temperature on a given day. In contrast, classification models predict a discrete category from a finite set of labels, for example, determining if an email is "spam" or "not spam." In essence, regression answers the question "How much?", while classification answers the question "Which class?".

A real-life example of a classification task is **email spam detection**, where an algorithm analyzes an email's content, sender, and headers to classify it as either "spam" or "not spam." A real-life example of a regression task is **predicting a student's final exam score** based on their homework grades, attendance, and past test results.

### **2A. Classification Algorithms**

#### **Logistic Regression**

Despite its name, Logistic Regression is a statistical model used for binary classification tasks. It works by applying a logistic function, also known as the sigmoid function, to the output of a linear equation. This function maps any real-valued number to a value between 0 and 1, which can be interpreted as a probability. For example, a model might predict a 0.85 probability that a patient has a specific disease, which would then be classified as a positive case if a decision threshold (e.g., 0.5) is used.

* **Use Case:** Predicting whether a customer will **'click'** on a specific advertisement or not.
* **Advantages:** It is simple, fast, and highly interpretable. It also performs well on linearly separable data and is computationally inexpensive.
* **Limitations:** It can struggle with complex, non-linear problems and is sensitive to irrelevant features.

#### **Decision Trees**

A Decision Tree models decisions and their possible consequences as a flowchart-like tree structure. Each internal node represents a test on a feature (e.g., "Is income \> $50,000?"), each branch represents an outcome of the test, and each leaf node represents the final class label. The model learns a series of if-then-else rules to partition the data and arrive at a classification.

* **Use Case:** Deciding whether a bank should **'approve'** or **'deny'** a loan application based on an applicant's financial history.
* **Advantages:** Decision Trees are easy to understand and visualize, and they can handle both numerical and categorical data without extensive preprocessing.
* **Limitations:** A single tree can be prone to overfitting, where it learns the training data too well and performs poorly on new data. They are also highly sensitive to small changes in the training data.

#### **Random Forest**

Random Forest is an ensemble learning method that improves upon the limitations of a single Decision Tree. It operates by constructing a "forest" of many individual Decision Trees. Each tree is trained on a random subset of the training data and a random subset of the features. To make a prediction, all the trees in the forest vote, and the class with the most votes becomes the final classification. This collective decision-making process significantly reduces overfitting and improves accuracy.

* **Use Case:** Classifying tumors as **'malignant'** or **'benign'** based on cell features.
* **Advantages:** It is highly accurate, robust to overfitting, and can handle large datasets with many features.
* **Limitations:** The model is less interpretable than a single Decision Tree due to its complexity and a large number of trees. It can also be computationally more expensive to train.

### **2B. Extended Task – Research KNN Algorithm**

#### **K-Nearest Neighbors (KNN)**

K-Nearest Neighbors (KNN) is a simple but powerful non-parametric classification algorithm. It is a "lazy learner" because it does not explicitly build a model during the training phase; instead, it memorizes the entire training dataset. To classify a new data point, the algorithm calculates the distance (e.g., Euclidean distance) between this new point and all points in the training set. It then identifies the **'k'** nearest neighbors to the new data point. The final classification is determined by a majority vote of the class labels of these 'k' neighbors.

This algorithm is good at solving problems where the class of a data point is heavily influenced by the class of its closest neighbors. A common real-world application is **recommendation systems**, where a user's preferences are classified based on the preferences of other users who are "close" to them (i.e., have similar tastes).

Compared to the algorithms in Section 2, KNN's main strength is its simplicity and effectiveness for many classification problems, particularly with small datasets. It is easy to implement and there is no training phase. However, a major weakness is its computational cost, as it needs to compute the distance to every single data point in the training set for each new prediction. This makes it very slow and inefficient for large datasets. It also suffers from the "curse of dimensionality," as its performance degrades significantly when dealing with a high number of features.

### **3\. Classification Metrics**

* **Accuracy:** Measures the proportion of all predictions that were correct. It provides a simple, overall measure of the model's performance.
* **Precision:** Of all the instances that the model predicted as positive, Precision measures how many were actually positive. It focuses on avoiding false positives.
* **Recall:** Of all the instances that were actually positive, Recall measures how many were correctly identified by the model. It focuses on avoiding false negatives.
* **F1-Score:** The F1-Score is the harmonic mean of Precision and Recall. It provides a single score that balances both metrics, which is particularly useful when dealing with imbalanced datasets.
* **Confusion Matrix:** A table that visually summarizes the performance of a classification model. It breaks down the total predictions into four key categories: True Positives, True Negatives, False Positives, and False Negatives, providing a complete picture of where the model made errors.

#### **Comparison Table**

| Metric                     | Question it answers                                     | When to Use                                                             | Weaknesses                                                                                  |
| :------------------------- | :------------------------------------------------------ | :---------------------------------------------------------------------- | :------------------------------------------------------------------------------------------ |
| **Accuracy**         | How many predictions are correct overall?               | When classes are balanced.                                              | Can be misleading on imbalanced datasets.                                                   |
| **Precision**        | Of predicted positives, how many are actually positive? | When the cost of a false positive is high (e.g., medical diagnosis).    | Does not account for false negatives; can be high even if many positives are missed.        |
| **Recall**           | Of actual positives, how many are caught?               | When the cost of a false negative is high (e.g., fraud detection).      | Does not account for false positives; can be high with many incorrect positive predictions. |
| **F1-Score**         | How well does the model balance Precision and Recall?   | When classes are imbalanced and you need a balanced performance metric. | Less intuitive than Accuracy, and doesn't reveal the full breakdown of errors.              |
| **Confusion Matrix** | What are the counts of True/False Positives/Negatives?  | As a primary tool to understand all types of errors made by the model.  | Not a single, numerical score; requires interpretation of four values.                      |

### **4\. Imbalanced Data Problem**

Imbalanced data refers to a classification problem where the number of instances in one class (the majority class) is significantly higher than the number of instances in the other class (the minority class). For example, in a credit card fraud detection dataset, legitimate transactions might outnumber fraudulent ones by 99 to 1\.

In such cases, accuracy can be highly misleading. A simple model that always predicts the majority class would achieve a very high accuracy. For instance, in the fraud detection example, a model that always classifies a transaction as "legitimate" would still have 99% accuracy. However, this model would be completely useless, as it would fail to detect a single fraudulent transaction.

For imbalanced datasets, metrics that focus on the minority class are more reliable. **Precision** and **Recall** are much better indicators of performance. **F1-Score** is also highly reliable because it provides a single, balanced metric that penalizes models with poor performance in either Precision or Recall. The **Confusion Matrix** is the most comprehensive tool, as it visually reveals the exact number of false negatives (missed fraudulent transactions) and false positives (legitimate transactions flagged as fraud), allowing for a detailed understanding of the model's failure points.

### **5\. Real-World Case Study**

#### **Fraud Detection using Machine Learning**

* **Goal:** The primary objective of this project is to develop a classification model to detect fraudulent credit card transactions in real-time. The ultimate goal is to minimize financial losses for both the bank and its customers by identifying and blocking suspicious transactions as they occur.
* **Data Used:** The data for this project is highly imbalanced, consisting of millions of legitimate transactions and only a small fraction of fraudulent ones. Features typically include transaction amount, transaction time, location of the transaction, the merchant's category, and historical user behavior patterns.
* **Model Applied:** Given the imbalanced nature of the data and the need to identify complex, non-linear patterns, an ensemble method such as **Random Forest** is a highly effective choice for this problem. The model's ability to handle high-dimensional data and provide robust predictions makes it suitable for this task.
* **Key Results/Insights:** The key results of a fraud detection model are typically measured by a high **Recall** score. In this context, achieving high recall is critical to ensure that a large percentage of actual fraudulent transactions are successfully identified, even if it results in a small number of false positives (legitimate transactions being flagged). Key insights from such a model often reveal unusual patterns, such as a large transaction occurring at a location far from the cardholder's usual spending habits or a series of small, rapid-fire transactions in a short period. The model serves as a crucial line of defense in the financial industry.
