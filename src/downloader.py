import os
from kaggle import api

def download_dataset(dataset_ref, path="outputs/data"):
    os.makedirs(path, exist_ok=True)
    api.dataset_download_files(dataset_ref, path=path, unzip=True)