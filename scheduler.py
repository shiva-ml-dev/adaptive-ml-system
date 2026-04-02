import time
from monitoring.performance import calculate_accuracy
from retraining.retrain import retrain_model

file_path = "logs/predictions.csv"

while True:
    print("Checking model accuracy...")

    try:
        acc = calculate_accuracy(file_path)

        if acc is None:
            print("No data available or missing columns")
        else:
            print(f"Current Accuracy: {acc:.2f}")

            if acc < 0.8:
                print("Low accuracy detected. Retraining model...")
                retrain_model()
            else:
                print("Model is performing well")

    except Exception as e:
        print(f"Error: {e}")

    time.sleep(60)