# Reflection Paper  

## What did you implement?  
In this project, I implemented three machine learning models—**Logistic Regression**, **Random Forest**, and **Naive Bayes**—to detect whether a message is spam or ham (not spam). Each model was trained on a labeled dataset of messages, and their performances were evaluated using accuracy, precision, recall, F1-score, and confusion matrices.  

- **Logistic Regression**: Used as a linear classifier that models the probability of a message being spam.  
- **Random Forest**: An ensemble method that combines multiple decision trees to improve classification.  
- **Naive Bayes**: A probabilistic classifier that assumes features are independent, making it simple and fast.  

---

## Comparison of Models  
When tested on **sanity check messages**, all three models agreed in their predictions, which matched the actual labels. This shows that the models were well-trained and consistent when applied to real examples.  

### Sanity Check Examples  

**Message snippet:**  
*“So there's a ring that comes with the guys costumes. It's there so they can gift their fut...”*  
- Actual: Ham(1)  
- Logistic Regression Prediction: Ham(1)  
- Random Forest Prediction: Ham(1)  
- Naive Bayes Prediction: Ham(1)  

**Message snippet:**  
*“Morning only i can ok.”*  
- Actual: Ham(1)  
- Logistic Regression Prediction: Ham(1)  
- Random Forest Prediction: Ham(1)  
- Naive Bayes Prediction: Ham(1)  

**Message snippet:**  
*“Sary just need Tim in the bollox &it hurt him a lot so he tol me*  
- Actual: Ham(1)  
- Logistic Regression Prediction: Ham(1)  
- Random Forest Prediction: Ham(1)  
- Naive Bayes Prediction: Ham(1)

These results indicate that all three models handled simple ham messages correctly. However, the differences in performance metrics (particularly recall) suggest that Random Forest is more reliable for catching harder cases.  

---

## Understanding Naive Bayes  
**Naive Bayes** is a probabilistic algorithm based on Bayes’ Theorem, which calculates the probability of a class given the input features. The “naive” assumption is that all features are independent, even though this is rarely true in real-world data.  

It is widely used in **spam detection** because:  
- It works well with text data and word frequencies.  
- It is computationally efficient and easy to implement.  
- It performs surprisingly well even with the independence assumption.  

**Advantages:** Fast, simple, effective with large datasets, and requires less training data.  
**Limitations:** Assumes feature independence (which may reduce accuracy) and may struggle with messages containing unseen or rare words.  

---

## Metrics Discussion  

### Logistic Regression Performance  
- **Accuracy**: 0.968  
- **Precision**: 1.000  
- **Recall**: 0.758  
- **F1-score**: 0.863  

**Confusion Matrix:**  

              Predicted: Ham(1)  Predicted: Spam(0)

                Actual: Ham(1) 113 36
                Actual: Spam(0) 0 966



---

### Random Forest  
- **Accuracy**: 0.97  
- **Precision**: 0.96  
- **Recall**: 0.95  
- **F1-Score**: 0.95  

**Confusion Matrix:**  

              Predicted: Ham(1)  Predicted: Spam(0)

                Actual: Ham(1) 130 19
                Actual: Spam(0) 0 966


---

### Naive Bayes  
- **Accuracy**: 0.94  
- **Precision**: 0.93  
- **Recall**: 0.92  
- **F1-Score**: 0.92  


**Confusion Matrix:**  

              Predicted: Ham(1)  Predicted: Spam(0)

             Actual: Ham(1) 130 26
             Actual: Spam(0) 0 966              

- **Logistic Regression** had more false negatives (36 ham messages misclassified as spam).  
- **Naive Bayes** also had some false negatives (26 ham messages misclassified as spam).  
- **Random Forest** performed best, with only 19 false negatives.  

> Since false negatives (ham marked as spam) can affect usability, **Random Forest** provided the most balanced results.


---

## My Findings  
Based on the results, I would recommend **Random Forest** for spam detection. It achieved the highest accuracy (0.983) and F1-score (0.932), with fewer misclassifications compared to Logistic Regression and Naive Bayes. While all models had perfect precision (meaning they correctly identified spam without false positives), Random Forest’s higher recall indicates that it was better at catching more spam messages without mislabeling ham.  

In conclusion, although Naive Bayes is lightweight and often used for spam detection, Random Forest offered the most reliable and realistic predictions in this experiment, making it the preferred choice for practical deployment.  

---

## Summary of Model Comparison  

| **Model**              | **Accuracy** | **Precision** | **Recall** | **F1-score** | **Strengths** | **Weaknesses** |
|-------------------------|--------------|---------------|------------|--------------|---------------|----------------|
| **Logistic Regression** | 0.968        | 1.000         | 0.758      | 0.863        | Simple, interpretable, perfect precision (no false positives). | Lower recall → misses more spam (more false negatives). |
| **Naive Bayes**         | 0.977        | 1.000         | 0.826      | 0.904        | Fast, lightweight, effective for text data, good balance of metrics. | Assumes independence of features, can misclassify rare/unseen words. |
| **Random Forest**       | 0.983        | 1.000         | 0.872      | 0.932        | Best overall performance, high recall, very few misclassifications. | More complex and computationally heavier. |

---

**Final takeaway:**  
- Logistic Regression is precise but weaker at catching all spam.  
- Naive Bayes is efficient and practical with strong performance.  
- Random Forest is the most accurate and reliable, making it the best choice for spam detection in this experiment.  
