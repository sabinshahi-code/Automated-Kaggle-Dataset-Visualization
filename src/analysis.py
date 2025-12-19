import os
import pandas as pd

def load_dataset(data_path="outputs/data"):
    for file in os.listdir(data_path):
        if file.endswith(".csv"):
            return pd.read_csv(os.path.join(data_path, file))
    raise FileNotFoundError("CSV file not found")


def process_dataset(df, output_path="outputs"):
    os.makedirs(output_path, exist_ok=True)

    summary = df.describe(include="all")
    summary.to_csv(os.path.join(output_path, "summary_statistics.csv"))

    missing_values = df.isnull().sum()
    missing_values.to_csv(os.path.join(output_path, "missing_values.csv"))

    return summary, missing_values

