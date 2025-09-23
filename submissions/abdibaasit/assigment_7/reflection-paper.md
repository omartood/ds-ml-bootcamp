# Reflection Paper – Spam Detection

## What I Implemented

I built a spam detection system using **Logistic Regression (LR)**, **Random Forest (RF)**, and **Naive Bayes (NB)**.  
The dataset consisted of text messages labeled as either **spam (0)** or **ham (1)**.  

Data preparation involved **TF-IDF Vectorizer** to convert words into numbers, then training the three models to predict spam.

---

## Model Comparison (Sanity Check)

| Message | True Label | LR | RF | NB |
|---------|-----------|----|----|----|
| FREE RINGTONE text FIRST to 87131… | Spam | Spam | Spam | Spam |
| Crazy ar he’s married. Ü like gd looking guys… | Ham | Ham | Ham | Ham |
| Hey now am free you can call me. | Ham | Ham | Ham | Ham |

All three models correctly classified the messages.

---

## Understanding Naive Bayes

Naive Bayes is a **probability-based algorithm** assuming each word is independent.  

**Why it's good for spam detection:** Spam often contains repeated keywords like `"free"`, `"win"`, `"congratulations"`. Naive Bayes can detect these patterns quickly.

**Advantages:** Fast, simple, effective on small data  
**Limitations:** Less accurate with complex word patterns

---

## Metrics Discussion

### Logistic Regression

| Metric    | Value |
|-----------|-------|
| Accuracy  | 0.968 |
| Precision | 1.000 |
| Recall    | 0.758 |
| F1-Score  | 0.863 |

**Confusion Matrix:**

|           | Pred Ham | Pred Spam |
|-----------|----------|-----------|
| Actual Ham| 966      | 0         |
| Actual Spam| 36      | 113       |

---

### Random Forest

| Metric    | Value |
|-----------|-------|
| Accuracy  | 0.983 |
| Precision | 1.000 |
| Recall    | 0.872 |
| F1-Score  | 0.932 |

**Confusion Matrix:**

|           | Pred Ham | Pred Spam |
|-----------|----------|-----------|
| Actual Ham| 966      | 0         |
| Actual Spam| 19      | 130       |

---

### Naive Bayes

| Metric    | Value |
|-----------|-------|
| Accuracy  | 0.977 |
| Precision | 1.000 |
| Recall    | 0.826 |
| F1-Score  | 0.904 |

**Confusion Matrix:**

|           | Pred Ham | Pred Spam |
|-----------|----------|-----------|
| Actual Ham| 966      | 0         |
| Actual Spam| 26      | 123       |

---

## Key Takeaways

- All three models had **perfect precision** (no ham marked as spam).  
- Recall differences:  
  - LR: 0.758  
  - NB: 0.826  
  - RF: 0.872  
- Random Forest performed best overall, especially in detecting spam messages.

---

## My Findings

All three models performed well, but **Random Forest** was the best.  
It had the highest recall and F1-score, meaning it detected more spam while still avoiding mistakes.  
**Logistic Regression** was simpler but weaker at detecting spam.  
**Naive Bayes** was fast and strong but not as accurate as Random Forest.  

**Final choice:** Random Forest, because it provides the most balanced and realistic results for spam detection.
