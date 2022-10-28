import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from src.preprocess.transformers import (RainfallInitialPreprocess, 
                                        CentralBankInitialPreprocess,
                                        CentralBankPIBPreprocess,
                                        CentralBankIMACECPreprocess,
                                        MilkPricePreprocess)

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

    pib_columns = [c for c in cb_data.columns if c.lower().startswith('pib')]

    pipeline = Pipeline(
        [
            ('CentralBankPIBPreprocess', CentralBankPIBPreprocess())
        ]
    )

    transformed = pipeline.transform(cb_data)

    for c in pib_columns:
        assert transformed[c].dtype == np.int64
    
def test_cb_imacec_iv_preprocess(cb_data):

    imacec_iv_columns = [c for c in cb_data.columns if c.lower().startswith('imacec')] + \
        ['Indice_de_ventas_comercio_real_no_durables_IVCM']

    pipeline = Pipeline(
        [
            ('CentralBankIMACECPreprocess', CentralBankIMACECPreprocess())
        ]
    )

    transformed = pipeline.transform(cb_data)

    for c in imacec_iv_columns:
        assert transformed[c].min() > 30
        assert transformed[c].max() > 100 
        assert transformed[c].dtype == np.float64

def test_milk_price_preprocess(milk_price_data):

    pipeline = Pipeline(
        [
            ('MilkPricePreprocess', MilkPricePreprocess())
        ]
    )

    transformed = pipeline.transform(milk_price_data)

    assert 'mes' in transformed.columns
    assert 'ano' in transformed.columns
    assert 'mes-ano' in transformed.columns
    
    for mes_ano in transformed['mes-ano'].sample(5):
        assert len(mes_ano.split('-')) == 2
        assert int(mes_ano.split('-')[0])  <= 12
        assert int(mes_ano.split('-')[0])  > 0

        assert int(mes_ano.split('-')[1])  >= 1979
        assert int(mes_ano.split('-')[1])  < 2022
    


    



