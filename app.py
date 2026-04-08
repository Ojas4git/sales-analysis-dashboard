import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📊 Sales Analysis Dashboard")

# Load data
data = pd.read_csv("Sample - Superstore.csv", encoding='latin1')

# Convert date
data['Order Date'] = pd.to_datetime(data['Order Date'])

st.write("---")

# KPI Section
total_sales = data['Sales'].sum()
total_profit = data['Profit'].sum()
total_orders = data['Order ID'].nunique()

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Total Profit", f"${total_profit:,.0f}")
col3.metric("Total Orders", total_orders)

st.write("---")

# Sales by Category
st.subheader("Sales by Category")
category_sales = data.groupby('Category')['Sales'].sum()

fig1, ax1 = plt.subplots()
category_sales.plot(kind='bar', ax=ax1)
st.pyplot(fig1)

# Monthly Sales Trend
st.subheader("Monthly Sales Trend")
monthly_sales = data.groupby(data['Order Date'].dt.to_period('M'))['Sales'].sum()

fig2, ax2 = plt.subplots()
monthly_sales.plot(ax=ax2)
st.pyplot(fig2)

# Top 10 Products
st.subheader("Top 10 Products")
top_products = data.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

fig3, ax3 = plt.subplots()
top_products.plot(kind='barh', ax=ax3)
st.pyplot(fig3)

# Region Sales
st.subheader("Sales by Region")
region_sales = data.groupby('Region')['Sales'].sum()

fig4, ax4 = plt.subplots()
region_sales.plot(kind='bar', ax=ax4)
st.pyplot(fig4)