#  Spending Clustering

## 1. What I Implemented  
In this project, I applied **K-Means clustering** to segment customers based on two features: **Annual Income** and **Spending Score**.  

- First, I scaled the features using **StandardScaler** to ensure both variables contributed equally.  
- Next, I ran a **loop for k = 1 to 10** and recorded the **SSE (inertia)** values to create an elbow curve.  
- I also computed **Silhouette Scores** and the **Davies–Bouldin Index (DBI)** for k = 2–5 to compare cluster quality.  
- After selecting the best k, I trained the final model, retrieved the cluster centers, and added a new **Cluster label** column to the dataset.  
- Finally, I saved the results into `spending_labeled_clusters.csv`.  

---

## 2. Choosing K  
I chose **k = 4** for the final model.  

- **SSE (Elbow method):** There was a sharp drop from k=1→4, and after that the curve flattened.  
- **Silhouette Score:** The highest score within k=2–5 was at k=4 (≈0.73), meaning the clusters were compact and well-separated.  
- **Davies–Bouldin Index (DBI):** DBI was lowest at k=4 (≈0.39), confirming good separation.  

Together, these metrics showed that **4 clusters** gave the best balance between compactness and separation.  

---

## 3. Cluster Interpretation  
Based on the centers (income vs spending), the four clusters can be interpreted as:  

1. **Cluster 0: Low Income, Low Spending**  
   - Customers with limited income and very cautious spending.  
   - **Business action:** Offer budget-friendly promotions to encourage small purchases.  

2. **Cluster 1: High Income, High Spending**  
   - Affluent customers who are willing to spend heavily.  
   - **Business action:** Target with premium loyalty programs and exclusive offers.  

3. **Cluster 2: Low Income, High Spending**  
   - Customers with lower income but high enthusiasm for spending.  
   - **Business action:** Introduce discounts or installment payment options to retain them.  

4. **Cluster 3: Mid Income, Mid Spending**  
   - Average customers with balanced income and spending.  
   - **Business action:** Upsell mid-range products and provide personalized recommendations.  

---

## 4. Limitations & Next Steps  
- **Limitations:**  
  The segmentation only uses **two features** (Income and Spending Score). This leaves out other important factors such as **Age, Gender, Frequency of Visits, Online Purchases, or Product Preferences**. Without these, the clusters may not fully capture real customer behavior.  

- **Next Steps:**  
  A clear improvement would be to **add a third feature (e.g., Age)** and test whether more meaningful clusters emerge.  
  Additionally, experimenting with **DBSCAN or Hierarchical Clustering** could provide alternative insights, especially for detecting non-spherical clusters.  

---