# Machine Learning Assignment

## 1. Define Machine Learning using a real-life example
*Definition:*  
Machine learning is a subset of artificial intelligence that uses algorithms trained on data to create self-learning models.  

*Example Applications:*  
- Stock price prediction  

---

## 2. Compare Supervised Learning and Unsupervised Learning

### Supervised Learning
- *Definition:* Uses labeled datasets to train algorithms to classify data and predict outcomes.  
- *Types:* Regression, Classification  
- *Example:* Fruit sorting (healthy vs damaged)  
- *Goal:* Prediction  

### Unsupervised Learning
- *Definition:* Works with data that does not contain labels or explicit instructions.  
- *Types:* Clustering, Dimensionality Reduction  
- *Example:* Fraud detection / anomaly detection  
- *Goal:* Find hidden patterns  

---

## 3. What causes Overfitting? How can it be prevented?

*Overfitting:*  
When a model fits the training data too closely, it fails to generalize to new, unseen data.  

*Prevention Methods:*  
- Split data: train, validate, test  
- Cross-validation  
- Feature selection  
- Dropout (for neural networks)  
- Collect more data  

---

## 4. Explain how training data and test data are split, and why this process is necessary

- *Training Data:* Used to teach the machine learning model.  
- *Test Data:* A separate dataset the model has never seen before.  

*Typical Split:*  
- Training Set: ~70–80%  
- Test Set: ~20–30%  

*Why it’s necessary:*  
- *Avoid Overfitting:* Prevents the model from memorizing instead of learning.  
- *Generalization Check:* Ensures the model performs well on unseen data.  
- *Fair Evaluation:* Measures true model performance without bias.  

---

## 5. Case Study: Machine Learning in Transportation

*Case Study Title:*  
Predicting Public Transport Ridership Loss During Crises  

*Source:*  
European Transport Research Review (2025) —  
“Machine learning framework to estimate ridership loss in public transport during external crises: case study of bus network in Stockholm”  

*What the Study Did:*  
- Built an ML framework to forecast ridership and financial losses during crises.  
- Used 10 years of Stockholm bus network data (line number 4).  
- Tested 7 algorithms:  
  - Multiple Linear Regression  
  - Decision Tree  
  - Random Forest  
  - Bayesian Ridge Regression  
  - Neural Networks  
  - Support Vector Regression  
  - k-Nearest Neighbors (kNN)  
- Applied *10-fold cross-validation* to evaluate performance.  

*Key Findings:*  
- *kNN* was the most accurate (average R² = 0.65).  
- Predicted ridership losses during COVID-19:  
  - 2020: ~49% decline  
  - 2021: ~82% decline  
- Predictions matched passenger count & ticket validation records.  

*Why This Matters:*  
- Provides actionable insights for transit planners.  
- Supports crisis preparedness and decision-making.  
- Flexible model: Can be adapted to other networks and crises.  

---
