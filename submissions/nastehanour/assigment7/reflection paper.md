# Reflection Paper – Spam Detection with Logistic Regression, Random Forest & Naive Bayes

---

## 1. What did you implement?

In this project, I implemented a spam detection system that classifies messages as either spam or ham. I used three machine learning algorithms: **Logistic Regression**, **Random Forest**, and **Naive Bayes (MultinomialNB)**. The process included:

- Loading and cleaning the dataset  
- Handling missing values  
- Encoding labels (spam = 0, ham = 1)  
- Splitting data into training (80%) and testing (20%) sets  
- Converting messages into TF-IDF features  
- Training the three models  
- Evaluating them with **accuracy, precision, recall, F1-score,** and **confusion matrix**  

I also performed **single-message predictions** to compare model behavior on specific examples.

---

## 2. Comparison of Models: Sanity Check Results

**For the sample messages:**

### "Free entry in 2 a weekly competition!"
- Logistic Regression: Ham  
- Random Forest: Ham  
- Naive Bayes: Spam  
- **Most realistic:** Naive Bayes  

### "I will meet you at the cafe tomorrow"
- All models: Ham  
- **All correct:** Normal message  

### "Congratulations, you won a free ticket"
- All models: Ham  
- **Not realistic:** Likely spam, misclassified by all  

### "You have been selected for a $1000 gift card. Claim now!"
- All models: Spam  
- **All correct:** Clear spam  

**Summary:**  
Naive Bayes correctly identified some less obvious spam messages. Random Forest had the highest overall accuracy, while Logistic Regression missed more spam messages. All models were consistent on obvious ham and spam.

---

## 3. Understanding Naive Bayes

**What is Naive Bayes?**  
Naive Bayes is a probabilistic classifier based on Bayes’ theorem. It assumes independence between features (words) and predicts the probability of a message being in a certain class.

**Why is it used in spam detection?**  
It is fast, simple, and effective for text classification. It works well with high-dimensional data, like SMS or email text, and can quickly process large datasets.

**Advantages:**
- Fast and easy to implement  
- Works well with large datasets  
- Good for real-time filtering  

**Limitations:**
- Assumes features are independent, which may not be true  
- May be less accurate than Random Forest on complex patterns  

---

## 4. Metrics Discussion

- **Accuracy:** Random Forest performed best (0.98), followed by Naive Bayes (0.97) and Logistic Regression (0.97).  
- **Precision:** All models had high precision, indicating few false positives.  
- **Recall:** Random Forest had the highest recall, catching more spam. Logistic Regression had lower recall (missed spam).  
- **F1-Score:** Random Forest highest, balancing precision and recall.  
- **Confusion Matrix:** Shows Random Forest had fewer false negatives (missed spam) than the other models.

---

## 5. Findings and Recommendation

Based on my results, **Random Forest** is the recommended model for spam detection. It achieves the highest accuracy, recall, and F1-score, and misses fewer spam messages. Naive Bayes is fast and effective for tricky messages, but Random Forest provides more reliable overall performance. Logistic Regression is interpretable and precise but less effective at catching all spam.

**Conclusion:**  
Random Forest offers the best balance between detecting spam and avoiding false alarms. In real-world applications, updating the models and combining them could further improve performance.
