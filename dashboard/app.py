import streamlit as st
import pandas as pd
import requests
import os

st.title("Adaptive ML Dashboard")

# -----------------------------
# Load Data
# -----------------------------
file_path = "logs/predictions.csv"

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
else:
    df = pd.DataFrame(columns=["feature1", "feature2", "prediction"])

st.subheader("Latest Data")

if df.empty:
    st.write("No data available yet")
else:
    st.dataframe(df.tail())

# -----------------------------
# Accuracy
# -----------------------------
st.subheader("Accuracy")

if not df.empty and "prediction" in df.columns:
    st.write(len(df))  # simple metric
else:
    st.write("0")

# -----------------------------
# Live Prediction
# -----------------------------
st.subheader("Live Prediction")

f1 = st.number_input("Feature1", 0)
f2 = st.number_input("Feature2", 0)

if st.button("Predict"):
    try:
        res = requests.post(
            "https://adaptive-ml-system-1.onrender.com/predict",
            json={"feature1": f1, "feature2": f2}
        )
        st.success(res.json())
    except:
        st.error("API error")