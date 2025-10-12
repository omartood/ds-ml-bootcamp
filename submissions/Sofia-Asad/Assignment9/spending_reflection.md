# Reflection Paper 

## What I Implemented
In this task, I applied **K-Means clustering** to a spending dataset using two features: **Income_$** and **SpendingScore**. First, I handled missing values by filling them with the median. Then, I used **StandardScaler** to normalize the data so that both features were on the same scale.  

Next, I performed a loop from **k=1 to k=9** to calculate the **SSE (inertia)** for each cluster size. This allowed me to observe the “elbow” shape and evaluate where clustering stabilized. After that, I ran K-Means with the chosen k value and added the cluster labels back into the original dataset.  

Finally, I evaluated the clustering using two metrics:
- **Silhouette Score** (higher is better, shows good separation between clusters)  
- **Davies–Bouldin Index (DBI)** (lower is better, shows compact and distinct clusters).  

I also calculated the **cluster centers** and converted them back to the original scale for interpretation.

---

## Choosing K
I selected **K = 4** clusters. The decision was based on:
- The **SSE elbow method**, which started to flatten around k=4.  
- The **Silhouette Score**, which showed reasonable separation at k=4.  
- The **DBI value**, which was relatively low compared to other choices, suggesting stable clusters.  

---

## Cluster Interpretation
Based on the cluster centers, the groups can be described in plain language:

1. **Low Income / Low Spending**  
   - Customers with limited income and spending.  
   - *Business Action:* Basic retention strategy, maybe keep them engaged with affordable offers.  

2. **Low Income / High Spending**  
   - Customers who spend a lot despite lower income.  
   - *Business Action:* Offer loyalty rewards to encourage repeat purchases.  

3. **High Income / Low Spending**  
   - Customers with money but low spending habits.  
   - *Business Action:* Targeted marketing or upselling campaigns to unlock their potential.  

4. **High Income / High Spending**  
   - Best customers with strong income and spending power.  
   - *Business Action:* Premium services, VIP programs, or exclusive offers to retain them.  

---

## Limitations & Next Steps
This clustering only used **two features** (Income and SpendingScore). In reality, segmentation could be improved by adding more information, such as:  
- Age groups  
- Frequency of store visits  
- Online purchases or browsing behavior  

### Next Step
A concrete next step would be to **add a third feature** (such as Age) and re-run K-Means to see if the clusters become more meaningful. Another option is to try a different clustering algorithm like **DBSCAN**, which can capture irregular cluster shapes.  
