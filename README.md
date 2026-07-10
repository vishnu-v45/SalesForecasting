# 📈 Sales Forecasting & Demand Analytics Dashboard

An end-to-end Machine Learning project that analyzes historical retail sales data to forecast future demand, detect sales anomalies, and segment products based on demand patterns. The project includes an interactive Streamlit dashboard for business users to explore insights without requiring any programming knowledge.

---

## 🚀 Project Overview

Effective inventory management is one of the biggest challenges in retail. Overstocking increases holding costs, while understocking leads to lost sales and dissatisfied customers.

This project addresses these challenges by combining:

- Exploratory Data Analysis (EDA)
- Time Series Forecasting
- Machine Learning
- Anomaly Detection
- Product Demand Segmentation
- Interactive Business Dashboard

The solution enables business stakeholders to make informed inventory and supply chain decisions using predictive analytics.

---

## ✨ Features

### 📊 Sales Overview Dashboard
- Interactive KPI Cards
- Total Sales by Year
- Monthly Sales Trend
- Sales by Region
- Sales by Category
- Region & Category Filters

### 🔮 Forecast Explorer
- XGBoost-based Sales Forecast
- Forecast Horizon Selection (1–3 Months)
- Interactive Forecast Charts
- Model Performance (MAE & RMSE)

### 🚨 Anomaly Detection
- Isolation Forest Anomaly Detection
- Weekly Sales Trend
- Detected Sales Anomalies
- Downloadable Anomaly Report

### 📦 Product Demand Segmentation
- K-Means Clustering
- PCA Cluster Visualization
- Demand Segment Analysis
- Recommended Stocking Strategy

---

# 🧠 Machine Learning Models

## Forecasting Models Compared

- SARIMA
- Prophet
- XGBoost ✅ (Best Model)

Evaluation Metrics:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Percentage Error (MAPE)

---

## Anomaly Detection

Model Used:

- Isolation Forest

Purpose:

- Detect unusual sales spikes and drops
- Identify abnormal business events

---

## Product Segmentation

Algorithm:

- K-Means Clustering

Visualization:

- Principal Component Analysis (PCA)

Purpose:

- Group products into High, Medium, and Low Demand segments.

---

# 📁 Project Structure

```text
SalesForecasting_VishnuVardhan/
│
├── app.py
├── requirements.txt
├── README.md
├── analysis.ipynb
│
├── data/
│   └── train.csv
│
├── outputs/
│   ├── monthly_sales.csv
│   ├── weekly_sales.csv
│   ├── forecast_results.csv
│   ├── anomalies.csv
│   └── clusters.csv
│
└── pages/
    ├── Sales_overview.py
    ├── Forecast_explorer.py
    ├── Anomaly_report.py
    └── Product_demand_segments.py
```

---

# 📊 Dashboard Pages

## 🏠 Home
Project overview and navigation.

## 📊 Sales Overview
Business KPIs, yearly sales, monthly trends, regional analysis and category analysis.

## 🔮 Forecast Explorer
Interactive XGBoost sales forecasts with configurable forecast horizon.

## 🚨 Anomaly Report
Visualization of unusual sales events detected using Isolation Forest.

## 📦 Product Demand Segmentation
K-Means clustering results with PCA visualization and stocking recommendations.

---

# 🛠️ Tech Stack

### Programming Language

- Python

### Data Analysis

- Pandas
- NumPy

### Visualization

- Plotly
- Matplotlib

### Machine Learning

- Scikit-Learn
- XGBoost
- Prophet
- Statsmodels

### Web Framework

- Streamlit

---

# 📈 Business Insights

The project provides actionable insights for retail businesses by:

- Forecasting future sales demand
- Detecting unusual sales behavior
- Optimizing inventory allocation
- Supporting supply chain planning
- Reducing stock-outs and excess inventory

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/SalesForecasting_VishnuVardhan.git
```

Navigate to the project directory

```bash
cd SalesForecasting_VishnuVardhan
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

# 📷 Dashboard Preview

Add screenshots here after deployment.

Example:

```
images/

home.png

sales_overview.png

forecast.png

anomaly.png

clusters.png
```

---

# 🌐 Live Demo

**Streamlit App**

Paste your deployed Streamlit link here.

Example:

```
https://salesforecasting.streamlit.app
```

---

# 💻 GitHub Repository

Paste your GitHub repository link here.

Example:

```
https://github.com/your-username/SalesForecasting_VishnuVardhan
```

---

# 📌 Future Improvements

- Real-time sales forecasting
- Automated model retraining
- Cloud database integration
- REST API deployment
- User authentication
- Inventory optimization module
- Email alerts for anomalies

---

# 👨‍💻 Author

**Vishnu Vardhan**

Mechanical & Aerospace Engineering Undergraduate

Interested in:
- Machine Learning
- Artificial Intelligence
- Data Science
- Software Engineering

GitHub:
https://github.com/your-username

LinkedIn:
(Add your LinkedIn URL)

---

# ⭐ If you found this project useful, consider giving it a star!
