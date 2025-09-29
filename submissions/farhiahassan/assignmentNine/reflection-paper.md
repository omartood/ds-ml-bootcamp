# Part B – Reflection Paper

## 1. What I Implemented

I implemented a **K-Means clustering workflow** on customer data to segment them based on **Income** and **Spending Score**. The workflow included:

1. **Feature Selection** – Selected `Income_$` and `SpendingScore` as the key variables for clustering.  
2. **Scaling** – Standardized the features using `StandardScaler` to ensure both features contribute equally to the distance calculations.  
3. **K-Means Clustering** – Applied the `KMeans` algorithm with multiple values of `K` to identify patterns in customer behavior.  
4. **Evaluation Metrics** – Calculated **Silhouette Score** (measures cluster cohesion and separation) and **Davies–Bouldin Index** (measures cluster similarity) to assess cluster quality.  
5. **Labeling** – Assigned cluster labels to each customer for analysis and interpretation.

---

## 2. Choosing K

I selected **K = 4** clusters because:

- The **SSE (Sum of Squared Errors)** plot showed an "elbow" at 4, indicating diminishing returns for higher K.  
- **Silhouette Score** was reasonably high (~0.729), suggesting that clusters are fairly well separated.  
- **Davies–Bouldin Index** was low (~0.387), indicating clusters are compact and distinct.  

This combination of metrics justified the choice of 4 clusters.

---

## 3. Cluster Interpretation

Based on the clustering results, the segments can be described as:

1. **Cluster 0 – Low Income / High Spending**  
   - These customers have lower income but tend to spend a lot.  
   - **Business Action:** Offer **loyalty programs** to encourage repeat purchases.

2. **Cluster 1 – High Income / High Spending**  
   - Wealthier customers with strong spending habits.  
   - **Business Action:** Provide **upsell or premium offers** for high-value products.

3. **Cluster 2 – Low Income / Low Spending**  
   - Customers with limited income and spending.  
   - **Business Action:** Focus on **retention and cost-effective promotions** to keep them engaged.

4. **Cluster 3 – Moderate Income / Moderate Spending**  
   - Middle-tier customers in both income and spending.  
   - **Business Action:** Encourage **cross-selling or bundle deals** to increase revenue.

---

## 4. Limitations & Next Steps

**Limitations:**

- Only two features (`Income_$` and `SpendingScore`) were used, which may oversimplify customer behavior.  
- Other important factors like **Age**, **VisitsPerMonth**, and **OnlinePurchases** could provide better segmentation.

**Next Steps:**

- Include 1–2 additional features (e.g., Age, OnlinePurchases) to improve clustering.  
- Experiment with other clustering algorithms like **DBSCAN** to detect irregularly shaped clusters.  
- Test different scaling methods or feature transformations to improve cluster quality metrics.

---

**Conclusion:**  
K-Means clustering successfully segmented customers into meaningful groups. The clusters provide actionable insights for targeted marketing and business strategies, though incorporating more features could yield even richer segmentation.
