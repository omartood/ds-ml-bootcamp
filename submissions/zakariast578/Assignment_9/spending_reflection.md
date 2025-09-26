# Customer Segmentation Analysis

## 1. Implementation Workflow

I implemented a K-Means clustering model to segment customers based on their annual income and spending score. My workflow consisted of the following steps:

1. **Data Loading and Preparation**: I loaded the `customers_l9_dataset.csv` dataset and dropped the `CustomerID`, `Gender`, and `Age` columns to focus solely on income and spending behavior.

2. **Feature Scaling**: To ensure that both features (`Annual Income (k$)` and `Spending Score (1-100)`) contributed equally to the clustering process, I standardized them using `StandardScaler`. This prevents the model from being biased towards features with larger scales.

3. **Elbow Method (SSE Loop)**: I ran a loop for `k` from 1 to 10 to determine the optimal number of clusters. For each `k`, I trained a K-Means model and calculated the Sum of Squared Errors (SSE), which is the sum of squared distances of samples to their closest cluster center. A lower SSE indicates denser clusters.

4. **Model Training and Labeling**: Based on the analysis, I chose `K=9` and trained the final K-Means model. I then used this model to predict the cluster for each customer and added the labels to the original DataFrame.

5. **Metric Evaluation**: To validate the quality of the clusters, I calculated the **Silhouette Score** (0.45) and the **Davies-Bouldin Index (DBI)** (0.79). A Silhouette Score closer to 1 and a DBI closer to 0 indicate well-defined, separated clusters.

## 2. Choosing K

I selected **K=9** for the final model. This decision was based on a combination of the following metrics:

* **Sum of Squared Errors (SSE)**: The "elbow" in the SSE plot appeared around K=8 or K=9. After this point, the decrease in SSE for each additional cluster became less significant, suggesting diminishing returns. The drop from K=8 to K=9 was smaller than previous drops, and the drop from K=9 to K=10 was even smaller.
* **Silhouette Score**: The score of 0.45 indicates that the clusters are reasonably well-separated. While not perfect, it's a solid score for this type of dataset.
* **Davies-Bouldin Index (DBI)**: The DBI of 0.79 further supports the choice of K=9. A lower DBI is better, and this value suggests that the clusters are distinct enough for meaningful interpretation.

Choosing K=9 provided a good balance between model complexity (not too many clusters) and explanatory power (enough clusters to capture different customer behaviors).

## 3. Cluster Interpretation

Here is a description of each of the 9 clusters and a suggested business action for each:

| Cluster | Description | Annual Income (k$) | Spending Score (1-100) | Business Action |
| :--- | :--- | :--- | :--- | :--- |
| **0** | **High-Income Savers** | High (87.75) | Low (17.58) | Launch targeted campaigns for premium products or investment services to encourage spending. |
| **1** | **Low-Income Cautious** | Low (25.72) | Low (20.27) | Offer budget-friendly deals and loyalty programs to build brand loyalty and increase purchase frequency. |
| **2** | **High-Income Spenders** | High (86.53) | High (82.12) | Treat as VIPs. Offer exclusive access to new products, personalized services, and high-value upsells. |
| **3** | **Average Joes** | Mid (55.29) | Mid (49.51) | Standard marketing is effective. Use personalized recommendations based on past purchases to drive sales. |
| **4** | **Low-Income High-Spenders** | Low (26.30) | High (78.56) | This group might be young or taking on debt. Offer flexible payment options or student discounts. |
| **5** | **Elite Spenders** | Very High (109.71) | High (88.28) | Provide exclusive luxury products and white-glove services. Focus on retention and brand advocacy. |
| **6** | **Low-Income Risk Group** | Very Low (16.50) | Very High (80.50) | This group's spending exceeds their income, indicating potential risk. Approach with caution, perhaps with financial wellness resources. |
| **7** | **Low-Income Minimalists** | Very Low (19.50) | Very Low (13.33) | Focus on engagement and introducing entry-level products. Small, frequent promotions may be effective. |
| **8** | **Mid-Income Savers** | Mid (57.81) | Low (14.65) | Launch re-engagement campaigns to understand their needs better. Offer incentives to try new product categories. |

## 4. Limitations & Next Steps

**Limitations:**

The current segmentation is based only on two features: income and spending score. This provides a good high-level overview but lacks depth. Important demographic and behavioral information that could improve segmentation includes:

* **Age and Gender**: These were in the original dataset but were dropped. Including them could reveal patterns like "young male high-spenders" vs. "middle-aged female savers."
* **Purchase History**: Data on `Number of Visits`, `Items per Basket`, and `Product Categories` would allow for more granular, behavior-based segmentation.
* **Online vs. In-Store**: Understanding where customers shop could help tailor marketing channels and offers.

**Next Steps:**

A concrete next step would be to **incorporate the `Age` feature into the model**. By clustering on three features (`Annual Income`, `Spending Score`, and `Age`), we could uncover more nuanced customer profiles. For example, we might find that two clusters with similar income and spending scores are actually different age groups with different motivations (e.g., students vs. retirees). This would allow for even more targeted and effective business strategies.
