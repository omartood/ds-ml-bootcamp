# ===============================
# Customer Segmentation (Clustering)
# - K-Means + Clustering Metrics
# ===============================

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, davies_bouldin_score

# --------------------------------
# 1) Load dataset
# --------------------------------
CSV_PATH = "dataset/customers_l9_dataset.csv"
df = pd.read_csv(CSV_PATH)
print("\n=== INITIAL SNAPSHOT ===")
print(df.head())

# --------------------------------
# 2) Select features for clustering
# --------------------------------
FEATURES = ["Age", "Annual Income ($)", "Spending Score (1-100)"]
X = df[FEATURES].copy()

# Fill missing numeric values (if any) with median
for col in FEATURES:
    if X[col].isna().any():
        X[col] = X[col].fillna(X[col].median())

print("\n=== FEATURES HEAD ===")
print(X.head())

# --------------------------------
# 3) Scale features
# --------------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print("\nScaled shape:", X_scaled.shape)

# --------------------------------
# 4) Elbow method (print SSE)
# --------------------------------
print("\n=== ELBOW METHOD (SSE per k) ===")
for k in range(1, 11):
    km = KMeans(n_clusters=k, n_init="auto", random_state=42)
    km.fit(X_scaled)
    print(f"k={k} → SSE={km.inertia_:.2f}")

# --------------------------------
# 5) Fit K-Means with chosen k
# --------------------------------
K = 5  # adjust based on SSE values above
kmeans = KMeans(n_clusters=K, n_init="auto", random_state=42)
labels = kmeans.fit_predict(X_scaled)

df["Cluster"] = labels.astype(int)
print("\n=== SAMPLE WITH CLUSTERS ===")
print(df.head())

# --------------------------------
# 6) Evaluate clustering
# --------------------------------
sil = silhouette_score(X_scaled, labels)
dbi = davies_bouldin_score(X_scaled, labels)
print("\n=== METRICS ===")
print(f"Silhouette Score : {sil:.3f} (closer to +1 is better)")
print(f"Davies–Bouldin   : {dbi:.3f} (lower is better)")

# --------------------------------
# 7) Cluster centers (back to original units)
# --------------------------------
centers_scaled = kmeans.cluster_centers_
centers_original = scaler.inverse_transform(centers_scaled)

centers_df = pd.DataFrame(centers_original, columns=FEATURES)
centers_df.index.name = "Cluster"

print("\n=== CLUSTER CENTERS (Original Units) ===")
print(centers_df.round(2))

# --------------------------------
# 8) Sanity checks (3 customers)
# --------------------------------
sample_idx = [0, 1, 2]  # change to any row numbers
sanity = df.loc[sample_idx, FEATURES + ["Cluster"]]
print("\n=== SANITY CHECK (3 Customers) ===")
print(sanity)

# --------------------------------
# 9) Save labeled dataset
# --------------------------------
OUT_PATH = "customers_labeled_clusters.csv"
df.to_csv(OUT_PATH, index=False)
print(f"\nSaved clustered dataset → {OUT_PATH}")
