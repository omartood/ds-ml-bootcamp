# 📘 Lesson 7 – Assignment - Spam detection using Logistic Regression, Random Forest, and Naive bayes.

## 1.  **what did you implement?**
i implemented a spam detection using tree different machine learning models: **Logistic Regression**,
**Random Forest**, and **Naive Bayes**.the dataset was transformed into numerical Features using TF-IDF (Term Frequency–Inverse Document Frequency). the models were trained to distinguish between spam and ham messages.

and the process has several key steps common to all tree models:

- **Data Preprocessing:** The dataset was split into training and testing sets, and the text data was transformed into numerical features using TF-IDF.

- **Model Training:** The models were trained on the training data using the fit() method.

- **Model Evaluation:** The models were evaluated on the testing data using the score() method.

- **feature extraction(Vectorization):** The cleaned text was then converted into a numerical format that the models could understand. I used a technique called CountVectorizer, which transforms the text into a "bag of words." This means it creates a vocabulary of all unique words in the dataset and then counts the frequency of each word in every message. The resulting matrix of word counts became the input for my models 

- **Logistic Regression:** A linear classifier that uses a logistic function to model the relationship between the input features and the target variable.

- **Random Forest:** A meta estimator that fits a number of decision tree classifiers on various subsets of the dataset and uses averaging to improve the predictive accuracy of the model.

- **Naive Bayes:** A simple and effective classifier that assumes that the features are conditionally independent given the class label.
 
 ## 2. **Comparison of Models:**


**How predictions differed:** 
- When testing on a single row from the test set, the Logistic Regression prediction and the Random Forest prediction were both close to the actual label, but usually not exactly the same.
- The Naive Bayes prediction was often different from the actual label, often indicating a false positive or false negative.
- In general, the Naive Bayes model had the lowest accuracy, followed by the Random Forest model, and then the Logistic Regression model.

**Reasons for the differences:** 
- The Naive Bayes model assumes that the features are conditionally independent given the class label, which may not be true in the case of spam detection.
- The Random Forest model is a meta estimator that fits a number of decision tree classifiers on various subsets of the dataset and uses averaging to improve the predictive accuracy of the model.
- The Logistic Regression model is a linear classifier that uses a logistic function to model the relationship between the input features and the target variable.

###  **Which model gave more realistic results and why**:

Random Forest gave more realistic results for this single row.

**Reason:**
- Random Forest averages predictions from multiple decision trees, which helps it capture complex, non-linear relationships in the data.
- The Random Forest model is a meta estimator that fits a number of decision tree classifiers on various subsets of the dataset and uses averaging to improve the predictive accuracy of the model.

 ## 3. **Understanding Naive Bayes:**

**What is Naive Bayes?**

Naive Bayes is a simple and effective classifier that assumes that the features are conditionally independent given the class label.

**Why is it often used in spam detection?**

Naive Bayes is often used in spam detection because it is a simple and effective classifier that assumes that the features are conditionally independent given the class label.

- **Advantages:**
- Naive Bayes is a simple and effective classifier that assumes that the features are conditionally independent given the class label.
- It is often used in spam detection because it is a simple and effective classifier that assumes that the features are conditionally independent given the class label.

- **Limitations:**
- Naive Bayes is a simple and effective classifier that assumes that the features are conditionally independent given the class label.
- It is often used in spam detection because it is a simple and effective classifier that assumes that the features are conditionally independent given the class label.


#### 4. **What does the Confusion Matrix tell you about false positives and false negatives**:    

The Confusion Matrix tells us about false positives and false negatives.

**False Positives:**    
- False positives occur when the model predicts a positive label for a negative example.
- These are cases where the model incorrectly classifies a non-spam message as spam.

**False Negatives:**    
- False negatives occur when the model predicts a negative label for a positive example.
- These are cases where the model incorrectly classifies a spam message as non-spam.  

## 5. **Your Findings**:  

**Which model you would recommend for spam detection and why**: 

I would recommend the Random Forest model for spam detection because it has the highest accuracy and is a good generalization of the data.

**Reason:**
- The Random Forest model is a meta estimator that fits a number of decision tree classifiers on various subsets of the dataset and uses averaging to improve the predictive accuracy of the model.
- The Random Forest model is a good generalization of the data, as it captures complex, non-linear relationships in the data.

