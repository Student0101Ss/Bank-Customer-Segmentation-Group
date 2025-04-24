import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the RFM data
rfm_file = r"D:\1. 2025 Work\A. Saeed Work 2025\Data Warehouse and Business Intelligence\rfm_values.csv"
rfm = pd.read_csv(rfm_file)

# Set up plot style
sns.set(style="whitegrid")

# ----------------------------
# Plot Recency Distribution
# ----------------------------
plt.figure(figsize=(6, 4))
sns.histplot(rfm['Recency'], bins=30, kde=True)
plt.title("Distribution of Recency")
plt.xlabel("Days Since Last Transaction")
plt.ylabel("Number of Customers")
plt.show()

# ----------------------------
# Plot Frequency Distribution
# ----------------------------
plt.figure(figsize=(6, 4))
sns.histplot(rfm['Frequency'], bins=30, kde=True)
plt.title("Distribution of Frequency")
plt.xlabel("Number of Transactions")
plt.ylabel("Number of Customers")
plt.show()

# ----------------------------
# Plot Monetary Distribution (with log scale)
# ----------------------------
plt.figure(figsize=(6, 4))
sns.histplot(rfm['Monetary'], bins=30, kde=True, log_scale=(True, False))
plt.title("Distribution of Monetary (Log Scale)")
plt.xlabel("Total Amount Spent by Customer (INR) [Log Scale]")
plt.ylabel("Number of Customers")
plt.show()
