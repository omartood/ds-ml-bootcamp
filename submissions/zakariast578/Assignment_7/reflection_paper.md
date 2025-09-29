**What Did I Implement?** 

In this project, I built a **Spam Detection System** using three machine learning models: **Logistic Regression, Random Forest, and Naive Bayes**. The dataset contained SMS/email messages labeled as either *spam* (0) or *ham* (1). After preprocessing the data (handling missing values, encoding labels, and converting text into numerical vectors using **TF-IDF**), I trained and evaluated each model. 

* **Logistic Regression** was used as a baseline linear model.   
* **Random Forest** was applied as a non-linear ensemble model that combines multiple decision trees.   
* **Naive Bayes (MultinomialNB)** was used as a probabilistic model commonly applied in spam detection tasks. 

 

**Comparison of Models** 

I tested all three models on real messages from the dataset and some custom examples. For clear spam messages (e.g., *“Congratulations\! You’ve won a free course”*), all models correctly predicted **Spam**. For normal messages (e.g., *“I will meet you at the cafe tomorrow”*), all models predicted **Ham** correctly. 

However, in one test message (*“Free entry in 2 a weekly competition\!”*), **Logistic Regression and Random Forest predicted Ham**, while **Naive Bayes predicted Spam**. This shows that Naive Bayes was more sensitive to spam-like words, even if the message was ambiguous. 

 

**Understanding Naive Bayes** 

**Naive Bayes** is a simple probabilistic algorithm based on Bayes’ theorem. It assumes that all features (words in a message) are **independent** given the class label. 

* **Why used in spam detection?**   
   Because spam often contains certain keywords (e.g., “free”, “win”, “congratulations”), Naive Bayes can quickly detect these word patterns and classify messages.   
* **Advantages:**   
* Fast to train and predict, even on large text datasets.   
* Works well when features (words) strongly indicate class labels.   
* Requires less computational resources.   
* **Limitations:**   
* The independence assumption is unrealistic since words are not fully independent in natural language.   
* May misclassify ambiguous or short messages where spam words appear in normal contexts. 

 

**Metrics Discussion** 

The evaluation metrics show the following: 

* **Accuracy:** Logistic Regression (0.97), Random Forest (0.98), Naive Bayes (0.98).   
* **Precision:** All three models achieved **1.00**, meaning they had **no false positives** (they never labeled a Ham message as Spam).   
* **Recall:** Logistic Regression (0.76) was lower than Random Forest (0.86) and Naive Bayes (0.83). This means Logistic Regression missed more spam messages.   
* **F1-Score:** Random Forest (0.92) performed best, followed by Naive Bayes (0.90), and Logistic Regression (0.86). 

 

   **Confusion Matrix** shows that: 

* Logistic Regression misclassified 36 spam messages as ham (false negatives).   
* Random Forest misclassified 21 spam messages as ham.   
* Naive Bayes misclassified 26 spam messages as ham.   
   None of the models misclassified ham as spam (false positives \= 0). 

 

**Findings** 

Based on the results, **Random Forest** performed best overall, achieving the highest F1-score and recall. This means it balanced precision and recall better, detecting more spam messages while still avoiding false alarms. 

Although **Naive Bayes** is simple and fast, it slightly underperformed compared to Random Forest, but still did better than Logistic Regression in recall. Logistic Regression, while precise, missed more spam messages and is therefore less reliable for this task. 

**I would recommend Random Forest for spam detection**, since it had the best balance between precision and recall, achieved the highest F1-score, and correctly identified the largest number of spam messages without mislabeling normal ones. 

 

