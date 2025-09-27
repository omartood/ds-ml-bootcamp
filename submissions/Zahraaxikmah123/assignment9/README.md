# Assignment 9 – Spending Pattern Clustering

This repository contains my solution for **Assignment 9: Spending Pattern Analysis with K-Means Clustering**.

## Overview

The goal of this assignment was to segment customers based on their income and spending score using the K-Means clustering algorithm. The workflow included data preparation, feature scaling, elbow method for optimal cluster selection, model training, evaluation, and interpretation of results.

## Files

- **spending_clustering.ipynb** – Jupyter Notebook with all code, outputs, and step-by-step explanations.
- **spending_labeled_clusters.csv** – Output file with cluster labels for each customer.
- **spending_reflection.md** – Reflection paper discussing the workflow, cluster selection, interpretation, and next steps.

## Key Steps

1. **Data Loading:** Imported the dataset and selected relevant features.
2. **Preprocessing:** Handled missing values and scaled features.
3. **Elbow Method:** Used SSE to determine the best number of clusters.
4. **Clustering:** Trained K-Means and labeled each customer.
5. **Evaluation:** Calculated Silhouette Score and Davies-Bouldin Index.
6. **Interpretation:** Analyzed cluster centers and suggested business actions.
7. **Saving Results:** Exported the labeled dataset for further use.

## How to Run

1. Open `spending_clustering.ipynb` in Jupyter Notebook.
2. Run all cells step by step.
3. Review the outputs and saved files.

---

**Author:** [Saara Iidle]  
**Assignment:** Assignment 9 – Spending Pattern Clustering  
**Date:** 26 September 2025