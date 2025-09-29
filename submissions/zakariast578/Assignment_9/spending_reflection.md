# K-Means Clustering Analysis: Customer Spending Behavior

#### **1. Implementation Overview**

I implemented a K-Means clustering model to segment customers based on their income and spending scores. Here is a summary of the workflow:

* **Data Loading and Preparation**: The `spending_l9_dataset.csv` dataset was loaded, and the `Income_$` and `SpendingScore` columns were selected as the features for clustering.
* **Scaling**: To ensure that both features contributed equally to the clustering process, I used `StandardScaler` to scale the data. This prevents the `Income_$` feature, with its larger numerical range, from dominating the distance calculations.
* **Elbow Method (SSE Loop)**: I calculated the Sum of Squared Errors (SSE) for K values from 1 to 10. The SSE represents the total distance of data points from their respective cluster centers. By observing how the SSE changes as K increases, we can identify an "elbow point" where the rate of SSE reduction slows, suggesting an optimal number of clusters.
* **Model Training and Labeling**: Based on the analysis, I selected an optimal K, trained the K-Means model on the scaled data, and assigned a cluster label to each customer in the dataset.
* **Metric Evaluation**: To validate the chosen K, I calculated the **Silhouette Score** and the **Davies-Bouldin Index (DBI)**. The Silhouette Score measures how similar a data point is to its own cluster compared to other clusters, while the DBI evaluates the average similarity between each cluster and its most similar one.

#### **2. Choosing K**

* **Which K did you pick and why?**
  I chose **K=4**. The SSE loop showed a significant drop in inertia from K=1 to K=4, after which the reduction became more gradual. This "elbow" at K=4 suggests that adding more clusters beyond this point yields diminishing returns.

* **Refer to SSE, Silhouette, and DBI you printed.**
  * **SSE**: The SSE values were: `k=1, SSE=280.00`, `k=2, SSE=115.35`, `k=3, SSE=65.58`, and `k=4, SSE=38.94`. The drop from 3 to 4 clusters is substantial (a reduction of over 40%), while the drop from 4 to 5 is less pronounced (`SSE=31.11`).
  * **Silhouette Score**: The score for K=4 was **0.49**, which is a respectable value indicating that the clusters are reasonably dense and well-separated.
  * **Davies-Bouldin Index (DBI)**: The DBI for K=4 was **0.72**. A lower DBI is better, and this value, in conjunction with the other metrics, supports the choice of four distinct clusters.

#### **3. Cluster Interpretation**

Based on the cluster centers (converted back to their original scale), I can define the four customer segments:

* **Cluster 0: High Income, Low Spending**
  * **Description**: This group has a high average income (around $87k) but a very low spending score (16.2). They are cautious spenders or savers.
  * **Business Action**: Target this group with premium, high-value products or investment opportunities. Since they don't spend much, exclusive offers or loyalty programs that reward high-value purchases could be effective.

* **Cluster 1: Low Income, High Spending**
  * **Description**: This cluster has a low average income (around $25.8k) but a high spending score (79.7). These are likely younger customers or bargain hunters who are highly engaged.
  * **Business Action**: Engage this group with promotions, discounts, and trendy, lower-cost items. They are prime candidates for "buy now, pay later" financing options.

* **Cluster 2: Average Income, Average Spending**
  * **Description**: This is the "average" customer, with a moderate income (around $55.4k) and a medium spending score (49.5). They are consistent but not extravagant.
  * **Business Action**: Focus on upselling and cross-selling. Introduce them to new product lines or slightly more premium versions of what they already buy. Personalized recommendations could work well here.

* **Cluster 3: High Income, High Spending**
  * **Description**: This is the ideal customer segment, with a high income (around $86.5k) and a high spending score (82.1). They have the means and the willingness to spend.
  * **Business Action**: Treat this group as VIPs. Offer them exclusive access to new products, personalized services, and a premium loyalty program to ensure their retention.

#### **4. Limitations & Next Steps**

* **What information might improve segmentation?**
  The current segmentation is based solely on income and spending. It could be significantly improved by including additional demographic and behavioral data, such as:
  * **Age**: To better distinguish between life stages (e.g., young professionals vs. established families).
  * **Number of Visits**: To differentiate between frequent shoppers and occasional visitors.
  * **Online vs. In-Store Purchases**: To understand channel preferences and tailor marketing efforts accordingly.

* **One concrete next step:**
  A valuable next step would be to **try clustering with three features**. Adding `Age` to `Income_$` and `SpendingScore` could reveal more nuanced segments. For example, a "Young, High-Spending" group might emerge that was previously mixed in with other clusters, allowing for more targeted marketing campaigns.
