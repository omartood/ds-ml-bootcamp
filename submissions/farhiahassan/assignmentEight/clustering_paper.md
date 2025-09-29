# Lesson 8 — Clustering (Unsupervised Learning)


## 1. Introduction to Clustering
In Machine Learning, **clustering** is a method of **unsupervised learning** that groups data points into clusters based on similarity. Unlike supervised learning, clustering does not depend on labeled datasets. Instead, it uncovers hidden patterns and structures in the data by identifying groups with shared characteristics.  

For instance, a hospital might use clustering to identify groups of patients with similar symptoms, even without predefined categories. On the other hand, **supervised learning** requires labeled outcomes. For example, in a medical dataset, a classification model may predict whether a patient has diabetes (*yes/no*) based on known labels.  

Thus:  
- **Supervised learning** = requires labels (answers are known).  
- **Unsupervised learning (clustering)** = finds hidden patterns without labels.  

---

## 2. Clustering Algorithms

### a) K-Means Clustering
**How it works:**  
K-Means divides data into *k* clusters by iteratively assigning each data point to the closest cluster centroid and then updating the centroids until they stabilize.  

**Use case:**  
K-Means is widely used in **customer segmentation** to identify distinct shopper groups.  

**Advantages:**  
- Easy to understand and computationally efficient.  
- Scales well to large datasets.  

**Limitations:**  
- Requires choosing *k* beforehand.  
- Struggles with irregular cluster shapes and noise.  

---

### b) Hierarchical Clustering
**How it works:**  
Hierarchical clustering builds a nested tree of clusters known as a **dendrogram**. It has two main approaches:  
- **Agglomerative (bottom-up):** Each point starts as its own cluster, and clusters are merged step by step.  
- **Divisive (top-down):** All points start in one cluster, which is split recursively.  

**Use case:**  
Used in **genetics** to classify DNA sequences by similarity.  

**Advantages:**  
- Provides insights at multiple levels of granularity.  
- No need to pre-specify the number of clusters.  

**Limitations:**  
- Computationally expensive for large datasets.  
- Sensitive to noise and outliers.  

---

### c) DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
**How it works:**  
DBSCAN identifies clusters as dense regions of points separated by areas of low density. It uses two parameters:  
- **ε (epsilon):** the neighborhood radius.  
- **minPts:** minimum number of points to form a cluster.  

**Use case:**  
Applied in **geographical mapping**, such as detecting hotspots of seismic activity.  

**Advantages:**  
- Can find arbitrarily shaped clusters.  
- Naturally detects outliers as noise.  

**Limitations:**  
- Requires careful parameter tuning.  
- Struggles when cluster densities vary widely.  

---

## 3. Clustering Metrics

### Elbow Method
The Elbow Method determines the optimal number of clusters (*k*) in K-Means. By plotting the **sum of squared errors (SSE)** for different *k* values, the “elbow” in the curve indicates the most suitable number of clusters.  

### Silhouette Score
The Silhouette Score measures how well-separated clusters are by comparing cohesion (intra-cluster similarity) and separation (distance between clusters). The score ranges from -1 to +1:  
- **+1** → well-separated clusters.  
- **0** → overlapping clusters.  
- **-1** → incorrect clustering.  

### Davies–Bouldin Index
The Davies–Bouldin Index evaluates average similarity between clusters. A **lower value** indicates better separation and less overlap between clusters.  

---

### Comparison Table

| Metric              | What it Measures                     | Good Value Means         | When Useful                    |
|----------------------|--------------------------------------|--------------------------|--------------------------------|
| **Elbow Method**     | Drop in SSE vs. number of clusters   | Clear bend in the curve  | Choosing best *k* in K-Means   |
| **Silhouette Score** | Cohesion and separation of clusters  | Close to +1              | Assessing cluster quality      |
| **DB Index**         | Average similarity between clusters  | Lower is better          | Comparing multiple models      |

---

## 4. Challenges in Clustering
Clustering is often more challenging than supervised learning because **no labels are available** to validate results directly. Algorithms must rely on structural assumptions, which may not always capture true data patterns.  

**Common challenges include:**  

1. **Choosing the right number of clusters:**  
   Algorithms like K-Means require a predefined *k*, but real-world datasets rarely reveal the “true” cluster count.  

2. **Noise and outliers:**  
   Outliers can significantly affect centroid-based methods like K-Means. While DBSCAN handles noise better, it depends heavily on parameter tuning.  

3. **High-dimensional data:**  
   In datasets with many features, the concept of distance becomes less meaningful, making it difficult to detect meaningful clusters. This is known as the “curse of dimensionality.”  

---

## 5. Real-World Case Study: Medical Image Segmentation
A practical example of clustering can be found in **medical imaging**, particularly in segmenting MRI scans to identify different tissue types. The goal is to assist radiologists in detecting abnormalities more efficiently.  

**Goal of the project:**  
To segment brain MRI images into meaningful regions, such as gray matter, white matter, and cerebrospinal fluid, enabling earlier diagnosis of neurological conditions.  

**Data used:**  
MRI scan images where each pixel’s intensity represents tissue characteristics.  

**Clustering model applied:**  
K-Means clustering was applied to group pixels based on intensity values. In some studies, DBSCAN was also used to highlight abnormal dense regions, such as tumors.  

**Key results and insights:**  
- K-Means effectively separated tissue regions in the brain.  
- Outlier detection via DBSCAN helped identify unusual growths.  
- The automated segmentation reduced manual workload for radiologists and improved diagnostic accuracy.  

---

## 📚 References
1. Han, J., Kamber, M., & Pei, J. (2011). *Data Mining: Concepts and Techniques*. Elsevier.  
2. scikit-learn documentation: https://scikit-learn.org/stable/modules/clustering.html  
3. Tan, P., Steinbach, M., & Kumar, V. (2018). *Introduction to Data Mining*. Pearson.  
4. Zhang, Y., Brady, M., & Smith, S. (2001). Segmentation of brain MR images through a hidden Markov random field model and the expectation-maximization algorithm. *IEEE Transactions on Medical Imaging*, 20(1), 45–57.  
