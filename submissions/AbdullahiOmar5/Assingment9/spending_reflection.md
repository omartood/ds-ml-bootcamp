# K-Means Clustering for Customer Segmentation Analysis

## I. K-Means Implementation Workflow

**Objective**: Segment customers using K-Means based on two features: Income and Spending Score.

### Workflow Description

- **Data Preparation**: Selected Income and Spending Score features for clustering.
- **Data Scaling**: Normalized features using `StandardScaler` to ensure equal contribution to clustering.
- **Optimal K Determination**: Iterated across K values, calculating:
  - Sum of Squared Errors (SSE)
  - Silhouette Score
  - Davies-Bouldin Index (DBI)
- **Model Finalization**: Trained final K-Means model with chosen K=4 and added cluster labels to customer data.

---

## II. Choosing the Optimal K=4

**Rationale for K=4 Clusters**:

- **SSE (Elbow Method)**:
  - Sharpest drop from K=1 (400.00) to K=4 (21.37)
  - K=5 shows further reduction (19.09), but K=4 is past the "bend" — optimal balance point

- **Silhouette Score**:
  - K=4 model achieved **0.729** (closer to +1 is better)
  - Indicates well-separated, dense clusters

- **Davies-Bouldin Index (DBI)**:
  - K=4 model returned **0.387** (lower is better)
  - Confirms excellent cluster distinction

**Conclusion**: K=4 offers the best balance between model complexity and interpretability.

---

## III. Cluster Interpretation and Business Action

| Cluster | Interpretation (Plain Language) | Business Action Suggestion |
|--------|----------------------------------|-----------------------------|
| 0      | Medium Income, High Spending     | Loyalty/Upsell: Offer a premium loyalty program to capitalize on high spending. |
| 1      | Low Income, Low Spending         | Retention: Offer deep-discount or volume-based incentives to increase visit frequency. |
| 2      | High Income, High Spending       | Exclusivity: Market high-margin, exclusive products and VIP events. |
| 3      | High Income, Low Spending        | Activation: Run campaigns to convert high income into retail spending. |

---

## IV. Limitations & Next Steps

### Information to Improve Segmentation

Current segmentation uses only two demographic features. Adding behavioral and lifecycle data would enhance depth and actionability.

**Recommended Features**:
- **Age**: Distinguishes life stages (e.g., young professionals vs. retirees)
- **Visits Per Month**: Indicates customer engagement and loyalty
- **Online Purchases**: Reveals preferred shopping channel (in-store vs. e-commerce)

### Concrete Next Step

Retrain the model using **three features**: Income, Spending Score, and Age.

This would:
- Deepen segment understanding
- Potentially split high-spending groups by generational buying behavior
