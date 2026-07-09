import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Sales Overview")

df = pd.read_csv("data/train.csv")

df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)

df["Year"] = df["Order Date"].dt.year


sales_year = df.groupby("Year")["Sales"].sum().reset_index()

fig = px.bar(
    sales_year,
    x="Year",
    y="Sales",
    title="Total Sales by Year"
)

st.plotly_chart(fig)

monthly = pd.read_csv("outputs/monthly_sales.csv")

fig = px.line(
    monthly,
    x="Order Date",
    y="Sales",
    title="Monthly Sales Trend"
)

st.plotly_chart(fig)

category = st.selectbox(
    "Category",
    ["All"] + list(df["Category"].unique())
)

filtered = df.copy()

if region != "All":
    filtered = filtered[
        filtered["Region"] == region
    ]

if category != "All":
    filtered = filtered[
        filtered["Category"] == category
    ]

st.dataframe(filtered)