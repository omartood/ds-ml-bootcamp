# Reflection Paper – Spam Detection Models

## 1. What Did I Implement?

In this project, I implemented three classification models—**Logistic Regression, Random Forest, and Naive Bayes**—to detect spam messages.  

- The text messages were first converted into **TF–IDF features**, which measure the importance of each word.  
- Next, the models were trained using the training dataset and evaluated on the test dataset.  
- Finally, I compared the models using **performance metrics** (Accuracy, Precision, Recall, F1-Score, Confusion Matrix) and conducted **three sanity checks** on individual messages.  

---

## 2. Comparison of Models on Sanity Checks

Here are the results of the three sanity checks:

| Index | Text Snippet | Actual | Logistic Regression | Random Forest | Naive Bayes |
|-------|--------------|--------|---------------------|---------------|-------------|
| 8     | Dear good morning now only i am up | Ham (1) | Ham (1) | Ham (1) | Ham (1) |
| 1091  | FREE POLYPHONIC RINGTONE... | Spam (0) | Spam (0) | Spam (0) | Spam (0) |
| 1081  | Email AlertFrom: Low-cost prescripiton drugs... | Spam (0) | Ham (1) ❌ | Ham (1) ❌ | Ham (1) ❌ |

### Analysis
- All models correctly classified the first two messages.  
- For the third message (Index 1081), **all three models failed**, predicting Ham instead of Spam.  
- This suggests that messages with disguised spam wording remain a challenge for all models.  

---

## 3. Understanding Naive Bayes

- **What is Naive Bayes?**  
  A probabilistic algorithm based on **Bayes’ Theorem**. It assumes that all features (words) are independent given the class label.  

- **Why use it in spam detection?**  
  It is **fast, efficient, and effective** with high-dimensional text data. Each word contributes probability toward spam or ham classification, which suits spam filtering well.  

- **Advantages:**  
  - Works well on large and sparse text data.  
  - Simple to implement and computationally efficient.  
  - Requires less training data than complex models.  

- **Limitations:**  
  - The independence assumption is rarely true in natural text.  
  - May misclassify disguised spam messages.  
  - Less flexible compared to ensemble models like Random Forest.  

---

## 4. Metrics Discussion

### Performance Summary

| Model                | Accuracy | Precision | Recall | F1-Score |
|-----------------------|----------|-----------|--------|----------|
| Logistic Regression   | 0.968    | 1.000     | 0.758  | 0.863    |
| Random Forest         | 0.983    | 1.000     | 0.872  | 0.932    |
| Naive Bayes           | 0.977    | 1.000     | 0.826  | 0.904    |

### Confusion Matrices (side by side)

|                     | **Pred: Ham (1)** | **Pred: Spam (0)** |
|---------------------|-------------------|--------------------|
| **Logistic Regression – Actual Ham (1)** | 966 | 0 |
| **Logistic Regression – Actual Spam (0)** | 36 | 113 |
| **Random Forest – Actual Ham (1)** | 966 | 0 |
| **Random Forest – Actual Spam (0)** | 19 | 130 |
| **Naive Bayes – Actual Ham (1)** | 966 | 0 |
| **Naive Bayes – Actual Spam (0)** | 26 | 123 |

---

### Interpretation
- **Random Forest** had the highest accuracy (0.983) and recall (0.872).  
- **Naive Bayes** performed slightly worse but still good (recall 0.826).  
- **Logistic Regression** missed the most spam (recall 0.758).  
- None of the models produced false positives (no Ham misclassified as Spam).  

---

## 5. Findings and Recommendation

Overall, all three models are effective, but **Random Forest** performed best across most metrics:  
- It caught the most spam (highest recall).  
- It balanced accuracy and F1-score better than the others.  
- It produced **zero false positives** (did not mislabel Ham as Spam).  

While Naive Bayes is attractive for its simplicity and Logistic Regression is solid, the **Random Forest** model is the most reliable for spam detection in this project.  

**Recommendation:** Deploy **Random Forest** as the main model for spam detection, with Naive Bayes as a lightweight alternative when speed or simplicity is prioritized.  
