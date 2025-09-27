🎓 Assignment 9 – Spending Pattern Analysis with K-Means (Clustering)

Part B – Reflection Paper.


## 1. What did you implement?

I implemented a **K-Means clustering workflow** to segment customers based on their income and spending behavior.

- **Data Preparation**: Selected features (`Income_$`, `SpendingScore`), handled missing values using the **median**, and normalized features with **StandardScaler**.
- **Model Training**: Used the **Elbow Method** (SSE values for k=1 to 10) to identify a good number of clusters.
- **Clustering & Labeling**: Applied **K-Means with K=5**, added cluster labels to the dataset.
- **Evaluation**: Measured clustering quality with **Silhouette Score** (higher is better) and **Davies-Bouldin Index (DBI)** (lower is better).
- **Cluster Centers**: Converted cluster centroids back to original units for interpretation.
- **Sanity Check**: Verified results on a few sample rows and saved the labeled dataset.

---

## 2. Which K did you pick and why?

I picked **K = 5** clusters.  

- **SSE (Inertia)**: The elbow in the SSE curve appeared around **k=5**, indicating diminishing returns after that point.  
- **Silhouette Score**: The value was reasonably high (closer to +1), suggesting good separation between clusters.  
- **Davies-Bouldin Index (DBI)**: The DBI was relatively low (closer to 0), meaning clusters were compact and distinct.  

Together, these metrics supported that **K=5** provided a balanced segmentation.

---

## 3. Cluster Interpretation

Here’s a plain-language interpretation of the 5 clusters, with suggested business actions:

1. **Cluster 0 – Low Income / Low Spending**  
   - Customers have limited income and spend little.  
   - **Action**: Minimal marketing investment; consider low-cost promotions or awareness campaigns.

2. **Cluster 1 – Low Income / High Spending**  
   - Customers spend a lot despite low income.  
   - **Action**: Loyalty rewards or installment/discount options to retain them.

3. **Cluster 2 – High Income / Low Spending**  
   - Wealthy customers who spend cautiously.  
   - **Action**: Personalized premium offers or upselling strategies.

4. **Cluster 3 – High Income / High Spending**  
   - Best customers with both high income and spending.  
   - **Action**: VIP treatment, exclusive offers, retention programs.

5. **Cluster 4 – Middle Income / Moderate Spending**  
   - Average customers with balanced income and spending.  
   - **Action**: Targeted promotions to increase spending, cross-selling opportunities.

---

## 4. Limitations

- **Limitations**:  
  - Only **two features** (`Income_$`, `SpendingScore`) were used.  
  - This may oversimplify customer behavior.  
  - External factors like **Age**, **Visit Frequency**, **Online Purchases**, or **Tenure** could improve segmentation.  




