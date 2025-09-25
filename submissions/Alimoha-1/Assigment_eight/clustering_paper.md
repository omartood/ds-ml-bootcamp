# Lesson 8: Clustering (Unsupervised Learning)

## 1. Introduction to Clustering
Clustering is a technique in machine learning that organizes unlabeled data points into groups, or clusters, based on their similarity. Data points within the same cluster are more similar to each other than to those in other clusters. This is a core part of **unsupervised learning**, as it does not require pre-existing labels.

Unlike supervised learning, which uses labeled data to train a model, clustering works on unlabeled data. For example, a supervised model may predict house prices using historical data, while a clustering algorithm groups houses by shared characteristics (e.g., location, size, age), revealing natural groupings like "luxury homes" or "suburban family homes."

---

## 2. Clustering Algorithms

### **K-Means**
- **Idea:** Partition a dataset into a predefined number of clusters, `k`.  
- **Steps:**
  1. Randomly select `k` initial centroids.  
  2. Assign each data point to the nearest centroid.  
  3. Recalculate centroids as the mean of assigned points.  
  4. Repeat until centroids stabilize or max iterations are reached.  
- **Use Case:** Customer segmentation for targeted marketing.  
- **Advantages:** Efficient, simple, scalable.  
- **Limitations:** Requires predefining `k`, sensitive to noise/outliers, assumes spherical clusters.

### **Hierarchical Clustering**
- **Idea:** Builds a tree-like hierarchy of clusters (**dendrogram**).  
- **Types:**
  - **Agglomerative (Bottom-Up):** Start with each point as its own cluster and merge iteratively.  
  - **Divisive (Top-Down):** Start with all points in one cluster and split recursively.  
- **Use Case:** Genomic research to group genes by expression patterns.  
- **Advantages:** Visual dendrogram, no need to predefine clusters.  
- **Limitations:** Computationally expensive, sensitive to distance metric and linkage method.

### **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**
- **Idea:** Groups points in high-density areas, marks isolated points as outliers.  
- **Point Types:**
  - **Core Points:** ≥ minPts within epsilon radius.  
  - **Border Points:** Within epsilon of a core point.  
  - **Noise Points:** Neither core nor border.  
- **Use Case:** Anomaly detection in manufacturing.  
- **Advantages:** Can find arbitrarily shaped clusters, robust to noise, no need to specify number of clusters.  
- **Limitations:** Poor performance with varying cluster densities, sensitive to epsilon and minPts.

---

## 3. Clustering Metrics

| Metric | What It Measures | Good Value | When Useful |
|--------|----------------|------------|------------|
| **Elbow Method** | Optimal number of clusters (`k`) | Elbow point on WCSS plot | Determining `k` for K-Means |
| **Silhouette Score** | How well points fit in clusters | Close to +1 | Evaluating quality for known `k` |
| **Davies–Bouldin Index** | Average similarity between clusters | Close to 0 | Comparing clustering results |

- **Elbow Method:** Plots WCSS vs `k`; the "elbow" suggests optimal `k`.  
- **Silhouette Score:** Measures cohesion and separation (-1 to 1). High score = well-clustered.  
- **Davies–Bouldin Index:** Lower value = compact, well-separated clusters.

---

## 4. Challenges in Clustering
1. **Choosing `k`:** Difficult without prior knowledge. Methods like Elbow or Silhouette may give ambiguous results.  
2. **High-Dimensional Data:** Distance metrics become less meaningful (curse of dimensionality), reducing clustering effectiveness.

---

## 5. Real-World Case Study: Customer Segmentation in Retail

### **Goal**
Understand customer behavior to improve marketing efficiency with targeted strategies.

### **Data Used**
- Customer ID  
- Transaction dates  
- Purchase amounts  
- Product categories  
- Frequency & recency of purchases

### **Clustering Model**
- **Algorithm:** K-Means  
- **Number of clusters (`k`):** 4 (chosen using Elbow & Silhouette)  

### **Results / Insights**
1. **New Shoppers:** Recent purchase, low frequency → targeted ads.  
2. **Loyal Spenders:** Frequent, high-value purchases → special promotions.  
3. **Bargain Hunters:** Infrequent, low-value → discount campaigns.  
4. **Dormant Customers:** Long time without purchase → reactivation offers.  

**Outcome:** Tailored marketing led to increased customer engagement and higher ROI.
