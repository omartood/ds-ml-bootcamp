# 📘 Lesson 6 – Assignment.
## Whats the  **classification** in Machine Learning?
# Objectives 
at the end of article you will learn the 
1. Definition Classification in ML 
2. types of **classification** in ML.
3. How is it **different from regression**?
4.  Classification Algorithms.
5. Classification Metrics.
6. whats the Imbalanced Data Problem. 

## **1. Introduction to Classification**
## 1) Introduction:
Classification teaches a machine to sort things into categories. It learns by looking at examples with labels (like emails marked "spam" or "not spam"). After learning, it can decide which category new items belong to, like identifying if a new email is spam or not.

## 2) What is Classification?
> **classification** is a type of supervised learning task where the goal is to predict a label (category or class) for given input data.
 **For example,** a classification model might be trained on dataset of images labeled as either dogs or cats and it can be used to predict the class of new and unseen images as dogs or cats based on their features such as color, texture and shape. 

###  How is it **different from regression**?
**Regression:** predicts numbers like price or something like that 
**Classification:**predicts category or class like this email is spam or not span, this person healthy or sick.

### **2A. Classification Algorithms**
1. ### **Logistic Regression:**
> **Logistic Regression** is a supervised machine learning algorithm for predicting the probability of a categorical outcome, most commonly a binary outcome (e.g., yes/no, spam/not spam), using input variables. 
- It  **works** by applying a logistic (sigmoid) function to a linear combination of the input features, transforming the output into a probability value between 0 and 1. This probability is then used to classify the input into one of the predefined categories. 
- **real-world use case** 
- **Medical Diagnosis* : predicting whether a patient has a disease or not(Yes/No) based on the test. 

##  Advantages

1.  **Simple & Easy to Implement**
    -   Straightforward to understand and interpret.
2.  **Computationally Efficient**
    -   Requires less computation compared to complex models like Neural
        Networks.
3.  **Works Well with Linearly Separable Data**
    -   Performs very well when classes can be separated by a straight
        line (binary case).
4.  **Outputs Probabilities**
    -   Unlike some classifiers, it gives probability scores (e.g., 70%
        chance of spam).
5.  **Regularization Support**
    -   Can use L1 (Lasso) or L2 (Ridge) regularization to avoid
        overfitting.
6.  **Baseline Model**
    -   Often used as a first step before trying more complex models.
##  Limitations

1.  **Linear Decision Boundary**
    -   Struggles with complex, non-linear relationships unless combined
        with feature engineering.
2.  **Sensitive to Outliers**
    -   Extreme values can distort the model significantly.
3.  **Requires Feature Scaling**
    -   Works better when features are normalized/standardized.
4.  **Not Great with Many Features**
    -   Performance degrades if dataset has too many irrelevant or
        highly correlated features.
5.  **Binary Focused**
    -   Naturally suited for binary classification; multi-class requires
        extensions (e.g., one-vs-rest, softmax).
6.  **Assumes Independence of Features**
    -   Doesn't handle multicollinearity (when features are highly
        correlated) well.

### 2. **Decision Trees:** 
 > **Decision Trees:** is a supervised machine learning algorithm that uses a tree-like structure to predict the outcome of a target variable through a series of "if-then-else" conditional statements.
- he **works:** a decision tree splits the dataset based on feature values to create pure subsets ideally all items in a group belong to the same class. Each leaf node of the tree corresponds to a class label and the internal nodes are feature-based decision points.

- **real-world use case:**
    -**weather* predicting whether it will be rainy, sunny or cloudy.  

##  Advantages

1.  **Easy to Understand & Interpret**
    -   Visual representation makes results intuitive (like a
        flowchart).
2.  **Handles Both Types of Data**
    -   Works with **numerical** and **categorical** features.
3.  **No Need for Feature Scaling**
    -   Unlike Logistic Regression or SVM, no
        normalization/standardization required.
4.  **Captures Non-Linear Relationships**
    -   Can model complex decision boundaries without transformation.
5.  **Feature Importance**
    -   Naturally provides which features are most important for
        prediction.
6.  **Can Handle Missing Values**
    -   Some implementations can split even with missing data.

## Limitations

1.  **Overfitting** 
    -   Trees can grow too deep and fit noise in the data. (Solution:
        pruning, max_depth).
2.  **Unstable**
    -   Small changes in data can result in a very different tree
        structure.
3.  **Biased Toward Features with More Levels**
    -   Attributes with many unique values may dominate splits.
4.  **Not Always the Most Accurate**
    -   Alone, decision trees often perform worse than ensemble methods
        (Random Forest, Gradient Boosting).
5.  **Piecewise Constant Predictions**
    -   In regression, predictions are constant within intervals, not
        smooth.

### 3. **Random Forest:** 
 > **Random Forest:** is a machine learning algorithm that uses many decision trees to make better predictions. Each tree looks at different random parts of the data and their results are combined by voting for classification or averaging for regression which makes it as ensemble learning technique. This helps in improving accuracy and reducing errors.

- **real-world use case:**
  -**Financial Markets* predicting stock price movement trends.


#  Advantages

1.  **High Accuracy**
    -   Outperforms single models like Decision Trees due to averaging
        of multiple trees.
2.  **Robust to Overfitting**
    -   Combining many trees reduces the risk of fitting noise in the
        data.
3.  **Handles Non-Linear Data**
    -   Works well with complex decision boundaries.
4.  **Works with Large Datasets**
    -   Scales well to high-dimensional and large datasets.
5.  **Handles Missing Values & Outliers**
    -   Can manage incomplete and noisy data fairly well.
6.  **Feature Importance**
    -   Provides a ranking of which features are most important in
        predictions.
7.  **Versatile**
    -   Can be used for **classification**, **regression**, and even
        **feature selection**.

##  Limitations

1.  **Less Interpretable**
    -   Unlike a single decision tree, Random Forests are like a "black
        box" and hard to visualize.
2.  **Computationally Expensive**
    -   Training and prediction take longer because many trees are
        built.
3.  **Memory-Intensive**
    -   Requires more storage and processing power, especially with
        large forests.
4.  **Not Always Necessary**
    -   For small datasets or simple problems, simpler models (Logistic
        Regression, Decision Tree) may perform just as well.
5.  **Slower Predictions**
    -   Especially problematic in real-time applications since
        predictions require aggregating results from many trees.


### **2B. Extended Task – Research Another Algorithm**
 #### **Support Vector Machines (SVMs):**
 >  *Support Vector Machines (SVMs)* is a supervised machine learning algorithm used for classification and regression tasks. 
 - It tries to find the best boundary known as hyperplane that separates different classes in the data. 
 it is useful when you want to do binary classification like spam or not .
 - the main goal of SVM is to maximize the margin between the two classes, the large the margin the better the model performs on new and unseen data.  
- **How does it work (the core idea)?**
 - The key idea behind the SVM algorithm is to find the hyperplane that best separates two classes by maximizing the margin between them. This margin is the distance from the hyperplane to the nearest data points (support vectors) on each side.
 - **Real World Example**
     - **Email Spam**
     -   **Problem**: Classify emails as **Spam** or **Not Spam**.\
     -   **Features (X)**:
    -   Frequency of keywords ("free," "win")\
    -   Number of links\
    -   Email length\
    -   Sender reputation\
     -   **SVM Process**:
    -   Finds the hyperplane that separates spam from non-spam emails in
        the feature space.\
     -   **Output**: Spam / Not Spam. 
- **What are its strengths and weaknesses compared to the algorithms in Section 2?**


| Feature | **SVM** | **Logistic Regression** | **Decision Tree** | **Random Forest** |
|---------|---------|------------------------|-----------------|-----------------|
| **Interpretability** | Low (black box) | High | High | Low |
| **Accuracy on complex boundaries** | High (especially with kernels) | Low (linear only) | Medium | High |
| **Handles high-dimensional data** | Excellent | Good | Poor | Good |
| **Overfitting risk** | Low to medium | Medium | High (if unpruned) | Low |
| **Computational cost** | High (especially large datasets) | Low | Low | High |
| **Handles non-linear data** | Yes (with kernel) | No | Yes | Yes |


### **3. Classification Metrics**
 **1. Accuracy** is a fundamental metric used for evaluating the performance of a classification model. 
 - It tells us the proportion of correct predictions made by the model out of all predictions.


 **2. Precision** It measures how many of the positive predictions made by the model are actually correct.
 -  It's useful when the cost of false positives is high such as in medical diagnoses where predicting a disease when it’s not present can have serious consequences.

 **3. Recall**  measures how many of the actual positive cases were correctly identified by the model. It is important when missing a positive case (false negative) is more costly than false positives.


 **4. F1-Score** is the harmonic mean of precision and recall. It is useful when we need a balance between precision and recall as it combines both into a single number. A high F1 score means the model performs well on both metrics. Its range is [0,1].
- It balances the trade-off between Precision (how many predicted positives are actually positive) and Recall (how many actual positives are correctly predicted).

 **5. Confusion Matrix**  is a table used to evaluate the performance of a classification model. It shows how many predictions were correct and how many were incorrect, broken down by each class.

 - It’s called “confusion” matrix because it shows where the model is confusing one class for another.

- **Comparison table***

| Metric             | Focus / Measures                               | When to Use                                           | Strengths                                           | Weaknesses                                         |
|-------------------|-----------------------------------------------|-----------------------------------------------------|---------------------------------------------------|---------------------------------------------------|
| **Accuracy**       | Overall correctness of the model              | When classes are balanced                            | Simple to understand                               | Misleading for imbalanced datasets               |
| **Precision**      | Correctness of positive predictions           | When false positives are costly                      | Reduces false positives                             | Ignores false negatives                           |
| **Recall**         | Ability to find all positive cases            | When false negatives are costly                      | Reduces false negatives                             | Ignores false positives                           |
| **F1-Score**       | Balance between precision and recall          | When dataset is imbalanced or both FP/FN matter     | Combines precision and recall in one metric        | Can be less intuitive than accuracy              |
| **Confusion Matrix** | Counts of TP, TN, FP, FN                     | To understand detailed prediction errors            | Provides complete view of model performance       | Harder to summarize with a single number        |


### **4. Imbalanced Data Problem**
#### 1. What is Imbalanced Data?
In classification tasks, **imbalanced data** occurs when the classes in the dataset are **not represented equally**. That is, one class (the majority class) has **many more samples** than another class (the minority class).  

**Example:**  
- Fraud detection: Only 1% of transactions are fraudulent, 99% are normal.  
- Medical diagnosis: Rare disease cases are far fewer than healthy cases.

In such cases, standard models tend to **favor the majority class**, ignoring the minority class.  

---

#### 2. Why Accuracy Can Be Misleading
Accuracy measures the ratio of **correct predictions to total predictions**:

```text
Accuracy = (TP + TN) / (TP + TN + FP + FN)
```

In imbalanced datasets, a model could **predict only the majority class** and still achieve **high accuracy**, even though it **fails to detect the minority class**.  

**Example:**  
- Dataset: 1000 samples (990 normal, 10 fraudulent).  
- Model predicts all as normal:  
  - Accuracy = 990 / 1000 = 99% ✅  
  - But it **detects 0 frauds**, which is practically useless ❌

Thus, accuracy **does not reflect the model’s ability to handle minority classes**.  

---

#### 3. More Reliable Metrics
When dealing with imbalanced data, **metrics that focus on the minority class performance** are preferred:

| Metric | What it measures | Why it’s useful |
|--------|-----------------|----------------|
| **Precision** | Proportion of predicted positives that are actually positive: TP / (TP + FP) | Tells how many predicted positive cases are correct; avoids false alarms. |
| **Recall (Sensitivity)** | Proportion of actual positives correctly predicted: TP / (TP + FN) | Measures the model’s ability to detect all positive cases; important for rare events. |
| **F1-Score** | Harmonic mean of Precision and Recall: 2*(Precision*Recall)/(Precision+Recall) | Balances Precision and Recall; useful when both false positives and false negatives matter. |
| **ROC-AUC** | Area under the Receiver Operating Characteristic curve | Evaluates model’s ability to distinguish between classes regardless of threshold. |

**Summary:**  
- **Accuracy** → can be misleading.  
- **Precision, Recall, F1-Score, ROC-AUC** → better reflect performance on **minority class**, which is often the focus in imbalanced problems.
### **5. Real-World Case Study**
#### **Case Study: Real-Time Credit Card Fraud Detection at JPMorgan Chase**

**Goal of the Project:**
JPMorgan Chase aimed to enhance its credit card fraud detection capabilities by implementing an AI-driven system to identify and prevent fraudulent transactions in real-time. The primary objective was to reduce credit card fraud incidents and associated financial losses.

**Data Used:**
The system utilized anonymized transaction data, including:
- Transaction amounts and timestamps
- Merchant details
- Customer behavioral patterns
- Device information and geolocation data

**Classification Model Applied:**
JPMorgan Chase employed machine learning algorithms, particularly focusing on behavioral biometrics and anomaly detection techniques. These models analyzed transaction patterns and customer behavior to identify deviations indicative of potential fraud.

**Key Results and Insights:**
- The AI system enabled real-time detection of fraudulent transactions, significantly reducing the time between transaction initiation and fraud identification.
- The implementation led to a substantial decrease in credit card fraud incidents, with reports indicating a reduction of up to 60% in fraud cases.
- The system's ability to analyze vast amounts of transaction data quickly allowed for proactive fraud prevention, minimizing financial losses and enhancing customer trust.

**Reference:**
- JPMorgan Chase & Co. Case Study on Fraud Detection. (2022). *AI in Financial Services: Real-Time Fraud Prevention*. Retrieved from [https://www.jpmorganchase.com](https://www.jpmorganchase.com)