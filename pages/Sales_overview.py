import streamlit as st
import pandas as pd
import plotly.express as px

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"
# ----------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------

st.set_page_config(page_title="Sales Overview", page_icon="📊", layout="wide")

st.title("📊 Sales Overview Dashboard")

st.markdown(
"""
Analyze historical sales using interactive filters,
KPIs and business intelligence visualizations.
"""
)

# ----------------------------------------------------------
# LOAD DATA
# ----------------------------------------------------------

@st.cache_data
def load_data():

    sales = pd.read_csv(DATA_DIR / "train.csv")

    monthly = pd.read_csv(OUTPUT_DIR / "monthly_sales.csv")

    sales["Order Date"] = pd.to_datetime(
        sales["Order Date"],
        format="%d/%m/%Y",
        errors="coerce"
    )

    monthly["Order Date"] = pd.to_datetime(
        monthly["Order Date"],
        format="%d/%m/%Y",
        errors="coerce"
    )

    return sales, monthly


sales_df, monthly_df = load_data()

# ----------------------------------------------------------
# FILTERS
# ----------------------------------------------------------

st.sidebar.header("Filters")

regions = sorted(sales_df["Region"].unique())

categories = sorted(sales_df["Category"].unique())

selected_regions = st.sidebar.multiselect(
    "Region",
    regions,
    default=regions
)

selected_categories = st.sidebar.multiselect(
    "Category",
    categories,
    default=categories
)

filtered = sales_df[
    (sales_df["Region"].isin(selected_regions)) &
    (sales_df["Category"].isin(selected_categories))
].copy()

# ----------------------------------------------------------
# KPI CARDS
# ----------------------------------------------------------

total_sales = filtered["Sales"].sum()
total_orders = len(filtered)
avg_sales = filtered["Sales"].mean()

profit = (
    filtered["Profit"].sum()
    if "Profit" in filtered.columns
    else None
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "💰 Total Sales",
    f"${total_sales:,.0f}"
)

col2.metric(
    "🛒 Orders",
    f"{total_orders:,}"
)

col3.metric(
    "📦 Avg Sales",
    f"${avg_sales:,.2f}"
)

if profit is not None:
    col4.metric(
        "📈 Profit",
        f"${profit:,.0f}"
    )
else:
    col4.metric(
        "🌍 Regions",
        filtered["Region"].nunique()
    )

st.divider()

# ----------------------------------------------------------
# YEAR COLUMN
# ----------------------------------------------------------

filtered["Year"] = filtered["Order Date"].dt.year

yearly_sales = (
    filtered
    .groupby("Year", as_index=False)["Sales"]
    .sum()
)

# ----------------------------------------------------------
# YEARLY BAR CHART
# ----------------------------------------------------------

fig_year = px.bar(

    yearly_sales,

    x="Year",

    y="Sales",

    color="Sales",

    text_auto=".2s",

    title="Total Sales by Year",

    color_continuous_scale="Blues"

)

fig_year.update_layout(

    template="plotly_white",

    height=500

)

st.plotly_chart(
    fig_year,
    width='stretch' 
)

st.divider()

# ----------------------------------------------------------
# MONTHLY SALES TREND
# ----------------------------------------------------------

monthly_df = monthly_df.sort_values("Order Date")

fig_month = px.line(

    monthly_df,

    x="Order Date",

    y="Sales",

    markers=True,

    title="Monthly Sales Trend"

)

fig_month.update_traces(line=dict(width=3))

fig_month.update_layout(

    template="plotly_white",

    height=500

)

st.plotly_chart(
    fig_month,
    width='stretch' 
)

st.divider()

# ----------------------------------------------------------
# REGION & CATEGORY CHARTS
# ----------------------------------------------------------

left, right = st.columns(2)

# REGION

region_sales = (
    filtered
    .groupby("Region", as_index=False)["Sales"]
    .sum()
)

fig_region = px.bar(

    region_sales,

    x="Region",

    y="Sales",

    color="Region",

    title="Sales by Region"

)

fig_region.update_layout(
    template="plotly_white",
    showlegend=False,
    height=450
)

left.plotly_chart(
    fig_region,
    width='stretch' 
)

# CATEGORY

category_sales = (
    filtered
    .groupby("Category", as_index=False)["Sales"]
    .sum()
)

fig_category = px.pie(

    category_sales,

    names="Category",

    values="Sales",

    hole=0.45,

    title="Sales by Category"

)

fig_category.update_layout(height=450)

right.plotly_chart(
    fig_category,
    width='stretch' 
)

st.divider()

# ----------------------------------------------------------
# TOP SUB-CATEGORIES
# ----------------------------------------------------------

top10 = (

    filtered

    .groupby("Sub-Category", as_index=False)["Sales"]

    .sum()

    .sort_values("Sales", ascending=False)

    .head(10)

)

fig_sub = px.bar(

    top10,

    x="Sales",

    y="Sub-Category",

    orientation="h",

    color="Sales",

    text_auto=".2s",

    title="Top 10 Selling Sub-Categories",

    color_continuous_scale="Viridis"

)

fig_sub.update_layout(

    template="plotly_white",

    height=550

)

st.plotly_chart(
    fig_sub,
    width='stretch' 
)

st.divider()

# ----------------------------------------------------------
# REGION-CATEGORY HEATMAP
# ----------------------------------------------------------

pivot = filtered.pivot_table(

    index="Region",

    columns="Category",

    values="Sales",

    aggfunc="sum"

)

fig_heat = px.imshow(

    pivot,

    text_auto=True,

    aspect="auto",

    color_continuous_scale="YlGnBu",

    title="Sales Heatmap (Region vs Category)"

)

fig_heat.update_layout(height=500)

st.plotly_chart(
    fig_heat,
    width='stretch' 
)

st.divider()

# ----------------------------------------------------------
# DATA TABLE
# ----------------------------------------------------------

st.subheader("Filtered Dataset")

st.dataframe(
    filtered,
    width='stretch' ,
    height=400
)

csv = filtered.to_csv(index=False).encode("utf-8")

st.download_button(

    "⬇ Download Filtered Data",

    csv,

    file_name="filtered_sales.csv",

    mime="text/csv"
)