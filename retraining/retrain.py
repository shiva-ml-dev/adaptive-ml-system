import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

def retrain_model(file_path):
    df = pd.read_csv(file_path)

    X = df[["feature1", "feature2"]]
    y = df["actual"]

    model = LogisticRegression()
    model.fit(X, y)

    joblib.dump(model, "models/model.pkl")

    print("Model retrained successfully!")