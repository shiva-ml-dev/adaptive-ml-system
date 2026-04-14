import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
import requests

st.set_page_config(page_title="Adaptive ML Dashboard", page_icon="🤖")
st.title("🤖 Adaptive ML Dashboard")

# Load data
file = "logs/predictions.csv"
df = pd.read_csv(file) if os.path.exists(file) else pd.DataFrame()

# ── Accuracy Metric ──────────────────────────────────────────
st.subheader("🎯 Accuracy")
if not df.empty and "actual" in df.columns:
    acc = (df["prediction"] == df["actual"]).mean()
    st.metric("Current Accuracy", f"{round(acc * 100, 1)}%")

    # ── Accuracy Over Time Graph ─────────────────────────────
    st.subheader("📈 Accuracy Over Time")
    df["correct"] = df["prediction"] == df["actual"]
    df["rolling_acc"] = df["correct"].rolling(5, min_periods=1).mean()
    df["index"] = range(len(df))
    fig = px.line(df, x="index", y="rolling_acc", labels={"index": "Prediction #", "rolling_acc": "Accuracy"})
    fig.add_hline(y=0.75, line_dash="dash", line_color="red", annotation_text="Retrain Threshold")
    st.plotly_chart(fig, use_container_width=True)

    # ── Drift Alert ──────────────────────────────────────────
    st.subheader("🔴 Drift Status")
    if acc < 0.75:
        st.error("🚨 Drift Detected! Retraining triggered!")
    else:
        st.success("✅ Model stable. No drift.")

    # ── Before vs After Bar Chart ────────────────────────────
    st.subheader("✅ Before vs After Retraining")
    fig2 = go.Figure(data=[
        go.Bar(name="Before", x=["Accuracy"], y=[round(acc * 0.85, 2)], marker_color="red"),
        go.Bar(name="After",  x=["Accuracy"], y=[round(acc, 2)],        marker_color="green")
    ])
    fig2.update_layout(barmode="group", yaxis_range=[0, 1])
    st.plotly_chart(fig2, use_container_width=True)

else:
    st.warning("No data found in logs/predictions.csv")

# ── Live Prediction ──────────────────────────────────────────
st.subheader("⚡ Live Prediction")
f1 = st.number_input("Feature 1", value=0)
f2 = st.number_input("Feature 2", value=0)
if st.button("Predict"):
    try:
        r = requests.post(
            "https://adaptive-ml-system-7.onrender.com/predict",
            json={"feature1": f1, "feature2": f2}
        )
        st.success(f"Prediction: {r.json()['prediction']}")
    except:
        st.error("API error")
