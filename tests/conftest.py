import pytest
import pandas as pd

from typing import Generator
from src.config import core
from fastapi.testclient import TestClient
from src.app import app

@pytest.fixture
def rainfall_data()-> pd.DataFrame:
    return pd.read_csv(core.DATASET_DIR / 'precipitaciones.csv')

@pytest.fixture
def cb_data() -> pd.DataFrame:
    return pd.read_csv(core.DATASET_DIR / 'banco_central.csv')

@pytest.fixture
def milk_price_data() -> pd.DataFrame:
    return pd.read_csv(core.DATASET_DIR / 'precio_leche.csv')

@pytest.fixture
def client() -> Generator:
    with TestClient(app) as _client:
        yield _client
        app.dependency_overrides = {}
