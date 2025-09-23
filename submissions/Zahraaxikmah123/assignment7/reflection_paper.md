# Reflection Paper – Spam Detection with Logistic Regression, Random Forest & Naive Bayes

**Author:** Saara Iidle  
**Assignment:** 6 – Spam Detection Comparison

---

## 1. What did you implement?

In this project, I implemented a spam detection system using three different machine learning models: Logistic Regression, Random Forest, and Naive Bayes (MultinomialNB). I started by loading and cleaning the dataset, which contains SMS messages labeled as either "spam" or "ham". I handled missing values, encoded the labels (spam = 0, ham = 1), and split the data into features (messages) and target (category). The data was then divided into training (80%) and testing (20%) sets. I used TfidfVectorizer to convert the text messages into numerical features suitable for machine learning models. Each model was trained on the training data and evaluated on the test data using accuracy, precision, recall, F1-score, and confusion matrix. Finally, I performed single-message predictions to compare how each model classifies example messages.

---

## 2. Comparison of Models: Sanity Check Results

For the three sample messages:

1. **"Free entry in 2 a weekly competition!"**  
   - Logistic Regression: Ham  
   - Random Forest: Ham  
   - Naive Bayes: Spam  
   - **Most realistic:** Naive Bayes (this message is typical spam).

2. **"I will meet you at the cafe tomorrow"**  
   - All models: Ham  
   - **All correct:** This is a normal message.

3. **"Congratulations, you won a free ticket"**  
   - All models: Ham  
   - **Not realistic:** This is likely spam, but all models predicted ham.

4. **"You have been selected for a $1000 gift card. Claim now!"**  
   - All models: Spam  
   - **All correct:** This is a clear spam message.

**Summary:**  
Naive Bayes was the only model to correctly identify the first spam message, while all models correctly classified the obvious ham and spam examples. However, all models missed the third message, which is also typical spam. This shows that while the models are generally good, they can still miss some spam messages, especially those that are less obvious.

---

## 3. Understanding Naive Bayes

**What is Naive Bayes?**  
Naive Bayes is a probabilistic machine learning algorithm based on Bayes’ Theorem. It assumes that all features (in this case, words in a message) are independent of each other given the class label. Despite this "naive" assumption, it works surprisingly well for text classification tasks.

**Why is it often used in spam detection?**  
Naive Bayes is popular for spam detection because it is fast, simple, and effective with high-dimensional data like text. It can quickly learn from word frequencies and is not computationally expensive, making it suitable for real-time filtering.

**Advantages:**  
- Very fast to train and predict.
- Works well with large and high-dimensional datasets.
- Simple to implement and interpret.

**Limitations:**  
- The independence assumption is rarely true in real text, which can reduce accuracy.
- Can struggle when features (words) are highly correlated or when spam messages use new tricks.

---

## 4. Metrics Discussion

**Which model had better metrics?**  
- **Random Forest** had the highest overall accuracy (0.98), recall (0.87), and F1-score (0.93).
- **Logistic Regression** had high precision (1.0) but lower recall (0.76), meaning it missed more spam messages.
- **Naive Bayes** performed well, with accuracy (0.97) and recall (0.82), but slightly lower than Random Forest.

**Confusion Matrix Insights:**  
- All models had perfect precision (no false positives for spam), but recall varied.
- Random Forest had the fewest false negatives (missed spam), followed by Naive Bayes, then Logistic Regression.
- The confusion matrix shows that Random Forest is best at catching spam without misclassifying ham.

---

## 5. My Findings and Recommendation

Based on my results, I would recommend using the **Random Forest** model for spam detection in this dataset. It achieved the highest accuracy, recall, and F1-score, and its confusion matrix shows it misses fewer spam messages compared to the other models. While Naive Bayes is fast and did well on some tricky spam messages, Random Forest is more robust overall. Logistic Regression is simple and precise but less effective at catching all spam.

In summary, Random Forest provides the best balance between catching spam and avoiding false alarms. However, in real-world applications, it is important to keep updating the models and possibly combine them for even better performance.