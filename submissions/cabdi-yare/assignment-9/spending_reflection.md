#  Reflection – Spending Pattern Analysis with K-Means

##  What I Did  
In this project, I carried out *K-Means clustering* to analyze customer spending patterns using the features Income_$ and SpendingScore.  

###  Steps Followed  
1. *Data Cleaning & Preparation*  
   - Filled missing numeric values using the *median* to avoid bias from extreme values.  
   - Selected Income_$ and SpendingScore as the main features for segmentation.  

2. *Feature Scaling*  
   - Used *StandardScaler* to normalize the data.  
   - Scaling was essential because K-Means relies on distances.  

3. *Finding the Optimal K*  
   - Computed *SSE (Sum of Squared Errors)* for k = 1 to 10 and plotted the *elbow curve*.  
   - Calculated *Silhouette Scores* and *Davies–Bouldin Index (DBI)* for each k.  
   - Chose the value of *K* with the highest silhouette score and lowest DBI.  

4. *Model Training*  
   - Fit the *KMeans model* with the selected number of clusters.  
   - Assigned cluster labels to all customers.  

5. *Cluster Centers & Interpretation*  
   - Converted the cluster centers back to original units (Income, SpendingScore).  
   - Analyzed the results to understand customer groups.  

---

##  Choosing K  
The chosen K was *{best_k}*, because it:  
- Had the *highest Silhouette Score*  
- Showed a *clear elbow point* on the SSE curve  
- Had the *lowest Davies–Bouldin Index*, indicating well-separated clusters  

---

##  Cluster Insights  
Based on the cluster centers (Income / SpendingScore):  

- *Cluster 0 → Low Income / High Spending*  
  - These customers spend a lot despite lower income.  
  - *Action:* Provide loyalty discounts or special rewards.  

- *Cluster 1 → Medium Income / Medium Spending*  
  - Represent the "average" segment.  
  - *Action:* Run upsell and cross-sell campaigns.  

- *Cluster 2 → High Income / Low Spending*  
  - Wealthy but less engaged customers.  
  - *Action:* Offer premium products or retention programs.  

> You can adjust these insights based on your actual cluster centers.

---

##  Limitations  
- Only two features were used: Income_$ and SpendingScore.  
- K-Means assumes clusters are spherical, which might not reflect real customer behavior.  
- Other factors like age, visit frequency, and online activity were not included.  

---

##  Next Steps  
- *Add more features:* Age, VisitsPerMonth, OnlinePurchases for better segmentation.  
- *Try different algorithms:*  
  - K-Means with more than two features  
  - *DBSCAN* for density-based clusters  
  - *Hierarchical Clustering* for deeper insights  

---

##  Key Learning  
- Learned the importance of *feature scaling* in clustering.  
- Discovered how to evaluate clustering quality using *SSE, Silhouette Score, and DBI*.  
- Understood that *interpretation* is crucial — clusters must have a clear business meaning.