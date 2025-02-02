import streamlit as st
import pandas as pd
import numpy as np
from utils.data_processing import process_uploaded_data, load_sample_data
from utils.simulation import run_climate_simulation
from utils.visualization import (
    plot_temperature_trends,
    plot_sea_level_rise,
    plot_resource_depletion,
    plot_correlation_matrix
)

# Page configuration
st.set_page_config(
    page_title="FutureWorld - Climate Crisis Simulation",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
with open('assets/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Sidebar
st.sidebar.title("FutureWorld")
st.sidebar.subheader("Climate Crisis Simulation Platform")

# Data Input Section
data_source = st.sidebar.radio(
    "Select Data Source",
    ["Sample Data", "Upload Data"]
)

if data_source == "Upload Data":
    uploaded_file = st.sidebar.file_uploader(
        "Upload your climate data (CSV)",
        type=['csv']
    )
    if uploaded_file:
        data = process_uploaded_data(uploaded_file)
    else:
        data = load_sample_data()
else:
    data = load_sample_data()

# Simulation Parameters
st.sidebar.subheader("Simulation Parameters")
temperature_increase = st.sidebar.slider(
    "Temperature Increase (°C)",
    0.0, 4.0, 2.0, 0.1
)
timeframe = st.sidebar.slider(
    "Projection Timeframe (Years)",
    1, 50, 10
)
emission_reduction = st.sidebar.slider(
    "Emission Reduction Target (%)",
    0, 100, 30
)

# Main Content
st.title("Climate Crisis Simulation Dashboard")

# Run Simulation
simulation_results = run_climate_simulation(
    data,
    temperature_increase,
    timeframe,
    emission_reduction
)

# Dashboard Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Global Temperature Trends")
    fig_temp = plot_temperature_trends(simulation_results)
    st.plotly_chart(fig_temp, use_container_width=True)

    st.subheader("Resource Depletion Forecast")
    fig_resources = plot_resource_depletion(simulation_results)
    st.plotly_chart(fig_resources, use_container_width=True)

with col2:
    st.subheader("Sea Level Rise Projections")
    fig_sea = plot_sea_level_rise(simulation_results)
    st.plotly_chart(fig_sea, use_container_width=True)

    st.subheader("Impact Correlation Matrix")
    fig_corr = plot_correlation_matrix(simulation_results)
    st.plotly_chart(fig_corr, use_container_width=True)

# Export Options
st.subheader("Export Results")
if st.button("Export Simulation Data"):
    export_data = pd.DataFrame(simulation_results)
    csv = export_data.to_csv(index=False)
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="climate_simulation_results.csv",
        mime="text/csv"
    )
