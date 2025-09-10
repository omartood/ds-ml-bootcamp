---
title: "Research Assignment: Introduction to Machine Learning"
---

# 1. Define Machine Learning using a real-life example

Machine Learning (ML) is a field of Artificial Intelligence where
systems improve their performance by learning from data rather than
following strict human-coded rules. This enables computers to discover
patterns and make predictions.

Example: Fraud Detection in Banking

Banks use ML to detect fraudulent transactions. Instead of manually
programming thousands of rules, the ML model learns patterns from
millions of past transactions labeled as \'fraud\' or \'not fraud.\' The
model then automatically identifies suspicious behavior, such as unusual
purchases or sudden spending spikes.

# 2. Compare Supervised Learning and Unsupervised Learning

Supervised and Unsupervised learning differ mainly in the type of data
they use and the problems they solve.

  -----------------------------------------------------------------------
  Aspect                  Supervised Learning     Unsupervised Learning
  ----------------------- ----------------------- -----------------------
  Data                    Uses labeled data       Uses unlabeled data
                          (input + correct        (only inputs)
                          output)                 

  Goal                    Predict outcomes        Find hidden patterns
                          (classification,        (clustering,
                          regression)             dimensionality
                                                  reduction)

  Analogy                 Teacher gives both      Students explore
                          questions and answers   problems without
                                                  answers

  Example                 Loan approval           Customer segmentation
                          prediction              in marketing
  -----------------------------------------------------------------------

# 3. What causes Overfitting? How can it be prevented?

Overfitting happens when a model memorizes the training data instead of
learning general rules, leading to poor performance on unseen data.

  -----------------------------------------------------------------------
  Causes of Overfitting               Ways to Prevent Overfitting
  ----------------------------------- -----------------------------------
  Too many features or parameters     Use feature selection or
                                      dimensionality reduction

  Too little training data            Collect more data or use data
                                      augmentation

  Overly complex models               Use simpler models or apply
                                      regularization (L1, L2, dropout)

  Lack of validation                  Apply cross-validation to test
                                      generalization
  -----------------------------------------------------------------------

# 4. Training data vs Test data split

Datasets are divided to ensure models are evaluated on unseen data,
mimicking real-world scenarios.

  -----------------------------------------------------------------------
  Dataset Portion                     Purpose
  ----------------------------------- -----------------------------------
  Training Data                       Used to teach the model (like
                                      practice questions).

  Test Data                           Used to evaluate performance on new
                                      data (like an exam).
  -----------------------------------------------------------------------

Common split ratios: 80% training / 20% testing or 70/30. Sometimes, a
third set called validation data is included for model tuning.

# 5. Case Study: Application of Machine Learning in Business

Case: Customer Segmentation in Retail\
\
Objective: Businesses want to understand their customers to deliver
targeted marketing. Machine Learning helps divide customers into
meaningful groups based on shopping patterns.

Method:

A retail company collects data such as age, purchase frequency, and
spending habits. K-Means clustering (an unsupervised learning algorithm)
is applied to group customers into clusters: loyal high spenders,
occasional buyers, and new customers.

Findings & Impact:

Each group is targeted differently. High spenders get premium offers,
while new customers receive discounts. This personalized marketing
increased sales and customer loyalty.

# References

\- Bishop, C. M. (2006). Pattern Recognition and Machine Learning.
Springer.\
- Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep Learning. MIT
Press.\
- Research article: BMC Medical Informatics and Decision Making (2022),
application of ML in healthcare and business.
