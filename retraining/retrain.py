import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

def retrain_model(file_path):
    try:
        df = pd.read_csv(file_path)

        X = df[["feature1", "feature2"]]
        y = df["actual"]

        model = LogisticRegression()
        model.fit(X, y)

        joblib.dump(model, "models/model.pkl")

        print("Model retrained successfully!")

        with open("logs/status.txt", "w") as f:
            f.write("Model retrained successfully")

    except Exception as e:
        print(f"Error during retraining: {e}")

if __name__ == "__main__":
    retrain_model("logs/predictions.csv")