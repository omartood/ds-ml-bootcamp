# Spending Pattern Clustering – Reflection Paper

## 1. What Did I Implement?

In this assignment, I implemented customer spending segmentation using the K-Means clustering algorithm on a dataset containing customer income and spending scores. My workflow included the following steps:

- **Data Loading:** I loaded the dataset and inspected the first few rows to understand the structure.
- **Feature Selection:** I selected `Income_$` and `SpendingScore` as the features for clustering.
- **Missing Value Handling:** I filled any missing numeric values with the median of each column to ensure the data was clean for clustering.
- **Feature Scaling:** I standardized the features using `StandardScaler` so that both features contributed equally to the clustering process.
- **Elbow Method (SSE Loop):** I ran K-Means for k values from 1 to 10, printing the Sum of Squared Errors (SSE) for each k to help determine the optimal number of clusters.
- **Model Training and Labeling:** Based on the SSE trend, I chose k=4 and fit the final K-Means model, assigning a cluster label to each customer.
- **Evaluation:** I calculated the Silhouette Score and Davies-Bouldin Index (DBI) to evaluate the quality of the clustering.
- **Cluster Centers:** I printed the cluster centers in the original units for interpretation.
- **Sanity Check:** I printed a few random customer samples with their assigned clusters.
- **Saving Results:** I saved the labeled dataset as `spending_labeled_clusters.csv`.

---

## 2. Choosing K

After running the elbow method, I observed the following SSE values:

```
k=1 → SSE=400.00
k=2 → SSE=199.70
k=3 → SSE=79.37
k=4 → SSE=21.37
k=5 → SSE=19.09
...
```

There was a significant drop in SSE up to k=4, after which the decrease became much smaller. This "elbow" at k=4 indicated that four clusters was a reasonable choice.

To further validate this, I checked the clustering metrics for k=4:
- **Silhouette Score:** 0.7286 (higher is better; this is a strong value) 👍
- **Davies-Bouldin Score:** 0.3871 (lower is better; this is also a strong value)

Both metrics confirmed that k=4 provided well-separated and compact clusters.

---

## 3. Cluster Interpretation

Based on the cluster centers and average feature values, the clusters can be interpreted as follows:

| Cluster | Income_$ | SpendingScore | Description                  | Suggested Business Action         |
|---------|----------|---------------|------------------------------|-----------------------------------|
|   0     | 56.32    | 53.58         | Moderate income, moderate spending | Offer standard loyalty programs   |
|   1     | 28.92    | 19.60         | Low income, low spending     | Send basic promotions or discounts|
|   2     | 24.14    | 83.10         | Low income, high spending    | Target with budget-friendly upsells|
|   3     | 99.16    | 79.24         | High income, high spending   | Premium offers, VIP experiences   |

- **Cluster 0:** Customers with average income and spending. They may respond well to general loyalty programs.
- **Cluster 1:** Customers with low income and low spending. They might be price-sensitive, so discounts or entry-level offers could be effective.
- **Cluster 2:** Customers with low income but high spending. These are valuable customers who may appreciate budget-friendly upsells or exclusive deals. 🛍️
- **Cluster 3:** Customers with high income and high spending. They are ideal for premium offers, VIP experiences, or exclusive memberships. 👑

---

## 4. Limitations & Next Steps

**Limitations:**
- The segmentation only used two features (`Income_$` and `SpendingScore`). Including more information such as `Age`, `VisitsPerMonth`, or `OnlinePurchases` could lead to more meaningful clusters.
- K-Means assumes clusters are spherical and similar in size, which may not always fit real-world data.

**Next Steps:**
- I can try clustering with three features (e.g., add `Age` to the analysis) to see if the segmentation improves.
- I can experiment with other clustering algorithms like DBSCAN, which can find clusters of arbitrary shape and handle noise/outliers better.
- I can visualize clusters using scatter plots or dimensionality reduction for better interpretation. 📈

---

**In summary,** this assignment helped me understand the practical workflow of clustering, from data preparation to model evaluation and interpretation. The results provide actionable insights for customer segmentation and targeted marketing. 🚀