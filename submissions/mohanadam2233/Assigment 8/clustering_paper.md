# 📘 Assigment 8 — Clustering (Unsupervised Learning)

**Name:** Mohamed Adam  
**Course:** Machine Learning  
**Date:** September 24, 2025  

---

## 1. Introduction to Clustering

**Clustering** is a type of machine learning used to group data points into meaningful categories, called *clusters*. The idea is that items in the same cluster are more similar to each other than to items in other clusters. It is part of **unsupervised learning**, meaning the data has no labels or correct answers provided in advance.

This is different from **supervised learning** such as regression and classification. In supervised learning, the algorithm is trained on labeled data (for example, emails labeled as “spam” or “not spam”), and the model learns to predict these labels for new data. In clustering, we do not provide labels. Instead, the algorithm must discover natural patterns or groupings in the data.

- **Example of Clustering:** A company groups customers based on purchasing behavior to design personalized marketing campaigns.  
- **Example of Supervised Learning:** Predicting house prices based on features like size, location, and number of rooms.  

---

## 2. Clustering Algorithms

### a) K-Means
- **How it works:**  
  K-Means divides data into *k* groups. It starts by selecting *k* random points as “centroids.” Each data point is assigned to the nearest centroid, and then centroids are updated as the average of assigned points. This process repeats until the centroids stop changing much.
- **Use case:** Customer segmentation in marketing.  
- **Advantages:** Simple, fast, and works well with large datasets.  
- **Limitations:** Requires choosing *k* in advance, sensitive to outliers, and assumes clusters are spherical.  

---

### b) Hierarchical Clustering
- **How it works:**  
  This method builds a “tree” of clusters, also called a **dendrogram**. It starts either by joining the closest individual points (agglomerative) or splitting the dataset (divisive). The result shows how clusters merge step by step.  
- **Use case:** Organizing documents by topic in digital libraries.  
- **Advantages:** Does not need to set *k* at the beginning, provides a full structure of clusters.  
- **Limitations:** Expensive for large datasets, and cutting the dendrogram to choose clusters can be subjective.  

---

### c) DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
- **How it works:**  
  DBSCAN groups together points that are close in density. A cluster is formed when there are enough nearby points (within a given distance). Points that do not belong to any cluster are marked as outliers.  
- **Use case:** Detecting unusual patterns such as fraud or anomalies in credit card transactions.  
- **Advantages:** Can find clusters of any shape and handles noise well.  
- **Limitations:** Choosing good parameters (distance and density) is difficult; performance decreases with high-dimensional data.  

---

## 3. Clustering Metrics

To measure the quality of clustering, we use evaluation metrics:

- **Elbow Method:** Looks at the total distance within clusters as *k* increases. The “elbow point” where the curve bends is a good choice for *k*.  
- **Silhouette Score:** Measures how similar each point is to its own cluster compared to other clusters. Score ranges from -1 to +1. Higher values mean better clustering.  
- **Davies–Bouldin Index:** Compares distances between clusters and their internal compactness. Lower values mean better separation.  

---

### 📊 Comparison Table

| **Metric**            | **What it measures**                          | **Good Value**      | **When Useful**                               |
|------------------------|-----------------------------------------------|---------------------|-----------------------------------------------|
| Elbow Method           | Total within-cluster variation vs. *k*        | Clear bend (elbow)  | Choosing the number of clusters (*k*)         |
| Silhouette Score       | Similarity within and between clusters         | Close to +1         | Comparing quality of clustering across models |
| Davies–Bouldin Index   | Ratio of intra-cluster vs. inter-cluster distance | Closer to 0         | Evaluating overall separation of clusters     |

---

## 4. Challenges in Clustering

Clustering is harder than supervised learning because there are no labels to guide the process. The “true” groups are unknown, and different algorithms may produce very different results.

Two common challenges are:

1. **Choosing the right number of clusters (k):**  
   Many algorithms like K-Means need *k* in advance, but finding the best number is not always clear. Metrics like the Elbow Method can help, but the decision often depends on domain knowledge.  

2. **Handling noise and outliers:**  
   Real-world data often has unusual points that do not belong to any cluster. Algorithms like DBSCAN can detect them, but many methods (like K-Means) are highly sensitive to such points.  

Another challenge is dealing with **high-dimensional data**, where similarity becomes harder to measure because distances lose meaning in many dimensions.  

---

## 5. Real-World Case Study

**Image Segmentation in Medical Imaging**  

- **Goal:** To separate different regions in medical images, such as distinguishing tumors from healthy tissue in MRI scans.  
- **Data Used:** MRI brain scan images containing both normal tissue and abnormal growths.  
- **Clustering Model:** K-Means clustering was applied to segment the image into clusters of pixels with similar intensity levels.  
- **Results:** The algorithm successfully highlighted tumor regions, helping doctors to analyze size and shape. This supported early diagnosis and better treatment planning.  

This example shows how clustering can be applied in healthcare to detect and analyze critical patterns without manual labeling.  

---

## ✅ Conclusion

Clustering is an important technique in machine learning that finds hidden structures in data. Algorithms such as K-Means, Hierarchical Clustering, and DBSCAN provide different strengths and weaknesses. Metrics like the Elbow Method, Silhouette Score, and Davies–Bouldin Index help evaluate results. Although clustering is more difficult than supervised learning due to lack of labels and challenges like noise, it has wide applications in areas such as marketing, biology, and anomaly detection.  

---

**References**  
1. Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning*. Springer.  
2. Géron, A. (2019). *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow*. O’Reilly.  
3. Scikit-learn Documentation: https://scikit-learn.org  
