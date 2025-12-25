import os
import pandas as pd

def load_dataset(data_path="outputs/data"):
    for file in os.listdir(data_path):
        csv_files = [
            os.path.join(data_path, f)
            for f in os.listdir(data_path)
            if f.endswith(".csv")
        ]

        latest_csv = max(csv_files, key=os.path.getmtime)
        return pd.read_csv(latest_csv)

def process_dataset(df, output_path="outputs"):
    os.makedirs(output_path, exist_ok=True)

    summary = df.describe(include="all")
    summary.to_csv(os.path.join(output_path, "summary_statistics.csv"), index = False)

    missing_values = df.isnull().sum()
    missing_values.to_csv(os.path.join(output_path, "missing_values.csv"), index = False)

    return summary, missing_values

