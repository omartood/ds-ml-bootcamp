# Reflection Paper – K-Means Customer Segmentation

## Implementation Overview

In this project, I implemented a K-Means clustering workflow to segment customers based on their **Age**, **Income ($)**, and **Spending Score**. The workflow followed these main steps:

1. **Scaling** – All features were standardized using a scaler to ensure that differences in units (e.g., Age vs. Income) did not bias the clustering.
2. **K-Means Loop & SSE** – I evaluated multiple values of **K** using the Sum of Squared Errors (SSE) to identify the optimal number of clusters.  
3. **Metrics** – Each clustering result was evaluated using:
   - **Silhouette Score**: Measures cohesion vs. separation (closer to +1 is better).  
   - **Davies–Bouldin Index (DBI)**: Measures cluster similarity (lower is better).  
4. **Labeling** – Once the final **K** was chosen, each customer was assigned a cluster label, which was added to the dataset for interpretation.

---

## Choosing K

I selected **K = 4** based on the following criteria:

- **SSE (Elbow Method)** suggested diminishing returns after 4 clusters.  
- **Silhouette Score** was reasonably high, indicating good cluster separation:  
  **Silhouette Score: 0.697**
- **Davies–Bouldin Index** was relatively low, suggesting clusters were distinct:  
**DBI: 0.446**

This combination of metrics supported 4 as an optimal choice for capturing meaningful customer segments.

---

## Cluster Interpretation

Based on the cluster centers, each cluster can be described in plain language, with potential business actions:

| Cluster | Description                  | Business Action |
|---------|-----------------------------|----------------|
| 0       | Middle-aged, mid-income, moderate spenders | Offer targeted promotions to increase engagement and loyalty. |
| 1       | Older, low-income, low spenders | Focus on retention campaigns and budget-friendly deals. |
| 2       | Young, low-income, high spenders | Launch upsell campaigns or loyalty programs to maintain spending. |
| 3       | Middle-aged, high-income, high spenders | Offer premium products or exclusive memberships for upselling. |

A **sanity check** confirms these interpretations. For example, Cluster 2 includes young customers (ages 21–28) with low income but high spending scores, indicating strong engagement despite limited income.

---

## Limitations & Next Steps

**Limitations**:

- The dataset only includes Age, Income, and Spending Score. Additional variables like **Visits**, **Online Purchases**, or **Customer Loyalty** could improve segmentation.  
- K-Means assumes spherical clusters and may not capture irregular patterns in data.

**Next Steps**:

1. Test segmentation with additional features such as **Age × OnlinePurchases × Visits**.  
2. Experiment with **DBSCAN** or hierarchical clustering to detect clusters of varying shapes and densities.  
3. Analyze the effect of scaling and outliers on cluster quality for better robustness.
