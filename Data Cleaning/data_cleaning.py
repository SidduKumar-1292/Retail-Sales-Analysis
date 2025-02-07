import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv("sales_data.csv")

# Step 2: Display the first few rows
print("Original Data:\n", df.head())

# Step 3: Check for missing values
print("\nMissing values before cleaning:\n", df.isnull().sum())

# Step 4: Remove duplicate rows
df.drop_duplicates(inplace=True)

# Step 5: Fill missing values (if any)
df.fillna(0, inplace=True)  # Replace NaN values with 0

# Step 6: Convert MONTH column to proper format (if it contains numeric values)
if df['MONTH'].dtype in ['int64', 'float64']:
    df['MONTH'] = df['MONTH'].astype(int).astype(str).str.zfill(2)  # Ensure two-digit format (e.g., 01, 02, ...)

# Step 7: Convert YEAR and MONTH to a single DATE column
df['DATE'] = pd.to_datetime(df['YEAR'].astype(str) + '-' + df['MONTH'], format='%Y-%m')

# Step 8: Drop unnecessary columns (YEAR, MONTH) since we have DATE now
df.drop(columns=['YEAR', 'MONTH'], inplace=True)

# Step 9: Display cleaned data
print("\nCleaned Data:\n", df.head())

# Step 10: Save the cleaned dataset
df.to_csv("cleaned_sales_data.csv", index=False)

print("\nData cleaning completed. Cleaned file saved as 'cleaned_sales_data.csv'.")
