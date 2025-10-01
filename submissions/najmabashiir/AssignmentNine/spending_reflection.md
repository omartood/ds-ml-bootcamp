# 📄 Spending Pattern Analysis — Reflection (Part B)

**Dataset features used for clustering:** `Income_$`, `SpendingScore`  
**Algorithm:** K-Means (`k = 4`)  
**Your metrics:**  
- **Silhouette Score:** **0.729** (good separation)  
- **Davies–Bouldin Index:** **0.387** (low = good)  

---

## 1) What did I implement?

I implemented customer **spending segmentation** using **K-Means** on two standardized features: **Income_$** and **SpendingScore**.

**Workflow**
1. Selected features: `Income_$`, `SpendingScore` → handled numerics only.  
2. **Scaled** features with `StandardScaler` so both dimensions contribute equally.  
3. Ran an **SSE (inertia) loop** for `k = 1..10` to check the elbow trend.  
4. Trained **KMeans(n_clusters=4, random_state=42)**.  
5. Computed **Silhouette** and **DBI** to quantify separation and compactness.  
6. **Assigned labels** back to the dataset (column: `cluster`) and saved the labeled file.

---

## 2) Why choose K = 4?

- The **SSE** curve showed diminishing returns around **k ≈ 4** (elbow).  
- **Silhouette = 0.729** indicates **well-separated clusters** with strong cohesion (values near 1 are best).  
- **DBI = 0.387** is **low**, meaning clusters are compact and far from each other.  

Together, these justify **k = 4** as a balanced choice: simple enough to explain, while still capturing the distinct spending patterns in the data.

---

## 3) Interpreting the 4 clusters (plain language + action)

> I focus on the two features used (Income and SpendingScore). Ranges below are based on your labeled rows.

### **Cluster 2 — Low Income / High Spending (Young “trend seekers”)**
- **Pattern:** Income mostly **14–35**; **SpendingScore 70–98**. Many young shoppers.  
- **Example customers:** ID **10** (Income 29, Score 81), ID **20** (18, 98).  
- **Business action:** **Loyalty bundles** and **student offers**; promote **buy-now deals** and app-based rewards to retain high spenders despite low income.

### **Cluster 0 — Mid Income / Mid Spending (Steady value shoppers)**
- **Pattern:** Income around **46–80**; **SpendingScore ~40–67**. Balanced behavior.  
- **Example customers:** ID **67** (80, 55), ID **91** (72, 56).  
- **Business action:** **Value packs** and **personalized cross-sell** (e.g., complementary products); emphasize reliability/quality to increase basket size.

### **Cluster 1 — Low Income / Low Spending (Budget‑conscious & infrequent)**
- **Pattern:** Income **16–43**; **SpendingScore 8–29**; generally lower activity.  
- **Example customers:** ID **110** (29, 29), ID **103** (28, 8).  
- **Business action:** **Price-led promotions** and **starter discounts**; send **welcome-back coupons** to increase visit frequency.

### **Cluster 3 — High Income / High Spending (Premium enthusiasts)**
- **Pattern:** Income **82–115**; **SpendingScore 69–95**; frequent purchases.  
- **Example customers:** ID **197** (115, 87), ID **200** (115, 95).  
- **Business action:** **VIP program** (early access, exclusives), **personal shopping** services, and **high-margin upsells**.

---

## 4) Limitations & Next Steps

**Limitations**
- Clustering used only **two features**; behavior may depend on **VisitsPerMonth** and **OnlinePurchases** too.  
- K-Means assumes roughly **spherical clusters** and is sensitive to outliers.  
- Segment names are **inferred** (unsupervised) — interpretation needs business validation.

**Next Steps**
1. **Add a 3rd feature** (e.g., `VisitsPerMonth`) and re-evaluate (`Silhouette`, `DBI`).  
2. Try **DBSCAN** to detect **outliers** and non-spherical shapes.  
3. Produce **cluster center table** (inverse-scaled) and share with marketing for campaign design.  
4. Track **lift**: run small A/B tests per segment to validate actions (e.g., loyalty bundle → repeat rate).

---

## 5) Mini sanity check (one from each cluster)

| CustomerID | Income_$ | SpendingScore | Cluster | Segment Summary                      |
|-----------:|---------:|--------------:|:-------:|--------------------------------------|
| 10         | 29       | 81            |    2    | Low income / High spending           |
| 67         | 80       | 55            |    0    | Mid income / Mid spending            |
| 110        | 29       | 29            |    1    | Low income / Low spending            |
| 197        | 115      | 87            |    3    | High income / High spending (premium)|

These examples match the narratives above and support **k = 4** as a meaningful segmentation.

---

### ✅ Bottom line
- **K = 4** is justified by **SSE elbow + Silhouette 0.729 + DBI 0.387**.  
- The four segments are **distinct and actionable** for marketing and retention strategies.  
- Next, enrich with more features and validate via targeted campaigns.
