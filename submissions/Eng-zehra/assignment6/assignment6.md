## Assignment Six Classification
- Classification in machine learning is a supervised model that predicts the categories
- Regressiom in machine learning is model that uses to predicts continiuous numbers 
**Example of Classification : predicting weather an patient has Diabates not Diabates**
**Example of regression : Predicting stock price using historical data**
# 2A.Classification Algorithms #
*Logistic Regression*is a simple algorithm that predicts the probability of an outcome and uses sigmoid funtion
*Decision Tree* is like tree structure where data is splite branches using if/else
*Randam forest* is collection of decison trees each tree makes prediction the result is the majority
# For each algorithm and How it works (basic idea)
*Logistic Regression* use signamoid funtion take one input and one output
*Decision Tree*splites data using rules  if/else rules
*Randam forest*combines more decision trees each tree can make prediction
## K-Nearest Neighbors (KNN)
Classifies a new point based on the majority class of its nearest neighbors.
2. How it works (simple process):
    Choose a number K (how many neighbors to look at)
    Measure the distance between the new point and all training points (e.g., Euclidean distance)
    Pick the K closest points.
    Assign the class that most of those neighbors belong to
# Strengths and weaknesses 
Very simple, no training phase, works well with non-linear data
Slow for large datasets, sensitive to irrelevant features, needs feature scaling (normalization).
# Real Problem 
handwritten digit recognition
## 3. Classification Metrics
1. accurancy : Percentance of Correct predictions out of total predictions its suits when classes are balanced and
 its not good when classes are imbalanced
2. Precision :How many predicted positives are correct.
3. Recall :How many actual positives were found
4. F1-score :its like accurancy but classes are imbalanced
5. Confusion Matrix :a table that compares the predicted lebels with the actual labels

## Comparizon

| Metric               | What it Measures                                               | Best Use Case 

                                                            |
| -------------------- | -------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Accuracy**         | Percentage of **correct predictions** out of all predictions    | Works well when **classes are balanced**; not reliable for **imbalanced classes** |
| **Precision**        |  **predicted positives**, how many were actually positive       | Important when **false positives are valuable**                                     |
| **Recall**           | O **actual positives**, how many did the model identify         | Important when **missing positives is costly**                                    |
| **F1 Score**         | mean of **Precision and Recall**                                | Useful for **imbalanced classes**, balances precision & recall                    |
| **Confusion Matrix** | Table comparing **predicted labels** with **actual labels** (TP, FP, FN, TN) | Base for calculating all other metrics                                            |

# 4. Imbalanced Data Problem #
Imbalanced data happens when the number of rows in each class is very different.
if the accurancy is too hight,if the accurancy is too low
prefers f1 since its intended both sides recall and precision

## 5. Real-World Case Study ##
Goal: Detect fraudulent credit card transactions to reduce financial risk.
Data: 284,807 transactions, 30 features, highly imbalanced (0.17% fraud).
Model: Random Forest Classifier with balanced class weights, 100 trees, max depth 10.
Results: AUC = 0.97, Precision = 0.85, Recall = 0.91. Fraudulent transactions identified mainly by unusual amounts and timing patterns.