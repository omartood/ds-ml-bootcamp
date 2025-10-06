# Introduction to Machine Learning

> Research-oriented summary, examples, and figures for classroom or assignment use.  
> **Author: Ali Omar Abdi**  
> Images referenced in this document are expected to be in images/lesson-one/:
> - ml.png (traditional programming vs machine learning)
> - cats-dogs.png (training → model → prediction example)
> - pneumonia-pipeline.png (suggested: X-ray training → model → prediction)

---

## Table of contents
- [Definition](#1-definition-of-machine-learning-with-a-real-life-example)
- [Supervised vs Unsupervised Learning](#2-supervised-vs-unsupervised-learning)
- [Overfitting — Causes & Prevention](#3-overfitting---causes--prevention)
- [Train / Validation / Test Splits](#4-train--validation--test-splits)
- [Case Study — Diabetic Retinopathy Detection](#5-case-study--diabetic-retinopathy-detection)
- [Figures](#figures)
- [References](#references)

---

## 1. Definition of Machine Learning (with a real-life example)

Machine Learning (ML) is a branch of artificial intelligence where computer systems learn patterns from data to make decisions or predictions without being explicitly programmed for each specific task. Instead of following fixed rules, these systems improve their performance through experience.

**Real-life example — Email Spam Detection**  
Modern spam filters use machine learning to analyze millions of emails labeled as spam or not spam. The system learns to recognize suspicious phrases, sender reputation, and formatting. As users mark emails, the filter adapts and improves, blocking unwanted messages more effectively.

---

## 2. Supervised vs Unsupervised Learning

**Supervised learning:**  
Uses labeled examples (input-output pairs) to learn a mapping from inputs to outputs.  
*Example:* Predicting pneumonia from labeled chest X-rays.

**Unsupervised learning:**  
Uses unlabeled data to discover hidden patterns or groupings.  
*Example:* Segmenting retail customers into groups based on purchase history.

| Aspect           | Supervised Learning         | Unsupervised Learning        |
|------------------|----------------------------|-----------------------------|
| Training Data    | Labeled (input-output)     | Unlabeled (input only)      |
| Goal             | Predict outcomes           | Discover patterns/groups    |
| Common Tasks     | Classification, Regression | Clustering, Dimensionality  |
| Evaluation       | Compare to known answers   | Assess pattern usefulness   |
| Examples         | Spam detection, Diagnosis  | Customer grouping, Anomaly  |

---

## 3. Overfitting — Causes & Prevention

**What is overfitting?**  
Overfitting occurs when a model learns the training data too closely, including its noise, and fails to generalize to new data.

**Common causes:**  
- Excessive model complexity  
- Limited training data  
- Noisy or unrepresentative data  
- Training for too many iterations

**Prevention strategies:**  
- Cross-validation  
- Regularization (L1, L2)  
- Early stopping  
- Data augmentation  
- Dropout (for neural networks)  
- Ensemble methods

---

## 4. Train / Validation / Test splits

**Why split?**  
Splitting data into training, validation, and test sets ensures honest evaluation. The training set teaches the model, the validation set tunes parameters, and the test set provides an unbiased performance estimate.

**Common strategies:**  
- Random split  
- Stratified split (maintain class balance)  
- Time-based split (for time series)  
- K-fold cross-validation

---

## 5. Case Study — Diabetic Retinopathy Detection

**Reference:** Gulshan, V., Peng, L., Coram, M., et al. (2016). "Development and Validation of a Deep Learning Algorithm for Detection of Diabetic Retinopathy." JAMA, 316(22), 2402-2410.

**Objective:**  
Develop a deep learning algorithm to detect diabetic retinopathy from retinal images.

**Data & methods:**  
- Dataset: 128,175 retinal images labeled by ophthalmologists  
- Model: Deep neural network trained to identify signs of retinopathy  
- Evaluation: Compared algorithm performance to eye specialists

**Key findings:**  
- The algorithm achieved sensitivity and specificity comparable to human experts  
- Enabled scalable, consistent screening in regions with limited access to eye care  
- Deployed in clinics in India and Thailand, screening thousands of patients

---

## Figures

> *Note:* Replace placeholders with actual images in images/lesson-one/ or correct paths as needed.

1. *Traditional programming vs. Machine Learning*  
   ![Traditional vs ML](images/lesson-one/ml.png)  
   Caption: Contrasting rule-based programming (data → program → output) with data-driven learning (data → model → output).

2. *Training → Model → Prediction (example)*  
   ![Training model prediction](images/lesson-one/cats-dogs.png)  
   Caption: Typical supervised pipeline: labeled training images → model learns distinguishing features → model predicts on new image.

3. *Pneumonia X-ray pipeline (suggested)*  
   ![Pneumonia pipeline](images/lesson-one/pneumonia-pipeline.png)  
   Caption: Training chest X-rays labeled by radiologists → CNN learns features → new X-ray → model predicts pneumonia probability.

---

## References

1. Gulshan, V., Peng, L., Coram, M., et al. (2016). "Development and Validation of a Deep Learning Algorithm for Detection of Diabetic Retinopathy." JAMA, 316(22), 2402-2410.
2. Mitchell, T. M. (1997). Machine Learning. McGraw-Hill.
3. Bishop, C. M. (2006). Pattern Recognition and Machine Learning. Springer.
4. Hastie, T., Tibshirani, R., & Friedman, J. (2009). The Elements of Statistical Learning. Springer.
5. Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep Learning. MIT Press.
6. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013). An Introduction to Statistical Learning. Springer.
7. Srivastava, N., Hinton, G., Krizhevsky, A., et al. (2014). "Dropout: A Simple Way to Prevent Neural Networks from Overfitting." JMLR, 15, 1929-1958.
8. Kohavi, R. (1995). "A Study of Cross-Validation and Bootstrap for Accuracy Estimation and Model Selection." IJCAI, 14(2), 1137-1145.
9. Google AI Blog. (2018). "Applying Deep Learning to Improve Eye Care in India and Globally."
10. Abràmoff, M. D., Lavin, P. T., Birch, M., et al. (2018). "Pivotal Trial of an Autonomous AI-based Diagnostic System for Detection of Diabetic Retinopathy." npj Digital Medicine, 1(39).

---

## License & notes
- This README is provided for educational use. If you include real patient X-rays or other sensitive clinical data when creating figures, ensure appropriate ethical approvals, anonymization, and licensing.
- To preview locally: open this README.md in a Markdown previewer (VS Code, GitHub, GitLab, or grip CLI).
