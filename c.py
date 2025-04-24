import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
rfm = pd.read_csv("rfm_clustered_final.csv")
transactions = pd.read_csv("cleaned_bank_transactions.csv")

# Merge datasets on CustomerID
merged = pd.merge(transactions, rfm, on='CustomerID', how='inner')

# Step 1: Find top 5 locations by number of transactions
top_locations = merged['CustLocation'].value_counts().head(5).index.tolist()
print("Top 5 Locations by Number of Transactions:", top_locations)

# Filter only top 5 locations
top_location_data = merged[merged['CustLocation'].isin(top_locations)]

# Step 2: Analyze cluster distribution in top locations
cluster_location_summary = top_location_data.groupby(['CustLocation', 'Cluster']).agg({
    'CustomerID': 'nunique',
    'Recency': 'mean',
    'Frequency': 'mean',
    'Monetary': 'mean'
}).rename(columns={'CustomerID': 'Unique_Customers'}).reset_index()

print("\n📊 Cluster-wise Summary in Top 5 Locations:")
print(cluster_location_summary)

# Step 3: Visualize cluster distribution per location
plt.figure(figsize=(12, 6))
sns.countplot(data=top_location_data, x='CustLocation', hue='Cluster', palette='Set2')
plt.title("Cluster Distribution Across Top 5 Locations")
plt.ylabel("Number of Transactions")
plt.xlabel("Customer Location")
plt.legend(title="Cluster")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
