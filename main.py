import argparse
from src.dataset_search import search_dataset
from src.downloader import download_dataset
from src.analysis import load_dataset, process_dataset
from src.visualization import get_visualizations
from src.report_generator import fetch_report
from src.logger import initialize_logger

def parse_args():
    parser = argparse.ArgumentParser(
        description="Automated Kaggle Dataset Fetching and Analysis Pipeline"
    )

    parser.add_argument(
        "--query",
        required=True,
        help="Keyword to search on Kaggle for dataset"
    )

    parser.add_argument(
        "--report",
        default="html",
        choices=["html"],
        help="Report Format (default: html)"
    )

    return parser.parse_args()

def main():
    args = parse_args()
    logger = initialize_logger()

    logger.info("Automation Started")
    logger.info(f"CLI arguments: query={args.query}, report={args.report}")

    try:
        dataset_ref = search_dataset(args.query)
        logger.info(f"Found dataset: {dataset_ref}")

        download_dataset(dataset_ref)
        logger.info("Dataset downloaded successfully")

        df = load_dataset()
        logger.info("Dataset loaded")

        process_dataset(df)
        logger.info("Data Processing Completed.")

        get_visualizations(df)
        logger.info("Visualizations files created")

        report_path = fetch_report(df)
        logger.info(f'Report generated at: {report_path}')
    except Exception as e:
        logger.exception(f'Pipeline execution failed {e}')

if __name__=="__main__":
    main()