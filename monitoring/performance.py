import pandas as pd

def calculate_accuracy(file_path):
    df = pd.read_csv(file_path)

    # check required columns
    if "prediction" not in df.columns or "actual" not in df.columns:
        return None

    correct = (df["prediction"] == df["actual"]).sum()
    total = len(df)

    accuracy = correct / total if total > 0 else 0

    return accuracy
def check_retraining_needed(accuracy, drift):
    if drift or accuracy < 0.8:
        return True
    return False