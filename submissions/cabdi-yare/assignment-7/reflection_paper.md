# Reflection Paper – Spam Detection Project

## Part B – Reflection

### 1. What Did I Implement?
For this assignment, I created a spam detection system to classify messages as either *Spam* or *Ham. I used three models: **Logistic Regression, **Random Forest, and **Naive Bayes. I converted the text messages into numbers using **TF-IDF* so that the models could understand the content and make predictions.

---

### 2. Comparison of Models
I tested how well each model worked using *Accuracy, Precision, Recall, and F1-Score*. Here is a summary:

| Model               | Accuracy | Precision | Recall | F1-Score |
|--------------------|---------|----------|--------|----------|
| Logistic Regression | 0.96    | 0.95     | 0.94   | 0.94     |
| Random Forest       | 0.97    | 0.96     | 0.95   | 0.95     |
| Naive Bayes         | 0.94    | 0.93     | 0.92   | 0.92     |

*Manual Test Messages:*

1. "Free entry in 2 a weekly competition!" → *Spam* (All models agreed)  
2. "I will meet you at the cafe tomorrow" → *Ham* (All models agreed)  
3. "Congratulations, you won a free ticket" → *Spam* (All models agreed)  

*Observation:* Random Forest produced slightly more consistent predictions compared to the other two models.

---

### 3. Understanding Naive Bayes
Naive Bayes is a probabilistic model that classifies data based on the likelihood of features appearing in each class. It assumes that all words (features) are independent from each other.

*Advantages:*
- Very fast and efficient, even with large datasets
- Works well with text classification tasks like spam detection
- Performs surprisingly well even with limited training data

*Limitations:*
- The independence assumption is rarely true for natural language, which can affect accuracy
- May underperform compared to more complex models when word relationships are important

Despite these limitations, Naive Bayes is a popular choice for spam detection because of its simplicity and speed.

---

### 4. Metrics Discussion
The evaluation metrics helped me understand how well each model performed:

- *Accuracy:* Random Forest scored the highest (*97%*), measuring the overall percentage of correct predictions.  
- *Precision:* Showed how many of the predicted spam messages were truly spam. Random Forest and Logistic Regression had high precision, producing fewer false spam alerts.  
- *Recall:* Measured how many actual spam messages were correctly identified. Random Forest performed best, missing fewer spam messages.  
- *F1-Score:* Combined Precision and Recall into one metric. Random Forest achieved the highest F1-Score (*0.95*), making it the most reliable model overall.

The confusion matrices revealed where the models made mistakes:  
- *False Positives (FP):* Ham messages incorrectly labeled as Spam (inconvenient for users)  
- *False Negatives (FN):* Spam messages incorrectly labeled as Ham (more serious as spam reaches the inbox)  

Random Forest had fewer false positives and false negatives than the other models, which explains its superior performance.

---

### 5. Findings and Recommendation
Based on the tests, I would recommend using *Random Forest* for spam detection. It gave the best overall results and separated spam from ham most accurately. Logistic Regression is also a good option for simpler or faster setups. Naive Bayes is useful for speed but was slightly less accurate on this dataset.