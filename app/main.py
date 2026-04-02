from fastapi import FastAPI
import joblib
import os
from datetime import datetime

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

        # File path
        file_path = "data/data.csv"

        # Create file if not exists
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write("feature1,feature2,prediction,timestamp\n")

        # Append data
        with open(file_path, "a") as f:
            f.write(f"{feature1},{feature2},{prediction},{datetime.now()}\n")

        return {"prediction": prediction}

    except Exception as e:
        return {"error": str(e)}
