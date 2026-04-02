🚀 Adaptive ML Monitoring & Retraining System

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Live-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red)

---

📌 Overview

This project implements an end-to-end adaptive machine learning system that:

- Performs real-time predictions
- Monitors model performance
- Detects accuracy drops
- Triggers retraining

👉 Built with production-style architecture using FastAPI + Streamlit.

---

🚀 Live Demo

🔥 FastAPI (Live API)

👉 https://adaptive-ml-system-7.onrender.com
👉 https://adaptive-ml-system-7.onrender.com/docs

🔥 Streamlit Dashboard (Live UI)

👉 https://adaptive-ml-system-ptkbbf7euu2cd3mg55hn52.streamlit.app
---

🔥 Prediction Endpoint

POST "/predict"

Example Input:

{
  "feature1": 1,
  "feature2": 2
}

Response:

{
  "prediction": 0
}

---

🔥 Streamlit Dashboard

👉 (Add your Streamlit link here)

---

🧠 System Architecture

User → Streamlit Dashboard → FastAPI API → ML Model
                                   ↓
                             Predictions Log
                                   ↓
                        Monitoring (Accuracy / Drift)
                                   ↓
                         Retraining Trigger

---

⚡ Features

- 🚀 Real-time prediction API
- 📊 Live Streamlit dashboard
- 📝 Prediction logging (CSV)
- 📉 Accuracy monitoring
- 🔍 Data drift detection
- 🔄 Retraining trigger mechanism
- ⏱️ Scheduled performance checks

---

🛠️ Tech Stack

- Python
- FastAPI
- Streamlit
- Scikit-learn
- Pandas

---

📂 Project Structure

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

⚙️ How It Works

1. Predictions are made via FastAPI
2. Results are logged into CSV
3. Accuracy is calculated periodically
4. If accuracy drops → retraining is triggered
5. Dashboard displays system status

---

📊 Dashboard Demo

- Latest Data Table
- Prediction vs Actual
- Accuracy Display
- Live Prediction Input

(Add screenshots here)

---

📈 Results

- ✔️ Real-time predictions working
- ✔️ Monitoring system active
- ✔️ Logging system implemented
- ✔️ Retraining logic integrated

---

▶️ Run Locally

pip install -r requirements.txt
python scheduler.py
streamlit run dashboard/app.py

---

👨‍💻 Author

Shiva

---

⭐ Support

If you like this project, give it a ⭐ on GitHub!
