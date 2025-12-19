from kaggle import api

def search_dataset(query):
    datasets = api.dataset_list(search=query)
    if not datasets:
        raise ValueError("No datasets found")
    return datasets[0].ref