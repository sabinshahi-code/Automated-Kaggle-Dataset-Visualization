import os
import tempfile
from kaggle import api

def download_dataset(dataset_ref):
    
    with tempfile.TemporaryDirectory() as tmpdir:
        api.dataset_download_files(dataset_ref, path=tmpdir, unzip=True)

        # download file to temprorary location

        csv_files = []
        for root, _, files in os.walk(tmpdir):
            for f in files:
                if f.lower().endswith(".csv"):
                    csv_files.append(os.path.join(root, f))

        if not csv_files:
            raise TypeError(f'Sorry but no CSV file found in this dataset')
        
        #select one latest downloaded csv_file
        selected_csv = max(csv_files, key=os.path.getmtime)

        # Now storing file to output dir
        final_path = os.path.join("outputs/data", os.path.basename(selected_csv))
        os.makedirs("outputs/data", exist_ok=True)
        os.replace(selected_csv, final_path)
