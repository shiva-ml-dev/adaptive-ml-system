from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    feature1: float
    feature2: float

@app.get("/")
def home():
    return {"message": "API running"}

@app.post("/predict")
def predict(data: InputData):
    f1 = data.feature1
    f2 = data.feature2

    # dummy logic (replace with your model)
    result = 1 if f1 + f2 > 5 else 0

    return {"prediction": result}