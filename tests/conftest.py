import pytest

import pandas as pd

from src.config import core

@pytest.fixture
def rainfall_data()-> pd.DataFrame():
    return pd.read_csv(core.DATASET_DIR / 'precipitaciones.csv', nrows=100)