# Lesson 8 Assignment — Clustering (Unsupervised Learning)

**Goal:** Understand the key concepts, algorithms, and evaluation metrics of Clustering in Machine Learning.

## 1. Introduction to Clustering

Clustering in Machine Learning is an unsupervised learning technique where algorithms group similar data points together without predefined labels. The main objective is to discover hidden structures or patterns within the data.

**Difference from Supervised Learning:**  
- Supervised Learning (Regression/Classification): Works with labeled data (inputs + outputs are known).  
- Clustering (Unsupervised): Works without labels, grouping based on similarity only.  

**Examples:**  
- Clustering example: Grouping hotel reviews into clusters such as “positive,” “neutral,” and “negative.”  
- Supervised example: Predicting whether an email is spam or ham using labeled training data.  

---

## 2. Clustering Algorithms

### 2.1 K-Means
- **How it works:** Iteratively assigns data points to the nearest centroid, updates centroids, and repeats until convergence.  
- **Use Case:** Segmenting hotel reviews into categories (positive/negative).  
- **Advantages:** Simple, scalable, efficient.  
- **Limitations:** Requires predefining *k*; sensitive to outliers.  

---

### 2.2 Hierarchical Clustering
- **How it works:** Builds a cluster tree (dendrogram) using bottom-up (agglomerative) or top-down (divisive) approaches.  
- **Use Case:** Grouping hotels by service similarity (location, amenities, pricing).  
- **Advantages:** No need to set *k* in advance; gives clear hierarchy.  
- **Limitations:** Computationally heavy for large datasets.  

---

### 2.3 DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
- **How it works:** Groups dense regions together and treats sparse points as outliers.  
- **Use Case:** Detecting unusual hotel booking patterns (fraud/noise).  
- **Advantages:** Finds arbitrarily shaped clusters; handles noise well.  
- **Limitations:** Sensitive to parameter settings (ε, MinPts).  

---

## 3. Clustering Metrics

Since clustering lacks labels, internal validation metrics are commonly used.

### Elbow Method
- **Measures:** Total within-cluster variation (*inertia*).  
- **Good Value:** “Elbow point” where adding more clusters does not reduce variation much.  
- **Usefulness:** Choosing *k* in K-Means.  

---

### Silhouette Score
- **Measures:** How well each data point fits into its cluster vs. neighboring clusters.  
- **Good Value:** Close to +1 = good separation, 0 = overlapping clusters.  
- **Usefulness:** Checking clustering quality.  

---

### Davies–Bouldin Index
- **Measures:** Ratio of within-cluster compactness to between-cluster separation.  
- **Good Value:** Lower = better.  
- **Usefulness:** Comparing compactness and separation.  

---

### Comparison Table of Metrics

| Metric               | What it Measures                               | Good Value        | Best Used For                     |
|----------------------|------------------------------------------------|-------------------|------------------------------------|
| Elbow Method         | Within-cluster variation (inertia)             | Elbow in the plot | Determining number of clusters (*k*) |
| Silhouette Score     | Cluster cohesion vs. separation                | Close to +1       | Evaluating cluster quality          |
| Davies–Bouldin       | Compactness vs. separation ratio               | Close to 0        | Comparing separation across models  |

---

## 4. Challenges in Clustering

Clustering is harder than supervised learning because no ground truth labels exist for validation.

**Common Challenges:**  
1. **Choosing optimal *k*:** Algorithms like K-Means need *k*, which is not always obvious.  
2. **Handling outliers:** Outliers distort cluster formation (DBSCAN helps here).  
3. **High-dimensional data:** Text data (like hotel reviews) can be sparse; dimensionality reduction (PCA, t-SNE) is required.  

---

## 5. Real-World Case Study: Hotel Review Clustering

### Goal
To analyze thousands of online hotel reviews and group them into clusters (positive, neutral, negative) — enabling hotel managers to detect frequent issues and strengths.

### Data
- Source: Hotel booking platforms.  
- Format: Thousands of text reviews.  
- Preprocessing: Text converted into vectors using TF–IDF.  

### Clustering Models Used
- **K-Means (k = 3):** For sentiment-based clusters.  
- **Hierarchical Clustering:** For deeper subgrouping (e.g., “cleanliness” vs. “staff”).  

### Results
- K-Means grouped reviews into meaningful sentiment categories.  
- Negative reviews highlighted recurring problems with cleanliness and Wi-Fi.  
- Hierarchical clustering separated reviews further into subtopics like room service vs. location.  
- Outcome: Helped managers prioritize improvements and boost customer satisfaction.  
