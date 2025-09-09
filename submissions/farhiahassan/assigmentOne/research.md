# Research Assignment  
## Introduction to Machine Learning  

### 1. Defining Machine Learning (with a real-life example)  
Machine Learning is a technology that allows computers to learn from data and improve their performance on tasks without being explicitly programmed.  

**Example:** Credit-card fraud detection. Banks use models trained on labeled transactions to assign risk scores. As new outcomes arrive, the system retrains and improves fraud detection performance.  

---

### 2. Supervised vs. Unsupervised Learning  

| Aspect         | Supervised Learning                  | Unsupervised Learning                 |
|----------------|--------------------------------------|---------------------------------------|
| Training data  | Labeled (features + target)          | Unlabeled (features only)             |
| Goal           | Learn mapping from inputs → outputs  | Discover structure/patterns            |
| Algorithms     | Regression, SVM, Trees, Neural Nets  | k-Means, PCA, Autoencoders             |
| Evaluation     | Accuracy, AUC, RMSE                  | Silhouette score, reconstruction error |

**Example of Supervised:** Crop-yield prediction using weather and satellite data.  
**Example of Unsupervised:** Network anomaly detection without prior labels.  

---

### 3. Overfitting: Causes and Prevention  
- **Causes:** Models may learn noise instead of the true pattern due to high complexity, small data, or repeated tuning.  
- **Prevention:** Use cross-validation, regularization, early stopping, more data/augmentation, and strict leakage control.  

---

### 4. Train/Test Split: How and Why  
- **How:** Data is split into training and testing sets. Random splits or chronological splits (for time-series) are used. Stratification ensures class balance.  
- **Why:** To estimate model performance on unseen data and avoid overfitting.  

---

### 5. Case Study: Skin Cancer Detection  
- **Source:** Esteva et al., *Nature* (2017).  
- **Method:** A deep CNN was trained on ~129,450 images across ~2,000 diseases and tested on biopsy-proven cases.  
- **Findings:** The model matched dermatologist-level performance in classifying skin lesions.  
- **Impact:** Demonstrated AI’s potential in clinical diagnosis, with implications for low-resource healthcare.  

---

### References  
- Mitchell, T. M. (1997). *Machine Learning*. McGraw-Hill.  
- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.  
- Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning*. Springer.  
- Scikit-learn Documentation: train_test_split.  
- Esteva, A. et al. (2017). Dermatologist-level classification of skin cancer with deep neural networks. *Nature*, 542, 115‒118.  
- Hafez, I. Y. et al. (2025). A systematic review of AI in credit card fraud detection. *Journal of Big Data*.  
- Business Insider. Mastercard AI in fraud-detection systems.  
- Pinto, A. et al. (2024). Unsupervised anomaly detection. *Discover Artificial Intelligence*.  
- Agyemang, E. F. et al. (2024). Anomaly detection with unsupervised ML. *Heliyon/Elsevier*.  
