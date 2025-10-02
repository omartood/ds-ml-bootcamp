# Lesson 8 — Clustering (Unsupervised Learning)

---

## 1. Introduction to Clustering

Clustering is an **unsupervised learning technique** in machine learning that involves grouping a set of objects or data points into clusters based on their similarity (Jain, 2010). Unlike supervised learning, clustering does **not require labeled data**; the algorithm identifies patterns or structures inherent in the dataset. The primary goal is to ensure that **data points within the same cluster are more similar to each other** than to those in other clusters.

In contrast, **supervised learning** (such as regression or classification) relies on labeled datasets to train a model to predict outcomes or categories (Tan et al., 2019). For example, in supervised learning, a model may predict whether an email is spam or not based on pre-labeled examples. In clustering, no labels exist; the algorithm must determine the natural grouping of the data.  

**Example of clustering:** A retail company may use clustering to segment customers based on purchasing behavior, without predefined categories (Wu et al., 2019).  
**Example of supervised learning:** Predicting a house price based on features such as area, number of bedrooms, and location.

---

## 2. Clustering Algorithms

### 2.1 K-Means

**How it works:**  
K-Means is a **partition-based clustering algorithm** that divides data into `k` clusters. It starts by initializing `k` centroids randomly, then iteratively assigns each data point to the nearest centroid and recalculates centroids based on the mean of assigned points. The process repeats until centroids stabilize (Jain, 2010; Tan et al., 2019).

**Use case:** Market segmentation to group customers with similar buying habits (Wu et al., 2019).  

**Advantages:**  
* Simple and computationally efficient.  
* Works well with large datasets.  

**Limitations:**  
* Requires specifying the number of clusters `k` in advance.  
* Sensitive to outliers and initial centroid placement.  

---

### 2.2 Hierarchical Clustering

**How it works:**  
Hierarchical clustering builds a **tree-like structure** (dendrogram) to represent nested clusters. It can be **agglomerative** (bottom-up: merging clusters) or **divisive** (top-down: splitting clusters). The dendrogram allows analysts to choose clusters at different levels of granularity (Xu & Wunsch, 2005; Aggarwal & Reddy, 2013).

**Use case:** Document clustering for organizing news articles or research papers.  

**Advantages:**  
* Does not require specifying the number of clusters in advance.  
* Provides a detailed hierarchy of relationships.  

**Limitations:**  
* Computationally expensive for large datasets.  
* Sensitive to noise and outliers.  

---

### 2.3 DBSCAN (Density-Based Spatial Clustering of Applications with Noise)

**How it works:**  
DBSCAN groups **dense regions of data points** into clusters and identifies sparse regions as noise. It requires two parameters: `eps` (neighborhood radius) and `minPts` (minimum points to form a dense region). Unlike K-Means, DBSCAN can detect clusters of **arbitrary shapes** and handle noise effectively (Ester et al., 1996; Aggarwal & Reddy, 2013).

**Use case:** Identifying geographical hotspots of crime or disease outbreaks.  

**Advantages:**  
* Can find clusters of any shape.  
* Robust to outliers and noise.  

**Limitations:**  
* Performance depends on parameter selection (`eps` and `minPts`).  
* Struggles with varying density clusters.  

---

## 3. Clustering Metrics

Clustering evaluation metrics assess the **quality of clustering results**, often without requiring labeled data (Charrad et al., 2014; Rousseeuw, 1987).

| Metric                  | What it Measures                              | Good Value                     | When Useful                                      |
|--------------------------|-----------------------------------------------|--------------------------------|------------------------------------------------|
| **Elbow Method**         | Total within-cluster variance vs. `k`        | “Elbow” point in plot          | Choosing optimal number of clusters `k`       |
| **Silhouette Score**     | How similar points are to their cluster vs. others | Close to 1 (well-separated)   | Evaluating compactness and separation         |
| **Davies–Bouldin Index** | Average similarity between clusters          | Close to 0 (low intra-cluster similarity) | Comparing different clustering models |

**Explanation of metrics:**  

* **Elbow Method:** Plots the total sum of squared distances within clusters for different values of `k`. The point where the reduction slows (“elbow”) suggests an optimal number of clusters (Charrad et al., 2014).  
* **Silhouette Score:** Measures how similar a point is to its cluster compared to other clusters. Values range from -1 to 1; higher scores indicate better-defined clusters (Rousseeuw, 1987).  
* **Davies–Bouldin Index:** Quantifies the ratio of intra-cluster distance to inter-cluster distance. Lower values indicate more distinct clusters (Aggarwal & Reddy, 2013).

---

## 4. Challenges in Clustering

Clustering is generally **more challenging than supervised learning** because it lacks labeled data, making it difficult to validate results objectively (Jain, 2010).  

**Common challenges include:**  

1. **Choosing the right number of clusters (`k`):** Selecting too few or too many clusters can lead to misleading patterns. Methods like the Elbow Method help, but decisions often remain subjective (Charrad et al., 2014).  
2. **Handling noise and outliers:** Outliers can distort cluster centroids, especially in algorithms like K-Means, leading to inaccurate clustering (Ester et al., 1996).  
3. **Dealing with high-dimensional data:** In datasets with many features, distances between points become less meaningful (curse of dimensionality), reducing clustering effectiveness (Aggarwal & Reddy, 2013).

---

## 5. Real-World Case Study: Customer Segmentation in Retail

**Goal:**  
The primary objective of this project was to **segment customers into distinct groups** to improve marketing effectiveness, enhance customer retention, and increase overall sales. By understanding the behavior and preferences of different customer types, the company aimed to create **personalized marketing campaigns** and **targeted promotions** (Wu et al., 2019).

**Data used:**  
The dataset included several features collected over multiple years:  

* **Transaction history:** Frequency of purchases, total spending, and items bought per transaction.  
* **Demographic information:** Age, gender, income level, location.  
* **Behavioral metrics:** Time since last purchase, response to previous promotions, preferred shopping channels (online vs. in-store).  
* **Engagement data:** Newsletter subscriptions, loyalty program participation, and website interactions.  

The dataset contained **thousands of customers** and **hundreds of features**, which required preprocessing steps such as normalization, missing value handling, and feature selection before applying clustering (Tan et al., 2019).

**Clustering model applied:**  
* **Algorithm:** K-Means clustering  
* **Number of clusters (`k`):** 5, determined using the **Elbow Method** to minimize intra-cluster variance while avoiding unnecessary complexity.  
* **Process:**  
  1. Data was cleaned and standardized.  
  2. K-Means iteratively assigned customers to the nearest centroid based on Euclidean distance.  
  3. Centroids were recalculated until convergence.  
  4. Each customer was labeled according to their cluster for analysis.

**Key results and insights:**  
1. **Customer segmentation:**  
   * **Cluster 1:** High-value frequent buyers — loyal customers who shop regularly and spend above average.  
   * **Cluster 2:** Bargain hunters — occasional buyers primarily attracted by discounts.  
   * **Cluster 3:** New customers — recently acquired, with limited purchase history.  
   * **Cluster 4:** Seasonal shoppers — tend to buy during holidays or special promotions.  
   * **Cluster 5:** Low-engagement customers — rarely purchase and have minimal engagement.  

2. **Marketing strategy improvements:**  
   * Personalized email campaigns were designed for each cluster, e.g., exclusive offers for high-value customers and targeted discounts for bargain hunters.  
   * Loyalty programs were adjusted to retain high-value customers and encourage engagement from low-activity groups.  

3. **Business impact:**  
   * Improved customer retention and satisfaction.  
   * Increased sales revenue due to more effective targeting.  
   * Identification of untapped opportunities for cross-selling and upselling.  
   * Insights into customer behavior helped guide future product development and inventory management.

**Conclusion:**  
This case demonstrates the practical value of clustering in **real-world retail applications**. By grouping customers with similar characteristics, businesses can move from **generic marketing strategies** to **data-driven, personalized engagement**, resulting in measurable improvements in revenue and customer loyalty.

---

## References

1. Jain, A. K. (2010). *Data clustering: 50 years beyond K-Means.* Pattern Recognition Letters, 31(8), 651–666.  
2. Xu, R., & Wunsch, D. (2005). *Survey of clustering algorithms.* IEEE Transactions on Neural Networks, 16(3), 645–678.  
3. Ester, M., Kriegel, H.-P., Sander, J., & Xu, X. (1996). *A density-based algorithm for discovering clusters in large spatial databases with noise.* Proceedings of KDD, 226–231.  
4. Tan, P.-N., Steinbach, M., & Kumar, V. (2019). *Introduction to Data Mining* (2nd ed.). Pearson.  
5. Aggarwal, C. C., & Reddy, C. K. (2013). *Data Clustering: Algorithms and Applications.* Chapman & Hall/CRC.  
6. Ankerst, M., Breunig, M. M., Kriegel, H.-P., & Sander, J. (1999). *OPTICS: Ordering points to identify the clustering structure.* SIGMOD Record, 28(2), 49–60.  
7. Wu, J., Ding, X., & He, X. (2019). *Customer segmentation using K-Means clustering and DBSCAN: A retail analytics approach.* Journal of Retailing and Consumer Services, 50, 322–332.  
8. Charrad, M., Ghazzali, N., Boiteau, V., & Niknafs, A. (2014). *NbClust: An R package for determining the relevant number of clusters in a dataset.* Journal of Statistical Software, 61(6), 1–36.  
9. Rousseeuw, P. J. (1987). *Silhouettes: A graphical aid to the interpretation and validation of cluster analysis.* Journal of Computational and Applied Mathematics, 20, 53–65.  
10. Verma, A., & Srivastava, S. (2020). *Comparative study of clustering algorithms in data mining.* International Journal of Computer Applications, 175(16), 7–13.
