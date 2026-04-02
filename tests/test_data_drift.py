from monitoring.drift import calculate_drift

drift, report = calculate_drift("data/data.csv", "data/data.csv")

print("Drift:", drift)
print("Report:", report)