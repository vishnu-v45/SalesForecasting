import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"
# ------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------

st.set_page_config(
    page_title="Forecast Explorer",
    page_icon="🔮",
    layout="wide"
)

st.title("🔮 Sales Forecast Explorer")

st.markdown(
"""
Explore future sales predicted by the **XGBoost Forecasting Model**.
Select a category or customer segment and forecast horizon.
"""
)

# ------------------------------------------------------------
# LOAD DATA
# ------------------------------------------------------------

@st.cache_data
def load_forecast():
    return pd.read_csv(OUTPUT_DIR / "forecast_results.csv")

forecast_df = load_forecast()

# ------------------------------------------------------------
# SIDEBAR
# ------------------------------------------------------------

st.sidebar.header("Forecast Options")

segments = forecast_df["Segment"].unique().tolist()

selected_segment = st.sidebar.selectbox(
    "Choose Segment",
    segments
)

forecast_horizon = st.sidebar.slider(
    "Forecast Horizon (Months)",
    1,
    3,
    3
)

# ------------------------------------------------------------
# FILTER DATA
# ------------------------------------------------------------

selected_data = forecast_df[
    forecast_df["Segment"] == selected_segment
]

# ------------------------------------------------------------
# FORECAST VALUES
# ------------------------------------------------------------

month_columns = [
    "Month 1",
    "Month 2",
    "Month 3"
]

forecast_values = selected_data.iloc[0][month_columns].values

months = ["Month 1", "Month 2", "Month 3"]

months = months[:forecast_horizon]

forecast_values = forecast_values[:forecast_horizon]

# ------------------------------------------------------------
# KPI CARDS
# ------------------------------------------------------------

c1, c2, c3 = st.columns(3)

c1.metric(
    "Selected Segment",
    selected_segment
)

c2.metric(
    "Forecast Horizon",
    f"{forecast_horizon} Months"
)

c3.metric(
    "Average Forecast",
    f"${sum(forecast_values)/len(forecast_values):,.0f}"
)

st.divider()

# ------------------------------------------------------------
# FORECAST CHART
# ------------------------------------------------------------

forecast_chart = pd.DataFrame({

    "Month": months,

    "Forecast Sales": forecast_values

})

fig = px.line(

    forecast_chart,

    x="Month",

    y="Forecast Sales",

    markers=True,

    title="Forecasted Sales"

)

fig.update_traces(
    line=dict(width=4)
)

fig.update_layout(

    template="plotly_white",

    height=550

)

st.plotly_chart(
    fig,
    width='stretch' 
)

# ------------------------------------------------------------
# BAR CHART
# ------------------------------------------------------------

fig2 = px.bar(

    forecast_chart,

    x="Month",

    y="Forecast Sales",

    text_auto=".2s",

    color="Forecast Sales",

    color_continuous_scale="Viridis",

    title="Forecast Comparison"

)

fig2.update_layout(

    template="plotly_white",

    height=500

)

st.plotly_chart(
    fig2,
    width='stretch' 
)

# ------------------------------------------------------------
# MODEL PERFORMANCE
# ------------------------------------------------------------

st.subheader("📈 Model Performance")

metric1, metric2 = st.columns(2)

#
# Replace these values with your notebook values
#

MAE = 148.76
RMSE = 236.14

metric1.metric(

    "MAE",

    round(MAE,2)

)

metric2.metric(

    "RMSE",

    round(RMSE,2)

)

st.info(
"""
Lower MAE and RMSE indicate better forecasting performance.

The XGBoost model achieved the best performance among all
tested models (SARIMA, Prophet and XGBoost).
"""
)

st.divider()

# ------------------------------------------------------------
# FORECAST TABLE
# ------------------------------------------------------------

st.subheader("Forecast Values")

st.dataframe(
    selected_data,
    use_container_width=True,
    
)

csv = selected_data.to_csv(index=False).encode("utf-8")

st.download_button(

    "⬇ Download Forecast",

    csv,

    "forecast.csv",

    "text/csv"

)

# ------------------------------------------------------------
# ALL SEGMENTS COMPARISON
# ------------------------------------------------------------

st.subheader("Forecast Comparison Across Segments")

comparison = forecast_df.melt(

    id_vars="Segment",

    value_vars=["Month 1","Month 2","Month 3"],

    var_name="Month",

    value_name="Forecast"

)

fig3 = px.bar(

    comparison,

    x="Segment",

    y="Forecast",

    color="Month",

    barmode="group",

    title="Forecast Comparison"

)

fig3.update_layout(

    template="plotly_white",

    height=600

)

st.plotly_chart(

    fig3,

    width='stretch' 

)