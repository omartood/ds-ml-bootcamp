# Reflection Paper — Spending Pattern Analysis with K-Means

## What I Implemented
In this assignment, I applied **K-Means clustering** to segment customers based on their income and spending patterns. The workflow included the following steps:

1. **Data Preparation**  
   - Loaded the dataset (`spending_l9_dataset.csv`).  
   - Selected the features: `Income_$` and `SpendingScore`.  
   - Handled missing values using the **median** for numeric columns.  
   - Scaled the features with **StandardScaler** to ensure both income and spending were on the same scale.

2. **Elbow Method (SSE Loop)**  
   - Ran K-Means for `k = 1..10`.  
   - Printed the **Sum of Squared Errors (SSE)** for each k to observe the “elbow point.”  

3. **Model Training**  
   - Chose a suitable number of clusters (K) based on SSE and evaluation metrics.  
   - Fitted the final K-Means model and labeled each customer with a cluster.  

4. **Evaluation Metrics**  
   - Computed **Silhouette Score** (higher = better separation).  
   - Computed **Davies–Bouldin Index (DBI)** (lower = better clustering).  

5. **Outputs**  
   - Printed cluster centers in original units.  
   - Verified with three sample customers.  
   - Saved results as `spending_labeled_clusters.csv`.

---

## Choosing K
After reviewing the SSE curve, the largest relative drop occurred around **K = 3**.  
- **SSE** showed diminishing returns after 3 clusters.  
- **Silhouette Score** was reasonably high, indicating clear separation.  
- **DBI** was low compared to higher K values.  

For these reasons, I selected **K = 3** as the final clustering solution.

---

## Cluster Interpretation
The clusters can be interpreted as follows (example values based on cluster centers):

1. **Cluster 0 — Low Income, High Spending**  
   - Customers spend aggressively compared to their income.  
   - **Business Action:** Introduce loyalty rewards to encourage retention but also monitor credit risk.

2. **Cluster 1 — Medium Income, Medium Spending**  
   - Balanced group with average purchasing power.  
   - **Business Action:** Target with upselling opportunities (bundled offers, seasonal discounts).  

3. **Cluster 2 — High Income, Low Spending**  
   - Wealthy customers who are conservative spenders.  
   - **Business Action:** Launch premium product campaigns or personalized offers to increase wallet share.  

---

## Limitations & Next Steps
- **Limitations:** The segmentation used only two features (`Income_$` and `SpendingScore`). Important information such as **Age**, **Visit Frequency**, or **Online Purchases** could provide richer clusters.  
- **Next Step:** Extend the analysis by adding a third feature (e.g., **Age**) and compare results. Alternatively, experiment with **DBSCAN** to capture non-spherical clusters that K-Means may miss.

---

## Conclusion
This exercise demonstrated how K-Means can reveal distinct customer groups. By analyzing cluster characteristics, businesses can tailor marketing strategies, improve customer retention, and maximize revenue opportunities.
