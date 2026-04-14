import time
from monitoring.performance import calculate_accuracy
from monitoring.drift import calculate_drift
from retraining.retrain import retrain_model

file_path = "logs/predictions.csv"
data_path = "data/data.csv"

last_retrain_time = 0
cooldown = 300

while True:
    print("Checking system health...")

    try:
        acc = calculate_accuracy(file_path)

        if acc is None:
            print("No data available or missing columns")
        else:
            print(f"Current Accuracy: {acc:.2f}")

        drift, report = calculate_drift(data_path, file_path)
        print(f"Drift Score: {drift}")

        retrain_needed = False

        if acc is not None and acc < 0.8:
            print("Low accuracy detected")
            retrain_needed = True

        if drift is not None and drift > 0.3:
            print("Data drift detected")
            retrain_needed = True

        current_time = time.time()

        if retrain_needed:
            if current_time - last_retrain_time > cooldown:
                print("Retraining model")
                retrain_model()
                last_retrain_time = current_time
            else:
                print("Recently retrained, skipping")
        else:
            print("Model is performing well")

    except Exception as e:
        print(f"Error: {e}")

    time.sleep(60)