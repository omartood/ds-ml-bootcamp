## 1. Introduction to Classification

*Classification* is a part of Machine Learning that involves *sorting data into categories. For example, a system might need to decide whether a patient has **diabetes or not* using medical test results. The key point is that the output is a *specific category*, not a number.  

Classification is different from regression. Regression predicts *numerical values, while classification predicts **labels or classes*. For instance, predicting a patient’s blood sugar level is regression, whereas predicting if they have diabetes is classification.  

*Examples:*  
- *Classification:* Identifying the species of a flower (setosa, versicolor, or virginica) based on leaf measurements.  
- *Regression:* Estimating tomorrow’s temperature in a city based on weather patterns.  

In many real-life situations, we need classification. It is used in medicine, finance, agriculture, and even social media to make decisions where the outcome falls into categories.

---

## 2A. Classification Algorithms

### Logistic Regression

*How it works:*  
Logistic Regression calculates the *probability* that a given input belongs to a certain class. If the probability is above a chosen threshold (usually 0.5), the input is assigned to that class.  

*Example use case:*  
Predicting whether a patient is at risk of developing heart disease based on factors like cholesterol, blood pressure, and age.  

*Advantages:*  
- Easy to understand and implement  
- Works well for small to medium-sized datasets  
- Good when features have a linear relationship with the outcome  

*Limitations:*  
- Cannot capture complex patterns  
- Sensitive to irrelevant features or correlations  

---

### Decision Trees

*How it works:*  
Decision Trees split the data into branches based on the most important features. Each decision point asks a question about a feature, and each branch leads to a classification result at the leaf nodes.  

*Example use case:*  
Predicting whether a customer will purchase a product online based on browsing habits, device type, and time spent on product pages.  

*Advantages:*  
- Simple to visualize and interpret  
- Can work with numerical and categorical data  
- Requires little preprocessing  

*Limitations:*  
- Can overfit if the tree becomes too complex  
- Sensitive to small changes in the data  

---

### Random Forest

*How it works:*  
Random Forest creates *many decision trees* from random samples of the dataset. Each tree votes for a class, and the majority decision becomes the final prediction. This reduces errors and improves accuracy.  

*Example use case:*  
Predicting the type of crop disease in agriculture based on soil, rainfall, and plant health indicators.  

*Advantages:*  
- More accurate and stable than a single tree  
- Reduces overfitting  
- Works well with many features  

*Limitations:*  
- Harder to interpret than a single tree  
- Requires more computing resources  

---

## 2B. Extended Task – Support Vector Machines (SVM)

*What it’s good for:*  
SVM is effective for *binary classification*, especially with high-dimensional or complex datasets.  

*How it works:*  
SVM finds the *best line or hyperplane* that separates two classes. The points closest to this line, called *support vectors, help define the boundary. For non-linear data, **kernel functions* transform the data so that it can be separated linearly in a higher-dimensional space.  

*Example use case:*  
Determining if an image contains a cat or a dog by analyzing pixel values.  

*Advantages:*  
- Works well with high-dimensional data  
- Can handle non-linear relationships  
- Often gives high accuracy  

*Limitations:*  
- Training can be slow for large datasets  
- Needs careful parameter tuning  
- Less interpretable than trees or logistic regression  

---

## 3. Classification Metrics

Evaluating how well a classification model works is crucial. Common metrics include:

- *Accuracy:* Percentage of correctly predicted labels. Works best with balanced datasets.  
- *Precision:* Out of all predicted positives, how many are actually correct. Important when false positives are costly.  
- *Recall:* Out of all actual positives, how many were correctly predicted. Important when missing positives is costly.  
- *F1-Score:* Combines precision and recall into a single score. Useful when both false positives and negatives matter.  
- *Confusion Matrix:* Shows counts of true positives, false positives, true negatives, and false negatives. Helpful for detailed analysis.  

| Metric        | Focus                                        | When to use                          | Weakness/Notes                       |
|---------------|----------------------------------------------|-------------------------------------|-------------------------------------|
| Accuracy      | Overall correctness                           | Balanced datasets                    | Misleading for imbalanced datasets  |
| Precision     | Correct positive predictions                  | Costly false positives               | Ignores missed positives             |
| Recall        | Capturing actual positives                     | Costly false negatives               | Ignores false positives              |
| F1-Score      | Balance between precision and recall          | Both false positives and negatives matter | Less intuitive than accuracy       |
| Confusion Matrix | True vs predicted labels                     | Detailed error analysis              | Can be large with many classes      |

---

## 4. Imbalanced Data Problem

Imbalanced data occurs when one class has far more examples than another. For example, in spam detection, most emails are legitimate, and only a few are spam.  

In such cases, *accuracy can be misleading. A model that predicts all emails as non-spam could seem highly accurate but would fail to catch spam emails. Metrics like **precision, recall, and F1-score* are better for evaluating performance on imbalanced datasets. A *confusion matrix* also helps to understand where the model is making mistakes.

---

## 5. Real-World Case Study: Email Spam Detection

*Goal:*  
Automatically detect and filter spam emails to make email services safer and easier to use.  

*Data used:*  
A dataset containing emails labeled as “spam” or “not spam.” Features include words in the subject and body, sender information, and other metadata.  

*Classification model applied:*  
Naive Bayes classifier, which calculates the probability that certain words appear in spam versus non-spam emails to make predictions.  

*Key results:*  
- High precision and recall in detecting spam  
- Showed that preprocessing and feature extraction are important  
- Helped users filter out unwanted or malicious emails efficiently  

---

## References

1. Bishop, C. M. (2006). Pattern Recognition and Machine Learning. Springer.  
2. Han, J., Kamber, M., & Pei, J. (2011). Data Mining: Concepts and Techniques. Morgan Kaufmann.  
3. Géron, A. (2019). Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow. O’Reilly Media.  
4. Brownlee, J. (2020). Classification Metrics for Machine Learning. Machine Learning Mastery