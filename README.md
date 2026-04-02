Adaptive ML Monitoring and Retraining System

Overview

This project implements an adaptive machine learning system that continuously monitors model performance and automatically triggers retraining when accuracy drops below a threshold.

Features

- Real-time prediction logging
- Model performance monitoring
- Automatic retraining trigger
- Streamlit dashboard for visualization
- Scheduler for periodic checks

Tech Stack

- Python
- Scikit-learn
- Pandas
- Streamlit

Project Structure

adaptive-ml-system/

├── app/
├── dashboard/
├── monitoring/
├── retraining/
├── tests/
├── data/
├── models/
├── scheduler.py
├── requirements.txt

How it Works

1. Predictions are logged in a CSV file
2. Accuracy is calculated periodically
3. If accuracy < 0.8, retraining is triggered
4. Dashboard displays performance and status

Dashboard Preview

Main Dashboard

"Dashboard" (screenshots/dashboard.png)

Accuracy & Retraining Trigger

"Accuracy" (screenshots/accuracy.png)

Prediction Distribution

"Chart" (screenshots/chart.png)

Run Project

pip install -r requirements.txt
python scheduler.py
streamlit run dashboard/app.py

Author

Shiva
