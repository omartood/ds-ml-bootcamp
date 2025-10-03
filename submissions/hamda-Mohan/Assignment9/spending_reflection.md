 
# Reflection Paper – Spending Pattern Analysis with K-Means

## 1. What Did You Implement?

In this assignment, I implemented **customer segmentation using K-Means clustering**.

The workflow included:

* **Data Preparation:**
  Selected features `Annual Income ($)` and `Spending Score (1-100)` from the dataset. Missing values were filled with the **median**.

* **Feature Scaling:**
  Standardized the features using `StandardScaler` (mean = 0, standard deviation = 1).

* **Model Training (Elbow Check):**
  Trained KMeans for `k = 1..10` and printed the **SSE (inertia)** to identify the "elbow point."

* **Final Model:**
  Based on the elbow method, **k = 5** clusters were chosen and each customer was assigned a cluster label.

* **Evaluation:**
  Calculated clustering metrics:

```text
Silhouette Score = 0.555
Davies–Bouldin Index (DBI) = 0.572
```

* **Cluster Centers:**
  Inverse-transformed cluster centers to original units (income & spending score).

* **Output:**
  Added `Cluster` column, performed a sanity check with sample rows, and saved the labeled dataset to **`customers_labeled_data.csv`**.

---

## 2. Choosing K

```text
SSE values for k = 1..10:
k = 1 → SSE = 400.00
k = 2 → SSE = 273.67
k = 3 → SSE = 157.70
k = 4 → SSE = 109.23
k = 5 → SSE = 65.57
k = 6 → SSE = 60.13
k = 7 → SSE = 49.67
k = 8 → SSE = 37.32
k = 9 → SSE = 32.50
k = 10 → SSE = 30.06
```

* The **sharpest drop** in SSE occurred between `k=2` and `k=5`.
* At **k=5**, the trade-off between SSE, Silhouette (0.555), and DBI (0.572) suggested a good clustering solution.

* Therefore, **k = 5** was chosen as the final model.

---

## 3. Cluster Interpretation

Cluster centers (original units):

| Cluster | Annual_Income_($) | Spending_Score_(1-100) |
| ------- | ----------------- | ---------------------- |
| 0       | 55.30             | 49.52                  |
| 1       | 86.54             | 82.13                  |
| 2       | 25.73             | 79.36                  |
| 3       | 88.20             | 17.11                  |
| 4       | 26.30             | 20.91                  |

**Business Meaning:**

| Cluster | Description                       | Suggested Action                                         |
| ------- | --------------------------------- | -------------------------------------------------------- |
| 0       | Middle-income, average spending   | Promote seasonal bundles, upselling strategies           |
| 1       | High income, high spending (VIPs) | Offer loyalty programs, premium services, VIP events     |
| 2       | Low income, high spending         | Provide affordable deals, budget-friendly loyalty offers |
| 3       | High income, low spending         | Targeted marketing campaigns to encourage spending       |
| 4       | Low income, low spending          | Awareness campaigns, entry-level discounts to attract    |

---

## 4. Limitations & Next Steps

### Limitations

* Only two features were used (Income & Spending Score).
* Other potentially useful features such as visit frequency, online purchases, or product preferences were not included.
* K-Means assumes spherical clusters, which may not perfectly represent real-world spending.

### Next Steps

1. **Add More Features:** Incorporate  Visit Frequency, Online Purchases,product preferences, or membership status for more accurate segmentation.
2. **Try Alternative Algorithms:** Explore **DBSCAN** or hierarchical clustering.
3. **Cluster Validation:** Compare results with multiple clustering metrics.
4. **Business Testing:** Validate cluster-driven strategies with actual sales data.

---

## 5. Conclusion

Using K-Means, customers were segmented into **five meaningful groups**:

* **VIPs, budget spenders, balanced buyers, disengaged wealthy, and low-value groups**.

This segmentation enables **targeted strategies**, loyalty programs, and personalized promotions to improve **customer satisfaction** and **business revenue**.

---
