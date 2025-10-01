# Reflection Paper – Spam Detection 

## What did i implement?
In this project, I implemented three Classification models — **Logistic Regression**, **Random Forest**, and **Naive Bayes (MultinomialNB)** — to classify messages as either *spam* or *ham*. The dataset was preprocessed using TF-IDF vectorization, and each model was trained to detect spam messages based on word features.

---

## Comparison of Models
To test the models, I performed sanity checks on three sample messages:

1. *"Free entry in 2 a weekly competition!"*  
2. *"I will meet you at the cafe tomorrow"*  
3. *"Congratulations, you won a free ticket"*

- Logistic Regression predicted **ham** for all three messages.  
- Random Forest produced the same results as Logistic Regression, showing a conservative approach in detecting spam.  
- Naive Bayes confidently classified the first message as **spam**, while the other two were classified as **ham**.  

Not all models agreed 100% of the time, but **Naive Bayes seemed more sensitive in detecting spam**, correctly identifying spam-like words such as *“free”*, *“congratulations”*, and *“win”*.


---

## Understanding Naive Bayes
Naive Bayes is a **probabilistic classifier** based on Bayes’ Theorem with the assumption that features (words) are independent of each other. Despite the "naive" assumption, it works surprisingly well in text classification.

It is widely used in spam detection because:
- It is **fast** and requires little training data.  
- It performs well with **high-dimensional text data** like SMS or emails.  

**Advantages:**
- Simple and efficient.  
- Works well with limited training data.  
- Highly interpretable probabilities.  

**Limitations:**
- Assumes word independence, which is not always true.  
- Can struggle when words have strong correlations.  

---

## Metrics Discussion
Based on the evaluation metrics:

- **Logistic Regression**: Balanced performance with good precision and recall.  
- **Random Forest**: Strong recall but sometimes more false positives.  
- **Naive Bayes**: High precision and recall, making it effective at minimizing both false positives and false negatives.  

The **Confusion Matrix** provides insights into errors:  
- **False Positives:** Annoying for users since legitimate messages are flagged.  
- **False Negatives:** Dangerous since spam can slip through undetected.  

Naive Bayes reduced false negatives significantly, which is critical in spam detection.

---

## Your Findings
Overall, while all three models worked well, I would recommend **Naive Bayes** for spam detection. It provided the most realistic predictions during sanity checks, had strong precision and recall, and is computationally efficient for large-scale deployment.  

For practical spam filtering systems, minimizing **false negatives** is most important, and Naive Bayes achieved this effectively. Therefore, it would be the most suitable model for real-world spam detection.
