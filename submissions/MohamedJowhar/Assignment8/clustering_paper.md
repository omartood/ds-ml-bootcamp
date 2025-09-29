# Introduction to Clustering in Machine Learning

Clustering is one of the **unsupervised machine learning** methods. It does not have labels and works by making groups. It differs from other machine learning methods, which have labels.

**Examples:** Segmenting customers versus predicting whether an email is spam or not, or estimating house prices.

## 1. K-Means
K-Means is a type of **unsupervised machine learning** used to group data based on similarities. You can choose the number of groups you want, for example, 3, 4, or any number.

## 2. Hierarchical Clustering
Hierarchical Clustering is another type of **unsupervised machine learning**. It groups data without needing you to choose the number of clusters. It has **bottom-up (agglomerative)** and **top-down (divisive)** approaches.

## 3. DBSCAN
DBSCAN is another type of **unsupervised machine learning**. It groups data without needing you to choose the number of clusters. It can detect **irregular-shaped clusters**, **noise**, or **outliers**.


# K-Means Clustering

## How It Works (Basic Idea)
1. Choose the number of clusters **K**.  
2. Randomly place **K centroids**.  
3. Assign each data point to the **nearest centroid**.  
4. Update the centroids based on the mean of points in each cluster.  
5. Repeat steps 3–4 **until clusters do not change**.  

## Real-World Use Case
**Customer segmentation in retail:** Group customers based on shopping behavior, for example, high spenders and low spenders.

## Main Advantages
- Simple and easy to understand.  
- Fast for large datasets.  

## Main Limitations
- Must specify the number of clusters (**K**) beforehand.  
- Sensitive to outliers.  
- Not good for irregularly shaped clusters.


# 2. DBSCAN (Density-Based Clustering)

## How It Works (Basic Idea)
- Points in **dense regions** form clusters.  
- Points far from any cluster are marked as **noise** or **outliers**.  

## Real-World Use Case
**GPS locations in a city:**  
- Clusters represent popular areas like parks or malls.  
- Noise could be people walking alone in empty streets.  

## Main Advantages
- Automatically finds the number of clusters.  
- Can detect noise and outliers.  

## Main Limitations
- Struggles with clusters of varying densities (dense clusters near sparse clusters).  
- Noise points can sometimes make clustering less clear.

# 3. Hierarchical Clustering

## How It Works (Basic Idea)
Hierarchical Clustering can be done in **two main approaches**:  
- **Agglomerative (Bottom-Up):** Start with each data point as its own cluster and merge the closest clusters step by step.  
- **Divisive (Top-Down):** Start with all data points in one cluster and split it step by step into smaller clusters.  

## Real-World Use Case
**Document clustering:** Group news articles or research papers based on content similarity.  
- Example: Articles about sports may form one cluster, while articles about politics form another.  

## Main Advantages
- No need to specify the number of clusters in advance.  
- Visual dendrogram helps understand relationships between clusters.  

## Main Limitations
- Computationally expensive for large datasets.  

# Clustering Evaluation Methods

## Elbow Method
The Elbow Method is a way to choose the best number of clusters (K) for K-Means clustering.

## Silhouette Score
The Silhouette Score is a way to measure how good a clustering result is. The score ranges from -1 to 1.

## Davies–Bouldin (DB) Index
The Davies–Bouldin (DB) Index is a way to measure the quality of clustering.
# Clustering Evaluation Metrics Comparison

| Metric                  | What It Measures                                   | Good Value Means                             | When It Is Useful                            |
|-------------------------|--------------------------------------------------|---------------------------------------------|---------------------------------------------|
| Elbow Method            | Helps you figure out the best number of clusters | The point where adding more clusters doesn’t help much | When you need to choose how many clusters to use in K-Means |
| Silhouette Score        | Shows how well points fit in their own group compared to other groups | Close to 1 → points are in the right group | When you want to check if your clusters are clear and well separated |
| Davies–Bouldin (DB) Index | Tells you how good the clusters are based on how tight and separate they are | Lower score → clusters are tight and far from each other | When comparing different cluster results to see which one is better |
# Clustering Evaluation Metrics Comparison

| Metric                  | What It Measures                                   | Good Value Means                             | When It Is Useful                            |
|-------------------------|--------------------------------------------------|---------------------------------------------|---------------------------------------------|
| Elbow Method            | Helps you figure out the best number of clusters | The point where adding more clusters doesn’t help much | When you need to choose how many clusters to use in K-Means |
| Silhouette Score        | Shows how well points fit in their own group compared to other groups | Close to 1 → points are in the right group | When you want to check if your clusters are clear and well separated |
| Davies–Bouldin (DB) Index | Tells you how good the clusters are based on how tight and separate they are | Lower score → clusters are tight and far from each other | When comparing different cluster results to see which one is better |
# Challenges in Clustering

Clustering is often **harder than supervised learning** because, unlike supervised learning, clustering does **not have labels or correct answers**. This makes it difficult to know if the clusters you create are truly meaningful or useful.

📌 Real-World Case Study: Customer Segmentation at MetLife
🎯 Goal of the Project

MetLife aimed to enhance its marketing and customer engagement strategies by moving beyond basic demographic data. The goal was to identify distinct customer segments based on attitudes, behaviors, and needs, allowing for more personalized and effective outreach.

📊 Data Used

MetLife collected comprehensive data through in-depth surveys, capturing:

Demographic information: Age, income, family status

Firmographic data: Employment details, industry

Attitudinal insights: Values, preferences, and concerns

Needs-based information: Specific insurance and financial requirements

🧠 Clustering Model Applied

The company employed advanced segmentation tools, utilizing clustering algorithms to analyze the survey responses. These algorithms grouped customers into distinct segments based on shared characteristics and behaviors.

🔑 Key Results or Insights

Identification of distinct customer segments: MetLife uncovered several unique customer groups, each with specific needs and preferences.

Strategic targeting: The insights allowed MetLife to tailor its marketing efforts, product offerings, and customer service approaches to better align with each segment.

Operational efficiency: By focusing on the most relevant customer segments, MetLife aimed to optimize resource allocation and improve overall customer satisfaction.