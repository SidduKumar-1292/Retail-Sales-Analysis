import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the cleaned dataset
df = pd.read_csv("cleaned_sales_data.csv")

# Step 2: Convert DATE to datetime format
df["DATE"] = pd.to_datetime(df["DATE"])

# Step 3: Extract month & year for visualization
df["Month"] = df["DATE"].dt.strftime("%Y-%m")

# Step 4: Total sales per supplier (Bar Chart)
plt.figure(figsize=(10, 5))
supplier_sales = df.groupby("SUPPLIER")["RETAIL SALES"].sum().reset_index()
sns.barplot(x="SUPPLIER", y="RETAIL SALES", data=supplier_sales, palette="viridis")
plt.xticks(rotation=45)
plt.xlabel("Supplier")
plt.ylabel("Total Sales")
plt.title("Total Sales per Supplier")
plt.show()

# Step 5: Monthly Sales Trend (Line Chart)
monthly_sales = df.groupby("Month")["RETAIL SALES"].sum()
plt.figure(figsize=(10, 5))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o', linestyle='-', color='b')
plt.xticks(rotation=45)
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Monthly Sales Trend")
plt.grid()
plt.show()

# Step 6: Most Sold Items (Pie Chart)
top_items = df.groupby("ITEM DESCRIPTION")["RETAIL SALES"].sum().sort_values(ascending=False).head(5)
plt.figure(figsize=(7, 7))
plt.pie(top_items, labels=top_items.index, autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])
plt.title("Top 5 Most Sold Items")
plt.show()

# Step 7: Correlation Heatmap
plt.figure(figsize=(8, 5))
sns.heatmap(df[["RETAIL SALES", "RETAIL TRANSFERS", "WAREHOUSE SALES"]].corr(), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()

print("\nData Visualization Completed Successfully! ✅")
