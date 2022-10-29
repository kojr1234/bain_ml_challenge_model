import logging
from pydantic import BaseModel
from typing import Sequence
from pathlib import Path
import yaml
import src

SOURCE_ROOT = Path(src.__file__).resolve().parent
ROOT = SOURCE_ROOT.parent
DATASET_DIR = SOURCE_ROOT / "data"
CONFIG_FILE_PATH = SOURCE_ROOT / 'config.yml'
TRAINED_MODEL_DIR = SOURCE_ROOT / 'model'
LOGS_DIR = ROOT / 'logs'

class AppConfig(BaseModel):
    """
    Application configuration class
    """
    pipeline_save_file: str

class ModelConfig(BaseModel):
    """
    Model configuration class
    """

    target: str
    features: Sequence[str]
    test_size: float
    random_state: int
    gridsearch: dict
    
class Config(BaseModel):
    """
    Main config object
    """
    app_config: AppConfig
    model_config: ModelConfig

def fetch_config_from_yaml() -> dict:
    """
    Parse YAML containing the package configuration
    """

    with open(CONFIG_FILE_PATH, "r") as conf_file:
        _cfg = yaml.load(conf_file, Loader=yaml.Loader)
        return _cfg
    raise OSError(f"Did not find config file at path: {CONFIG_FILE_PATH}")

def create_and_validate_config() -> dict:
    """
    Run validation on config values.
    """
    parsed_config = fetch_config_from_yaml()

    _config = Config(
        app_config=AppConfig(**parsed_config),
        model_config=ModelConfig(**parsed_config)
    )

    return _config

config = create_and_validate_config()