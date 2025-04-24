# Step 8: K-Means Clustering on Transformed RFM Data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Load the transformed RFM data
rfm = pd.read_csv("D:/1. 2025 Work/A. Saeed Work 2025/Data Warehouse and Business Intelligence/rfm_values_transformed.csv")

# Extract the log-transformed RFM values
rfm_log = rfm[['Recency_log', 'Frequency_log', 'Monetary_log']]

# Step 1: Standardize the data
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm_log)

# Step 2: Use Elbow Method to find the optimal K
wcss = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(rfm_scaled)
    wcss.append(kmeans.inertia_)

# Plot the Elbow Curve
plt.figure(figsize=(6, 4))
plt.plot(range(1, 11), wcss, marker='o')
plt.title("Elbow Method - Optimal K")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")
plt.xticks(range(1, 11))
plt.grid(True)
plt.show()

# Step 3: Apply K-Means with optimal K (assume K=4 here)
kmeans = KMeans(n_clusters=4, random_state=42)
rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)

# Step 4: Analyze cluster profiles
cluster_profile = rfm.groupby('Cluster').agg({
    'Recency': 'mean',
    'Frequency': 'mean',
    'Monetary': 'mean',
    'CustomerID': 'count'
}).rename(columns={'CustomerID': 'Num_Customers'})

print("\nCluster Profiles:")
print(cluster_profile)

# Step 5: Visualize the clusters
sns.set(style="whitegrid")
plt.figure(figsize=(8, 5))
sns.scatterplot(data=rfm, x='Recency', y='Monetary', hue='Cluster', palette='Set2')
plt.title("Customer Segments based on Recency and Monetary")
plt.xlabel("Recency (Days)")
plt.ylabel("Monetary (INR)")
plt.legend(title='Cluster')
plt.show()
