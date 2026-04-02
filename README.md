Adaptive Machine Learning Monitoring and Auto-Retraining System

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Live-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red)

---

Overview

This project implements an end-to-end adaptive machine learning system that:

- Performs real-time predictions
- Monitors model performance
- Detects accuracy drops
- Automatically triggers retraining

Built with a production-style architecture using FastAPI and Streamlit.

---

## Live Demo

Streamlit Dashboard:
[Open Live Dashboard](https://adaptive-ml-system-ptkbbf7euu2cd3mg55hn52.streamlit.app)

FastAPI API:
https://adaptive-ml-system-7.onrender.com

API Documentation:
https://adaptive-ml-system-7.onrender.com/docs


## Dashboard Demo

### Main Dashboard
![Dashboard](screenshots/dashboard.png)

### Accuracy Monitoring
![Accuracy](screenshots/accuracy.png)

### Live Prediction
![Prediction](screenshots/prediction.png)

---

System Architecture

User → Streamlit Dashboard → FastAPI API → ML Model → Predictions Log → Monitoring (Accuracy/Drift) → Retraining Trigger

---

Features

- Real-time prediction API
- Live Streamlit dashboard
- Prediction logging (CSV)
- Accuracy monitoring
- Data drift detection
- Retraining trigger mechanism
- Scheduled performance checks

---

Key Highlights

- End-to-end ML system with API, UI, and monitoring
- Real-time predictions using FastAPI
- Live dashboard using Streamlit
- Accuracy monitoring and retraining trigger
- Production deployment using Render and Streamlit Cloud

---

Tech Stack

- Python
- FastAPI
- Streamlit
- Scikit-learn
- Pandas

---

Project Structure

adaptive-ml-system/
│── app/
│── dashboard/
│── monitoring/
│── retraining/
│── tests/
│── data/
│── models/
│── logs/
│── scheduler.py
│── requirements.txt

---

How It Works

1. Predictions are made via FastAPI
2. Results are logged into CSV
3. Accuracy is calculated periodically
4. If accuracy drops, retraining is triggered
5. Dashboard displays system status

---

Results

- Real-time predictions working
- Monitoring system active
- Logging system implemented
- Retraining logic integrated

---

Run Locally

pip install -r requirements.txt
python scheduler.py
streamlit run dashboard/app.py

---

Author

Shiva

---

Support

If you like this project, consider giving it a star on GitHub.
