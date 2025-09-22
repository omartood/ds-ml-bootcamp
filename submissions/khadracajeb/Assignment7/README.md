# Assignment: Spam Detection with Logistic Regression, Random Forest & Naive Bayes

**Due:** Monday, September 22, 2025 — 12:00 PM (Africa/Mogadishu / EAT)

## Summary

This assignment focuses on detecting spam messages using machine learning models. Three models were implemented and evaluated:

- **Logistic Regression**
- **Random Forest Classifier**
- **Naive Bayes (MultinomialNB)**

The text messages were transformed into TF–IDF features, which were then used to train and test all three models. Performance metrics and single-message sanity checks were conducted to assess accuracy and reliability.

---

## Files Included

- `spam_detection.ipynb`  
  Contains all code for:
  - Loading and preprocessing the dataset (`mail_l7_dataset.csv`)
  - Splitting data into training and test sets
  - Text feature extraction using TF–IDF
  - Training Logistic Regression, Random Forest, and Naive Bayes models
  - Evaluating performance metrics (Accuracy, Precision, Recall, F1-Score, Confusion Matrix)
  - Performing at least 3 single-message sanity checks

- `reflection_paper.md`  
  Includes:
  - Description of the implementation
  - Comparison of model predictions on sanity checks
  - Explanation of Naive Bayes, its advantages and limitations
  - Discussion of evaluation metrics
  - Recommendation of the best model for spam detection

---

## Learning Outcomes

Through this assignment, I learned to:

- Preprocess text data and handle missing values  
- Encode categorical labels (spam=0, ham=1)  
- Split data into training and test sets  
- Transform text into TF–IDF numeric features  
- Train and evaluate **Logistic Regression**, **Random Forest**, and **Naive Bayes** models  
- Analyze and compare model performance using metrics and confusion matrices  
- Conduct sanity checks on individual messages to verify predictions  

---

## Notes

- The models were evaluated on the same test set for fair comparison.  
- Random Forest showed the best overall performance, with the highest recall and F1-Score.  
- Naive Bayes is simple and fast, making it suitable for lightweight spam filtering tasks.  
- Logistic Regression performed reasonably well but missed more spam messages compared to Random Forest.  

---

**Alhamdulillah for understanding and completing this assignment successfully!** 
