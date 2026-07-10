import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Sales Forecasting Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.main {
    background-color:#f8f9fa;
}

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

h1,h2,h3{
    color:#003366;
}

div[data-testid="metric-container"]{
    background:white;
    padding:15px;
    border-radius:12px;
    box-shadow:0 2px 8px rgba(0,0,0,.08);
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("📈 Sales Forecasting Dashboard")

st.markdown("""
### Interactive Business Intelligence Dashboard

This dashboard demonstrates an end-to-end Machine Learning pipeline for retail sales forecasting using:

- 📊 Exploratory Data Analysis
- 🤖 XGBoost Forecasting
- 🚨 Isolation Forest Anomaly Detection
- 📦 K-Means Demand Segmentation
- 📈 Interactive Plotly Visualizations
""")

st.divider()

# --------------------------------------------------
# PROJECT SUMMARY
# --------------------------------------------------

c1, c2 = st.columns([2,1])

with c1:

    st.subheader("Project Overview")

    st.write("""
This project analyzes historical retail sales data to identify sales trends,
forecast future demand, detect unusual sales behavior, and segment products
based on demand characteristics.

The forecasting model was compared against multiple approaches
(SARIMA, Prophet and XGBoost), with XGBoost selected as the final model
based on its superior forecasting performance.

Use the navigation panel on the left to explore each analysis.
""")

with c2:

    st.info("""
### Model Used

✅ XGBoost

Forecast Horizon

**3 Months**
""")

st.divider()

# --------------------------------------------------
# FEATURES
# --------------------------------------------------

st.subheader("Dashboard Pages")

a,b = st.columns(2)

with a:

    st.success("📊 Sales Overview")

    st.write("""
- KPI Cards
- Sales by Year
- Monthly Trend
- Region Analysis
- Category Analysis
""")

    st.success("🔮 Forecast Explorer")

    st.write("""
- XGBoost Forecast
- 1–3 Month Horizon
- Forecast Charts
- Model Metrics
""")

with b:

    st.success("🚨 Anomaly Report")

    st.write("""
- Isolation Forest
- Weekly Anomalies
- Download Report
""")

    st.success("📦 Product Demand Segments")

    st.write("""
- KMeans Clustering
- PCA Visualization
- Demand Segments
""")

st.divider()

st.caption("Developed using Streamlit • Plotly • XGBoost • Scikit-Learn")