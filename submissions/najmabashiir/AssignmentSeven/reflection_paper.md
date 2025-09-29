# 📄 Reflection Paper — Spam Detection (Lesson 7)

## 1. What did you implement?

I built a **spam detection system** using three classifiers: **Logistic Regression, Random Forest, and Naive Bayes**.  
The dataset contained email messages with labels `spam (0)` and `ham (1)`. Messages were converted into **TF-IDF features**, and each model was trained and tested on an 80/20 split.  
Performance was measured using **Accuracy, Precision, Recall, F1-Score, and Confusion Matrices**.  

---

## 2. Comparison of Models — Sanity Checks

Example message tested:  

```
FREE RINGTONE text FIRST to 87131 for a poly or text GET to 87131 for a true tone! ...
```

- **Actual:** Spam (0)  
- **Logistic Regression:** Spam (0)  
- **Random Forest:** Spam (0)  
- **Naive Bayes:** Spam (0)  

📌 All three models agreed and correctly identified this as spam.  
This shows that even simple spam messages with obvious keywords are reliably caught.  

---

## 3. Understanding Naive Bayes

- **What it is:** Naive Bayes is a probabilistic model based on **Bayes’ Theorem**, assuming features (words) are conditionally independent given the class.  
- **Why used for spam:** Spam detection works well with **word frequencies** (e.g., “free”, “win”, “prize”). Naive Bayes handles text data efficiently.  
- **Advantages:** Very fast, low memory use, good for high-dimensional text.  
- **Limitations:** Assumes independence between words, which is unrealistic; may misclassify when word context matters.  

---

## 4. Metrics Discussion (using my results)

### Logistic Regression Performance
- Accuracy: **0.968**  
- Precision: **1.000**  
- Recall: **0.758**  
- F1-Score: **0.863**  

Confusion Matrix:
- Ham: 966/966 correct, **0 false alarms**  
- Spam: 113 caught, **36 missed** (false negatives)  

---

### Random Forest Performance
- Accuracy: **0.983**  
- Precision: **1.000**  
- Recall: **0.872**  
- F1-Score: **0.932**  

Confusion Matrix:
- Ham: 966/966 correct, **0 false alarms**  
- Spam: 130 caught, **19 missed** (fewest false negatives)  

---

### Naive Bayes Performance
- Accuracy: **0.977**  
- Precision: **1.000**  
- Recall: **0.826**  
- F1-Score: **0.904**  

Confusion Matrix:
- Ham: 966/966 correct, **0 false alarms**  
- Spam: 123 caught, **26 missed**  

---

### Interpretation
- **Precision = 1.0** for all models → none of them wrongly flagged ham as spam (no false positives).  
- Models differ mainly in **Recall** (how much spam they catch):  
  - Logistic Regression missed **36 spam** (lowest Recall).  
  - Naive Bayes missed **26 spam**.  
  - Random Forest missed only **19 spam** (highest Recall).  

---

## 5. Findings

- **Random Forest** was the best overall: highest Accuracy (0.983), Recall (0.872), and F1-Score (0.932). It caught the most spam while never mislabeling ham.  
- **Naive Bayes** was a strong and efficient baseline, better than Logistic Regression on Recall, but slightly behind Random Forest.  
- **Logistic Regression** was simplest and interpretable but missed the most spam (Recall 0.758).  

👉 **Recommendation:** Use **Random Forest** for spam detection since it balances accuracy and recall best, while keeping precision perfect. Naive Bayes can serve as a fast backup, and Logistic Regression as a baseline model.  

---
