from fastapi import FastAPI
import joblib
import os
from datetime import datetime
import pandas as pd

app = FastAPI()

# Load model
model = joblib.load("models/model.pkl")


@app.get("/")
def home():
    return {"message": "Adaptive ML System is running"}


@app.post("/predict")
def predict(feature1: float, feature2: float):

    try:
        # Model prediction
        input_data = [[feature1, feature2]]
        pred = model.predict(input_data)

        # Safe prediction extraction
        if hasattr(pred, "__len__"):
            prediction = int(pred[0])
        else:
            prediction = int(pred)

        # Logging
        log_data = {
            "feature1": feature1,
            "feature2": feature2,
            "prediction": prediction,
            "timestamp": datetime.now()
        }

        df = pd.DataFrame([log_data])

        # Create logs folder if not exists
        if not os.path.exists("logs"):
            os.makedirs("logs")

        try:
            df.to_csv("logs/predictions.csv", mode='a', header=False, index=False)
        except:
            df.to_csv("logs/predictions.csv", index=False)

        return {"prediction": prediction}

    except Exception as e:
        return {"error": str(e)}