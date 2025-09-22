# Comparison of the 3 Sanity Check Messages

## Message 1
**Text:** "FREE RINGTONE text FIRST to 87131 ..."  
**Actual:** Spam  

**Predictions:**  
- Logistic Regression → Spam  
- Random Forest → Ham  
- Naive Bayes → Spam  

**Observation:** Random Forest was too conservative and missed this obvious spam. Logistic Regression and Naive Bayes correctly detected it because they are more sensitive to spam keywords.

## Message 2
**Text:** "I'm wif him now buying tix lar..."  
**Actual:** Ham  

**Predictions:** All models predicted Ham  

**Observation:** All models agreed, correctly identifying a normal message.

## Message 3
**Text:** "No management puzzeles."  
**Actual:** Ham  

**Predictions:** All models predicted Ham  

**Observation:** Again, all models agreed.

## Conclusion
The models mostly agreed on normal messages (Ham). Differences appeared with obvious spam, where Random Forest was conservative and misclassified it as Ham. Naive Bayes and Logistic Regression gave more realistic predictions for spam detection because they quickly pick up on spam keywords.

---

# Understanding Naive Bayes

### 1. What is Naive Bayes?
Naive Bayes is a probabilistic machine learning algorithm based on Bayes’ Theorem.  
It calculates the probability that a message belongs to a certain class (spam or ham) based on the words it contains.  
The “naive” assumption is that all words are independent, which is not always true, but works well for text classification.

### 2. Why is it used in spam detection?
- Effective for text data; handles word frequencies and probabilities easily.  
- Fast, detects spam keywords like "FREE", "WIN", or "PRIZE".  
- Works reasonably even with limited data; popular in email and SMS spam filtering.

### 3. Advantages and Limitations

**Advantages**  
- Simple and easy to implement.  
- Works well with large text datasets.  
- Fast to train and predict.  
- Handles many features efficiently.

**Limitations**  
- Assumes word independence, often not true in real language.  
- May misclassify messages where context matters more than keywords.  
- Less accurate for very complex patterns compared to Random Forest or Neural Networks.

---

# Metrics Discussion

## Model Comparison

| Model               | Accuracy | Precision | Recall | F1-Score |
|--------------------|----------|-----------|--------|----------|
| Logistic Regression | 0.968    | 1.000     | 0.758  | 0.863    |
| Random Forest       | 0.983    | 1.000     | 0.872  | 0.932    |
| Naive Bayes         | 0.977    | 1.000     | 0.826  | 0.904    |

**Observations:**  
- Accuracy: Random Forest slightly better (0.983).  
- Precision: All models perfect (1.000), no Ham misclassified as Spam.  
- Recall: Random Forest highest (0.872), Logistic Regression lowest (0.758).  
- F1-Score: Random Forest highest (0.932), best balance between Precision and Recall.

---

# Confusion Matrix

|                | Predicted Ham | Predicted Spam |
|----------------|---------------|----------------|
| Actual Ham     | True Negative | False Positive |
| Actual Spam    | False Negative| True Positive  |

- False Positives (FP): Ham misclassified as Spam. All models had 0 FP.  
- False Negatives (FN): Spam misclassified as Ham. Logistic Regression had the most FN.

---

# Conclusion

Random Forest had the best overall performance due to higher Recall and F1-Score, while all models avoided false alarms.  

Random Forest correctly identified the most spam messages compared to Logistic Regression and Naive Bayes, providing a good balance between not mislabeling normal messages and catching spam.  

Logistic Regression and Naive Bayes are fast and simple but may miss spam in borderline cases. Random Forest captures complex patterns better, making it the recommended model for practical spam detection.
