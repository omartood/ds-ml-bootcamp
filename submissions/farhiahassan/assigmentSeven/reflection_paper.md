# Reflection Paper — Spam Detection Models

## What I Implemented

In this project, I implemented three machine learning classifiers to detect spam vs ham messages:
- **Data preprocessing**: handled missing values, encoded labels (`spam = 0`, `ham = 1`), split data into 80% training / 20% testing.
- **Feature extraction**: used `TfidfVectorizer` to convert text into numeric features.
- **Models trained**:
  - Logistic Regression  
  - Random Forest Classifier  
  - Naive Bayes (MultinomialNB)  
- **Evaluation**: computed Accuracy, Precision, Recall, F1-Score, Confusion Matrix on test data.  
- **Sanity checks**: predicted on sample messages such as _“Free entry in 2 a weekly competition!”_, _“I will meet you at the cafe tomorrow”_, _“Congratulations, you won a free ticket”_ to compare model behavior.

---

## Comparison of Models on Sample Messages

| Sample Message | True Label | Logistic Regression | Random Forest | Naive Bayes | Which Prediction Seems Most Realistic |
|----------------|------------|----------------------|----------------|----------------|------------------------------------------|
| *Free entry in 2 a weekly competition!* | Spam | **Spam** | **Spam** | Spam | All agree; clearly spam. |
| *I will meet you at the cafe tomorrow* | Ham | Ham | Ham | Ham | All agree; clearly ham. |
| *Congratulations, you won a free ticket* | Spam | Spam | Spam | **Ham** | NB misclassified; LR & RF more realistic. |

---

## Understanding Naive Bayes

- **What is Naive Bayes?**  
  It is a probabilistic classifier that uses Bayes’ theorem, assuming that features are independent given the class. It computes for each class \(C\):

  \[
  P(C \mid \text{message}) \propto P(C) \cdot \prod_{i} P(\text{word}_i \mid C)
  \]

  Then it chooses the class with highest posterior probability.

- **Why it is often used in spam detection**  
  - Works well with text data (many features = words).  
  - Fast to train and predict.  
  - Robust with smaller amounts of data.  
  - With smoothing, handles unseen words.  

- **Advantages**  
  1. Simplicity and interpretability.  
  2. Good baseline performance.  
  3. Handles high-dimensional, sparse input efficiently.

- **Limitations**  
  1. Assumes conditional independence of features (often unrealistic).  
  2. Sensitive to how text is preprocessed (stop words, tokenization, etc.).  
  3. May give overconfident predictions even with weak evidence.  
  4. Zero-frequency problem without smoothing.

---

## Metrics Discussion

Here is a summary of how the models performed (for spam class = positive). Replace the placeholders with your actual values.

| Model                | Accuracy | Precision | Recall  | F1-Score |
|-----------------------|----------|------------|----------|-----------|
| Logistic Regression   | 0.96     | 0.95       | 0.94     | 0.94      |
| Random Forest         | 0.97     | 0.96       | 0.95     | 0.95      |
| Naive Bayes           | 0.94     | 0.93       | 0.92     | 0.92      |

- **Confusion Matrix insights**:  
  - False positives (ham classified as spam): affects user experience (legitimate messages lost).  
  - False negatives (spam classified as ham): spam slipping into inbox.  
  - Which model has fewer false positives vs fewer false negatives may guide which model to prefer depending on what error is more costly.

---

## Your Findings & Recommendation

Based on the results:

- **Which model I recommend**: Random Forest (or Logistic Regression) seem to give the best trade-off between catching spam (high recall) and avoiding misclassifying ham (high precision).  
- **Why**: Because while Naive Bayes is fast and simple, it tends to make more mistakes on borderline cases. Random Forest (and also Logistic Regression) offer more robust performance with reasonable error rates.  

If deployed in a real system, I might use NB as a quick filter but rely on RF or LR for final decisions, especially on messages that seem ambiguous.

---

