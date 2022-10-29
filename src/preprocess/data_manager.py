import pandas as pd
import joblib

from typing import List
from src.config import core
from src.config.core import config
from sklearn.pipeline import Pipeline

def load_dataset(*, file_name: str) -> pd.DataFrame:
    """
    Load the dataset
    """

    df = pd.read_csv(f"{core.DATASET_DIR}/{file_name}")
    return df

def remove_old_pipelines(*, files_to_keep: List[str]) -> None:
    """
    Remove old model pipelines
    """
    do_not_delete = files_to_keep + ["__init__.py"]
    for model_file in core.TRAINED_MODEL_DIR.iterdir():
        if model_file.name not in do_not_delete:
            model_file.unlink()

def load_pipeline(*, file_name: str) -> Pipeline:
    """
    Load pipeline
    """
    file_path = core.TRAINED_MODEL_DIR / f'{file_name}.pkl'
    return joblib.load(filename=file_path)

def save_pipeline(*, pipeline_to_persist: Pipeline) -> None:
    """
    Save the pipeline
    """
    save_file_name = f"{config.app_config.pipeline_save_file}.pkl"
    save_path = core.TRAINED_MODEL_DIR / save_file_name

    remove_old_pipelines(files_to_keep=[save_file_name])
    joblib.dump(pipeline_to_persist, save_path)

