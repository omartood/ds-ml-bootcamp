# Clustering (Unsupervised Learning)

---

## Clustering  

Clustering is a task that partitions or groups data points according to their similarities or dissimilarities. It aims at unlabelled data grouping and categorization into meaningful structures or patterns. The following are several types of clustering algorithms:



**How is it different from supervised learning (regression/classification)**

Supervised learning uses labelled data for tasks like classification, while unsupervised learning identifies patterns in unlabelled data. Each approach has its strengths, as supervised learning excels in a more precise task, while unsupervised learning is useful when hidden structures are not found.

**one real-life example of clustering and one of supervised learning.**

- **Clustering:** **customer segmentation**. A retail company can analyze transaction data to group customers into clusters such as frequent buyers, occasional shoppers, and discount seekers. This helps tailor marketing strategies to each group.  
- **Supervised Learning:** A common use of supervised learning is **email spam detection**. Algorithms are trained on labeled datasets containing examples of spam and non-spam emails. The model learns to classify new emails based on features like keywords and sender information.  

---

## Clustering Algorithms  

### K-Means Clustering  
K-Means is one of the most widely used clustering algorithms due to its simplicity and efficiency. This centroid-based method organizes data points around central vectors (centroids) that represent clusters.  

**How it works:**  
1. Randomly initialize *k* centroids.  
2. Assign each data point to its nearest centroid.  
3. Recalculate the centroids based on assigned points.  
4. Repeat until convergence or the maximum iterations are reached.  

**Use case:** Customer segmentation in retail to group buyers by purchasing behavior.  

**Advantages:**  
- Simple and computationally efficient.  
- Works well on large datasets.  

**Limitations:**  
- Requires specifying *k* in advance.  
- Sensitive to outliers.  
- Works best for spherical clusters of similar size.  

---

### Hierarchical Clustering  
Hierarchical clustering builds a tree-like structure of clusters that shows relationships at multiple levels.  

**How it works:**  
- *Agglomerative clustering* (bottom-up): Each point starts as its own cluster, and similar clusters are merged iteratively.  
- *Divisive clustering* (top-down): All data starts in one cluster, which is then recursively split into smaller groups.  

**Use case:** Document clustering in digital libraries or research databases.  

**Advantages:**  
- No need to specify the number of clusters in advance.  
- Produces interpretable dendrograms.  

**Limitations:**  
- Computationally expensive for large datasets.  
- Sensitive to noisy data.  

---

### DBSCAN (Density-Based Spatial Clustering of Applications with Noise)  
DBSCAN identifies clusters as dense regions separated by areas of lower density.  

**How it works:**  
- Groups points that are within a given distance (*ε*) and have at least *minPts* neighbors.  
- Finds clusters of arbitrary shapes.  
- Marks points in sparse regions as outliers.  

**Use case:** Fraud detection in credit card transactions.  

**Advantages:**  
- Can detect clusters of arbitrary shapes.  
- Handles noise and outliers well.  
- Does not require specifying the number of clusters beforehand.  

**Limitations:**  
- Choice of parameters (*ε* and *minPts*) greatly affects results.  
- Struggles with datasets of varying densities.  

---

## Clustering Metrics  
 

### Silhouette Score  
The Silhouette Score measures how well data points are grouped within their clusters compared to other clusters.  
- Ranges from -1 to 1.  
- Close to 1: Points fit well in their cluster.  
- Close to 0: Points lie between two clusters.  
- Close to -1: Points may be in the wrong cluster.  

### Davies–Bouldin Index (DBI)  
The DBI evaluates the average similarity between clusters by comparing intra-cluster compactness with inter-cluster separation.  
- Lower values = better clustering.  
- Higher values = overlapping or poorly separated clusters.  

### Elbow Method  
The Elbow Method is a visual approach for determining the optimal number of clusters (*k*). It plots the within-cluster variance (inertia) against *k*. The “elbow point” — where the decrease in variance slows down — indicates the best choice for *k*.  

---

### 📊 Comparison Table of Clustering Metrics  

| Metric              | What It Measures                              | Good Value             | When Useful                                |
|----------------------|-----------------------------------------------|------------------------|--------------------------------------------|
| Elbow Method        | Reduction in within-cluster variance vs. *k* | Elbow point            | Choosing the optimal number of clusters    |
| Silhouette Score    | Cohesion vs. separation of clusters           | Close to 1             | Comparing cluster quality across methods   |
| Davies–Bouldin Index| Compactness vs. separation of clusters        | Close to 0             | Evaluating compactness & separation        |

---

## Challenges in Clustering  

Clustering is considered harder than supervised learning because there are **no predefined labels** to verify the results. Success depends on the data structure and the algorithm’s assumptions.  

**Two common challenges include:**  

1. **Choosing the right number of clusters:**  
   Algorithms like K-Means require specifying *k* in advance. Choosing too few clusters oversimplifies, while too many clusters cause fragmentation. Metrics like the Elbow Method and Silhouette Score can help, but they may not always provide a clear answer.  

2. **Handling noise and outliers:**  
   Real-world datasets often contain anomalies. K-Means is highly sensitive to outliers, while DBSCAN handles them better but requires careful parameter tuning.  

3. **High-dimensional data (optional extra):**  
   As dimensions increase, distance measures become less meaningful (curse of dimensionality). Dimensionality reduction techniques such as PCA or t-SNE are often applied before clustering.  

---

## 5. Real-World Case Study: Customer Segmentation 

**Goal of the project:**  
To group customers into meaningful segments based on their demographic and purchasing behavior so that businesses can target each group with personalized strategies and improve marketing effectiveness.  

**Data they used:**  
A dataset of **2,240 customer records (29 features)** including details such as marital status, education, income, number and types of items purchased, and date of customer enrollment. After preprocessing (removing nulls, dropping irrelevant columns, and scaling), the dataset had **2,216 records**.  

**Clustering model applied:**  
- Data visualization was aided by **t-SNE** for dimensionality reduction.  
- Clustering was performed using **K-Means**, with the **Elbow Method** applied to determine the optimal number of clusters (*k ≈ 5–6*).  

**Key results or insights:**  
- Customers were divided into **5 clusters** with distinct purchasing behaviors.  
- Segmentation revealed groups such as high-income frequent buyers, discount-driven shoppers, and low-engagement customers.  
- Businesses could design **personalized ads, targeted promotions, and customer retention strategies**, leading to stronger growth and improved customer satisfaction.  

---

