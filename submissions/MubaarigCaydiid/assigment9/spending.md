# K-Means Clustering Report

## 1. What Did You Implement?

I used **K-Means** to segment the data into meaningful groups. The workflow included:

### Scaling
I applied **standardization/normalization** so all features contribute equally to the clustering.

### SSE (Elbow Method)
I calculated **Sum of Squared Errors (SSE)** for different K values (K = 1–14) to identify the elbow point.

### Evaluation Metrics
- **Silhouette Score:** Measures how well each point fits within its assigned cluster. Higher is better.
- **Davies-Bouldin Index (DBI):** Measures cluster compactness and separation. Lower is better.

### Labeling
I assigned descriptive labels to the clusters for better business understanding.

## 2. Choosing K

Based on the metrics, the optimal K was **4**, showing a clear elbow in SSE, a good Silhouette Score, and a low DBI.

- **SSE (Elbow Curve):** The curve shows a distinct bend at K = 4.

## 3. Cluster Interpretation

### Cluster 1 – Low Income / Low Spending
- **Description:** Budget-conscious customers who spend very little.
- **Business Action:** Offer small discounts or promotions to increase spending.

### Cluster 2 – High Income / Low Spending
- **Description:** Customers with high income but low spending.
- **Business Action:** Provide moderate advertising to encourage more purchases.

### Cluster 3 – High Income / High Spending
- **Description:** VIP customers generating the most revenue.
- **Business Action:** Create loyalty programs, exclusive offers, or early access to products.

### Cluster 4 – Low Income / High Spending
- **Description:** Risky customers who might churn if not managed carefully.
- **Business Action:** Implement retention strategies like flexible payment plans or special offers.