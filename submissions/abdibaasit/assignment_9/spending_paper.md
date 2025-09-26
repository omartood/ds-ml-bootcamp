# Reflection Paper: K-Means Clustering

## What I Implemented
In this project, I applied the **K-Means clustering algorithm** to a dataset containing customer information.  
The workflow was as follows:

1. **Feature Selection** – I selected `Income` and `SpendingScore` as the main features.  
2. **Scaling** – Used `StandardScaler` so that both features had equal weight.  
3. **Elbow Method (SSE)** – Ran K-Means for k=1 to 10 and plotted the Sum of Squared Errors (SSE).  
4. **Model Training** – Chose `k=4` and fitted K-Means on the scaled data.  
5. **Evaluation** – Calculated metrics:  
   - Silhouette Score = **0.779** (good separation).  
   - Davies–Bouldin Index = **0.307** (low, meaning compact clusters).  
6. **Labeling** – Assigned each customer to a cluster and reviewed sample points.

---

## Choosing K
From the **SSE curve**, the “elbow” appeared around **k=4**, where adding more clusters gave only small improvements.  
The **Silhouette Score (0.779)** also showed that clusters were well separated, and the **DBI (0.307)** confirmed compactness.  
Therefore, I selected **k=4** as the best balance of performance and interpretability.  

---

## Cluster Interpretation
Using the cluster centers (income and spending score), the groups can be explained as:  

1. **Cluster 0 – Low Income, Low Spending**  
   - Customers with limited income and limited purchases.  
   - **Business Action**: Low priority; offer budget-friendly deals to retain.  

2. **Cluster 1 – High Income, High Spending**  
   - Wealthy and active customers.  
   - **Business Action**: VIP loyalty program and exclusive offers.  

3. **Cluster 2 – Low Income, High Spending**  
   - Customers spend a lot despite lower income.  
   - **Business Action**: Encourage retention with promotions or payment flexibility.  

4. **Cluster 3 – High Income, Low Spending**  
   - Customers have money but are not spending much.  
   - **Business Action**: Upsell through personalized recommendations and marketing.  

---

## Limitations & Next Steps
- **Missing Features**: I only used two variables (`Income`, `SpendingScore`). Including **Age, Visits per Month, or Online Purchases** could improve segmentation.  
- **Fixed K**: K-Means requires `k` in advance, which may not always be clear.  
- **Next Step**: Test with **three features** (e.g., add Age) or try a different algorithm such as **DBSCAN**, which can find clusters without predefining k.  

---

## Conclusion
K-Means clustering with k=4 gave a clear customer segmentation with good quality metrics.  
The clusters provide useful insights for targeted marketing strategies, but adding more features or testing other algorithms could improve the business value of the analysis.
