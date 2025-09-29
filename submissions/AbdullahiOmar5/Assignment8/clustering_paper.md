# Lesson 8 — Clustering (Unsupervised Learning)

## 1. Introduction to Clustering 

### What is clustering in Machine Learning?
Clustering in machine learning means grouping things that look similar into groups called clusters. Imagine you have a bunch of different objects, and you want to put the ones that are alike into the same group.

### How is it different from supervised learning (regression/classification)?
Supervised learning needs labeled data and is about making predictions or decisions, while clustering is about exploring the data to find hidden groups without prior knowledge.

### Give one real-life example of clustering and one of supervised learning.
- **Clustering example (Healthcare):** Hospitals use clustering to group patients with similar symptoms or medical histories. This helps doctors identify patterns, such as groups of patients likely to have the same disease or respond to similar treatments, even if the exact disease is not yet diagnosed.  
- **Supervised learning example (Healthcare):** Disease diagnosis. The computer learns from medical records labeled with diseases like diabetes or heart disease. Using these labeled examples, it can predict the disease a new patient might have based on their medical test results and symptoms.

---

## 2. Clustering Algorithms

### K-Means
K-Means groups data into a number (K) of clusters. It starts by picking K random points called centroids. Then, it puts each data point in the group with the closest centroid. After that, it moves each centroid to the center (average) of the points in its group. This repeats until the groups don’t change anymore.  

**Example:** Imagine you have 10 fruits on a table and you want to put them into 2 groups: apples and oranges. K-Means will start by picking 2 random spots as centers and then will put each fruit into the group of the closest center. It keeps moving the centers to the middle of fruits in each group until the groups no longer change.

---

### Hierarchical Clustering
Hierarchical Clustering makes a tree of groups. It starts with each data point as its own group. Then it joins the closest two groups step by step until everything is in one big group. You can choose where to cut the tree to make your final groups.  

**Example:** Suppose you have different animals and you want to group them by how similar they are. At first, each animal is alone. Then, the two most similar animals (like a dog and a wolf) join together. Next, these smaller groups join with other similar groups (like a fox with the dog-wolf group). This keeps going until all animals form one family tree.

---

### DBSCAN
DBSCAN finds groups by looking for areas where points are close to many neighbors. It gives clusters to points where neighbors are dense and marks points far away as noise or outliers. You don’t need to decide the number of clusters before running DBSCAN, and it can find clusters of different shapes.  

**Example:** Imagine a playground with kids playing in groups. DBSCAN looks for groups where kids play very close together. Kids who are far away playing alone are considered noise or outliers. Unlike K-Means, DBSCAN can find groups that are different shapes, not just round groups.

---

## 3. Clustering Metrics

### Elbow Method
The Elbow Method helps decide the best number of clusters (K) to use in algorithms like K-Means. You run the clustering for different K values and calculate how much the points differ from their cluster center (called "sum of squared errors" or SSE). As you increase K, SSE decreases because clusters get smaller. The "elbow" point is where the improvement starts to slow down, suggesting a good number of clusters to choose.

### Silhouette Score
This measures how well each data point fits in its cluster compared to other clusters. It ranges from -1 to +1.  
- A high score (close to +1) means the point is well matched to its cluster and far from others.  
- A score close to 0 means the point is on the border between clusters.  
- Negative means it may be in the wrong cluster.

### Davies–Bouldin Index
This index measures how well the clusters are separated. It calculates the average similarity between each cluster and its most similar other cluster. Lower values mean better clustering because groups are far apart and compact internally.

---

## 4. Challenges in Clustering

### Why is clustering considered harder than supervised learning?
Clustering is harder than supervised learning because:
- Supervised learning gets help from labeled data with clear right answers, like "this is a cat" or "this is spam." This makes learning easier because the model knows what to look for.  
- Clustering has no labels or answers given. The computer has to figure out groups by itself, which is more like solving a puzzle without guidance.  
- In supervised learning, you know how many groups or categories there are. In clustering, you don’t always know the number of groups and have to guess or test to find out.  
- It’s easier to check if supervised learning is right because you can compare predictions to known answers. In clustering, it’s harder to say if the groups found are good because there are no true answers.

---

### Common Challenges in Clustering

#### 1. Choosing the right number of clusters (k)
In clustering, you don't always know how many groups (clusters) your data should be split into. Picking too many groups can make the results confusing, while too few groups might miss important differences.  

**Example:** Imagine sorting fruits. If you choose 2 groups, you might put apples and oranges together. If you choose 5 groups, you might separate apples into many small groups, which may be too detailed.

#### 2. Handling noise and outliers
Noise means random or unusual data points that don’t fit well into any group. Outliers are points very different from others. These can confuse clustering algorithms and change the groups wrongly.  

**Example:** Imagine grouping students by their test scores. If one student has an extremely low score due to illness, that score is an outlier. Including this unusual score might pull a group’s average and make other students wrongly grouped.

#### 3. Dealing with high-dimensional data
When the data has many features or dimensions (like hundreds or thousands), clustering becomes very hard. This is because the data points all look very similar in a high-dimensional space, making it difficult to find real groups.  

**Example:** Imagine trying to group people based on a huge list of details—height, weight, favorite movie, daily steps, blood pressure, heart rate, and many more. With so many details, it’s hard to tell who really belongs in the same group because some details might be irrelevant, and distances between points become less meaningful.

---

## 5. Real-World Case Study

**Project:** Customer Segmentation in Retail Marketing  

**Goal:**  
The goal was to group households into meaningful clusters based on their spending behavior and demographics, so personalized marketing campaigns could be targeted effectively.  

**Data Used:**  
The company collected data about households such as income, family size, occupation of the head of the household, and distance from urban areas.  

**Clustering Model Applied:**  
They used K-Means clustering to divide the households into groups based on similarities in the data.  

**Key Results or Insights:**  
The clustering revealed groups such as small families who are high spenders, large families who spend less, and other distinct segments. This allowed the marketing team to create customized advertisements and offers, improving customer engagement and increasing sales.  

**Reference:**  
Omol, E. (2024). *Application Of K-Means Clustering For Customer Segmentation In Grocery Stores In Kenya*. International Journal of Science, Technology & Management, 5(1), 192-200. https://doi.org/10.46729/ijstm.v5i1.1024
