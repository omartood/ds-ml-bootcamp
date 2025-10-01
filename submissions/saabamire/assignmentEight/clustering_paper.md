#  Lesson 8 Assignment — Clustering (Unsupervised Learning)


## 1. Introduction to Clustering  

Clustering is a way in Machine Learning where we put data into groupsnbased on similarity. Things that look similar go to the same group, and things that are different go to other groups. The important point is that in clustering, the computer does not know the answers before, the algorithm must discover the groups on its own.
 
This is not the same as supervised learning. In supervised learning, we already have examples with labels. For example, if we want to teach the computer to know if a fruit is an apple or a banana, we give it many labeled examples first. But in clustering, we only give the fruits and the computer tries to make groups without knowing the name.  In clustering, the groups are hidden and need to be found

**Example:**  
- *Clustering*: A library system grouping books into topics like history, science, or stories, without being told the categories.  
- *Supervised learning*: Predicting if a person will pass or fail an exam based on their past scores.  

---

## 2. Clustering Algorithms  

### 2.1 K-Means  
**Basic idea:** Choose a number of clusters (*k*). The algorithm picks random centers, assigns each point to the closest center, then updates the centers until the groups stop changing.  

**Example use:** A shop uses it to find types of shoppers, like those who buy small items often or those who buy many things once a month. 

**Advantages:** Simple and fast, works well for large datasets.  
**Limitations:** Must know the number of clusters in advance, and it works best with round-shaped clusters.  

---

### 2.2 Hierarchical Clustering  
**Basic idea:** it makes a tree of clusters. At the start, each point is its own cluster. Then it joins the closest clusters step by step until all points are in one group. The tree shows how clusters are combined.

**Example use:** Grouping countries by economic indicators like GDP, population, and trade.  

**Advantages:** No need to set the number of clusters at the beginning. Gives a full picture of how data is connected.  
**Limitations:** Slow with large data, and once groups are joined, they cannot be separated.  

---

### 2.3 DBSCAN  
**Basic idea:** Finds groups by looking at areas with many close points If many points are close together, they become a cluster. Points that are far away are seen as noise.

**Example use:** Detecting unusual travel patterns in GPS data.  

**Advantages:** Works well with clusters of different shapes, and can handle noise.  
**Limitations:** Needs correct parameter values and struggles when clusters have different densities.  

---

## 3. Clustering Metrics  

To know if clustering is good, we use different evaluation methods:  

- **Elbow Method:** Tests different numbers of clusters and looks for a bend in the graph that shows the best choice.  
- **Silhouette Score:** Checks how well a point fits inside its own cluster compared to other clusters. Score goes from -1 to 1, higher is better.  
- **Davies–Bouldin Index:** Looks at how close clusters are and how tight they are inside. Lower values mean better clustering.  

### Comparison Table  

| Metric              | What It Measures                     | Good Value       | When Useful                        |
|----------------------|---------------------------------------|------------------|------------------------------------|
| Elbow Method         | Finds the right number of clusters   | Clear bend       | Choosing *k* in K-Means            |
| Silhouette Score     | Separation between clusters          | Close to 1       | Checking quality of clustering     |
| Davies–Bouldin Index | Compactness and distance of clusters | Close to 0       | Comparing overall cluster results  |  

---

## 4. Challenges in Clustering  

Clustering is harder than supervised learning because there are no labels to check if the groups are correct. We only guess based on patterns.  

**Common challenges:**  
1. **Number of clusters:** Some algorithms need us to set the number of clusters first, but we often do not know the right value.  
2. **Noise and outliers:** Strange data points can confuse the algorithm and reduce accuracy.  
3. **High dimensions:** With many features, it becomes difficult to measure distance correctly, making clustering less effective.  

---

## 5. Real-World Case Study  


**Case:  Customer Segmentation in Online Retail**  
- **Goal:** To identify groups of online shoppers and make product suggestions more personalized.
- **Data Used:** Purchase records from an online store, including items bought, quantity, and spending patterns.
- **Method:** K-Means clustering was applied to divide customers into groups such as frequent buyers, seasonal shoppers, and low-spending customers.  
- **Result:** The company created targeted marketing strategies for each group. This improved customer engagement and increased overall sales.  

---

## References  

1. Scikit-learn Documentation: https://scikit-learn.org/stable/modules/clustering.html  
2. Tan, P.-N., Steinbach, M., & Kumar, V. (2019). *Introduction to Data Mining*. Pearson.  
3. Hudaib, A., & Fakhouri, H. N. (2022). K-Means Clustering Approach for Intelligent Customer Segmentation Using Customer Purchase Behavior Data. Sustainability, 14(12), 7243. https://doi.org/10.3390/su14127243
