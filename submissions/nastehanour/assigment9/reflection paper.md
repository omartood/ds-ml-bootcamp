# Spending Pattern Analysis – Reflection Paper

## 1. Implementation
I performed **customer segmentation** using **K-Means clustering** on `Income_$` and `SpendingScore`.

**Steps followed:**
- **Data preparation**: Filled missing values with median and scaled the features.
- **Elbow method**: Tested K = 1–10 to identify the optimal number of clusters.
- **Model training**: Selected **K = 4** and trained the model with `random_state=42`.
- **Evaluation**: Calculated **Silhouette Score = 0.729** and **Davies–Bouldin Index = 0.387**.
- **Labeling**: Added cluster labels to the dataset and saved it as `spending_labeled_clusters.csv`.

---

## 2. Choosing K
**K = 4** was selected because:
- SSE reduction slowed after 4 clusters (Elbow method).
- Silhouette Score and Davies–Bouldin Index indicated well-separated, compact clusters.

---

## 3. Cluster Interpretation
| Cluster | Description | Business Action |
|---------|------------|----------------|
| 0 | Medium Income / Medium Spending | Promote upselling or premium products |
| 1 | Low Income / Low Spending | Offer discounts or affordable packages |
| 2 | Low Income / High Spending | Loyalty rewards and personalized promotions |
| 3 | High Income / Mixed Spending | Premium offerings, exclusive memberships |

---

## 4. Limitations & Future Work
- **Limitations**: Only two features (`Income_$`, `SpendingScore`) were used. Adding features like Age, Visit Frequency, or Online Purchases could provide deeper insights.
- **Future Work**: Include more features and experiment with alternative clustering methods such as **DBSCAN** or **Hierarchical Clustering**.

---

## Conclusion
**K-Means clustering** effectively segmented customers into meaningful groups. With **K = 4**, clusters were well-separated and provided actionable insights for business strategy.
