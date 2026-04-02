import pandas as pd

def calculate_drift(train_path, new_path, threshold=0.1):
    train = pd.read_csv(train_path)
    new = pd.read_csv(new_path)

    drift_report = {}

    for col in train.columns:
        if train[col].dtype != 'object':  # numeric columns ಮಾತ್ರ
            train_mean = train[col].mean()
            new_mean = new[col].mean()

            diff = abs(train_mean - new_mean)

            drift_report[col] = diff

    drift_detected = any(diff > threshold for diff in drift_report.values())

    return drift_detected, drift_report