# Lesson 6 — Classification  

---

## 1. Introduction to Classification  

Classification is a supervised learning technique in Machine Learning where the task is to categorize data into predefined groups. A model is trained on labeled examples and then applied to predict the class of unseen observations. Unlike regression, which predicts continuous numerical values, classification predicts discrete categories.  

For example, detecting whether an email is *spam* or *not spam* is a classification problem because the outputs are categorical. In contrast, estimating the price of a house based on its features is a regression problem since the output is a continuous value.  

---

## 2A. Classification Algorithms  

### Logistic Regression  
Logistic Regression is a statistical model designed for binary classification tasks. It uses the logistic (sigmoid) function to transform inputs into probabilities between 0 and 1. A threshold determines the predicted class.  
- **Use case:** Predicting whether a patient has a disease based on diagnostic results.  
- **Advantages:** Easy to implement and interpret; efficient for linearly separable data.  
- **Limitations:** Poor performance with non-linear data and complex feature interactions.  

### Decision Trees  
Decision Trees classify data by recursively splitting it according to feature values, forming a tree-like structure. Each branch represents a decision rule, and each leaf represents a final prediction.  
- **Use case:** Loan approval systems based on income, credit history, and age.  
- **Advantages:** Simple to visualize and understand; supports both categorical and numerical features.  
- **Limitations:** Prone to overfitting; sensitive to small changes in data.  

### Random Forest  
Random Forest is an ensemble learning method that combines multiple decision trees. Each tree is trained on a random subset of the data and features, and the results are aggregated, usually by majority vote.  
- **Use case:** Fraud detection in banking transactions.  
- **Advantages:** High accuracy, robustness, and ability to handle large datasets.  
- **Limitations:** Computationally intensive; less interpretable than a single tree.  

---

## 2B. Extended Task – Research Another Algorithm  

### Support Vector Machines (SVM)  
Support Vector Machines are classification models that separate classes by finding the optimal hyperplane in a high-dimensional space. The algorithm maximizes the margin between data points of different classes. For data that is not linearly separable, kernel functions are used to project data into higher dimensions.  
- **Problem suitability:** Well-suited for high-dimensional problems such as text classification.  
- **Use case:** Email filtering for spam versus non-spam.  
- **Strengths:** Strong theoretical foundation; effective in small to medium datasets with many features.  
- **Weaknesses:** Slow to train on very large datasets; performance depends on kernel choice. Compared to Random Forest, SVMs are less interpretable but offer clear separation boundaries.  

---

## 3. Classification Metrics  

- **Accuracy:** The proportion of correct predictions among all predictions. Reliable only for balanced datasets.  
- **Precision:** The percentage of predicted positives that are truly positive. Important when false positives are costly.  
- **Recall:** The percentage of actual positives correctly identified. Critical when false negatives are costly.  
- **F1-Score:** The harmonic mean of precision and recall. Useful when data is imbalanced.  
- **Confusion Matrix:** A detailed table summarizing true positives, true negatives, false positives, and false negatives.  

**Comparison Table**  

| Metric          | Focus                           | When to Use                        | Weaknesses                  |  
|-----------------|--------------------------------|------------------------------------|-----------------------------|  
| Accuracy        | Overall correctness            | Balanced datasets                  | Misleading with imbalance   |  
| Precision       | Correctness of positives       | When false positives are costly     | Ignores false negatives     |  
| Recall          | Capturing positives            | When false negatives are costly     | Ignores false positives     |  
| F1-Score        | Balance of precision & recall  | When both errors matter             | Hard to interpret directly  |  
| Confusion Matrix| Full breakdown of outcomes     | For detailed analysis               | More complex to summarize   |  

---

## 4. Imbalanced Data Problem  

Imbalanced data occurs when one class significantly outweighs others in a dataset. For example, in fraud detection, the majority of transactions are legitimate, while only a small fraction are fraudulent.  

In such cases, accuracy can be misleading. A model predicting every transaction as legitimate may achieve over 95% accuracy, yet fail to detect any fraud. For these scenarios, precision, recall, and F1-score are more reliable. Recall ensures rare but important cases are detected, precision minimizes false alarms, and F1-score balances both.  

---

## 5. Real-World Case Study  

### Fraud Detection in Financial Transactions  

- **Goal of the project:**  
  To identify fraudulent credit card transactions and minimize financial losses.  

- **Data they used:**  
  A large dataset of anonymized credit card transactions, including features such as transaction amount, time, and user behavior. Fraudulent cases represented less than 1% of the total data, creating an imbalanced dataset.  

- **Classification model applied:**  
  A **Random Forest classifier**, enhanced with data balancing techniques such as oversampling and class weighting.  

- **Key results or insights:**  
  The model achieved a **recall rate above 90%**, meaning most fraudulent transactions were successfully detected. This result demonstrated that ensemble methods like Random Forest, when combined with proper handling of class imbalance, can provide effective and reliable solutions for financial fraud detection.  

---

## References  

Han, J., Kamber, M., & Pei, J. (2011). *Data Mining: Concepts and Techniques*. Elsevier.  

Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning: Data Mining, Inference, and Prediction*. Springer.  

UCI Machine Learning Repository. (2013). *Credit Card Fraud Detection Dataset*. Retrieved from https://archive.ics.uci.edu  

Zhang, C., & Ma, Y. (2012). *Ensemble Machine Learning: Methods and Applications*. Springer.  
