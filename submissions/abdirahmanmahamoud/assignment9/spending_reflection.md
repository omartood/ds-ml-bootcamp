# Spending Pattern Analysis – Reflection Paper

## 1. What did you implement?

In this assignment, I implemented a customer segmentation workflow using **K-Means clustering** on the features `Income_$` and `SpendingScore`.  
The main steps I followed were:

- **Data preparation**: I selected the two numeric features, handled any missing values with the **median**, and scaled them using `StandardScaler`.
- **SSE loop (Elbow method)**: I trained KMeans models with values of `k` from 1 to 10 and printed the corresponding Sum of Squared Errors (SSE). This helped me to observe how the error decreases with more clusters.
- **Model training**: Based on the elbow trend, I selected **K = 4** clusters and trained the final model with `random_state=42`.
- **Evaluation**: I computed and printed two metrics: **Silhouette Score** and **Davies–Bouldin Index**.
- **Labeling**: The final cluster labels were added as a new column (`Cluster`) to the dataset, and the file was saved as `spending_labeled_clusters.csv`.

---

## 2. Choosing K

I chose **K = 4** clusters. The reasons for this decision were:

- From the **SSE elbow check**, the reduction in error stabilized after 4 clusters, suggesting diminishing returns beyond this point.
- The **Silhouette Score** was **0.729**, which is relatively close to +1, indicating well-separated clusters.
- The **Davies–Bouldin Index** was **0.387**, which is a low value, meaning the clusters were compact and distinct.

Together, these metrics confirmed that **4 clusters** was a good balance between separation and compactness.

---

## 3. Cluster Interpretation

Based on the cluster centers (in original units) and a quick sanity check of customer samples:

- **Cluster 0 (Medium Income / Medium Spending)**  
  Example: Income 65, Spending Score 54  
  _Interpretation_: Balanced customers, spending in line with their income.  
  _Business Action_: Target with upselling campaigns and premium recommendations.

- **Cluster 1 (Low Income / Low Spending)**  
  Example: Income 26, Spending Score 18  
  _Interpretation_: Budget-conscious customers with limited purchasing power.  
  _Business Action_: Provide discounts or budget-friendly bundles to retain them.

- **Cluster 2 (Low Income / High Spending)**  
  Example: Income 33, Spending Score 78  
  _Interpretation_: Customers spending more despite having low income.  
  _Business Action_: Offer loyalty rewards and personalized promotions to encourage repeat purchases.

- **Cluster 3 (High Income / Varied Spending)**  
  _Interpretation_: Customers with higher income but mixed spending patterns.  
  _Business Action_: Focus on premium offers, exclusive memberships, and long-term retention strategies.

---

## 4. Limitations & Next Steps

- **Limitations**: The dataset only had two features (`Income_$` and `SpendingScore`), which limits the depth of the segmentation. Important factors such as **Age**, **Number of Visits**, or **Online Purchases** could provide better insights into customer behavior.
- **Next Steps**: As a concrete improvement, I would add more features (e.g., Age or Purchase Frequency) and test alternative clustering methods like **DBSCAN** or **Hierarchical Clustering** to see if they reveal more natural groupings.

---

## Conclusion

This analysis demonstrated how K-Means can effectively segment customers into meaningful groups. With **K = 4**, the model achieved good separation (Silhouette Score = 0.729, DBI = 0.387) and produced clusters that can guide actionable business strategies.
