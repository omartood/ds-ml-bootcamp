# Assignment 6 — Classification  

## 1. Introduction to Classification  
Classification is a **supervised machine learning task** where the goal is to assign input data into one of several predefined categories. The model is trained with labeled examples and learns to recognize the boundaries that separate different classes.  

Unlike **regression**, which predicts continuous values, classification predicts discrete labels. For example:  

- **Classification example:** Detecting whether a bank transaction is *fraudulent* or *legitimate.*  
- **Regression example:** Predicting the number of product sales next month.  

---

## 2A. Core Classification Algorithms  

### Logistic Regression  
- **How it works:** Uses a logistic (sigmoid) function to map a weighted sum of features into probabilities between 0 and 1.  
- **Use case:** Predicting whether a patient is at risk of heart disease.  
- **Advantages:** Simple, interpretable, outputs probability estimates.  
- **Limitations:** Performs poorly with complex, non-linear data.  

### Decision Trees  
- **How it works:** Recursively splits data into branches using feature values, forming a tree structure that leads to classification outcomes.  
- **Use case:** Classifying plants by physical characteristics.  
- **Advantages:** Easy to visualize, handles both numerical and categorical data.  
- **Limitations:** Overfits easily; unstable with small data changes.  

### Random Forest  
- **How it works:** Builds many decision trees on random subsets of data and features. Predictions are made by majority vote across trees.  
- **Use case:** Predicting whether a customer will default on a loan.  
- **Advantages:** Reduces overfitting, robust to noise, works well with large datasets.  
- **Limitations:** Harder to interpret than a single tree; computationally heavier.  

---

## 2B. Extended Algorithms  

### Naive Bayes  
- **Problem it solves:** Effective in **text classification** tasks such as spam filtering or sentiment analysis.  
- **How it works:** Applies Bayes’ Theorem, assuming all features are independent given the class. It selects the class with the highest probability.  
- **Application:** Filtering spam emails.  
- **Strengths:** Very fast, efficient with high-dimensional data, works with small training sets.  
- **Weaknesses:** Independence assumption rarely holds; struggles when features are correlated.  

### K-Nearest Neighbors (KNN)  
- **Problem it solves:** Suitable for problems based on similarity, such as image recognition or recommendation systems.  
- **How it works:** Classifies an input based on the majority class among its *k* nearest neighbors in the feature space.  
- **Application:** Handwritten digit recognition (MNIST dataset).  
- **Strengths:** Simple, flexible, no explicit training phase.  
- **Weaknesses:** Slow prediction for large datasets; sensitive to irrelevant or unscaled features.  

---

## 2C. Algorithm Comparison  

| Algorithm           | Works with Non-linear Data | High-Dimensional Data | Training Speed | Prediction Speed | Interpretability | Sensitive to Scaling | Typical Use Cases          |
|---------------------|----------------------------|-----------------------|----------------|-----------------|-----------------|----------------------|---------------------------|
| Logistic Regression | No                         | Yes                   | Fast           | Fast            | High            | No                   | Medical risk prediction   |
| Decision Trees      | Yes                        | Yes                   | Fast           | Fast            | High            | No                   | Plant classification      |
| Random Forest       | Yes                        | Yes                   | Moderate       | Moderate        | Medium          | No                   | Loan default prediction   |
| Naive Bayes         | No                         | Excellent             | Very Fast      | Very Fast       | High            | Yes (correlation issue) | Spam filtering          |
| KNN                 | Yes                        | Poor with many dims   | None (lazy)    | Slow (large k)  | Low             | Yes                  | Image recognition         |

---

## 3. Classification Metrics  

### Key Definitions  
- **Accuracy:** Fraction of correct predictions over total predictions.  
- **Precision:** Proportion of predicted positives that are actually correct.  
- **Recall:** Proportion of actual positives that are correctly identified.  
- **F1-Score:** Harmonic mean of precision and recall.  
- **Confusion Matrix:** A table showing counts of true/false positives and negatives for all classes.  

### Comparison Table  

| Metric         | What It Measures                                | When to Use                        | Weaknesses                          |
|----------------|-------------------------------------------------|------------------------------------|-------------------------------------|
| Accuracy       | Overall correctness of predictions              | Balanced datasets                  | Misleading for imbalanced datasets  |
| Precision      | % of positive predictions that are correct       | When false positives are costly     | Ignores false negatives             |
| Recall         | % of actual positives correctly identified       | When false negatives are costly     | Ignores false positives             |
| F1-Score       | Balance between precision and recall             | When classes are imbalanced         | Less intuitive than accuracy        |
| Confusion Matrix | Full breakdown of TP, TN, FP, FN              | Detailed error analysis             | Complex for many classes            |

---

## 4. Imbalanced Data Problem  
Imbalanced data occurs when some classes are much more frequent than others. Example: fraud detection, where fraudulent transactions represent less than 5% of the data.  

- **Why accuracy is misleading:** A model that predicts all transactions as “legitimate” may achieve 95–98% accuracy but never detect fraud.  
- **Better metrics:** Precision, Recall, and F1-Score are more reliable because they focus on identifying minority classes.  

---

## 5. Real-World Case Study: Spam Detection  

- **Goal:** Automatically filter spam emails to improve user safety and email experience.  
- **Data:** Large collections of emails labeled spam/not spam, with features such as word frequency, sender domain, and hyperlinks.  
- **Model:** Naive Bayes (widely used due to speed and suitability for text), often combined with ensemble methods.  
- **Results:** High recall ensures most spam is caught; precision prevents misclassifying legitimate emails. Spam filters significantly improve email security worldwide.  

---

## References  

- Raschka, S. (2015). *Python Machine Learning*. Packt Publishing.  
- Scikit-learn Documentation. (2024). [Naive Bayes and KNN](https://scikit-learn.org/stable/supervised_learning.html)  
- Wikipedia contributors. (2024). *Naive Bayes spam filtering*. Wikipedia.  
- Alpaydin, E. (2021). *Introduction to Machine Learning*. MIT Press.  
