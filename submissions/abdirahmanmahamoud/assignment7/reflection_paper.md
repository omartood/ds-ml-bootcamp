# Reflection Paper — Spam Detection Models

## 1. Introduction

In this reflection paper, I will evaluate and compare the performance of three machine learning algorithms used for spam detection: **Logistic Regression**, **Random Forest**, and **Naive Bayes**. The dataset was divided into training and testing sets with the following dimensions:

- **X_train**: (4457, 3322)
- **X_test**: (1115, 3322)

The evaluation metrics include **Accuracy, Precision, Recall, F1-Score**, and **Confusion Matrices**.  
The purpose of this reflection is to understand not only the numerical results but also the practical implications of each model.

---

## 2. Logistic Regression

### Results

- **Accuracy**: 0.956
- **Precision**: 1.000 (positive = spam=0)
- **Recall**: 0.671 (positive = spam=0)
- **F1-Score**: 0.803

### Confusion Matrix

|                      | Pred: Ham (1) | Pred: Spam (0) |
| -------------------- | ------------- | -------------- |
| **Actual: Ham (1)**  | 100           | 49             |
| **Actual: Spam (0)** | 0             | 966            |

### Reflection

Logistic Regression achieved **high precision**, meaning it rarely misclassified ham messages as spam. However, its **recall was low** (0.671), which indicates that the model failed to capture a significant portion of ham messages correctly. This imbalance between precision and recall suggests that Logistic Regression is highly conservative in labeling spam but sacrifices recall performance.

From a real-world perspective, missing ham emails may frustrate users because legitimate messages are wrongly filtered. This weakness makes Logistic Regression less practical compared to other models in this experiment.

---

## 3. Random Forest

### Results

- **Accuracy**: 0.984
- **Precision**: 1.000 (positive = spam=0)
- **Recall**: 0.879 (positive = spam=0)
- **F1-Score**: 0.936

### Confusion Matrix

|                      | Pred: Ham (1) | Pred: Spam (0) |
| -------------------- | ------------- | -------------- |
| **Actual: Ham (1)**  | 131           | 18             |
| **Actual: Spam (0)** | 0             | 966            |

### Reflection

Random Forest demonstrated **excellent performance**, achieving both high precision and strong recall. With an F1-score of **0.936**, it strikes a good balance between precision and recall. Unlike Logistic Regression, Random Forest reduces the risk of missing ham messages, which makes it more reliable.

The ensemble nature of Random Forest allows it to generalize better, reducing variance and improving robustness. This suggests that Random Forest is not only accurate but also more stable in handling different types of spam and ham messages.

In practice, this means fewer legitimate emails will be lost and spam filtering will remain strict. As a result, Random Forest stands out as the **best model** among the three.

---

## 4. Naive Bayes

### Results

- **Accuracy**: 0.986
- **Precision**: 0.978 (positive = spam=0)
- **Recall**: 0.913 (positive = spam=0)
- **F1-Score**: 0.944

### Confusion Matrix

|                      | Pred: Ham (1) | Pred: Spam (0) |
| -------------------- | ------------- | -------------- |
| **Actual: Ham (1)**  | 131           | 18             |
| **Actual: Spam (0)** | 0             | 966            |

### Reflection

Naive Bayes performed **surprisingly well**, even slightly surpassing Random Forest in terms of recall (0.913 vs. 0.879). Its precision, however, was slightly lower at 0.978. This indicates that while Naive Bayes captured more ham messages correctly, it also introduced a small number of misclassifications.

Given its simplicity and speed, Naive Bayes is a highly efficient model for spam detection. Its performance here proves that classical probabilistic models can compete strongly with more advanced ensemble methods.

---

## 5. Comparative Analysis

### Strengths and Weaknesses

- **Logistic Regression**: High precision, poor recall → risk of missing ham emails.
- **Random Forest**: Balanced performance, very robust, strong F1-score.
- **Naive Bayes**: Excellent recall, lightweight, very competitive performance.

### Best Choice

Overall, **Random Forest** is the most reliable model for spam detection in this experiment. It combines accuracy, precision, and recall effectively. Naive Bayes is also a strong candidate, particularly when computational efficiency is important.

---

## 6. Conclusion

Through this evaluation, I learned that:

1. Different algorithms excel in different aspects (precision vs. recall).
2. Ensemble methods like Random Forest often provide the best trade-offs.
3. Simpler models such as Naive Bayes can still achieve excellent performance.

This experiment deepened my understanding of **model evaluation, trade-offs, and practical application** in spam detection systems. In the future, combining multiple models (stacking or hybrid approaches) could further improve results.
