# 1️⃣ K-Means Workflow Implementation

**Steps implemented:**

**Data preparation:**
- Selected features: `"Income_$"` and `"SpendingScore"`
- Checked for missing values and replaced them with median

**Scaling:**
- Used `StandardScaler()` to normalize the features
- Ensures K-Means treats both features equally

**Choosing K:**
- Ran K-Means for `k = 1 to 10` and plotted SSE (inertia) to see the “elbow” point

**Model fitting & labeling:**
- Fitted K-Means with `n_clusters = 4` and `random_state = 42`
- Assigned each customer to a cluster (`0, 1, 2, 3`) using `fit_predict()`

**Metrics:**
- **Silhouette Score** → 0.729 → indicates fairly well-separated clusters
- **Davies–Bouldin Index (DBI)** → 0.387 → lower value indicates good compactness and separation

**Sanity check:**
- Checked sample rows with their assigned cluster labels to ensure reasonable grouping

---

# 2️⃣ Choosing K

**Chosen K:** 4

**Why:**
- SSE elbow: noticeable drop until 4, then smaller improvements
- Silhouette score was highest near 4
- DBI was lowest at 4 → clusters are compact and well-separated

---

# 3️⃣ Cluster Interpretation

| Cluster | Description                   | Typical Features                     | Suggested Business Action                       |
|---------|-------------------------------|-------------------------------------|------------------------------------------------|
| 0       | Mid-value customers           | Moderate Income & Spending           | Offer cross-sell products to increase spending|
| 1       | Low-value customers           | Low Income & Spending, older         | Retention campaigns, discounts, or loyalty program |
| 2       | Young, active high-spenders   | Low Income but high Spending, young | Encourage repeat purchases, loyalty program   |
| 3       | High-value customers          | High Income & Spending, active      | Upsell premium products, priority offers      |

---

# 4️⃣ Limitations & Next Steps

**Limitations:**
- Only 2 features were used (`Income_$`, `SpendingScore`) → other features like `Age`, `VisitsPerMonth`, `OnlinePurchases` may improve segmentation
- K-Means assumes spherical clusters → may not capture irregular shapes

**Next steps:**
1. Try adding more features like `Age`, `VisitsPerMonth`, `OnlinePurchases`
2. Compare K-Means with DBSCAN or Hierarchical clustering
3. Visualize clusters in 2D/3D to confirm separation
