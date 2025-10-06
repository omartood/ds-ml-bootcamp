# Introduction to Machine Learning

> Research-oriented summary, examples, and figures for classroom or assignment use.  
> **Author: Ali Omar Abdi**  
> Images referenced in this document are expected to be in images/lesson-one/:
> - [Traditional programming vs machine learning](https://upload.wikimedia.org/wikipedia/commons/5/51/Machine_learning_vs_traditional_programming.png)
> - [Training → model → prediction example](https://upload.wikimedia.org/wikipedia/commons/6/69/Cats_and_dogs_training_example.png)
> - [Pneumonia pipeline](https://upload.wikimedia.org/wikipedia/commons/8/8c/Pneumonia_Xray_ML_pipeline.png)

---

## Table of contents
- [Definition](#1-definition-of-machine-learning-with-a-real-life-example)
- [Supervised vs Unsupervised Learning](#2-supervised-vs-unsupervised-learning)
- [Overfitting — Causes & Prevention](#3-overfitting---causes--prevention)
- [Train / Validation / Test Splits](#4-train--validation--test-splits)
- [Case Study — CheXNet (Pneumonia Detection)](#5-case-study--chexnet-pneumonia-detection)
- [Figures](#figures)
- [References](#references)

---

## 1. Definition of Machine Learning (with a real-life example)

*Definition (in my own words).*  
Machine Learning (ML) is a field of study in which algorithms automatically discover patterns from data to improve performance on a defined task without being explicitly programmed for every rule. An ML model generalizes patterns from past examples and applies those patterns to new, unseen cases.

*Real-life example — Chest X-ray pneumonia screening.*  
A convolutional neural network (CNN) can be trained on thousands of labeled chest X-rays (labels: Pneumonia / Normal). The model learns visual features associated with pneumonia (e.g., lung opacities) and can then flag new X-rays as likely pneumonia, supporting clinicians in triage and diagnosis.

---

## 2. Supervised vs Unsupervised Learning

*Short conceptual distinction:*

- *Supervised learning*: Uses labeled examples (x, y) to learn a mapping x → y. Typical tasks: classification and regression.  
  *Example:* Predicting pneumonia from labeled chest X-rays.

- *Unsupervised learning*: Uses unlabeled inputs x to discover structure, clusters, or reduced representations.  
  *Example:* Segmenting patients into subgroups using electronic health record (EHR) features (no labels).

*Comparison table*

| Aspect | Supervised learning | Unsupervised learning |
|---|---:|---|
| Input data | Labeled (input + target) | Unlabeled (only input) |
| Goal | Predict targets | Discover structure (clusters, latent factors) |
| Algorithms | Logistic regression, Random Forest, CNNs | K-means, PCA, Hierarchical clustering |
| Example | X-ray classification (Pneumonia/Normal) | Patient segmentation for targeted care |

---

## 3. Overfitting — causes & prevention

*What is overfitting?*  
Overfitting occurs when a model learns noise or idiosyncratic details in the training data instead of the underlying general pattern — resulting in low training error but poor performance on new data.

*Common causes*
- Model capacity too high relative to dataset size (e.g., complex deep networks on small datasets).
- Insufficient or unrepresentative training examples.
- Noisy labels or measurement errors.
- Data leakage (information used in training that wouldn’t be available at prediction time).

*Prevention strategies*
- *Regularization* (L1 / L2 penalties) to discourage extreme parameter values.
- *Early stopping* using a validation set.
- *Cross-validation* for robust performance estimation.
- *Data augmentation* or collecting more high-quality data.
- *Model simplification* and feature selection.
- *Ensembling* (bagging, boosting) to reduce variance.

---

## 4. Train / Validation / Test splits

*Why split?*  
Splitting data enables honest assessment of model generalization. The training set teaches the model; the validation set selects hyperparameters and controls early stopping; the test set gives the final unbiased performance estimate.

*Common strategies*
- *Simple split*: e.g., 80% train / 20% test.
- *Train / validation / test*: e.g., 60% / 20% / 20%.
- *k-fold cross-validation*: Rotate validation across k folds to maximize use of limited data.
- *Stratified splits*: Maintain class proportions for imbalanced classification.
- *Time-aware splits*: For temporal data, train on earlier time windows, test on later windows.

---

## 5. Case study — CheXNet: Radiologist-level pneumonia detection

*Reference:* Rajpurkar, P., Irvin, J., Zhu, K., et al. (2017). CheXNet: Radiologist-Level Pneumonia Detection on Chest X-Rays with Deep Learning. arXiv:1711.05225.

*Objective:*  
Train a deep neural network to detect pneumonia from frontal chest radiographs and compare performance to practicing radiologists.

*Data & methods:*  
- Dataset: ChestX-ray14 (>100k frontal chest X-rays, multiple pathology labels).  
- Model: DenseNet-121 convolutional neural network trained end-to-end to predict radiographic pathologies.  
- Evaluation: Compared model predictions vs. radiologist labels using metrics like AUC, sensitivity, specificity.

*Key findings:*  
- CheXNet achieved performance comparable to practicing radiologists for pneumonia detection on the evaluated test set.  
- The study demonstrates potential for automated screening/triage, particularly in resource-limited settings.  
- Authors highlighted the need for further prospective clinical validation and careful attention to generalization (different imaging devices, populations).

---

## Figures

> *Note:* All images below use public browser links for universal access.

1. *Traditional programming vs. Machine Learning*  
   ![Traditional vs ML](https://upload.wikimedia.org/wikipedia/commons/5/51/Machine_learning_vs_traditional_programming.png)  
   Caption: Contrasting rule-based programming (data → program → output) with data-driven learning (data → model → output).

2. *Training → Model → Prediction (example)*  
   ![Training model prediction](https://upload.wikimedia.org/wikipedia/commons/6/69/Cats_and_dogs_training_example.png)  
   Caption: Typical supervised pipeline: labeled training images → model learns distinguishing features → model predicts on new image.

3. *Pneumonia X-ray pipeline (suggested)*  
   ![Pneumonia pipeline](https://upload.wikimedia.org/wikipedia/commons/8/8c/Pneumonia_Xray_ML_pipeline.png)  
   Caption: Training chest X-rays labeled by radiologists → CNN learns features → new X-ray → model predicts pneumonia probability.

---

## References

1. Mitchell, T. M. (1997). Machine Learning. McGraw-Hill.  
2. Rajpurkar, P., Irvin, J., Zhu, K., et al. (2017). CheXNet: Radiologist-Level Pneumonia Detection on Chest X-Rays with Deep Learning. arXiv:1711.05225.  
   - URL: https://arxiv.org/abs/1711.05225  
3. Esteva, A., Robicquet, A., Ramsundar, B., et al. (2019). A guide to deep learning in healthcare. Nature Medicine, 25, 24–29.  
4. Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep Learning. MIT Press.

---

## License & notes
- This README is provided for educational use. If you include real patient X-rays or other sensitive clinical data when creating figures, ensure appropriate ethical approvals, anonymization, and licensing.
- To preview locally: open this README.md in a Markdown previewer (VS Code, GitHub, GitLab, or grip CLI).