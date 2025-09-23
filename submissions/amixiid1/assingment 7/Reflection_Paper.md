# Reflection Paper: Spam Detection with Logistic Regression, Random Forest, and Naive Bayes

## What Did I Implement?
In this project, I implemented a **spam detection system** using three machine learning models: Logistic Regression, Random Forest, and Naive Bayes.  
The dataset contained SMS messages labeled as either *ham* (legitimate) or *spam* (unwanted advertisements).  
I preprocessed the text using **TF-IDF vectorization**, which transforms text into numerical features that machine learning models can process.  
Each classifier was then trained on 80% of the data and evaluated on the remaining 20%. Finally, I tested the models with three custom example messages to compare their predictions.

## Comparison of Models
For the three sanity check messages:

1. *“Free entry in 2 a weekly competition!”* → All models classified this correctly as **Spam**.  
2. *“I will meet you at the cafe tomorrow”* → All models classified this correctly as **Ham**.  
3. *“Congratulations, you won a free ticket”* → Logistic Regression and Naive Bayes classified it as **Spam**, while Random Forest occasionally leaned towards **Ham**.  

This shows that Logistic Regression and Naive Bayes are more consistent in detecting typical spam-like keywords, while Random Forest can sometimes be less sensitive to short, keyword-heavy spam texts.

## Understanding Naive Bayes
**Naive Bayes** is a probabilistic classifier based on Bayes’ Theorem.  
It assumes that all features (words in a message) are conditionally independent given the class label. Despite this “naive” assumption, it performs surprisingly well in text classification tasks.  

- **Why for spam detection?**  
  Spam emails often contain certain keywords (“free,” “win,” “claim now”) that strongly indicate spam. Naive Bayes handles such word-frequency signals efficiently.  

- **Advantages:**  
  - Very fast and lightweight.  
  - Works well with high-dimensional text data.  
  - Requires little training data.  

- **Limitations:**  
  - The independence assumption is unrealistic, as words in language often depend on each other.  
  - May struggle when spam uses subtle or context-dependent language.

## Metrics Discussion
When comparing model performance:  
- **Logistic Regression** achieved strong accuracy, with balanced precision and recall.  
- **Random Forest** sometimes had slightly higher overall accuracy, but could produce more false negatives (failing to detect spam).  
- **Naive Bayes** had slightly lower accuracy but higher sensitivity to spam, making it less likely to miss spam messages.  

The **Confusion Matrix** provides insight into **false positives (ham misclassified as spam)** and **false negatives (spam misclassified as ham)**.  
False positives reduce user experience (legitimate messages blocked), while false negatives pose a risk (spam slipping through).  
A good spam filter should minimize both, but especially false negatives.

## Findings
Overall, I recommend **Logistic Regression** for spam detection in this dataset.  
It offers the best balance between accuracy, precision, and recall, while remaining relatively simple and interpretable.  
Naive Bayes is also a strong candidate when speed and simplicity are critical, particularly for mobile applications.  
Random Forest, while powerful, is less interpretable and sometimes less reliable on short spam-like texts.  

**In summary, Logistic Regression provides the most practical combination of reliability and interpretability, making it my preferred choice for real-world spam detection.**
