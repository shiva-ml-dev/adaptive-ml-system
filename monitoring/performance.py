import pandas as pd

def calculate_accuracy(file_path):
    try:
        df = pd.read_csv(file_path)

        # check required columns
        if "prediction" not in df.columns or "actual" not in df.columns:
            return None

        total = len(df)
        if total == 0:
            return None

        correct = (df["prediction"] == df["actual"]).sum()
        accuracy = correct / total

        return accuracy

    except Exception as e:
        print("Error in calculate_accuracy:", e)
        return None


def check_retraining_needed(accuracy, drift):
    if accuracy is None:
        return False

    if drift or accuracy < 0.8:
        return True

    return False