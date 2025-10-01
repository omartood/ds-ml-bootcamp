# Reflection Paper – Spam Detection with Logistic Regression, Random Forest & Naive Bayes

---

## 1. Dataset Details

- **Total Messages:** 5,574 messages.  
- **Spam vs Ham Ratio:** 747 spam messages (13.4%) and 4,827 ham messages (86.6%).  
- **Preprocessing:**  
 - Checked for missing values; the dataset had none.
  - Converted all messages to lowercase.  
  - Removed punctuation and unnecessary whitespace.  
  - Removed English stop words using `TfidfVectorizer(stop_words='english')`.  

This preprocessing ensures the models focus on meaningful words in the messages rather than noise.

---

## 2. Feature Engineering

- **TF-IDF Vectorization:**  
  TF-IDF was chosen over CountVectorizer because it not only counts the frequency of words but also considers their uniqueness across messages. This helps models identify words that are strong indicators of spam.

- **Parameters Used:**  
  - `min_df=1` → ignore words that appear in fewer than 1 document.  
  - `stop_words='english'` → removes common words that do not carry meaning.  
  - `lowercase=True` → ensures consistency by converting all text to lowercase.  

TF-IDF allows the models to capture the importance of words in the context of spam detection.

---

## 3. Model Hyperparameters

| Model               | Hyperparameters           |
|--------------------|---------------------------|
| Logistic Regression | `max_iter=1000`           |
| Random Forest       | `n_estimators=200`        |
| Naive Bayes         | default parameters        |

These hyperparameters were chosen to ensure convergence (Logistic Regression) and stable predictions (Random Forest). Naive Bayes works well with default settings for text classification.

---

## 4. What did you implement?

In this project, I implemented a spam detection system using three machine learning models: **Logistic Regression**, **Random Forest**, and **Naive Bayes (MultinomialNB)**.  

The steps I followed were:  

1. Loaded and cleaned the dataset containing SMS messages labeled as "spam" (0) or "ham" (1).  
2. Checked for missing values and ensured the data was clean.  
3. Encoded the labels and split the data into training (80%) and testing (20%) sets.  
4. Converted the text messages into numerical vectors using **TfidfVectorizer**.  
5. Trained all three models on the training set.  
6. Evaluated their performance on the test set using **Accuracy**, **Precision**, **Recall**, **F1-Score**, and **Confusion Matrix**.  
7. Performed sanity checks on six sample messages to see how each model classified them.  

---

## 5. Comparison of Models: Sanity Check Results

The sanity check results for the sample indices `[986, 14, 119, 815, 260, 326]` were:

| Sample Index | Message                                                                                     | Actual | LR Predict | RF Predict | NB Predict |
|--------------|---------------------------------------------------------------------------------------------|--------|------------|------------|------------|
| 986          | FREE2DAY sexy St George's Day pic of Jordan! Txt PIC to 89080 dont miss out, then every... | Spam   | Ham        | Spam       | Spam       |
| 14           | FREE RINGTONE text FIRST to 87131 for a poly or text GET to 87131 for a true tone!...      | Spam   | Spam       | Spam       | Spam       |
| 119          | Rock yr chik. Get 100's of filthy films &XXX pics on yr phone now. rply FILTH to 69669... | Spam   | Ham        | Ham        | Ham        |
| 815          | FREE for 1st week! No1 Nokia tone 4 ur mobile every week just txt NOKIA to 8077...          | Spam   | Spam       | Spam       | Spam       |
| 260          | Guess what! Somebody you know secretly fancies you! Wanna find out who it is? Give us...    | Spam   | Spam       | Spam       | Ham        |
| 326          | U 447801259231 have a secret admirer who is looking 2 make contact with U-find out...       | Spam   | Ham        | Spam       | Spam       |

**Observations:**  

- Logistic Regression missed 3 out of 6 spam messages.  
- Random Forest correctly detected 5 out of 6 spam messages.  
- Naive Bayes correctly detected 4 out of 6 spam messages.  

**Summary:**  
Random Forest performed best overall on this set, catching more spam messages. Logistic Regression was precise in some cases but failed on others. Naive Bayes caught some tricky spam messages but missed one sample (index 260).  

---

## 6. Metrics Comparison
## 6. Metrics Comparison

**Summary Table of Model Performance:**

| Model               | Accuracy | Precision | Recall | F1-Score |
|--------------------|---------|-----------|--------|----------|
| Logistic Regression | 0.968   | 1.000     | 0.758  | 0.863    |
| Random Forest       | 0.983   | 1.000     | 0.872  | 0.932    |
| Naive Bayes         | 0.977   | 1.000     | 0.826  | 0.904    |

**Confusion Matrices for Test Set:**

- **Logistic Regression:**

|             | Pred Ham (1) | Pred Spam (0) |
|-------------|--------------|---------------|
| Actual Ham (1) | 966          | 0             |
| Actual Spam (0)| 36           | 113           |

- **Random Forest:**

|             | Pred Ham (1) | Pred Spam (0) |
|-------------|--------------|---------------|
| Actual Ham (1) | 966          | 0             |
| Actual Spam (0)| 19           | 130           |

- **Naive Bayes:**

|             | Pred Ham (1) | Pred Spam (0) |
|-------------|--------------|---------------|
| Actual Ham (1) | 966          | 0             |
| Actual Spam (0)| 26           | 123           |

**Insights:**

- **Random Forest** has the best balance between **catching spam** (high recall) and avoiding false positives.  
- **Logistic Regression** is precise but misses more spam messages (36 false negatives).  
- **Naive Bayes** performs well, slightly below Random Forest, catching most spam but with 26 false negatives.

---

## 7. Understanding Naive Bayes

**What is Naive Bayes?**  
Naive Bayes is a probabilistic classifier based on **Bayes’ Theorem**, assuming all features (words in a message) are independent given the class label. It works well for text classification despite this "naive" assumption.  

**Why it is often used in spam detection:**  
- Efficient with high-dimensional text data.  
- Fast to train and predict.  
- Can adapt quickly to different datasets and word frequencies.  

**Advantages:**  
- Quick training and prediction.  
- Handles large datasets efficiently.  
- Easy to implement and interpret.  

**Limitations:**  
- The independence assumption rarely holds for real text.  
- May miss spam when words are correlated or when new patterns appear.  

---

## 8. Findings and Recommendation

Based on the results:  

- **Random Forest** is the most robust model for spam detection in this dataset.  
- **Naive Bayes** is fast and effective for some tricky spam messages but less consistent overall.  
- **Logistic Regression** is simple and precise but may fail to catch all spam messages.  

**Conclusion:**  
For practical spam detection, **Random Forest** offers the best balance between accuracy and recall. It detects more spam messages while minimizing false positives. In real-world applications, combining models or continuously updating the model with new spam examples can further improve performance.  
