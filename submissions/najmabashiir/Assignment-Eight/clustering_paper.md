# 📘 Lesson 8 — Clustering

## 1. Introduction to Clustering  
**Clustering** is an unsupervised learning method where data points are grouped into clusters based on similarity. The goal is to ensure that items within the same cluster are more similar to each other than to those in other clusters.  

- **Difference from supervised learning:**  
  - *Supervised learning* (classification, regression) requires labeled data (input + output).  
  - *Clustering* has no labels — the algorithm discovers natural groupings.  

**Examples:**  
- Clustering: A retailer segments customers into groups based on buying patterns.  
- Supervised: Predicting whether an email is spam or not (with labeled examples).  

---

## 2. Clustering Algorithms  

### 🔹 K-Means  
- **How it works:** Chooses `k` centroids randomly, assigns points to the nearest centroid, updates centroids, and repeats until stable.  
- **Use case:** Customer segmentation in marketing.  
- **Advantages:** Simple, fast, scalable.  
- **Limitations:** Must predefine `k`, sensitive to outliers, assumes spherical clusters.  

### 🔹 Hierarchical Clustering  
- **How it works:** Builds a tree (dendrogram) by either merging smaller clusters (agglomerative) or splitting larger ones (divisive).  
- **Use case:** Grouping genes with similar expression in biology.  
- **Advantages:** No need to specify `k` at the start, provides hierarchy of clusters.  
- **Limitations:** Computationally expensive, sensitive to noise.  

### 🔹 DBSCAN (Density-Based Spatial Clustering of Applications with Noise)  
- **How it works:** Groups together points that are closely packed, marking points in low-density areas as outliers.  
- **Use case:** Detecting fraudulent financial transactions.  
- **Advantages:** Finds arbitrarily shaped clusters, handles noise/outliers well.  
- **Limitations:** Performance drops in high dimensions, requires careful tuning of parameters (`eps`, `minPts`).  

---

## 3. Clustering Metrics  

### Elbow Method  
- **Measures:** Total within-cluster variance (inertia).  
- **Good value:** At the “elbow” point where adding more clusters gives diminishing returns.  
- **Usefulness:** Selecting `k` in K-Means.  

### Silhouette Score  
- **Measures:** How well a point fits within its cluster vs. nearest other cluster. Range: [-1, 1].  
- **Good value:** Close to **1** → well-clustered.  
- **Usefulness:** Comparing clustering quality across models.  

### Davies–Bouldin Index (DBI)  
- **Measures:** Average similarity ratio between clusters (intra/inter-cluster distance).  
- **Good value:** Lower DBI → better separation.  
- **Usefulness:** Evaluating separation and compactness.  

**Comparison Table:**  

| Metric            | Measures                        | Good Value | When Useful                  |
|-------------------|---------------------------------|------------|-------------------------------|
| Elbow Method      | Inertia vs. number of clusters | Elbow point| Choosing optimal `k`          |
| Silhouette Score  | Cohesion & separation           | Near 1     | Evaluating clustering quality |
| Davies–Bouldin    | Avg. cluster similarity         | Lower      | Checking separation/compactness|

---

## 4. Challenges in Clustering  
- **Harder than supervised learning:** No ground truth labels, so evaluating quality is subjective.  

**Common challenges:**  
1. **Choosing `k`:** Many algorithms (like K-Means) need the number of clusters upfront, which is not always obvious.  
2. **Handling noise/outliers:** Outliers can distort centroids and cluster assignments.  
3. **High-dimensional data:** Distance metrics become less meaningful (“curse of dimensionality”).  

---

## 5. Real-World Case Study — Customer Segmentation (Retail Industry)  
- **Goal:** A large retailer wanted to understand customer groups to design personalized marketing.  
- **Data:** Transaction history, demographics, frequency of visits.  
- **Model applied:** K-Means clustering on standardized purchase data.  
- **Results:** Found **4 main segments** (e.g., bargain shoppers, loyal customers, seasonal buyers, premium buyers). This allowed targeted promotions and increased customer engagement.  

---
