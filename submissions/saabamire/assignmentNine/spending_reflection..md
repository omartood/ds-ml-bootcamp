# Reflection Paper – Spending clustering with K-Means  

## 1. What did you implement?  
In this assignment, I used **K-Means clustering** to group customers by their **Income** and **Spending Score**.  
I prepared the data by filling missing values (if any) with the **median** and scaling the features with **StandardScaler**.  
Then, I tried **different values of k (1 to 10)** and printed the **SSE (Elbow Method)** to find the best number of clusters.  
After that, I trained the K-Means model with the chosen `k`, added a new column **Cluster** to the dataset, and saved the results into `spending_labeled_clusters.csv`.  
Finally, I checked the cluster quality using **Silhouette Score** and **Davies–Bouldin Index (DBI)**, printed cluster centers, and did a small **sanity check** with sample customers.  

---

## 2. Choosing K  
I chose **k = 4**.  
The reasons are:  
- From the **SSE values**, the elbow point was clear around 4.  
- The **Silhouette Score** was good (0.73), meaning the clusters are well separated.  
- The **DBI** was low ( 0.39), meaning the clusters are compact and clear.  

So, **4 clusters** gave a good balance of quality and simplicity.  

---

## 3. Cluster Interpretation (with Sanity Check)  

Here is the **sanity check sample (6 customers)** from the dataset:  

| Customer (Index) | Income_$ | SpendingScore | Cluster | Meaning |
|------------------|----------|---------------|---------|---------|
| 30 | 27 | 80 | 2 | Low income but high spending |
| 72 | 50 | 55 | 0 | Middle income and middle spending |
| 106 | 31 | 26 | 1 | Low income and low spending |
| 56 | 57 | 38 | 0 | Middle income and middle spending |
| 178 | 92 | 81 | 3 | High income and high spending |
| 28 | 23 | 92 | 2 | Very low income but very high spending |

### My interpretation of the clusters:  

1. **Cluster 0 – Middle Income / Middle Spending**  
 
    Business action: Keep them with normal offers, maybe cross-sell products.  

2. **Cluster 1 – Low Income / Low Spending**  
    
    Business action: Give small discounts to motivate spending.  

3. **Cluster 2 – Low Income / High Spending**  
  
   Business action: Reward them with loyalty points because they spend a lot even with low income.  

4. **Cluster 3 – High Income / High Spending**  
   
    Business action: Offer premium products, VIP service, and keep them happy.  

---

## 4. Limitations & Next Steps  
In this assignment only used two features (**Income** and **Spending Score**). In real life, spending behavior is affected by more things like ** Number of Visits, or Online Purchases**. Adding these features would make the groups more accurate and useful.  

**Next step:** I would add **Online Purchases** as another feature and also try other clustering methods like **DBSCAN** or **Hierarchical Clustering** to compare results.  

