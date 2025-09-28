# Spending Pattern Clustering – Reflection Paper

## 1. Implementation Overview

In this project, I applied **K-Means clustering** to segment customers based on their **annual income** and **spending score**. The workflow involved several key stages:

* **Data Preparation:** The dataset was loaded and inspected. Missing numeric values were imputed with the median to ensure data consistency.
* **Feature Selection:** Only `Income_$` and `SpendingScore` were used for clustering.
* **Scaling:** Features were standardized with *StandardScaler* so that both contributed equally.
* **Model Exploration:** The **Elbow Method** was used by computing the **Sum of Squared Errors (SSE)** for `k = 1–10`.
* **Final Training:** Based on the elbow, the model was trained with **k = 4**. Each customer was assigned a cluster label.
* **Evaluation:** The clustering quality was assessed using the **Silhouette Score** and the **Davies–Bouldin Index (DBI)**.
* **Interpretation:** Cluster centers were transformed back into the original units for business meaning.
* **Output:** A labeled dataset was saved for future use.

---

## 2. Choosing the Number of Clusters (K)

The SSE values were:

* **k=1 → 400.00**
* **k=2 → 199.70**
* **k=3 → 79.37**
* **k=4 → 21.37**
* **k=5 → 19.09**

The sharp decrease flattened noticeably after **k=4**, forming a clear elbow.

Additional metrics supported this choice:

* **Silhouette Score:** 0.73 (high, showing well-separated groups)
* **Davies–Bouldin Index:** 0.39 (low, showing compact clusters)

Together, these confirmed that **k=4** was the most appropriate number of clusters.

---

## 3. Cluster Interpretation and Business Implications

| Cluster | Income_$ | SpendingScore | Interpretation                     | Suggested Action                 |
| ------- | -------- | ------------- | ---------------------------------- | -------------------------------- |
| 0       | ~56      | ~54           | Moderate income, moderate spending | Standard loyalty programs        |
| 1       | ~29      | ~20           | Low income, low spending           | Entry-level offers & discounts   |
| 2       | ~24      | ~83           | Low income, high spending          | Affordable upsell opportunities  |
| 3       | ~99      | ~79           | High income, high spending         | Premium services & VIP treatment |

**Summary of Segments:**

* **Cluster 0:** Balanced customers who fit standard loyalty offers.
* **Cluster 1:** Price-sensitive customers; should be targeted with discounts.
* **Cluster 2:** Valuable spenders despite low income; respond well to budget-friendly upsells.
* **Cluster 3:** High-value clients; ideal for exclusive memberships and luxury experiences.

---

## 4. Limitations and Next Steps

**Limitations**

* Only two variables (income, spending) were used; richer demographic or behavioral data (age, shopping frequency, online purchases) could improve insights.
* K-Means assumes clusters are spherical and equally sized, which may not reflect real-world complexity.

**Next Steps**

* Extend clustering with a third feature, such as **Age**, to test for stronger separation.
* Experiment with **DBSCAN** to capture irregular cluster shapes and handle outliers.
* Use **visualizations** (scatter plots, PCA reduction) to communicate results more effectively.

---