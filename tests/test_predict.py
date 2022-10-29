from src.pipeline import preprocess_data
from src.preprocess.data_manager import load_dataset
from src.preprocess.data_validation import validate_inputs
from src.config import core
from src.config.core import config
from src.predict import make_prediction

def test_data_validation():
    rainfall_data = load_dataset(file_name='precipitaciones.csv')
    cb_data = load_dataset(file_name='banco_central.csv')
    milk_data = load_dataset(file_name='precio_leche.csv')

    # I defined that Coquimbo should either receive an int or null value
    # this should yield an error
    rainfall_data['Coquimbo'] = 'abc'

    data_meta = validate_inputs(
        rainfall_data=rainfall_data,
        centralbank_data=cb_data,
        milkprice_data=milk_data
    )

    for k, v in data_meta.items():
        if k == 'rainfall':
            assert v['errors']
        else:
            assert not v['errors']
    
def test_predict():
    rainfall_data = load_dataset(file_name='precipitaciones.csv')
    cb_data = load_dataset(file_name='banco_central.csv')
    milkprice_data = load_dataset(file_name='precio_leche.csv')

    results = make_prediction(
        rainfall_data=rainfall_data, 
        centralbank_data=cb_data, 
        milkprice_data=milkprice_data
    )

    assert results['predictions'].min() > 0
    
    for k,v in results['errors'].items():
        assert not v



