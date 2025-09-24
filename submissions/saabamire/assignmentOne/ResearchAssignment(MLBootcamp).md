
Research Assignment one: Introduction to Machine Learning 

1. What is Machine Learning with real-life example? 

Machine Learning (ML) is a branch of artificial intelligence where computers improve their 
performance by learning patterns from data, instead of following only fixed instructions. In 
other words, the system “learns” from experience and becomes better over time. 

Real-life example: In agriculture, ML is used to detect plant diseases by analysing photos of 
leaves. Farmers can upload a picture, and the model identifies whether the crop is healthy or 
infected. This helps improve food production and reduce losses. 

2. What is difference between Supervised vs Unsupervised Learning 

Supervised Learning: uses data that already has labels (the “right answers”). The model is 
trained by comparing its predictions with the correct outcomes. 

Example: In finance, supervised ML is used to predict whether a credit card transaction is 
fraudulent or not, based on past labelled examples. 

Unsupervised Learning: the data has no labels. The system tries to find patterns or groups 
without being told what the correct answer is. 

Example: In marketing, unsupervised ML helps group customers into clusters based on their 
shopping behaviours, even if no one has pre-labelled those groups 

Key difference: Supervised uses labelled data (answers provided), while unsupervised 
discovers hidden structures from unlabelled data. 

### Summary Table 

| Feature       | Supervised Learning                   | Unsupervised Learning |
|---------------|---------------------------------------|-----------------------|
| Data Type     | Labelled data (with correct answers)  | Unlabelled data       |
| Main Goal     | Learn the mapping between input/output| Discover hidden patterns |
| Examples      | Fraud detection, disease diagnosis    | Customer segmentation |
| Output        | Predict outcomes (classification/regression) | Clusters, structures |

3. What is Overfitting: Causes & Prevention 

Overfitting: is too complex and model tries to memorize every detail in the training data but 
when it comes new it fails.  

**Causes of Overfitting:** 
- When the model is too complex and tries to memorize every detail in the training data. 
- When there is not enough training data, so the model cannot generalize well. 
- When noise or random errors in data are learned as if they were important patterns. 

**How to prevent it:** 
- Use simpler models instead of very complex ones. 
- Apply techniques like regularization, which controls the complexity of the model. 
- Collect more training data if possible. 
- Use cross-validation, where the data is tested in different folds to check stability. 

4. Splitting Training Data & Test Data 

- **Training Data**: Used to teach the model. 
- **Test Data**: Used at the end to check how well the model performs on new information. 

**Typical split:** 80% training / 20% testing.  
**Why:** Prevents overfitting and ensures generalization.

5. Case Study: Machine Learning in Healthcare 

**Study used:** “Dermatologist-level classification of skin cancer with deep neural networks” (Esteva et al., Nature, 2017).  

**Summary:**  
A deep learning model was trained on 129,000+ images of skin lesions, labelled with disease type.  
It was tested against dermatologists and performed at a similar expert level.  

**Importance:**  
ML can support doctors with fast and accurate preliminary diagnosis, especially in areas lacking specialists.  

### References  

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.  
- Esteva, A., Kuprel, B., Novoa, R. A., et al. (2017). *Dermatologist-level classification of skin cancer with deep neural networks*. Nature, 542, 115–118.  
- Géron, A. (2019). *Hands-On Machine Learning with Scikit-Learn and TensorFlow*. O’Reilly Media.  
- Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning*. Springer.  
- Kamilaris, A., & Prenafeta-Boldú, F. X. (2018). *Deep learning in agriculture: A survey*. Computers and Electronics in Agriculture, 147, 70–90.  
- Kohavi, R. (1995). *A study of cross-validation and bootstrap for accuracy estimation and model selection*. IJCAI.  
- Mitchell, T. M. (1997). *Machine Learning*. McGraw-Hill.  
- Scikit-learn Documentation: https://scikit-learn.org
