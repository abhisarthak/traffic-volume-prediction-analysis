import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Traffic Volume Prediction",
    page_icon="🚦",
    layout="wide"
)

# --------------------------------------------------
# PATHS
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "traffic_prediction_model.pkl"
FEATURES_PATH = BASE_DIR / "models" / "model_features.pkl"

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

@st.cache_resource
def load_model():
    model = joblib.load(MODEL_PATH)
    features = joblib.load(FEATURES_PATH)
    return model, features


model, model_features = load_model()

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🚦 Traffic Volume Prediction Dashboard")

st.markdown(
    """
    Predict hourly traffic volume using a machine learning model trained on
    historical traffic, temporal, and weather-related features.
    """
)

st.divider()

# --------------------------------------------------
# SIDEBAR INPUTS
# --------------------------------------------------

st.sidebar.header("Prediction Inputs")

hour = st.sidebar.slider(
    "Hour of Day",
    min_value=0,
    max_value=23,
    value=9
)

day_of_week = st.sidebar.selectbox(
    "Day of Week",
    options=list(range(7)),
    format_func=lambda x: [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ][x]
)

is_weekend = 1 if day_of_week >= 5 else 0

month = st.sidebar.slider(
    "Month",
    min_value=1,
    max_value=12,
    value=6
)


is_holiday_flag = st.sidebar.selectbox(
    "Holiday?",
    options=[0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)




# --------------------------------------------------
# CREATE INPUT DATA
# --------------------------------------------------

input_data = pd.DataFrame([{
    "hour": hour,
    "day_of_week": day_of_week,
    "is_weekend": is_weekend,
    "month": month,
    "is_holiday_flag": is_holiday_flag
}])

# Ensure exact feature order used during model training
input_data = input_data[model_features]

# Make prediction
prediction = model.predict(input_data)[0]


# --------------------------------------------------
# PREDICTION
# --------------------------------------------------

prediction = model.predict(input_data)[0]

# --------------------------------------------------
# MAIN DASHBOARD
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

col1.metric(
    "Predicted Traffic Volume",
    f"{prediction:,.0f} vehicles"
)

col2.metric(
    "Model Accuracy (R²)",
    "96.54%"
)

col3.metric(
    "Model MAE",
    "244 vehicles"
)

st.divider()

# --------------------------------------------------
# INPUT SUMMARY
# --------------------------------------------------

st.subheader("📊 Current Prediction Scenario")

summary_data = pd.DataFrame({
    "Feature": [
        "Hour",
        "Day of Week",
        "Month",
        "Weekend",
        "Holiday"
    ],
    "Value": [
        hour,
        ["Monday", "Tuesday", "Wednesday", "Thursday",
         "Friday", "Saturday", "Sunday"][day_of_week],
        month,
        "Yes" if is_weekend else "No",
        "Yes" if is_holiday_flag else "No"
    ]
})

st.dataframe(
    summary_data,
    use_container_width=True,
    hide_index=True
)

# --------------------------------------------------
# MODEL INFORMATION
# --------------------------------------------------

st.subheader("🤖 Model Information")

info_col1, info_col2 = st.columns(2)

with info_col1:
    st.info(
        """
        **Model:** HistGradientBoosting Regressor

        **Training Period:** October 2012 – December 2016

        **Test Period:** January 2017 – May 2017
        """
    )

with info_col2:
    st.success(
        """
        **Final Test Performance**

        • MAE: 243.72 vehicles

        • RMSE: 372.75 vehicles

        • R² Score: 0.9654
        """
    )

st.caption(
    "This dashboard is based on the Traffic Volume Prediction & Analysis project."
)