import pandas as pd

def calculate_drift(train_path, new_path):
    try:
        df1 = pd.read_csv(train_path)
        df2 = pd.read_csv(new_path)

        drift_score = 0

        for col in df1.columns:
            if col in df2.columns and df1[col].dtype != 'object':
                diff = abs(df1[col].mean() - df2[col].mean())
                drift_score += diff

        drift_score = drift_score / len(df1.columns)

        report = {"drift_score": drift_score}

        return drift_score, report

    except Exception as e:
        print("Drift error:", e)
        return None, None