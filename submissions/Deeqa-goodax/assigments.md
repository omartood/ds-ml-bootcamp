# Research Assigment: Intorduction to machine learning
## 1. **Definition:**
Machine learning  (ML) is a field of Artificial Intelligence where computers learn from data and improve their performance being explicity programmed with step by step rules (mitchell, 1997).
Instead of following fixed instructions, ML systems analyze data, identify patterns, and make predictions.
** Real-life Examples:**
**Facial Recognition**: Smartphones unlock by learning patterns in a user’s face. 
**Product Recommendations**: Amazon or Netflix recommend items or shows by analyzing user behavior.
## 2. Supervised vs Unsupervised Learning With Examples 

### **Supervised Learning**
 Works with **labeled data** (inputs paired with the correct outputs).  
 The model “learns” by example, like a student guided by a teacher. 
 **Example:** Predicting animal species (elephant, camel, cow) from labeled pictures.  

### **Unsupervised Learning**
 Works with **unlabeled data** (no categories provided).  
The model finds hidden patterns or groups in the data. 
**Example:** Grouping animals based on traits (e.g., size, diet) without knowing their species beforehand.  ## 3. Overfitting in Machine Learning

**Definition:**  
Overfitting happens when a model performs very well on the training data but poorly on new, unseen data.  
It means the model has “memorized” the training examples instead of learning general patterns.  

**Causes of Overfitting:**  
 Too complex models (many features or parameters).  
 Too little training data.  
 Too many training epochs (over-training).  

**Prevention Techniques:**  
 **Early Stopping** – stop training before the model learns noise.  
 **Pruning/Feature Selection** – remove irrelevant features.  
 **Regularization** – penalize unnecessary complexity.  
 **Ensembling** – combine multiple weak models (e.g., bagging, boosting).  
 **Data Augmentation** – create variations of training data (e.g., flipping images)
## 4. Training Data vs Test Data Split

**Definition:**  
ML datasets are divided into:  
 **Training Data** → teaches the model.  
 **Test Data** → evaluates how well the model performs on new data.  

**Common Split Ratios:**  
70% training / 30% testing  
80% training / 20% testing  

**Why It’s Necessary:**  
Prevents **overfitting**.  
Ensures **generalization** to real-world problems.  
Provides a **fair evaluation** between models.  

**Example:**  
In a medical dataset of 1,000 patient records:  
800 are used to train a disease prediction model.  
200 are used to test if the model works on unseen patients. 
## 5. Case Study: Breast Cancer Detection Using Machine Learning

**Background:**  
Breast cancer is one of the leading causes of death among women. Early detection is crucial for effective treatment, but analyzing mammograms can be difficult even for expert radiologists.  

**ML Application:**  
Researchers applied **Support Vector Machines (SVM)** and **Convolutional Neural Networks (CNNs)** to classify mammogram images (Spanhol et al., 2016).  

**Findings:**  
ML models achieved diagnostic accuracy comparable to trained radiologists.  
CNNs were especially powerful, automatically detecting features in images.  
Reduced false negatives improved patient survival by ensuring earlier treatment.  

**Impact:**  
Machine learning is now widely used as a decision-support tool in medical imaging, helping doctors diagnose breast cancer more accurately and efficiently.  

# References

Géron, A. (2019). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*. O’Reilly Media.  
Kuhn, M., & Johnson, K. (2013). *Applied Predictive Modeling*. Springer.  
Mitchell, T. M. (1997). *Machine Learning*. McGraw-Hill.  
Raschka, S., & Mirjalili, V. (2019). *Python Machine Learning*. Packt Publishing.  
Spanhol, F. A., Oliveira, L. S., Petitjean, C., & Heutte, L. (2016). A dataset for breast cancer histopathological image classification. *IEEE Transactions on Biomedical Engineering*, 63(7), 1455–1462.
 
