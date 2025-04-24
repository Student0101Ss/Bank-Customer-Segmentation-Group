import pandas as pd

# ----------------------------------------------
# Step 0: Load the dataset
# ----------------------------------------------
# Load the CSV file (update path if needed)
file_path = r"D:\1. 2025 Work\A. Saeed Work 2025\Data Warehouse and Business Intelligence\bank_transactions.csv"
df = pd.read_csv(file_path)

# Display the first few rows to understand data structure
print("Initial Data Snapshot:")
print(df.head())

# ----------------------------------------------
# Step 1: Identify and remove null values
# ----------------------------------------------
# Drop rows with any missing (NaN) values
df = df.dropna()
print(f"\nStep 1 Complete: Removed null values. Remaining rows: {len(df)}")

# ----------------------------------------------
# Step 2: Identify and remove invalid transaction amount values
# ----------------------------------------------
# Keep only positive transaction amounts
df = df[df['TransactionAmount (INR)'] > 0]
print(f"Step 2 Complete: Removed invalid (≤0) transaction amounts. Remaining rows: {len(df)}")

# ----------------------------------------------
# Step 3: Identify and remove invalid age values
# ----------------------------------------------
# Convert CustomerDOB to datetime (DD/MM/YYYY format handling)
df['CustomerDOB'] = pd.to_datetime(df['CustomerDOB'], errors='coerce', dayfirst=True)

# Filter out invalid or very old birth dates (e.g., before 1800)
df = df[df['CustomerDOB'].dt.year > 1800]
print(f"Step 3 Complete: Removed invalid CustomerDOB values. Remaining rows: {len(df)}")

# ----------------------------------------------
# Step 4: Display the 5 top Locations with maximum number of transactions
# ----------------------------------------------
# Use the correct column name: 'CustLocation'
top_locations = df['CustLocation'].value_counts().head(5)

print("\nStep 4 Result: Top 5 Locations with Most Transactions:")
print(top_locations)

# ----------------------------------------------
# Final Step: Save the cleaned dataset to a new CSV
# ----------------------------------------------
cleaned_file_path = r"D:\1. 2025 Work\A. Saeed Work 2025\Data Warehouse and Business Intelligence\cleaned_bank_transactions.csv"
df.to_csv(cleaned_file_path, index=False)
print(f"\nFinal Step: Cleaned data saved successfully to: {cleaned_file_path}")
