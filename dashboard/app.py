import streamlit as st
import pandas as pd
import time

st.title("Adaptive ML Monitoring Dashboard")

# Load data
file_path = "logs/predictions.csv"

def get_data():
    return pd.read_csv(file_path)

def get_accuracy():
    df = get_data()
    return (df["prediction"] == df["actual"]).mean()

# Get data
df = get_data()

# Show data
st.subheader("Latest Data")
st.dataframe(df.tail())

# Accuracy
accuracy = get_accuracy()

st.subheader("Model Accuracy")
st.write(f"Accuracy: {accuracy:.2f}")

# Retraining status
if accuracy < 0.8:
    st.error("Retraining Required")
else:
    st.success("Model is Stable")

# Prediction distribution
st.subheader("Prediction Distribution")
st.bar_chart(df["prediction"].value_counts())

# Auto refresh every 5 seconds
time.sleep(5)
st.rerun()