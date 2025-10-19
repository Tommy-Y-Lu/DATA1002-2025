# RUN INDIVIDUAL METHOD

# import numpy as np
# from sklearn.cluster import KMeans
# from sklearn.preprocessing import StandardScaler
# import matplotlib.pyplot as plt

# # 1. Generate some sample data
# X = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])

# # 2. Preprocessing (Scaling the data is often important for K-Means)
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)

# # 3. Apply K-Means clustering
# # We'll assume we want 2 clusters for this example.
# # n_init="auto" handles the initialization method, often K-Means++.
# kmeans = KMeans(n_clusters=2, random_state=0, n_init="auto")
# kmeans.fit(X_scaled)

# # 4. Get cluster assignments and centroids
# labels = kmeans.labels_
# centroids = kmeans.cluster_centers_

# # 5. Visualize the results (optional)
# plt.figure(figsize=(8, 6))
# plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels, cmap='viridis', s=100, alpha=0.8)
# plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label='Centroids')
# plt.title('K-Means Clustering')
# plt.xlabel('Scaled Feature 1')
# plt.ylabel('Scaled Feature 2')
# plt.legend()
# plt.grid(True)
# plt.show()

# # 6. Predict new data points (optional)
# new_data = np.array([[0, 0], [10, 10]])
# new_data_scaled = scaler.transform(new_data)
# predictions = kmeans.predict(new_data_scaled)
# print(f"Predictions for new data points: {predictions}")

# TEST GROUP OF METHODS

# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.datasets import make_blobs
# from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering

# # ----- Generate sample data -----
# X, y_true = make_blobs(
#     n_samples=500,
#     centers=4,
#     cluster_std=0.60,
#     random_state=0
# )

# # ----- Define clustering models -----
# models = {
#     "K-Means": KMeans(n_clusters=4, random_state=0),
#     "DBSCAN": DBSCAN(eps=0.5, min_samples=5),
#     "Agglomerative": AgglomerativeClustering(n_clusters=4)
# }

# # ----- Fit and plot results -----
# plt.figure(figsize=(12, 4))

# for i, (name, model) in enumerate(models.items(), 1):
#     y_pred = model.fit_predict(X)
    
#     plt.subplot(1, 3, i)
#     plt.scatter(X[:, 0], X[:, 1], c=y_pred, cmap='rainbow', s=15)
#     plt.title(name)
#     plt.xlabel('Feature 1')
#     plt.ylabel('Feature 2')

# plt.tight_layout()
# plt.show()