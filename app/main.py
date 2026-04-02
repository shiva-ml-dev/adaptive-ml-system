from fastapi import FastAPI
import threading
import time
from monitoring.performance import calculate_accuracy
from retraining.retrain import retrain_model

app = FastAPI()

# API
@app.get("/")
def home():
    return {"message": "API running"}

@app.post("/predict")
def predict(data: dict):
    f1 = data.get("feature1", 0)
    f2 = data.get("feature2", 0)
    prediction = 1 if (f1 + f2) > 5 else 0
    return {"prediction": prediction}


# Scheduler
def scheduler():
    file_path = "logs/predictions.csv"

    while True:
        try:
            acc = calculate_accuracy(file_path)

            if acc is not None:
                print("Accuracy:", acc)

                if acc < 0.8:
                    print("Retraining...")
                    retrain_model()
        except Exception as e:
            print("Error:", e)

        time.sleep(60)


# Run scheduler on startup
@app.on_event("startup")
def start():
    threading.Thread(target=scheduler, daemon=True).start()