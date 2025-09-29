# Reflection: Spending Pattern Analysis with K-Means

---

## 1. What did I implement?

In this assignment, I implemented an end-to-end customer segmentation project using the K-Means algorithm. The workflow was structured as follows:

1.  **Loading Dataset:** I began by loading the `spending_l9_dataset.csv` file into a pandas DataFrame.
2.  **Select Features for Clustering:** I selected the `Income_$` and `SpendingScore` columns as the features for the clustering analysis.
3.  **Feature Scaling:** To prepare the data for K-Means, I used `StandardScaler` to normalize the selected features, ensuring they were on the same scale.
4.  **Choosing K (Elbow Method):** I determined the optimal number of clusters by implementing the Elbow Method. This involved looping through K values from 1 to 10 and calculating the Sum of Squared Errors (SSE) for each.
5.  **Training and Labeling:** I trained the final KMeans model using the optimal K value of 4. I then added the resulting labels as a new `Cluster` column to the original DataFrame.
6.  **Evaluating the Clustering:** I evaluated the performance of the final model by calculating the Silhouette Score and the Davies-Bouldin Index (DBI).
7.  **Interpreting Cluster Centers:** To understand the resulting personas, I transformed the cluster centers from their scaled values back into their original, understandable units.
8.  **Sanity Check:** I performed a sanity check by displaying a random sample of three customers along with their assigned clusters to ensure the results were logical.
9.  **Save Labeled Dataset:** As the final step, I saved the complete DataFrame, including the new `Cluster` column, to a new file named `spending_labeled_clusters.csv`.

---

## 2. Choosing K

I chose **K=4** as the optimal number of clusters for this dataset. This decision was based on strong evidence from the SSE values and was confirmed by the evaluation metrics.

* **Elbow Method (SSE):** The printed SSE values showed a classic "elbow" pattern. The SSE decreased sharply until K=4 (SSE = 21.37). After this point, the decrease became very small; for instance, the drop to K=5 (SSE = 19.09) was minimal. This indicates that K=4 is the point of diminishing returns, making it the most efficient choice.

* **Evaluation Metrics:** The scores for K=4 confirmed that the clusters were well-defined.
    * The **Silhouette Score was 0.73**. This is an excellent score, as it's very close to +1, indicating that the clusters are dense and well-separated from one another.
    * The **Davies-Bouldin Index (DBI) was 0.39**. This is also a very strong score, as it's close to the ideal value of 0, which signifies that the clusters are compact and distinct.

---

## 3. Cluster Interpretation

By analyzing the cluster centers, I identified four distinct customer personas.

### Cluster Personas & Business Actions

| Cluster | Persona / Profile | Description | Suggested Business Action |
| :---: | :--- | :--- | :--- |
| **0** | **Standard** | Average income and average spending score. | Offer a loyalty program to encourage repeat buys. |
| **1** | **Cautious** | Low income and low spending score. | Provide special discounts and bundled deals. |
| **2** | **Target Audience** | Low income but a very high spending score. | Market new trends; offer flexible payment options. |
| **3** | **High-Value** | High income and a high spending score. | Give VIP treatment and exclusive access to products. |

### Summary of Cluster Interpretation

* **Cluster 0 (Standard):** This group is typical, middle-ground customers with average income and spending habits. The business goal for this group is to build loyalty and encourage more frequent purchases.
* **Cluster 1 (Cautious):** This group is budget-conscious, with low income and the lowest spending score. They are motivated by price, so the best strategy is to target them with discounts and high-value offers.
* **Cluster 2 (Target Audience):** This is a high-potential group that spends a lot despite having a low income. They are likely interested in trends, making them a prime audience for marketing new and exciting products.
* **Cluster 3 (High-Value):** This group is the best customer segment, with both high income and high spending. The focus for this group is retention through a premium experience, like VIP treatment and exclusive offers.

---

## 4. Limitations & Next Steps

### Limitations

* The analysis was based on only two features: `Income_$` and `SpendingScore`.
* Using just two dimensions might oversimplify customer behavior and could cause different types of customers to be grouped together.
* Other valuable features available in the dataset—such as `Age`, `VisitsPerMonth`, and `OnlinePurchases`—were not used, which could have provided deeper insights.

### Next Steps

* Re-run the K-Means analysis using three features (`Income_$`, `SpendingScore`, and `Age`) to create more detailed and nuanced customer personas.
* Explore alternative clustering algorithms, like DBSCAN, to see if a different approach can identify the clusters more effectively.
* Analyze the characteristics of each cluster using the unused features (e.g., `VisitsPerMonth`) to validate the personas and uncover additional behavioral patterns.