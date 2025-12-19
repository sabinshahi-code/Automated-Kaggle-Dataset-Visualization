from src.dataset_search import search_dataset
from src.downloader import download_dataset
from src.analysis import load_dataset, process_dataset
from src.visualization import get_visualizations
from src.report_generator import fetch_report
from src.logger import initialize_logger

def main():
    logger = initialize_logger()
    logger.info("Automation Started")

    query = input("Enter dataset keyword: ")
    logger.info(f"Dataset query received: {query}")

    dataset_ref = search_dataset(query)
    logger.info(f'Found dataset: {dataset_ref}')

    download_dataset(dataset_ref)
    logger.info('Dataset downloaded successfully')

    df = load_dataset()
    process_dataset(df)

    get_visualizations(df)
    logger.info("Visualizations files created")

    report_path = fetch_report(df)
    logger.info(f'Report generated at: {report_path}')


if __name__=="__main__":
    main()