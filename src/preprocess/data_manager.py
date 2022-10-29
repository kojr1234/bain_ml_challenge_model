import pandas as pd
from src.config import core

def load_dataset(*, file_name: str) -> pd.DataFrame:
    """
    Load the dataset
    """

    df = pd.read_csv(f"{core.DATASET_DIR}/{file_name}")
    return df