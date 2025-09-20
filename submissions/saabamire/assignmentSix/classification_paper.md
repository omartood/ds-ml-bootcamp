# Lesson 6 assignment — Classification



## 1. What is Classification?

Classification is a type of **supervised learning** where we predict **categories** instead of numbers.

- Example: A doctor can classify patients as **diabetic** or **non-diabetic** based on tests.
- Another example: A weather app can predict if tomorrow will be **sunny**, **rainy**, or **cloudy**.

**Key difference with Regression:**

- Regression predicts **numbers** (like temperature or weight).
- Classification predicts **labels or types** (like diabetic or non-diabetic).

---

## 2. Classification Algorithms

### Logistic Regression

- Works by calculating **probabilities** using a function called **sigmoid**.
- Example: Predict if a student **submits homework on time** based on previous submissions.
- Advantages: Simple, fast, good for small datasets.
- Limitations: Not good for overlapping or complex data.

### Decision Tree

- Splits data using **if/else rules** into a tree structure.
- Example: Classify animals as **mammals**, **birds**, or **reptiles** using features like skin type and egg-laying.
- Advantages: Easy to understand and explain.
- Limitations: Can **overfit** if tree is too big.

### Random Forest

- Combines **many Decision Trees** and takes a **majority vote**.
- Example: Predict if crops are **healthy**, **infested**, or **diseased** using leaf color, soil, and moisture.
- Advantages: More accurate, less overfitting.
- Limitations: Harder to interpret, slower than a single tree.

---

## 2B. Extended two Algorithms 

##  K-Nearest Neighbors (KNN)

- KNN predicts class based on the **closest neighbors** in the data.
- Example: Predict the **genre of a new book** in a library based on similarity to other books (length, topic, style).
- Strengths: Simple, intuitive, works well with small datasets.
- Weaknesses: Slow with large datasets, sensitive to noisy data.

##  Support Vector Machines (SVM)

- SVM finds the **best boundary (hyperplane)** that separates different classes in the data.  
- Example: Classify emails as **spam** or **not spam** based on text features.  
- Strengths: Works well with **high-dimensional data** and can handle **non-linear boundaries** using kernels.  
- Weaknesses: Can be **slow with very large datasets** and harder to interpret than simple models.  

---

## 3. Classification Metrics

When we build a classification model, we need to **check its performance**:

- **Accuracy:** How many predictions are correct overall. Works well if classes are balanced.
- **Precision:** Of all predicted positives, how many are really positive. Important when false positives are costly (e.g., healthy plant classified as diseased).
- **Recall:** Of all actual positives, how many were caught. Important when false negatives are dangerous (e.g., missing a diseased plant).
- **F1-Score:** Combines Precision and Recall, useful for **imbalanced datasets**.
- **Confusion Matrix:** Shows counts of **True Positives, False Positives, True Negatives, False Negatives**.

| Metric           | Focus                                           | When to Use                     |
| ---------------- | ----------------------------------------------- | ------------------------------- |
| Accuracy         | Overall correct predictions                     | Balanced datasets               |
| Precision        | Correctness of positive predictions            | Avoid false positives           |
| Recall           | How many actual positives were found           | Avoid false negatives           |
| F1-Score         | Balance of precision & recall                  | Imbalanced datasets             |
| Confusion Matrix | Full error breakdown (TP, FP, TN, FN)          | Detailed analysis               |

---

## 4. Imbalanced Data Problem

Imbalanced data happens when one class is **much more common** than another.

- Example: In a factory, 95% of products are **good** and 5% are **defective**.
- A model that always predicts “good” gets **95% accuracy**, but it **fails to find defective products**.

 **precision, recall, F1-score, and confusion matrix** are more reliable than accuracy because Accuracy can be misleading in imbalanced data because it is dominated by the majority class. Precision, recall, F1-score, and confusion matrix are more reliable because they measure how well the model detects the minority class and show errors for each class separately.

---

## 5. Real-World Case Study — Spam Email Detection

- **Goal:** Automatically detect if an email is **spam** or **not spam**.
- **Data:** Text of emails, sender information, keywords, and subject lines.
- **Model:** Naive Bayes classifier.
- **Result:** The model correctly identified most spam emails while keeping important emails safe.



---

## References

- Géron, A. (2019). *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow*. O’Reilly Media.  
- James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013). *An Introduction to Statistical Learning*. Springer.  
- Alpaydin, E. (2020). *Introduction to Machine Learning (4th ed.)*. MIT Press.  
- Deb, S. (2024). *Naïve Bayes Classification: Spam Email Detection*. Kaggle. Retrieved from [https://www.kaggle.com/code/satarupadeb/na-ve-bayes-classification-spam-email-detection](https://www.kaggle.com/code/satarupadeb/na-ve-bayes-classification-spam-email-detection)
