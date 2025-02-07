import pandas as pd

# Load the dataset
df = pd.read_csv("sales_data.csv")

# Display the first few rows
print(df.head())

# Check for missing values
print("\nMissing values:\n", df.isnull().sum())

# Display summary statistics
print("\nSummary Statistics:\n", df.describe())
