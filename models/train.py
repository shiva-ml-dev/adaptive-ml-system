import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Dummy dataset (will replace with real data later)
data = {
    "feature1": [1, 2, 3, 4, 5],
    "feature2": [5, 4, 3, 2, 1],
    "target": [0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["feature1", "feature2"]]
y = df["target"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "models/model.pkl")

print("Model trained and saved!")