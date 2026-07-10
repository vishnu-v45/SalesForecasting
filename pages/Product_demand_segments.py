import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"
# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Product Demand Segments",
    page_icon="📦",
    layout="wide"
)

st.title("📦 Product Demand Segmentation")

st.markdown("""
Products are grouped into demand segments using **K-Means Clustering**.

The clusters help identify:

- High-demand products
- Medium-demand products
- Low-demand products
""")

# ==========================================================
# LOAD DATA
# ==========================================================

@st.cache_data
def load_clusters():
    return pd.read_csv(OUTPUT_DIR / "clusters.csv")

cluster_df = load_clusters()

# ==========================================================
# KPI CARDS
# ==========================================================

total_products = len(cluster_df)

clusters = cluster_df["Cluster"].nunique()

segments = cluster_df["Demand Segment"].nunique()

largest_cluster = cluster_df["Demand Segment"].value_counts().idxmax()

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Products",
    total_products
)

c2.metric(
    "Clusters",
    clusters
)

c3.metric(
    "Demand Segments",
    segments
)

c4.metric(
    "Largest Segment",
    largest_cluster
)

st.divider()

# ==========================================================
# PCA SCATTER
# ==========================================================

st.subheader("PCA Cluster Visualization")

fig = px.scatter(

    cluster_df,

    x="PC1",

    y="PC2",

    color="Demand Segment",

    hover_data=["Sub-Category"],

    size_max=15,

    title="KMeans Product Clusters"

)

fig.update_layout(

    template="plotly_white",

    height=600

)

st.plotly_chart(

    fig,

    width='stretch' 

)

st.divider()

# ==========================================================
# CLUSTER DISTRIBUTION
# ==========================================================

left, right = st.columns(2)

cluster_count = (

    cluster_df

    .groupby("Demand Segment")

    .size()

    .reset_index(name="Products")

)

fig1 = px.pie(

    cluster_count,

    names="Demand Segment",

    values="Products",

    hole=0.45,

    title="Demand Segment Distribution"

)

left.plotly_chart(

    fig1,

    width='stretch' 

)

fig2 = px.bar(

    cluster_count,

    x="Demand Segment",

    y="Products",

    color="Demand Segment",

    text_auto=True,

    title="Products per Cluster"

)

fig2.update_layout(

    template="plotly_white",

    showlegend=False

)

right.plotly_chart(

    fig2,

    width='stretch' 

)

st.divider()

# ==========================================================
# TABLE
# ==========================================================

st.subheader("Demand Segment Table")

display = cluster_df[

    [

        "Sub-Category",

        "Cluster",

        "Demand Segment"

    ]

]

st.dataframe(

    display,

    width='stretch' ,

    height=450

)

csv = display.to_csv(index=False).encode("utf-8")

st.download_button(

    "⬇ Download Cluster Report",

    csv,

    "clusters.csv",

    "text/csv"

)

st.divider()

# ==========================================================
# SEGMENT STATISTICS
# ==========================================================

st.subheader("Cluster Statistics")

summary = (

    cluster_df

    .groupby("Demand Segment")

    .agg(

        Products=("Sub-Category", "count")

    )

    .reset_index()

)

st.dataframe(

    summary,

    width='stretch' 

)

st.divider()

# ==========================================================
# BUSINESS INSIGHTS
# ==========================================================

st.subheader("Business Insights")

st.success("""
### High Demand Cluster
- Maintain adequate inventory.
- Prioritize during promotions.
- Ensure stock availability.

### Medium Demand Cluster
- Monitor seasonal fluctuations.
- Target with marketing campaigns.

### Low Demand Cluster
- Consider bundling products.
- Optimize inventory.
- Review pricing strategy.
""")