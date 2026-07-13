import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"
# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Anomaly Report",
    page_icon="🚨",
    layout="wide"
)

st.title("🚨 Sales Anomaly Detection")

st.markdown("""
Isolation Forest was used to detect unusual sales behaviour.

Red points indicate detected anomalies.
""")

# ==========================================================
# LOAD DATA
# ==========================================================

@st.cache_data
def load_data():

    anomalies= pd.read_csv(OUTPUT_DIR / "anomalies.csv")

    weekly = pd.read_csv(OUTPUT_DIR / "weekly_sales.csv")

    anomalies["Order Date"] = pd.to_datetime(anomalies["Order Date"])

    weekly["Order Date"] = pd.to_datetime(weekly["Order Date"])

    return anomalies, weekly

anomaly_df, weekly_df = load_data()

# ==========================================================
# KPI CARDS
# ==========================================================

total_records = len(anomaly_df)

num_anomalies = len(anomaly_df[anomaly_df["Anomaly"] == -1])

normal_records = total_records - num_anomalies

percent = (num_anomalies / total_records) * 100

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Total Records",
    f"{total_records:,}"
)

c2.metric(
    "Anomalies",
    num_anomalies
)

c3.metric(
    "Normal Records",
    normal_records
)

c4.metric(
    "Anomaly %",
    f"{percent:.2f}%"
)

st.divider()

# ==========================================================
# SALES TREND
# ==========================================================

fig = go.Figure()

fig.add_trace(

    go.Scatter(

        x=weekly_df["Order Date"],

        y=weekly_df["Sales"],

        mode="lines",

        name="Weekly Sales",

        line=dict(width=3)

    )

)

anomaly_points = anomaly_df[
    anomaly_df["Anomaly"] == -1
]

fig.add_trace(

    go.Scatter(

        x=anomaly_points["Order Date"],

        y=anomaly_points["Sales"],

        mode="markers",

        marker=dict(

            color="red",

            size=10

        ),

        name="Detected Anomaly"

    )

)

fig.update_layout(

    title="Weekly Sales with Detected Anomalies",

    template="plotly_white",

    height=600

)

st.plotly_chart(
    fig,
    width='stretch' 
)

st.divider()

# ==========================================================
# ANOMALY TABLE
# ==========================================================

st.subheader("Detected Anomalies")

display = anomaly_points[

    [

        "Order Date",

        "Sales"

    ]

]

st.dataframe(
    display,
    use_container_width=True,
    height=400
)

csv = display.to_csv(index=False).encode("utf-8")

st.download_button(

    "⬇ Download Anomaly Report",

    csv,

    "anomalies.csv",

    "text/csv"

)

st.divider()

# ==========================================================
# SALES DISTRIBUTION
# ==========================================================

fig2 = px.histogram(

    anomaly_df,

    x="Sales",

    nbins=40,

    color="Anomaly",

    title="Sales Distribution"

)

fig2.update_layout(

    template="plotly_white",

    height=500

)

st.plotly_chart(

    fig2,

    width='stretch' 

)

st.divider()

# ==========================================================
# BOX PLOT
# ==========================================================

fig3 = px.box(

    anomaly_df,

    y="Sales",

    color="Anomaly",

    title="Outlier Distribution"

)

fig3.update_layout(

    template="plotly_white",

    height=500

)

st.plotly_chart(

    fig3,

    width='stretch' 

)

st.divider()

# ==========================================================
# SUMMARY
# ==========================================================

st.subheader("Business Insights")

st.success(f"""
Isolation Forest detected **{num_anomalies} anomalous sales periods**
representing **{percent:.2f}%** of the observations.

These unusual sales spikes or drops may indicate:

• Seasonal events

• Promotional campaigns

• Inventory shortages

• Data entry errors

These records should be investigated before making future forecasting decisions.
""")