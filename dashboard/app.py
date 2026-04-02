import streamlit as st
import pandas as pd
import os
import requests

st.title("Adaptive ML Dashboard")

file = "logs/predictions.csv"
df = pd.read_csv(file) if os.path.exists(file) else pd.DataFrame()

st.subheader("Latest Data")
st.dataframe(df.tail() if not df.empty else df)

st.subheader("Accuracy")
if not df.empty and "actual" in df:
    acc = (df["prediction"] == df["actual"]).mean()
    st.write(round(acc, 2))
else:
    st.write("No data")

st.subheader("Live Prediction")

f1 = st.number_input("Feature1", 0)
f2 = st.number_input("Feature2", 0)

if st.button("Predict"):
    try:
        r = requests.post(
            "https://adaptive-ml-system-api.onrender.com/predict",
            json={"feature1": f1, "feature2": f2}
        )
        st.success(r.json())
    except:
        st.error("API error")