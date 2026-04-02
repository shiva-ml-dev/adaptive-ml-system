import time
import schedule
import os

# flag to avoid repeated retraining
already_retrained = False

from monitoring.performance import calculate_accuracy
from retraining.retrain import retrain_model

# log file path
file_path = "logs/predictions.csv"


def job():
    global already_retrained

    print("Checking model performance...")

    # file exists check
    if not os.path.exists(file_path):
        print("No data found yet...")
        return

    accuracy = calculate_accuracy(file_path)
    print(f"Accuracy: {accuracy}")

    if accuracy < 0.8 and not already_retrained:
        print("Retraining started...")
        retrain_model(file_path)
        print("Retraining completed!")
        already_retrained = True

    elif accuracy < 0.8 and already_retrained:
        print("Already retrained. Waiting for improvement...")

    else:
        print("Model is stable (no retraining needed)")


# run every 10 seconds (for testing)
schedule.every(10).seconds.do(job)

print("Scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(1)