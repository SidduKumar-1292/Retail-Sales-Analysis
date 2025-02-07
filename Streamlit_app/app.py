import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff

# Configure Streamlit page
st.set_page_config(page_title="📊 Sales Dashboard", layout="wide")

# Load dataset
df = pd.read_csv("cleaned_sales_data.csv")
df["DATE"] = pd.to_datetime(df["DATE"])
df["Month"] = df["DATE"].dt.strftime("%Y-%m")  # Formatting month for better filtering

# Sidebar with dropdown filters
st.sidebar.title("🔍 Filters")

selected_supplier = st.sidebar.selectbox("Select Supplier", ["All"] + sorted(df["SUPPLIER"].unique()))
selected_month = st.sidebar.selectbox("Select Month", ["All"] + sorted(df["Month"].unique()))
selected_item_type = st.sidebar.selectbox("Select Item Type", ["All"] + sorted(df["ITEM TYPE"].unique()))

# Apply filters
filtered_df = df.copy()
if selected_supplier != "All":
    filtered_df = filtered_df[filtered_df["SUPPLIER"] == selected_supplier]
if selected_month != "All":
    filtered_df = filtered_df[filtered_df["Month"] == selected_month]
if selected_item_type != "All":
    filtered_df = filtered_df[filtered_df["ITEM TYPE"] == selected_item_type]

# Dashboard Title
st.title("📊 Interactive Sales Dashboard")
st.markdown("A **modern and user-friendly** dashboard with interactive filters and insights.")

# KPI Metrics
col1, col2, col3 = st.columns(3)
col1.metric(label="💰 Total Retail Sales", value=f"${filtered_df['RETAIL SALES'].sum():,.2f}")
col2.metric(label="📦 Total Retail Transfers", value=f"{filtered_df['RETAIL TRANSFERS'].sum():,}")
col3.metric(label="🏢 Total Warehouse Sales", value=f"{filtered_df['WAREHOUSE SALES'].sum():,}")

# 📈 Sales Trend Line Chart
st.subheader("📈 Monthly Sales Trend")
sales_trend = filtered_df.groupby("Month")["RETAIL SALES"].sum().reset_index()
fig1 = px.line(sales_trend, x="Month", y="RETAIL SALES", markers=True, title="Sales Trend Over Time")
st.plotly_chart(fig1, use_container_width=True)

# 🏭 Supplier Sales Performance Bar Chart
st.subheader("🏭 Supplier Sales Performance")
supplier_sales = filtered_df.groupby("SUPPLIER")["RETAIL SALES"].sum().reset_index()
fig2 = px.bar(supplier_sales, x="SUPPLIER", y="RETAIL SALES", color="RETAIL SALES", title="Sales by Supplier", text_auto=True)
st.plotly_chart(fig2, use_container_width=True)

# 🥇 Most Sold Items Pie Chart
st.subheader("🥇 Most Sold Items")
top_items = filtered_df.groupby("ITEM DESCRIPTION")["RETAIL SALES"].sum().sort_values(ascending=False).head(5)
fig3 = px.pie(names=top_items.index, values=top_items.values, title="Top 5 Most Sold Items", hole=0.4)
st.plotly_chart(fig3, use_container_width=True)

# 🔥 Sales Correlation Heatmap (Fixed)
st.subheader("🔥 Sales Correlation Heatmap")
correlation_matrix = filtered_df[["RETAIL SALES", "RETAIL TRANSFERS", "WAREHOUSE SALES"]].corr()
fig4 = ff.create_annotated_heatmap(
    z=correlation_matrix.values,
    x=list(correlation_matrix.columns),
    y=list(correlation_matrix.index),
    colorscale="RdBu",
    showscale=True
)
st.plotly_chart(fig4, use_container_width=True)

st.markdown("✅ **Dashboard Successfully Updated!** 🚀")
