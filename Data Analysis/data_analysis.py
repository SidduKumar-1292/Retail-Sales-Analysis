import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the cleaned dataset
df = pd.read_csv("cleaned_sales_data.csv")

# Step 2: Display summary statistics
print("\nSummary Statistics:\n", df.describe())

# Step 3: Total sales per supplier
supplier_sales = df.groupby("SUPPLIER")["RETAIL SALES"].sum().reset_index()
print("\nTotal Sales per Supplier:\n", supplier_sales)

# Step 4: Most sold items
most_sold_items = df.groupby("ITEM DESCRIPTION")["RETAIL SALES"].sum().sort_values(ascending=False).head(5)
print("\nMost Sold Items:\n", most_sold_items)

# Step 5: Monthly sales trends
df["DATE"] = pd.to_datetime(df["DATE"])
df["Month"] = df["DATE"].dt.strftime("%Y-%m")
monthly_sales = df.groupby("Month")["RETAIL SALES"].sum()

# Step 6: Plot Monthly Sales Trend
plt.figure(figsize=(10, 5))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o', linestyle='-', color='b')
plt.xticks(rotation=45)
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Monthly Sales Trend")
plt.grid()
plt.show()

# Step 7: Bar Chart for Supplier Sales
plt.figure(figsize=(10, 5))
sns.barplot(x="SUPPLIER", y="RETAIL SALES", data=supplier_sales)
plt.xticks(rotation=45)
plt.xlabel("Supplier")
plt.ylabel("Total Sales")
plt.title("Total Sales per Supplier")
plt.show()

print("\nData Analysis Completed Successfully! ✅")
