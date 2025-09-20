## 1. Introduction to Classification

Classification is a fundamental task in Machine Learning where the objective is to predict **categories** rather than continuous values. A classification model is trained on labeled data, where each observation belongs to a predefined class, and then used to predict the class of new, unseen data.

The key difference between classification and regression is in the nature of the output. **Regression** predicts continuous values (e.g., the price of a house), while **classification** predicts discrete categories (e.g., whether an email is spam or not).

**Example of classification:** predicting whether a patient has diabetes (Yes/No).  
**Example of regression:** predicting the patient’s blood sugar level (a continuous number).

---

## 2A. Classification Algorithms

### Logistic Regression

Despite its name, Logistic Regression is used for **classification**. It estimates the probability that an observation belongs to a particular class using the **sigmoid function**, which maps values to the range 0–1. If the probability exceeds a threshold (commonly 0.5), the model classifies the instance as positive.

_Use case:_ Email spam detection.  
_Advantages:_ Simple, interpretable, and computationally efficient.  
_Limitations:_ Works best for linear decision boundaries; struggles with complex relationships.

### Decision Trees

Decision Trees split data based on features using a tree-like structure. Each node represents a decision based on an attribute, and branches represent possible outcomes. They are intuitive and easy to visualize.

_Use case:_ Loan approval prediction based on income, age, and credit score.  
_Advantages:_ Easy to interpret, no need for feature scaling.  
_Limitations:_ Can overfit if not pruned; sensitive to small changes in data.

### Random Forest

Random Forest is an **ensemble method** that builds multiple decision trees and combines their predictions. By averaging or voting across many trees, it reduces overfitting and increases accuracy.

_Use case:_ Customer churn prediction.  
_Advantages:_ High accuracy, robust to noise, works well with high-dimensional data.  
_Limitations:_ Less interpretable than single trees; computationally heavier.

---

## 2B. Extended Task – Support Vector Machines (SVM)

Support Vector Machines are powerful classification algorithms designed to find the **optimal boundary (hyperplane)** that separates classes in the feature space. SVM maximizes the margin between classes, making it effective in handling complex, non-linear problems with the help of kernel functions.

_Problem suited for:_ Text classification and image recognition.  
_How it works:_ SVM identifies “support vectors” (critical data points) and builds a decision boundary that best separates the classes.  
_Application:_ Handwritten digit recognition (e.g., classifying MNIST dataset).  
_Strengths:_ Works well with high-dimensional data; effective for non-linear problems using kernels.  
_Weaknesses:_ Computationally expensive for large datasets; less interpretable compared to logistic regression.

---

## 3. Classification Metrics

Evaluating a classification model requires more than just accuracy. The following metrics provide a complete performance picture:

- **Accuracy:** Overall proportion of correct predictions.
- **Precision:** Of the predicted positives, how many are actually positive.
- **Recall (Sensitivity):** Of the actual positives, how many are correctly identified.
- **F1-Score:** The harmonic mean of Precision and Recall, useful in imbalanced data.
- **Confusion Matrix:** A table showing true positives, true negatives, false positives, and false negatives.

### Comparison Table

| Metric           | Question it Answers                           | Best Use Case                   | Weakness                  |
| ---------------- | --------------------------------------------- | ------------------------------- | ------------------------- |
| Accuracy         | How many predictions are correct overall?     | Balanced datasets               | Misleading in imbalance   |
| Precision        | Of predicted positives, how many are correct? | When false positives are costly | Ignores false negatives   |
| Recall           | Of actual positives, how many are caught?     | When false negatives are costly | Ignores false positives   |
| F1-Score         | Balance between precision & recall            | Imbalanced datasets             | Harder to interpret alone |
| Confusion Matrix | What exact errors were made?                  | Detailed error analysis         | Requires interpretation   |

---

## 4. Imbalanced Data Problem

**Imbalanced data** occurs when one class dominates the dataset. For example, in fraud detection, 98% of transactions may be legitimate and only 2% fraudulent. In such cases, a model that always predicts “legitimate” can achieve 98% accuracy — yet fail to identify any fraud.

This shows why accuracy can be misleading. Instead, metrics like **Precision, Recall, and F1-Score** are more reliable. Recall ensures we catch as many fraudulent cases as possible, while Precision ensures we minimize false alarms.

---

## 5. Real-World Case Study: Medical Diagnosis

One real-world use of classification is in **breast cancer detection**. Researchers have used the **Breast Cancer Wisconsin dataset**, which contains features of tumor cells (such as size, texture, and smoothness), to classify tumors as benign or malignant.

The goal of the project was to assist doctors in early detection of cancer. Models such as Logistic Regression and Random Forest were applied. The Random Forest model achieved higher accuracy and recall, meaning it was better at detecting malignant tumors.

The key insight was that machine learning can significantly improve diagnostic accuracy, reduce false negatives, and support healthcare professionals in making life-saving decisions.

---

## Conclusion

Classification is a core supervised learning technique where models predict categories rather than continuous numbers. Algorithms such as Logistic Regression, Decision Trees, Random Forest, and Support Vector Machines are widely used, each with unique strengths and weaknesses.

Model evaluation requires careful use of metrics beyond accuracy, especially when dealing with imbalanced datasets. In real-world applications such as medical diagnosis, fraud detection, and spam filtering, classification has proven to be a powerful tool with significant practical impact.
