# Spam Detection Project

This folder contains my work for **Assignment 6 – Spam Detection Comparison**. The project explores and compares three machine learning models for SMS spam detection: Logistic Regression, Random Forest, and Naive Bayes.

## Contents

- **spam_detection.ipynb**  
  Jupyter Notebook with all code for loading data, preprocessing, feature extraction, model training, evaluation, and sample predictions.  
  - Compares Logistic Regression, Random Forest, and Naive Bayes classifiers  
  - Shows performance metrics and confusion matrices  
  - Includes single-message predictions for sample texts

- **reflection_paper.md**  
  A short reflection paper (1–2 pages) discussing:
  - What I implemented in the project
  - Comparison of the three models and their predictions
  - Explanation of Naive Bayes and its use in spam detection
  - Discussion of evaluation metrics and confusion matrix results
  - My findings and recommendation for the best model

## How to Use

1. **Open `spam_detection.ipynb`**  
   - Run the notebook cell by cell to see the full workflow, results, and sample predictions.

2. **Read `reflection_paper.md`**  
   - Review my analysis, model comparison, and conclusions.

## Dataset

- The project uses `mail_l7_dataset.csv` (provided in class), which contains SMS messages labeled as "spam" or "ham".

## Requirements

- Python 3.x
- pandas, numpy, scikit-learn
- Jupyter Notebook

Install requirements (if needed):
```bash
pip install pandas numpy scikit-learn notebook
```

---

**Author:** Saara Iidle  
**Course:** Machine Learning  
**Assignment:** 6 – Spam Detection Comparison