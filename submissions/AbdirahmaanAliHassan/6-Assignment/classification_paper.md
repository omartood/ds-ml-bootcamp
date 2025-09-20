# Introduction to Classification

Machine Learning (ML) has become a cornerstone of modern data-driven decision-making, and classification is one of its most widely applied tasks. Classification refers to the process of assigning input data into one of several predefined categories. The essential idea is that, given past examples, the algorithm learns patterns that allow it to predict the class of unseen data. For example, an email service may label incoming messages as “spam” or “not spam,” a medical system may categorize tumors as “benign” or “malignant,” and a banking system may classify applicants as “low risk” or “high risk.”

Classification differs from **regression**, another fundamental task in ML. While classification predicts discrete labels, regression predicts continuous numerical values. For instance, house price prediction is a regression problem, because the target variable (price) can take any numeric value within a range. In contrast, predicting whether a borrower will default on a loan is classification, because the target is categorical (yes/no).

---

# 2A. Classification Algorithms

## Logistic Regression

Despite its name, Logistic Regression is a classification algorithm, not a regression model. It predicts the probability of an outcome belonging to a particular class using the logistic (sigmoid) function. Predictions above a threshold (commonly 0.5) are assigned to one class, while those below are assigned to another.

* **Use case**: Logistic regression is commonly applied in healthcare, for example predicting the likelihood of a patient developing heart disease based on risk factors such as age, cholesterol, and blood pressure.
* **Advantages**: Simple, interpretable, and computationally efficient.
* **Limitations**: Struggles with complex, non-linear decision boundaries and assumes a linear relationship between input variables and the log-odds of the output.

## Decision Trees

A Decision Tree is a flowchart-like structure where data is split at nodes based on feature conditions, leading to a prediction at the leaves. Each split is chosen to maximize separation between classes.

* **Use case**: Widely used in marketing for customer segmentation, helping companies decide whether to promote premium or standard services.
* **Advantages**: Easy to visualize and understand; handles both categorical and numerical data.
* **Limitations**: Prone to overfitting, meaning it can memorize the training data instead of generalizing well.

## Random Forest

Random Forest extends decision trees by creating an ensemble of many trees trained on random subsets of data and features. The final prediction is made through majority voting across the trees.

* **Use case**: Fraud detection in financial transactions, where robustness and accuracy are critical.
* **Advantages**: Reduces overfitting, improves accuracy, and handles high-dimensional data well.
* **Limitations**: Less interpretable than a single tree; requires more computational resources.

---

# 2B. Extended Task – Support Vector Machines (SVM)

Support Vector Machines (SVM) are particularly powerful when classes are not easily separable. The central idea is to find the “maximum margin hyperplane” that best separates the classes in the feature space. When data cannot be separated linearly, SVM uses kernels (such as polynomial or radial basis functions) to project the data into a higher-dimensional space where separation becomes possible.

* **Problem suitability**: Effective for high-dimensional problems like text classification and image recognition.
* **Application**: Widely applied in handwriting recognition, such as distinguishing digits in automated postal systems.
* **Strengths**: Robust to overfitting in high dimensions; effective with clear margins of separation.
* **Weaknesses**: Computationally expensive for very large datasets; parameter tuning (choice of kernel, regularization) can be complex compared to simpler models like Logistic Regression.

---

# 3. Classification Metrics

Evaluating classification models requires careful consideration of different metrics:

* **Accuracy**: The proportion of correctly classified samples among all samples.
* **Precision**: Of the predicted positives, the proportion that is truly positive. Important when false positives are costly.
* **Recall**: Of the actual positives, the proportion correctly identified. Critical when false negatives are costly.
* **F1-Score**: The harmonic mean of precision and recall, useful for balancing both concerns.
* **Confusion Matrix**: A tabular summary of true positives, true negatives, false positives, and false negatives, allowing a detailed view of performance.

### Table: Comparison of Metrics


| Metric           | Focus                    | Best Use Case       | Weakness                      |
| ---------------- | ------------------------ | ------------------- | ----------------------------- |
| Accuracy         | Overall correctness      | Balanced datasets   | Misleading in imbalanced data |
| Precision        | Avoiding false positives | Spam detection      | Ignores false negatives       |
| Recall           | Avoiding false negatives | Medical diagnosis   | Ignores false positives       |
| F1-Score         | Balance of both          | Imbalanced datasets | Less intuitive                |
| Confusion Matrix | Error distribution       | Model diagnostics   | No single performance score   |

---

# 4. Imbalanced Data Problem

In many real-world applications, data is **imbalanced**, meaning one class vastly outnumbers another. For example, fraudulent credit card transactions may represent less than 1% of all transactions. In such cases, accuracy is misleading: a model predicting “non-fraud” for every case might reach 99% accuracy, yet completely fail at detecting fraud.

To address this, metrics such as **Precision, Recall, and F1-Score** are more reliable. Precision ensures that detected fraud cases are truly fraudulent, recall ensures that most actual frauds are caught, and the F1-Score balances these two needs.

---

# 5. Real-World Case Study: Credit Card Fraud Detection

A well-known project in financial security applied classification techniques to detect fraudulent credit card transactions.

* **Goal**: To reduce financial loss by accurately identifying fraudulent activity in real time.
* **Data**: A dataset of 284,807 European card transactions, with only 0.17% labeled as fraud.
* **Model**: Random Forest classifiers, combined with oversampling techniques such as SMOTE (Synthetic Minority Oversampling Technique), were used to handle class imbalance.
* **Results**: The model achieved high recall for fraudulent transactions, ensuring most fraud attempts were caught. Accuracy alone was not the focus; instead, the F1-Score and confusion matrix provided a better assessment. This led to a practical model capable of reducing undetected fraud without overwhelming analysts with false alarms.

---

# References

* Géron, A. (2019). *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow*. O’Reilly Media.
* Han, J., Kamber, M., & Pei, J. (2011). *Data Mining: Concepts and Techniques*. Morgan Kaufmann.
* Kaggle. (2018). *Credit Card Fraud Detection Dataset*. Retrieved from [https://www.kaggle.com/mlg-ulb/creditcardfraud]()
