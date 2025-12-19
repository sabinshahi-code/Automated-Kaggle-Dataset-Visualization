import os
import matplotlib.pyplot as plt
import seaborn as sns

def get_visualizations(df, output_path="outputs/plots"):
    os.makedirs(output_path, exist_ok=True)

    numeric_columns = df.select_dtypes(include=["number"]).columns


    #For feature distribution plots

    for col in numeric_columns:
        plt.figure()
        df[col].hist()
        plt.title(f"Distribution of {col}")
        plt.xlabel(col)
        plt.ylabel("Occurence")
        plt.savefig(os.path.join(output_path, f"{col}_distribution.png"))
        plt.close()

    
    # Correlation heatmap

    if len(numeric_columns) > 1:
        plt.figure(figsize=(8, 6))
        sns.heatmap(df[numeric_columns].corr(), annot=True, cmap="coolwarm")
        plt.title("Correlation Heatmap")
        plt.savefig(os.path.join(output_path, "heatmap.png"))
        plt.close()

