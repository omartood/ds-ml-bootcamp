# Introduction to Machine Learning

## 1. Defining Machine Learning
Machine Learning (ML) is a field of computer science concerned with building systems that improve their performance on a task as they are exposed to more data. Instead of relying on explicitly programmed instructions, ML systems infer patterns and relationships within data to make predictions or decisions (Mitchell, 1997).

**Real-life example:** In modern agriculture, ML models are used to predict crop yields based on weather conditions, soil data, and satellite imagery. Rather than programming rules about rainfall or sunlight thresholds, algorithms analyze historical data and adapt to new environmental patterns, providing farmers with accurate, data-driven insights (Liakos et al., 2018).

---

## 2. Supervised vs. Unsupervised Learning

### Supervised Learning
- **Definition:** A paradigm where algorithms learn from labeled datasets, meaning that both the input features and their corresponding outputs are provided during training.
- **Example:** In finance, supervised ML models are trained to detect fraudulent transactions. The model is fed past transaction data labeled as "fraudulent" or "legitimate," enabling it to recognize suspicious patterns in new data (Bhattacharyya et al., 2011).

### Unsupervised Learning
- **Definition:** A paradigm where algorithms explore datasets without predefined labels, identifying hidden patterns or structures.
- **Example:** In retail, unsupervised learning can be used for customer segmentation. Clustering algorithms group customers based on purchasing behavior without prior knowledge of categories, which helps businesses personalize marketing strategies (Kohonen, 2001).

| Aspect                  | Supervised Learning                  | Unsupervised Learning               |
|-------------------------|--------------------------------------|-------------------------------------|
| Data type               | Labeled (inputs with outputs)        | Unlabeled (only inputs)             |
| Main tasks              | Classification, Regression           | Clustering, Dimensionality Reduction|
| Example domain          | Fraud detection in finance           | Customer segmentation in retail     |

---

## 3. Overfitting: Causes and Prevention

### Causes of Overfitting
Overfitting occurs when a model learns noise or random fluctuations in the training data instead of generalizable patterns. This leads to excellent performance on the training dataset but poor accuracy on unseen data. Common causes include:
- Excessive model complexity (e.g., too many parameters relative to data size).
- Insufficient training data.
- Training for too many iterations without regularization.

### Prevention Strategies
- **Regularization:** Techniques like L1/Lasso and L2/Ridge penalize overly complex models (Ng, 2004).
- **Cross-validation:** Splitting training data into multiple folds to test generalization during training.
- **Early stopping:** Monitoring validation performance and halting training before overfitting occurs.
- **Data augmentation:** Increasing dataset size through transformations, especially in image and speech domains.

---

## 4. Train/Test Split: Purpose and Process

### Process
A dataset is typically divided into two subsets:
- **Training set (e.g., 70–80%):** Used to fit the model parameters.
- **Test set (e.g., 20–30%):** Used to evaluate how well the model generalizes to unseen data.

### Importance
Without this division, a model might only memorize data (overfitting) and fail in real-world tasks. A train/test split provides an unbiased estimate of performance, ensuring the algorithm’s utility beyond the training data (Hastie, Tibshirani & Friedman, 2009).

In advanced practices, a **validation set** or **cross-validation** is introduced to fine-tune models before final testing.

---

## 5. Case Study: Machine Learning in Healthcare

**Title:** Predicting Sepsis in Intensive Care Units using Machine Learning

**Source:** Desautels, T. et al. (2016). "Prediction of sepsis in the intensive care unit with minimal electronic health record data: a machine learning approach." *JMIR Medical Informatics*.

### Summary of Findings
The study applied ML models to predict sepsis onset in ICU patients using minimal electronic health record (EHR) data such as vital signs and lab results. Traditional sepsis prediction relies on clinician judgment and predefined scoring systems, which can be delayed or inaccurate.

Key insights:
- The ML model achieved significantly higher sensitivity and specificity compared to conventional methods.
- Predictions could be made several hours before sepsis onset, allowing earlier interventions.
- Demonstrates ML’s potential to save lives by providing real-time, data-driven support for clinical decision-making.

---

## References
- Bhattacharyya, S., Jha, S., Tharakunnel, K., & Westland, J. C. (2011). "Data mining for credit card fraud: A comparative study." *Decision Support Systems*, 50(3), 602–613.
- Desautels, T., Calvert, J., Hoffman, J., Jay, M., Kerem, Y., Shieh, L., … & Das, R. (2016). "Prediction of sepsis in the intensive care unit with minimal electronic health record data: a machine learning approach." *JMIR Medical Informatics*, 4(3), e28.
- Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning: Data Mining, Inference, and Prediction*. Springer.
- Kohonen, T. (2001). *Self-Organizing Maps*. Springer.
- Liakos, K. G., et al. (2018). "Machine learning in agriculture: A review." *Sensors*, 18(8), 2674.
- Mitchell, T. M. (1997). *Machine Learning*. McGraw-Hill.
- Ng, A. Y. (2004). "Feature selection, L1 vs. L2 regularization, and rotational invariance." *Proceedings of the 21st International Conference on Machine Learning*.

