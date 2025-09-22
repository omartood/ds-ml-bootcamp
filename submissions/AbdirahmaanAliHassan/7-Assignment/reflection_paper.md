# Reflection Paper: 

## 1. What I Implemented

I built an end-to-end spam/ham classifier. Messages were cleaned by replacing missing text with empty strings, and labels were encoded as **spam = 0** and **ham = 1**. I used an **80/20 train–test split (stratified)** to keep the spam/ham ratio stable. Text was transformed with **TF-IDF** using **unigrams + bigrams** so phrases like “free entry” or “won ticket” become strong features. I then trained three models **Logistic Regression**, **Random Forest**, and **Multinomial Naive Bayes** and evaluated each using **Accuracy, Precision, Recall, F1-Score**, and the **Confusion Matrix** (treating spam=0 as the positive class for precision/recall/F1).

## 2. How Each Model Was Used

### 2.1 Logistic Regression (LR)

A linear decision boundary on TF-IDF features, optimized with regularization. Works well on high-dimensional sparse text.

### 2.2 Random Forest (RF)

An ensemble of many decision trees (bootstrap samples + feature subsampling) to capture non-linear patterns and interactions between n-grams.

### 2.3 Multinomial Naive Bayes (NB)

A probabilistic model assuming feature independence given the class; particularly effective for keyword-driven text with sparse vectors.

## 3. Comparison of the Three Sanity-Check Messages

* “**Free entry in 2 a weekly competition!**” → predicted **Spam**
* “**I will meet you at the cafe tomorrow**” → predicted **Ham**
* “**Congratulations, you won a free ticket**” → predicted **Spam**

In my run, **all three models agreed**. In general, if any disagreement occurs, NB is usually the most **aggressive** at flagging promotional phrases as spam, LR is typically **balanced**, and RF often agrees with LR while catching slightly more nuanced patterns thanks to its non-linearity.

## 4. Understanding Naive Bayes

### 4.1 What Is It?

A probabilistic classifier that applies **Bayes’ Rule** with the simplifying assumption that features (tokens/ngrams) are **conditionally independent** given the class. **MultinomialNB** models token counts/weights per class.

### 4.2 Why It Is Often Used for Spam Detection

* Handles **high-dimensional sparse** features very well
* **Extremely fast** to train and predict
* Performs strongly with **keyword-driven** signals (typical of spam)

### 4.3 Advantages

* **Speed** and **low memory** footprint
* Simple and stable **baseline**; outputs probabilities

### 4.4 Limitations

* The independence assumption is **unrealistic** for natural language
* Can **miss interactions/context** captured by LR/RF
* Probabilities may be **poorly calibrated** without post-processing

## 5. Metrics Discussion

I reported **Accuracy, Precision (spam), Recall (spam), F1 (spam)** and the **Confusion Matrix** for each model.

### 5.1 Which Model Did Better?

On this dataset, **Random Forest** typically gave the **best overall F1/Accuracy**, with **Logistic Regression** close behind. **Naive Bayes** was fastest and competitive but usually a bit lower on F1—either slightly more **false positives** (over-flagging ham) or **false negatives** (missing some spam), depending on the data and threshold.

### 5.2 Interpreting the Confusion Matrix

*(rows = actual, cols = predicted, order [0=spam, 1=ham])*

* **[0,0] TP:** spam correctly flagged
* **[0,1] FN:** spam missed (dangerous spam slips through)
* **[1,0] FP:** ham flagged as spam (annoying blocks legit mail)
* **[1,1] TN:** ham correctly allowed

For spam filters, **high Recall (spam)** reduces FN (less spam in the inbox). **High Precision (spam)** reduces FP (fewer real emails mistakenly blocked). The best model balances both.

## 6. Findings & Recommendation

Overall, I **recommend Random Forest** for this dataset: it provided the strongest **F1** and a good balance between catching spam (high recall) and avoiding false alarms (high precision). If simplicity and speed are priorities, **Logistic Regression** is an excellent alternative with competitive performance and easier deployment/tuning. **Naive Bayes** remains a valuable baseline very fast and effective on keyword-heavy spam though it may need **threshold tuning** or **additional features** to match LR/RF on F1.

What I implemented

I built an end-to-end spam/ham classifier. Messages were cleaned by replacing missing text with empty strings and labels were encoded as spam = 0, ham = 1. I used an 80/20 train–test split (stratified) to keep the spam/ham ratio stable. Text was transformed with TF-IDF using unigrams + bigrams so phrases like “free entry” or “won ticket” become strong features. I then trained three models Logistic Regression, Random Forest, and Multinomial Naive Bayes and evaluated each using Accuracy, Precision, Recall, F1-Score, and the Confusion Matrix (treating spam=0 as the positive class for precision/recall/F1).

How each model was used

Logistic Regression (LR): Linear decision boundary on TF-IDF features, optimized with regularization. Works well on high-dimensional sparse text.

Random Forest (RF): An ensemble of many decision trees (bootstrap samples + feature subsampling) to capture non-linear patterns and interactions between n-grams.

Multinomial Naive Bayes (NB): Probabilistic model assuming feature independence given the class; particularly effective for keyword-driven text with sparse vectors.

Comparison of the 3 sanity-check messages

“Free entry in 2 a weekly competition!” → predicted Spam

“I will meet you at the cafe tomorrow” → predicted Ham

“Congratulations, you won a free ticket” → predicted Spam

In my run, all three models agreed. In general, if any disagreement occurs, NB is usually the most aggressive at flagging promotional phrases as spam, LR is typically balanced, and RF often agrees with LR while catching slightly more nuanced patterns thanks to its non-linearity.

Understanding Naive Bayes

What is it?
A probabilistic classifier that applies Bayes’ Rule with the simplifying assumption that features (tokens/ngrams) are conditionally independent given the class. MultinomialNB models token counts/weights per class.

Why often used for spam detection?

Handles high-dimensional sparse features very well

Extremely fast to train and predict

Performs strongly with keyword-driven signals (typical of spam)

Advantages

Speed and low memory footprint

Simple and stable baseline; outputs probabilities

Limitations

The independence assumption is unrealistic for natural language

Can miss interactions/contexts captured by LR/RF

Probabilities may be poorly calibrated without post-processing

Metrics discussion

I reported Accuracy, Precision (spam), Recall (spam), F1 (spam) and the Confusion Matrix for each model.

Which model did better?
On this dataset, Random Forest typically gave the best overall F1/Accuracy, with Logistic Regression close behind. Naive Bayes was fastest and competitive but usually a bit lower on F1 either slightly more false positives (over-flagging ham) or false negatives (missing some spam), depending on the data and threshold.

Interpreting the Confusion Matrix (rows=actual, cols=predicted, order [0=spam, 1=ham]):

[0,0] TP: spam correctly flagged

[0,1] FN: spam missed (dangerous spam slips through)

[1,0] FP: ham flagged as spam (annoying blocks legit mail)

[1,1] TN: ham correctly allowed
For spam filters, high Recall (spam) reduces FN (less spam in the inbox). High Precision (spam) reduces FP (fewer real emails mistakenly blocked). The best model balances both.

Findings & recommendation

Overall, I recommend Random Forest for this dataset: it provided the strongest F1 and a good balance between catching spam (high recall) and avoiding false alarms (high precision). If simplicity and speed are priorities, Logistic Regression is an excellent alternative with competitive performance and easier deployment/tuning. Naive Bayes remains a valuable baseline very fast and effective on keyword-heavy spam though it may need threshold tuning or additional features to match LR/RF on F1.

If this were a production system, I would: (1) tune the decision threshold to match the desired precision–recall trade-off, (2) monitor FP/FN rates via the confusion matrix, and (3) periodically retrain with fresh data to track evolving spam vocabulary.