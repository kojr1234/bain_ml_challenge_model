import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from src.preprocess.transformers import (RainfallInitialPreprocess, 
                                        CentralBankInitialPreprocess,
                                        CentralBankPIBPreprocess)

def test_rainfall_initial_preprocess(rainfall_data):
    pipeline = Pipeline(
        [
            ('RainfallInitialPreprocess', RainfallInitialPreprocess())
        ]
    )

    transformed = pipeline.transform(rainfall_data)
    head = transformed.head(1)
    tail = transformed.tail(1)

    assert 'mes' in transformed.columns
    assert 'ano' in transformed.columns
    assert head.date.item() < tail.date.item()

def test_cb_initial_preprocess(cb_data):
    
    pipeline = Pipeline(
        [
            ('CentralBankInitialPreprocess', CentralBankInitialPreprocess())
        ]
    )

    transformed = pipeline.transform(cb_data)

    assert transformed['Periodo'].isnull().sum() == 0
    assert transformed['Periodo'].duplicated().sum() == 0
    assert type(transformed['Periodo'].iloc[0]) == pd.Timestamp

def test_cb_pib_preprocess(cb_data):

    pib_columns = [c for c in cb_data if c.startswith('PIB')]
    cb_data = cb_data[pib_columns]

    pipeline = Pipeline(
        [
            ('CentralBankPIBPreprocess', CentralBankPIBPreprocess())
        ]
    )

    transformed = pipeline.transform(cb_data)

    for c in transformed.columns:
        assert transformed[c].dtype == np.int64
    

