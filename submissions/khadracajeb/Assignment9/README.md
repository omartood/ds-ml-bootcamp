# Assignment: Spending Pattern Analysis with K-Means (Clustering)

## Summary

This assignment focuses on segmenting customers based on their **Income_$** and **SpendingScore** using **K-Means clustering**. The practical workflow included:

- **Data preprocessing and scaling**  
- **Elbow method** to determine the optimal number of clusters  
- **Model training** with K-Means  
- **Evaluation** using Silhouette Score and Davies–Bouldin Index (DBI)  
- **Cluster interpretation** and business insights  
- **Saving** the labeled dataset for further analysis  

---

## Files Included

- **`spending_clustering.ipynb`**  
  Contains all code for:  
  - Loading and preprocessing the dataset (`spending_l9_dataset.csv`)  
  - Selecting and scaling features (`Income_$`, `SpendingScore`)  
  - Elbow method to find the best k (1–10)  
  - Training K-Means with the chosen k and labeling clusters  
  - Evaluating clustering with Silhouette Score and DBI  
  - Displaying cluster centers in original units  
  - Printing a sanity check for 3 customer samples  

- **`spending_labeled_clusters.csv`**  
  Dataset with an added `Cluster` column for each customer  

- **`spending_reflection.md`**  
  Reflection paper including:  
  - Implementation workflow  
  - Choosing k  
  - Cluster interpretation with business actions  
  - Limitations and next steps  

---

## Learning Outcomes

Through this assignment, I learned to:

- Handle missing values in numeric features using **median imputation**  
- **Standardize features** for clustering  
- Apply the **elbow method** for K-Means to determine the optimal number of clusters  
- Train K-Means and assign **cluster labels** to customers  
- Evaluate clustering quality using **Silhouette Score** and **DBI**  
- Interpret clusters and suggest actionable **business strategies**  
- Save labeled datasets for **future analysis**  

---

## Notes

- SSE values were printed for k = 1–10 to identify the “elbow” point  
- Based on the elbow and evaluation metrics, **k = 4** was selected as the optimal number of clusters  
- Cluster centers were analyzed in original units to provide **meaningful business insights**  
- Sanity checks confirmed that customers were correctly labeled  
- This practical workflow is reusable for other segmentation problems in **retail or marketing analytics**  

---

**Alhamdulillah for understanding and completing this assignment successfully!**  
