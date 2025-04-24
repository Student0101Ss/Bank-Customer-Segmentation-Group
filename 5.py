import pandas as pd

# Load cleaned dataset
file_path = r"D:\1. 2025 Work\A. Saeed Work 2025\Data Warehouse and Business Intelligence\cleaned_bank_transactions.csv"
df = pd.read_csv(file_path)

# Ensure TransactionDate is datetime
df['TransactionDate'] = pd.to_datetime(df['TransactionDate'], errors='coerce', dayfirst=True)

# Drop rows with invalid dates
df = df.dropna(subset=['TransactionDate'])

# Reference date for Recency calculation (e.g., max date in dataset)
reference_date = df['TransactionDate'].max()

# Group by CustomerID to calculate RFM
rfm = df.groupby('CustomerID').agg({
    'TransactionDate': lambda x: (reference_date - x.max()).days,  # Recency
    'TransactionAmount (INR)': ['count', 'sum']                    # Frequency, Monetary
})

# Rename columns
rfm.columns = ['Recency', 'Frequency', 'Monetary']
rfm = rfm.reset_index()

# Save RFM table
rfm_file = r"D:\1. 2025 Work\A. Saeed Work 2025\Data Warehouse and Business Intelligence\rfm_values.csv"
rfm.to_csv(rfm_file, index=False)

# Show first 20 rows of the RFM table
print("\nFirst 20 Rows of RFM Table:")
print(rfm.head(20))
