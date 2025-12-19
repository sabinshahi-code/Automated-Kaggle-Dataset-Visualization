from src.dataset_search import search_dataset
from src.downloader import download_dataset
from src.analysis import load_dataset, process_dataset
from src.visualization import get_visualizations
from src.report_generator import fetch_report

def main():
    query = input("Enter dataset keyword: ")

    dataset_ref = search_dataset(query)
    print(f'Found dataset: {dataset_ref}')

    download_dataset(dataset_ref)
    print('Dataset downloaded successfully')

    df = load_dataset()
    process_dataset(df)

    get_visualizations(df)
    print("Visualizations files created")

    report_path = fetch_report(df)
    print(f'Report generated at: {report_path}')


if __name__=="__main__":
    main()