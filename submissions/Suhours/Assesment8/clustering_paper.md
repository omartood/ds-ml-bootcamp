# 📘 Lesson 8 — Clustering (Unsupervised Learning)
## 🎯 Objectives

By the end of this research paper, students will be able to:

* Understand what **Clustering** is and how it differs from supervised learning.
* Learn about common **Clustering algorithms**:

    * K-Means
    * Hierarchical Clustering
    * DBSCAN
* Understand how to **evaluate clustering models** using metrics:

    * Elbow Method
    * Silhouette Score
    * Davies–Bouldin Index


## 1) Introduction
In Machine learning, we often deal with large amounts of data. Sometimes, this data is not labeled, and we do not know the categories to which data belongs. In such cases, we use **Clustering** to **group** data into categories.
clustering helps us discover hidden patterns or grouping in the data by organizing similar data points together.

### What is Clustering?
> Clustering is an unsupervised machine learning technique that groups similar data points together into clusters based on their characteristics, without using any labeled data.

 **- How is it different from supervised learning (regression/classification)?**
  

**Key Differences**

| **Aspect** | **Clustering (Unsupervised Learning)** | **Supervised Learning (Regression/Classification)** |
|------------|-----------------------------------------|------------------------------------------------------|
| **Data** | Works with **unlabeled data**. | Works with **labeled data**. |
| **Goal** | Discover **hidden patterns** or groups. | Learn a **mapping** from input to output. |
| **Output** | Cluster assignments (Cluster 1, Cluster 2, …). | Predicted values (continuous or categorical). |
| **Algorithms** | K-Means, DBSCAN, Hierarchical. | Linear/Logistic Regression, Decision Trees, SVM. |
| **Evaluation** | Difficult (Silhouette score, Davies–Bouldin index). | Easier (Accuracy, Precision, Recall, F1, RMSE). |
| **Example** | Customer segmentation by purchase behavior. | Email spam detection. |

**In summary:**  
- **Supervised learning** = "I already know the answers (labels), teach me to predict them."  
- **Clustering (unsupervised)** = "I don’t know the answers, help me find the hidden groups."  

## 2) Clustering Algorithms

clustering can be done using different algorithms, each with its own strength and weaknesses.
the tree most common used  algorithms are:

* K-Means
* Hierarchical Clustering
* DBSCAN

**1) K-Means Clustering**

K-Means is a popular clustering algorithm that works by finding **k** centers (representative points) in the data and assigning each data point to the closest center.

**how does it work?**
 - find k centers in the data
 - assign each data point to the closest center
 - repeat until convergence
  
**advantages:**
 - easy to understand and implement
 - efficient for large datasets
 - can be sensitive to noise in the data

**limitations:**
 - sensitive to initial choice of centers
 - can be sensitive to noise in the data
 - can be slow for large datasets
 

**2) Hierarchical Clustering**

Hierarchical clustering is a clustering algorithm that builds a hierarchy of clusters by merging or splitting clusters based on their similarity.

**how does it work?**   
- start with all data points as separate clusters
- merge clusters that are similar
- repeat until all data points are in a single cluster

**advantages:**
- can handle large datasets
- can be sensitive to noise in the data
- can be slow for large datasets

**limitations:**
- can be sensitive to noise in the data
- can be slow for large datasets
- can be difficult to interpret

**3) DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**

DBSCAN is a density-based clustering algorithm that groups data points based on their density.

**how does it work?**

- assign each data point to a cluster based on its density
- assign data points to clusters based on their density
- assign data points to clusters based on their density

**advantages:**
- can handle large datasets
- can be sensitive to noise in the data
- can be slow for large datasets

**limitations:**
- can be sensitive to noise in the data
- can be slow for large datasets
- can be difficult to interpret


### **3. Clustering Metrics**


### 1. Elbow Method
- **Definition**: A heuristic used to determine the optimal number of clusters in algorithms like **K-Means**.  
- **How it works**: Plots the **Within-Cluster-Sum of Squares (WCSS)** or inertia (distance of each point to its assigned cluster center).  
- **What it measures**: The amount of variance explained by the clusters.  
- **Interpretation**: Look for the “elbow point” in the plot where adding more clusters does not significantly reduce WCSS. That point is the optimal cluster number.

---

### 2. Silhouette Score
- **Definition**: Measures how similar an object is to its own cluster compared to other clusters.  
 
- **Range**: -1 to 1  
- **Interpretation**:  
  - Close to **+1** → well clustered  
  - Around **0** → on/between cluster boundaries  
  - Negative values → probably misclassified

---

## 3. Davies–Bouldin Index (DBI)
- **Definition**: Measures the **average similarity between clusters**, where similarity is defined as the ratio of within-cluster scatter to between-cluster separation.  

- **Range**: \([0, \infty)\)  
- **Interpretation**:  
  - **Lower values** indicate better clustering (clusters are compact and well separated).  
  - 0 would be the ideal clustering (perfect separation).  

---

**Comparison Table**

| Metric                | What it Measures | Good Value | When Most Useful |
|------------------------|------------------|------------|------------------|
| **Elbow Method**       | Reduction of within-cluster variance (WCSS) as number of clusters increases | “Elbow point” (where WCSS stops decreasing significantly) | Choosing **initial number of clusters** (esp. for K-Means) |
| **Silhouette Score**   | Balance between cohesion (within cluster) and separation (between clusters) | Closer to **+1** is better | Comparing **different clustering results** or **validating cluster quality** |
| **Davies–Bouldin Index** | Ratio of within-cluster scatter to between-cluster separation | **Lower** (closer to 0) is better | Comparing clustering quality across **different algorithms** or **different k values** |


### **4. Challenges in Clustering**

#### Why is clustering considered harder than supervised learning?
Clustering is generally more difficult than supervised learning because:
- **No ground truth labels**: In supervised learning, models are trained with labeled data (e.g., "spam" or "not spam"). In clustering, labels are unknown, so it’s hard to directly measure correctness.  
- **Subjectivity**: What counts as a “good” cluster can vary depending on the application. Two different clustering solutions might both seem valid.  
- **Algorithm sensitivity**: Many clustering algorithms (like K-Means) are sensitive to initialization, scale of features, and noise in the dataset.  

---

#### Common Challenges in Clustering

1. **Choosing the right number of clusters (`k`)**
   - Many algorithms (e.g., K-Means) require specifying the number of clusters in advance.  
   - Picking too few clusters may merge distinct groups, while too many clusters may artificially split natural groups.  
   - Methods like the **Elbow Method**, **Silhouette Score**, and **Davies–Bouldin Index** are often used to guide this choice, but they don’t guarantee the “true” answer.

2. **Handling noise and outliers**
   - Outliers can distort cluster centroids and boundaries, leading to poor clustering.  
   - For example, in K-Means, a single outlier far away can pull the centroid toward it.  
   - Algorithms like **DBSCAN** are more robust, as they can classify outliers as “noise” rather than forcing them into clusters.

3. **Dealing with high-dimensional data**
   - In high dimensions (e.g., text or gene expression data), distances between points become less meaningful (“curse of dimensionality”).  
   - This makes it harder for algorithms to separate clusters effectively.  
   - Dimensionality reduction techniques like **PCA**, **t-SNE**, or **UMAP** are often used before clustering to mitigate this issue.

# 5. Real-World Case Study: Clustering in Practice

## Case Study 1: Customer Segmentation in the Real Estate Industry  

**Source**: *Customer Segmentation and Buyer Targeting Using K-Means Clustering: A Case Study of the Real Estate Industry* ([melekit-if.uwks.ac.id](https://melekit-if.uwks.ac.id/melekit/article/view/382?utm_source=chatgpt.com))

| Aspect | Details |
|--------|---------|
| **Goal** | To segment customers (buyers) in the real estate industry to better understand their characteristics and enable more targeted marketing strategies. |
| **Data Used** | Customer attributes such as age, income, job, type of house, payment method, and marital status collected by a real estate company in Indonesia. |
| **Clustering Model Applied** | **K-Means clustering** with: <br> - *Elbow Method* to find the optimal number of clusters (3) <br> - *Silhouette Score* for evaluation <br> - Visualizations (scatter plots, boxplots, pie charts) to interpret cluster profiles |
| **Key Results / Insights** | - Three distinct customer segments were identified. <br> - Clusters showed differences in income levels, house preferences, and payment methods. <br> - Allowed the company to design targeted marketing campaigns for each customer group. <br> - Visualization made the segmentation actionable and easy for stakeholders to understand. |

---

## Case Study 2: Image Segmentation in Medical Imaging  

**Source**: *Segmentation of Brain MR Images Using Genetically Guided Clustering* ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/17946576/?utm_source=chatgpt.com))

| Aspect | Details |
|--------|---------|
| **Goal** | To segment MRI brain images and handle intensity inhomogeneities (bias fields) for better medical image analysis. |
| **Data Used** | Magnetic Resonance (MR) brain images containing noise, artifacts, and intensity variations. |
| **Clustering Model Applied** | A modified **Fuzzy C-Means (FCM)** algorithm with: <br> - Genetic Algorithm (GA) optimization to avoid poor local minima <br> - Spatial neighborhood information to improve smoothness and reduce noise |
| **Key Results / Insights** | - Improved segmentation quality compared to standard FCM. <br> - Better distinction of brain tissue regions. <br> - More robust to noise and artifacts. <br> - Showed the value of hybrid approaches (FCM + GA + spatial features) in complex domains like medical imaging. |

---

## Lessons Learned Across Case Studies

- **Domain Knowledge is Crucial**: Feature selection (customer attributes or spatial image context) greatly affects clustering outcomes.  
- **Algorithm Enhancements Improve Results**: Standard clustering methods often need adaptations (e.g., GA optimization, dimensionality reduction, or evaluation metrics).  
- **Evaluation Matters**: Using metrics (Silhouette, DBI) and visualization ensures clusters are both numerically sound and interpretable by stakeholders.  
- **Scalability & Robustness**: Large datasets (millions of pixels or thousands of customers) demand efficient algorithms and resistance to noise/outliers.  

---

## References

1. Aprianto, D. & Astuti, Y. (2025). *Customer Segmentation and Buyer Targeting Using K-Means Clustering: A Case Study of the Real Estate Industry.* **Melek IT: Jurnal Ilmiah Teknologi Informasi**, 11(2).  
   [Available online](https://melekit-if.uwks.ac.id/melekit/article/view/382?utm_source=chatgpt.com)

2. Li, C., & Lee, C.-Y. (2007). *Segmentation of Brain MR Images Using Genetically Guided Clustering.* **Pattern Recognition**, 40(12), 3614–3628.  
   [PubMed Link](https://pubmed.ncbi.nlm.nih.gov/17946576/?utm_source=chatgpt.com)
3. geeksforgeeks.org. (2023). *K-Means Clustering Algorithm*. Retrieved from [https://www.geeksforgeeks.org/k-means-clustering-algorithm/](https://www.geeksforgeeks.org/k-means-clustering-algorithm/)

4. www.datacamp.com. (2023). *What is Machine Learning*. Retrieved from [https://www.datacamp.com/blog/what-is-machine-learning](https://www.datacamp.com/blog/what-is-machine-learning)