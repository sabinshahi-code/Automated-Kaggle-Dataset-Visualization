import logging
from kaggle import api

logger = logging.getLogger(__name__)

def search_dataset(query):
    logger.info(f'Searching kaggle for dataset {query}')
    datasets = api.dataset_list(search=query)
    if not datasets:
        logger.info("No datasets found")
        raise ValueError("No datasets found")
    return datasets[0].ref