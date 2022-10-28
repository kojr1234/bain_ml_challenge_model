import pandas as pd
from sklearn.pipeline import Pipeline
from src.preprocess.transformers import RainfallInitialPreprocess, CentralBankInitialPreprocess

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
            ('RainfallInitialPreprocess', CentralBankInitialPreprocess())
        ]
    )

    transformed = pipeline.transform(cb_data)

    assert transformed['Periodo'].isnull().sum() == 0
    assert transformed['Periodo'].duplicated().sum() == 0
    assert type(transformed['Periodo'].iloc[0]) == pd.Timestamp