import pandas as pd
# from sklearn.preprocessing import StandardScaler
# from sklearn.cluster import KMeans
# from sklearn.metrics import silhouette_score,davies_bouldin_score

# CSV_PATH = 'customers_l9_dataset.csv'
# df = pd.read_csv(CSV_PATH)
# # print(df.head())

# FEATURES = ['Annual Income ($)', 'Spending Score (1-100)']

# X = df[FEATURES].copy()
# # print(X.head())

# for col in FEATURES:
#     if X[col].isna().any():
#         median_value = X[col].median()
#         X[col]=X[col].fillna(median_value)


# # print("before",X.head())
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)
# # print("After",X_scaled[:5])

# for k in range(1, 11):
#     kmeans = KMeans(n_clusters=k, random_state=42)
#     kmeans.fit(X_scaled)
#     inertia = kmeans.inertia_
#     print(f'K={k}, Inertia={inertia:.3f}')


# km = KMeans(n_clusters=5, random_state=42)
# labels = km.fit_predict(X_scaled)
# df['Cluster'] = labels.astype(int)
# # print(df.head()) 

# silhouette_avg = silhouette_score(X_scaled, labels)
# davies_bouldin_avg = davies_bouldin_score(X_scaled, labels)
# # print("Model Evaluation Metrics:    ")
# # print(f'Silhouette Score: {silhouette_avg:.3f} (closer to 1 is better)')
# # print(f'Davies-Bouldin Index: {davies_bouldin_avg:.3f} (closer to 0 is better)')
# centers_scaled = km.cluster_centers_
# original_centers = scaler.inverse_transform(centers_scaled)
# centers_df = pd.DataFrame(original_centers, columns=FEATURES)

# # print("Change to Original unit : ",centers_df.round(2))
# sample_index = [0, 1, 23]
# sample_customers = df.loc[sample_index, FEATURES+['Cluster']]
# # print("Sample Customers with Cluster Assignments:")
# # print(sample_customers)

# # df.to_csv('clustered_customers.csv', index=False)
# print("Clustered data saved to 'clustered_customers.csv'")

df = pd.read_csv('clustered_customers.csv')
print(df["Cluster"].value_counts())


    
