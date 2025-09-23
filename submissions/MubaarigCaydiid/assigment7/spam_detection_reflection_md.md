# Spam Detection Reflection Paper

## 1. What did you implement?
I implemented a spam detection system that identifies whether a message is spam or not. I used three algorithms: Logistic Regression, Random Forest, and Naive Bayes to compare their performance in detecting spam and ham messages. The goal was to determine which model performs better in classifying messages correctly.

## 2. Briefly describe how you used the models

- **Logistic Regression (LR):** Predicts the probability of a message being spam or ham using a linear combination of features.
- **Random Forest (RF):** Uses multiple decision trees to make a final prediction. It reduces overfitting and provides robust and accurate predictions.
- **Naive Bayes (NB):** A probabilistic classifier based on Bayes Theorem. It assumes features are independent and predicts the category of a message based on the probabilities of its words.

## 3. Comparison of Models

**Single Message Check:**

| Actual | Logistic Regression | Random Forest | Naive Bayes |
|--------|-------------------|---------------|-------------|
| Spam (0) | Spam (1) | Spam (0) | Ham (0) |

The models gave different predictions. Random Forest performed best because its prediction was closest to the actual label, outperforming Logistic Regression and Naive Bayes in prediction accuracy.

## 4. Understanding Naive Bayes

- **What is Naive Bayes?**
  Naive Bayes is a simple probabilistic classifier that uses Bayes Theorem. It predicts the probability of a category for a message while assuming that all features (words) are independent.

- **Why is it often used in spam detection?**
  Naive Bayes is simple, fast, and effective for classifying emails and SMS messages without putting a heavy load on the computer.

- **Advantages:**
  - Easy to use and implement.
  - Works well with large text datasets.
  - Provides good predictions with minimal computation.

- **Limitations:**
  - Assumes that features are independent, which is not always true.
  - Sometimes less accurate than Random Forest or Logistic Regression.
  - Does not capture relationships between words in a message.

## 5. Metrics Discussion

- **Accuracy:** Random Forest performed best, providing better overall predictions compared to Logistic Regression and Naive Bayes.
- **Precision:** Random Forest achieved higher precision, meaning it correctly identified more spam messages.
- **Recall:** Random Forest also had the best recall, detecting spam messages more effectively.
- **F1-Score:** Random Forest achieved the highest F1-Score as a balance between precision and recall.
- **Confusion Matrix:** Shows True Positives (TP), False Positives (FP), True Negatives (TN), and False Negatives (FN), helping to understand the model's errors in predicting spam and ham.

## 6. Findings

I recommend Random Forest for spam detection because it achieved the best results across multiple metrics: accuracy, precision, recall, and confusion matrix performance. While Naive Bayes is simple and Logistic Regression is interpretable, Random Forest provides the most reliable predictions for detecting spam messages.

**Thank you!**