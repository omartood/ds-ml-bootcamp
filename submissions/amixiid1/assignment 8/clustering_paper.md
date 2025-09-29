# Assingment 8 = Clustering (Unsupervised Learning)

## 1. Introduction to Clustering
Clustering is an **unsupervised learning technique** in Machine Learning that groups similar data points together based on their characteristics. The goal is to organize unlabeled data into meaningful clusters, such that data points within the same cluster are more similar to each other than to those in different clusters.

Unlike **supervised learning** methods such as regression or classification, clustering does not rely on labeled data. In supervised learning, models are trained on input–output pairs to make predictions, while clustering seeks to discover hidden patterns without prior knowledge of the output.

- **Real-life example of clustering**: Customer segmentation in marketing, where customers are grouped based on purchasing behavior.  
- **Real-life example of supervised learning**: Email spam detection, where emails are classified as “spam” or “not spam” using labeled data.

---

## 2. Clustering Algorithms

### a) K-Means
**How it works**:  
K-Means divides data into *k* clusters by minimizing the distance between points and the cluster centroids. The algorithm iteratively updates centroids until the clusters stabilize.

**Use case**: Customer segmentation in e-commerce.  
**Advantages**: Simple, efficient, works well for large datasets.  
**Limitations**: Requires the number of clusters (*k*) to be specified in advance; sensitive to outliers.

---

### b) Hierarchical Clustering
**How it works**:  
Builds a hierarchy of clusters either by merging smaller clusters (agglomerative) or by splitting larger clusters (divisive). Results are often visualized in a dendrogram.

**Use case**: Document clustering in text mining.  
**Advantages**: No need to pre-specify the number of clusters; produces interpretable hierarchical structures.  
**Limitations**: Computationally expensive for large datasets; sensitive to noise.

---

### c) DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
**How it works**:  
Groups points that are closely packed together (high density) and labels points in sparse regions as outliers. It uses two parameters: *eps* (neighborhood size) and *minPts* (minimum points to form a cluster).

**Use case**: Identifying geographic hotspots (e.g., crime or disease outbreak regions).  
**Advantages**: Can discover clusters of arbitrary shapes; handles noise and outliers well.  
**Limitations**: Struggles with varying densities; parameter tuning can be challenging.

---

## 3. Clustering Metrics

### a) Elbow Method
Measures the total within-cluster sum of squares (WCSS). The “elbow” point in the curve helps estimate the optimal number of clusters.

### b) Silhouette Score
Measures how well points fit within their cluster compared to neighboring clusters. Values range from **–1 to 1**, where higher scores indicate better clustering.

### c) Davies–Bouldin Index
Measures the average similarity between each cluster and its most similar one. Lower values indicate better clustering.

---

### 📊 Comparison Table of Clustering Metrics

| Metric             | What It Measures                           | Good Value            | When Useful                                  |
|--------------------|--------------------------------------------|-----------------------|-----------------------------------------------|
| Elbow Method       | Cluster compactness (WCSS)                 | Elbow point on curve  | Choosing number of clusters (K-Means)         |
| Silhouette Score   | Separation & cohesion of clusters          | Close to 1            | Comparing clustering quality across methods   |
| Davies–Bouldin     | Similarity between clusters                | Closer to 0           | Evaluating overlapping or compact clusters    |

---

## 4. Challenges in Clustering
Clustering is often considered harder than supervised learning because the data is **unlabeled**, making it difficult to evaluate and validate models objectively.

- **Choosing the right number of clusters**: Many algorithms (e.g., K-Means) require pre-specifying *k*, but the true number of clusters is often unknown.  
- **Handling noise and outliers**: Outliers can distort centroids and cluster boundaries.  
- **High-dimensional data**: In many datasets (e.g., text, genomics), the distance between points becomes less meaningful as dimensionality increases.

---

## 5. Real-World Case Study: Customer Segmentation in Retail
A well-known application of clustering is **customer segmentation** in retail and e-commerce.

- **Goal**: To divide customers into distinct groups for targeted marketing strategies.  
- **Data used**: Purchase histories, demographic information, and browsing behavior.  
- **Clustering model applied**: K-Means was applied to segment customers into groups such as “frequent buyers,” “discount seekers,” and “new customers.”  
- **Key results**: Retailers gained insights into customer behavior, allowing them to design personalized marketing campaigns and improve customer retention.

---

## References
- Aggarwal, C. C. (2015). *Data Mining: The Textbook*. Springer.  
- Jain, A. K. (2010). *Data clustering: 50 years beyond K-means*. Pattern Recognition Letters.  
- Han, J., Kamber, M., & Pei, J. (2012). *Data Mining: Concepts and Techniques*. Morgan Kaufmann.  
