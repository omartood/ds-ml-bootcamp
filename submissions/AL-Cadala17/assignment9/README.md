# ✍️ Assignment 9: Spending Pattern Analysis with K-Means

---

## 1. 📋 Overview

This project focuses on the practical application of the **K-Means clustering algorithm** for customer segmentation. The main objective was to analyze a customer dataset and group individuals into distinct clusters based on their `Income_$` and `SpendingScore`. The goal is to identify meaningful customer personas that a business can use for targeted marketing strategies.

---

## 2. 🎯 Key Objectives

The following key objectives were successfully completed in this assignment:

* **Data Preparation**: The dataset was loaded, and the `Income_$` and `SpendingScore` features were selected, preprocessed, and scaled using `StandardScaler`.
* **Optimal K Selection**: The **Elbow Method** was used to determine the best number of clusters (K) by calculating the Sum of Squared Errors (SSE) for K values from 1 to 10.
* **Model Training**: A `KMeans` model was built and trained using the optimal K value of 4, and each customer in the dataset was assigned a cluster label.
* **Performance Evaluation**: The quality of the resulting clusters was evaluated using the **Silhouette Score** and the **Davies-Bouldin Index (DBI)**.
* **Analysis and Interpretation**: The cluster centers were analyzed to create distinct customer personas, and a sanity check was performed on random samples to validate the model's logic.

---

## 3. 📂 Included Files

This submission includes the following files:

* `spending_l9_dataset.csv`: The original, raw dataset used for the analysis.
* `spending_clustering.ipynb`: The Jupyter Notebook containing all the code for data preparation, model training, evaluation, and analysis.
* `spending_labeled_clusters.csv`: The final output dataset with a new `Cluster` column indicating the assigned segment for each customer.
* `spending_reflection.md`: The detailed reflection paper summarizing the project's findings, cluster interpretations, and next steps.