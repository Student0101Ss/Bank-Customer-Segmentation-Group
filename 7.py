import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------------------------
# Load the RFM dataset
# ----------------------------------------------
rfm_file = r"D:\1. 2025 Work\A. Saeed Work 2025\Data Warehouse and Business Intelligence\rfm_values.csv"
rfm = pd.read_csv(rfm_file)

# ----------------------------------------------
# Step 7: Discuss and Remove Skewness from the Data
# ----------------------------------------------

# Log-transform Recency, Frequency, and Monetary to reduce right skewness
rfm['Recency_log'] = np.log1p(rfm['Recency'])      # log1p handles log(0) by computing log(1 + x)
rfm['Frequency_log'] = np.log1p(rfm['Frequency'])
rfm['Monetary_log'] = np.log1p(rfm['Monetary'])

# Plot the transformed distributions
sns.set(style="whitegrid")

# Recency
plt.figure(figsize=(6, 4))
sns.histplot(rfm['Recency_log'], bins=30, kde=True)
plt.title("Log-Transformed Distribution of Recency")
plt.xlabel("Log(Recency)")
plt.ylabel("Number of Customers")
plt.show()

# Frequency
plt.figure(figsize=(6, 4))
sns.histplot(rfm['Frequency_log'], bins=30, kde=True)
plt.title("Log-Transformed Distribution of Frequency")
plt.xlabel("Log(Frequency)")
plt.ylabel("Number of Customers")
plt.show()

# Monetary
plt.figure(figsize=(6, 4))
sns.histplot(rfm['Monetary_log'], bins=30, kde=True)
plt.title("Log-Transformed Distribution of Monetary")
plt.xlabel("Log(Monetary)")
plt.ylabel("Number of Customers")
plt.xticks(np.arange(0, np.ceil(rfm['Monetary_log'].max()) + 1, 0.5))  # Add nice tick spacing
plt.show()

# ----------------------------------------------
# Save the transformed RFM dataset
# ----------------------------------------------
transformed_file_path = r"D:\1. 2025 Work\A. Saeed Work 2025\Data Warehouse and Business Intelligence\rfm_values_transformed.csv"
rfm.to_csv(transformed_file_path, index=False)
print(f"\nStep 7 Complete: Transformed RFM data saved to: {transformed_file_path}")
