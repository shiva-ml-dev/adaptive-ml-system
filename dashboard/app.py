import streamlit as st
import pandas as pd
import requests
import os

st.title("Adaptive ML Dashboard")

file_path = "logs/predictions.csv"

df = pd.read_csv(file_path) if os.path.exists(file_path) else pd.DataFrame()

st.subheader("Latest Data")
st.dataframe(df.tail())

if not df.empty:
    acc = (df["prediction"] == df["actual"]).mean()
else:
    acc = 0

st.subheader("Accuracy")
st.write(acc)

if acc < 0.8:
    st.write("Retraining Required")
else:
    st.write("Model is Stable")

if not df.empty:
    st.bar_chart(df["prediction"].value_counts())

st.subheader("Live Prediction")

f1 = st.number_input("Feature1", 0)
f2 = st.number_input("Feature2", 0)

if st.button("Predict"):
    res = requests.post(
        "https://adaptive-ml-system.onrender.com/predict",
        params={"feature1": f1, "feature2": f2}
    )
    st.write(res.json())