# 1. What is classification in machine learning?
Classification in machine learning is a supervised learning technique used to categorize data into predefined classes or labels based on input features. Classification is commonly used binary classification which is when the output variable has two possible classes or categories, such as fraud vs non-fraud in financial transactions. It is also used in multi-class classification where the output variable has more than two possible classes, such as classifying types of animals based on their features. And it is also used in multi-label classification where each sample can belong to multiple classes simultaneously, such as a movie that can be action and comedy at the same time.

## How is different from regression?
The main difference between classification and regression is the type of output they produce. Classification produces discrete labels or categories, while regression produces continues values. In classification, the goal is to assign input data to one of several predefined classes based on their features. In regression, the goal is to predict a continuous value based on input features.

## Give one real-life example of classification and one of regression.
- **Classification Example:** Fraud detection in financial transactions. The goal is to classify transactions as either fraudulent or non-fraudulent based on features such as transaction amount, location, and time.  
- **Regression Example:** Predicting weather temperature based on historical data. The goal is to predict the temperature for a given day based on features such as humidity, sunlight, wind speed, and atmospheric pressure.

---

# 2A. Classification Algorithms

## a. Logistic Regression
**How it works:**  
Models the probability that a data point belongs to a particular class using the logistic function (sigmoid function). This is an S-shaped curve that maps any real-valued number to a value between 0 and 1. It takes input features and calculates a value between 0 and 1 representing class membership probability. If probability > 0.5 then it predicts class 1 else class 0.  

**Use cases:**  
Commonly used in binary classification problems such as predicting likelihood of a disease based on patient data.  

**Main advantages:**  
Simple to implement and interpret, works well for linearly separable data.  

**Limitations:**  
Works best when the relationship between input features and output is linear, may struggle with complex relationships.  

---

## b. Decision Tree
**How it works:**  
Asks a series of simple yes/no questions based on input features to split the data into subsets. This process is repeated until a stopping criterion is met, such as reaching a maximum tree depth or having a minimum number of samples in a leaf node. It is easy to interpret and visualize, as the tree structure clearly shows the decision-making process.  

**Use cases:**  
Used in credit scoring to decide whether a loan should be approved or rejected, based on input features such as income, credit history, and loan amount.  

**Main advantages:**  
Easy to understand and interpret, you can visualize the decision path clearly.  

**Limitations:**  
Prone to overfitting, especially when the tree is deep and complex. May not perform well on small datasets.  

---

## c. Random Forest
**How it works:**  
Builds many decision trees, each using random samples of data and features. Each tree makes a prediction, then the model combines these predictions to get the final result. This reduces the risk of one tree's mistakes affecting the overall prediction.  

**Use cases:**  
Commonly used in binary classification problems such as predicting likelihood of a disease based on patient data.  

**Main advantages:**  
More accurate and robust than individual decision trees, since it reduces overfitting by averaging multiple trees.  

**Limitations:**  
Less interpretable than a single decision tree, as it is harder to visualize and understand the combined decision-making process.  

---

# 2B. Extended Task – Research Another Algorithm

**Algorithm:** Support Vector Machine (SVM)  

**What problem it is good for:**  
SVM is a good algorithm for both binary and multi-class classification problems, where you want to separate classes with a clear margin.  

**How it works:**  
SVM finds the best boundary called a hyperplane that separates different classes with the maximum margin, meaning the biggest gap between the closest data points of each class.  

**Real-life example:**  
SVM is used in handwriting recognition, where the goal is to classify handwritten characters into different categories based on their features.  

**Strengths:**
- Can work well even if you don't have a lot of training data  
- Works well even when you have many features  
- Usually doesn't get tricked by noise or small mistakes in your data  

**Weaknesses:**
- Can be slow to train on large datasets  
- Not very easy to understand how it makes decisions  
- Needs data to be scaled or normalized for best results  

---

# 3. Classification Metrics

## Accuracy
Measures the overall correctness of the model by calculating the ratio of correct predictions (both true positives and true negatives) to the total number of predictions made. It is a good metric when the classes are balanced.  
**Example:** If the model correctly identified 90 out of 100 tumors as malignant or benign, accuracy is 90%.  

---

## Precision
Measures the accuracy of positive predictions by calculating the ratio of true positives to the total number of positive predictions (true positives + false positives). It is important when the cost of false positives is high.  
**Example:** If the model predicted 40 tumors as malignant and 36 truly were malignant, precision is 36/40 = 90%.  

---

## Recall
Measures the ability of the model to identify all malignant tumors by calculating the ratio of true positives to the total number of actual positive cases (true positives + false negatives). It is important when the cost of false negatives is high.  
**Example:** If there were 50 malignant tumors total and the model found 36, recall is 36/50 = 72%.  

---

## F1-score
Measures the balance between precision and recall by calculating the harmonic mean of the two metrics. Useful when you need to balance precision and recall, especially in cases of imbalanced classes.  
**Example:** If the model has a precision of 90% and a recall of 72%, the F1-score is:  F1 = 2 * (0.9 * 0.72) / (0.9 + 0.72) = 0.8 or 80%

---

## Confusion Matrix
A table that summarizes the performance of a classification model by showing the counts of true positives, true negatives, false positives, and false negatives.  

**Example:**  

|                  | Predicted Malignant | Predicted Benign |
|------------------|----------------------|------------------|
| Actual Malignant | 36 (TP)             | 4 (FN)           |
| Actual Benign    | 14 (FP)             | 46 (TN)          |

In this example, the model correctly predicted 36 malignant tumors (true positives) and 46 benign tumors (true negatives), but it also incorrectly predicted 14 benign tumors as malignant (false positives) and missed 4 malignant tumors (false negatives).

---

# 4. Imbalanced Data Problem

**Definition:**  
Imbalanced data in classification tasks means some classes have many more samples than others.  
**Example:** In medical test dataset, 95% of the cases might be tumors that are benign, while only 5% are malignant. This can cause problems because the model might just learn to always predict the majority class (benign) and ignore the minority class (malignant), leading to poor performance on the important class.  

**Why can accuracy be misleading?**  
Accuracy measures the overall percentage of correct predictions, so if dataset is dominated by one class, a model can achieve high accuracy by always predicting the majority class.  
**Example:** If 95 out of 100 tumors are benign, predicting "benign" all the time gives 95% accuracy, even if the model never identifies malignant tumors.  

**More reliable metrics:**  
- **Precision:** Focus on how accurate positive predictions are, important when false positives matter.  
- **Recall:** Shows how well the model finds all actual positive cases, crucial when missing positive cases is costly.  
- **F1-score:** Balances precision and recall into one score, useful when both false positives and false negatives are critical.  
- **Confusion Matrix:** Provides detailed insight into all prediction types (correct, incorrect) to understand errors correctly.  

---

# 5. Real-World Case Study: Predicting Breast Cancer Using Supervised Machine Learning

**Goal:**  
To compare the performance of multiple supervised machine learning algorithms in classifying breast tumors as benign or malignant using the Wisconsin Breast Cancer Dataset. The aim was to identify which model provides the best diagnostic accuracy.  

**Data Used:**  
The Wisconsin Breast Cancer Dataset (WBCD), which contains features extracted from digitized images of fine needle aspirate (FNA) of breast masses. It includes measurements such as radius, texture, perimeter, area, smoothness, compactness, and class labels (benign or malignant).  

**Classification models applied:**  
- Random Forest  
- Logistic Regression  
- Support Vector Machine (SVM)  
- Neural Networks  

**Key Results:**  
- Random Forest showed the highest classification accuracy among all tested models.  
- Logistic Regression and SVM also performed well with comparable accuracy rates.  
- Neural Networks provided strong performance but required more tuning and computational resources.  
- The study confirmed that machine learning can effectively support breast cancer diagnosis with high accuracy, which can assist in early detection and treatment planning.  

**Reference:**  
Aamir, S., et al. (2022). *Predicting Breast Cancer Leveraging Supervised Machine Learning: A Comparative Study on Wisconsin Breast Cancer Dataset.* NCBI PMC. Available at: (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9398810/)
