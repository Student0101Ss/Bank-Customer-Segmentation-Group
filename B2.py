# rfm_kmeans_datamart.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Load transformed RFM data
rfm = pd.read_csv("D:/1. 2025 Work/A. Saeed Work 2025/Data Warehouse and Business Intelligence/rfm_values_transformed.csv")

# Extract log-transformed RFM values
rfm_log = rfm[['Recency_log', 'Frequency_log', 'Monetary_log']]

# Step 1: Standardize the data
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm_log)

# Step 2: Elbow Method to find optimal K
wcss = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(rfm_scaled)
    wcss.append(kmeans.inertia_)

# Plot Elbow Curve
plt.figure(figsize=(6, 4))
plt.plot(range(1, 11), wcss, marker='o')
plt.title("Elbow Method - Optimal K")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")
plt.grid(True)
plt.show()

# Step 3: Apply K-Means (Assume K=4)
optimal_k = 4
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)

# Step 4: Cluster Profiling
cluster_profile = rfm.groupby('Cluster').agg({
    'Recency': 'mean',
    'Frequency': 'mean',
    'Monetary': 'mean',
    'CustomerID': 'count'
}).rename(columns={
    'CustomerID': 'Num_Customers',
    'Recency': 'Avg_Recency',
    'Frequency': 'Avg_Frequency',
    'Monetary': 'Avg_Monetary'
}).reset_index()

# Sort by business value (High M and F, Low R)
cluster_profile_sorted = cluster_profile.sort_values(by=['Avg_Monetary', 'Avg_Frequency'], ascending=[False, False])

print("\n📊 Cluster Profiles (Sorted by Business Value):")
print(cluster_profile_sorted)

# Step 5: Visualize clusters (Recency vs Monetary)
sns.set(style="whitegrid")
plt.figure(figsize=(8, 5))
sns.scatterplot(data=rfm, x='Recency', y='Monetary', hue='Cluster', palette='Set2')
plt.title("Customer Segments based on Recency and Monetary")
plt.xlabel("Recency (Days)")
plt.ylabel("Monetary (INR)")
plt.legend(title='Cluster')
plt.show()

# Step 6 (Optional): High-value segments by location (if location available)
if 'City' in rfm.columns:
    segment_location = rfm.groupby(['Cluster', 'City']).agg({
        'CustomerID': 'count',
        'Monetary': 'mean'
    }).rename(columns={
        'CustomerID': 'Num_Customers',
        'Monetary': 'Avg_Monetary'
    }).reset_index()

    high_value_locations = segment_location.sort_values(by='Avg_Monetary', ascending=False)

    print("\n📍 Top High-Value Segments by Location:")
    print(high_value_locations.head(10))

# Step 7: Export final clustered dataset for data mart
rfm.to_csv("rfm_clustered_final.csv", index=False)
print("\n✅ Clustered RFM data exported as 'rfm_clustered_final.csv'")
