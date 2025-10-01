# Part-B Reflection Paper 

## What did you implement?

### Briefly describe how you used Logistic Regression, Random Forest, and Naive Bayes to detect spam.

First i import the necessary libraries. Like pandas, numpy and sklearn which i imported the models and metrics from it.  
Then i loaded the dataset using pandas and checked the first few rows to understand its structure. I encoded the labels to convert 'spam' and 'ham' into numerical values (0 and 1 respectively) for easier processing.  
Then i split the dataset into features (X) and target (y) variables. Also i split the dataset into training and testing sets using train_test_split from sklearn.  
After that i vectorized the text data using TfidfVectorizer from sklearn. This converts the text data into numerical features that can be used by the models.  
Then i trained the models using the training data and predicted the labels for the test data using Logistic Regression, Random Forest, and Multinomial Naive Bayes classifiers from sklearn.  
After that i printed the performance of each model using accuracy, precision, recall, and F1-score metrics that helps me to understand the effectiveness of each model in detecting spam.  
Then i printed the confusion matrix for each model to visualize the performance in terms of true positives, true negatives, false positives, and false negatives.  
Last but not least i performed a single sample sanity check by selecting a random message from the test set and predicting its label using all three models. This helped me to see how each model performs on an individual message level.

## 2. Comparison of Models:

### Compare the results of the 3 sanity check messages.

When i check three messages, the results are not different for each model. because if the actual label is spam then the model predicts spam and if the actual label is ham then the model predicts ham. So three models have the same results in single sample check. 

### Did all models agree? If not, which one gave more realistic predictions?

Yeah. All models agreed. Because if the actual label is spam then the model predicts spam and if the actual label is ham then the model predicts ham.

## 3. Understanding Naive Bayes:

### What is Naive Bayes?

Naive Bayes is a machine learning classification algorithm that predicts the category of a data point using probability. It is based on Bayes' theorem and assumes that the features are independent of each other.

### Why is it often used in spam detection?

Naive Bayes is often used in spam detection because it is simple to implement and easy to understand. It is also fast and can handle large datasets. And it works well with text data.

### What are its advantages and limitations?

#### Advantages:
- Simple and easy to implement
- Fast and scalable
- Works well with high-dimensional data
- Performs well even with small data
- Good probabilistic output

#### Limitations:
- Feature independence assumption
- Zero frequency problem
- Insensitive to feature correlation
- Assumes specific data distributions

## 4. Metrics Discussion:

### Which model had better Accuracy, Precision, Recall, F1-Score, and Confusion Matrix?

Random Forest Model is the best Accuracy, Recall, F1-Score, and Confusion Matrix. Naive Bayes Model is the second best model, where the Logistic Regression Model is the third one in terms of Accuracy, Recall, F1-Score, and Confusion Matrix. 

### What does the Confusion Matrix tell you about false positives and false negatives?

The confusion matrix tells me the false positives and false negatives. The false positives are the cases where the model predicts spam when the actual label is ham. The false negatives are the cases where the model predicts ham when the actual label is spam.

## 5. Your Findings

### Summarize in 1–2 paragraphs which model you would recommend for spam detection and why.

According to the results, i would recommend Random Forest Model for spam detection because it has the best Accuracy, Recall, F1-Score, and Confusion Matrix. And it is also simple to implement and easy to understand.  
Because the Random Forest Model has the best Accuracy, Recall, F1-Score, and Confusion Matrix, it is the best model for spam detection.
