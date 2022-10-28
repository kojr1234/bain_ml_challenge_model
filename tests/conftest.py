import pytest

import pandas as pd

from src.config import core

@pytest.fixture
def rainfall_data()-> pd.DataFrame():
    return pd.read_csv(core.DATASET_DIR / 'precipitaciones.csv', nrows=100)

@pytest.fixture
def centralbank_data() -> pd.DataFrame():
    return pd.read_csv(core.DATASET_DIR / 'banco_central.csv', nrows=100)