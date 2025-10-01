# Introduction to Clustering in Machine Learning

## 1. Clustering
- Clustering is a type of **machine learning** that belongs to **unsupervised learning**, which works with **unlabeled data** (output is unknown in advance).
- It groups data into different clusters (groups).
- **Regression** and **Classification** are types of **supervised learning**, where data is labeled (input and output are known).

### Real-world Examples
- **Clustering:** Customer segmentation, image segmentation
- **Supervised Learning:** Spam detection, house price prediction, car price prediction

## 2. Algorithms

### K-Means
- Groups data into clusters.
- **Example:** A company segments customers into high, medium, and low spenders.
- **Advantage:** Works well with spherical data.
- **Limitation:** Not suitable for data with irregular shapes.

### Hierarchical Clustering
- Creates a diagram showing how data is divided.
- **Advantage:** Handles outliers well and does not require specifying the number of clusters.
- **Limitation:** Computationally expensive and sensitive to noisy data.

### DBSCAN (Density-Based Clustering)
- Groups points in dense regions.
- Uses **epsilon** and **MinPts**.
- **Advantage:** Handles clusters of different shapes and outliers effectively.
- **Limitation:** Performs poorly with high-dimensional data.
- **Example:** Detecting fraudulent transactions.

## 3. Clustering Metrics

### Elbow Method
- Used to determine the optimal number of clusters.
- Measures how cluster centroids reduce distances between points.
- Look for the "elbow" in the graph.

### Silhouette Score
- Evaluates how well a sample fits within its cluster compared to others.
- **Range:** -1 to 1
  - Close to 1: Clear separation between clusters
  - Close to 0: Clusters are overlapping
  - Negative: Point may belong to the wrong cluster

### Davies–Bouldin Index (DBI)
- Measures cluster separation and compactness.
- **Range:** ≥ 0
  - Low value: Clusters are well separated
  - High value: Clusters overlap

## 4. Challenges in Clustering vs. Supervised Learning
- Supervised learning has labeled data; clustering only has features.
- Requires metrics like Silhouette and DBI instead of labels.

### Common Challenges
- **Choosing K:** Algorithms like K-Means need the number of clusters; methods like Elbow and Silhouette can help.
- **Handling Noise and Outliers:** Outliers can skew centroids (K-Means). DBSCAN handles outliers better.
- **High-dimensional Data:** Curse of dimensionality affects distance metrics; use cosine similarity for high dimensions.

## 5. Real-World Project Example
- **Objective:** Cluster people's health conditions based on disease presence using images.
- **Algorithm:** K-Means
- **Clusters:**
  - Cluster 1: Healthy individuals → Normal image features
  - Cluster 2: Low disease level → Mild symptoms
  - Cluster 3: High disease level → Significant visible symptoms

**Thanks My Teachers**

