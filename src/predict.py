from typing import Any, Union

import numpy as np
import pandas as pd

from src.pipeline import preprocess_data
from src.preprocess.data_manager import load_pipeline
from src.preprocess.data_validation import validate_inputs
from src.config.core import config

import logging
FORMAT = "%(asctime)s %(filename)s %(message)s"
logging.basicConfig(filename=core.LOGS_DIR / 'predict_logs', level=logging.INFO, format=FORMAT)
logger = logging.getLogger(__name__)

def make_prediction(*, 
    rainfall_data: Union[pd.DataFrame, dict],
    centralbank_data: Union[pd.DataFrame, dict],
    milkprice_data: Union[pd.DataFrame, dict]) -> dict[str,Any]:
    """
    This functions validates the data input and sees if there is no data
    inconsistency. Then, it creates a data structure storing all predictions
    """
    
    data_meta = validate_inputs(
        rainfall_data=rainfall_data,
        centralbank_data=centralbank_data,
        milkprice_data=milkprice_data
    )
    
    logging.info('Validating data!')

    no_errors = True
    for k, v in data_meta.items():
        if v['errors']:
            no_errors = False
    
    if no_errors:
        logging.info('Data validated and no errors found!')
    else:
        logging.warning('Data validated and errors found!')

    results = {
        "predictions": None,
        "errors": {k: v['errors'] for k,v in data_meta.items()}
    }

    if no_errors:
        final_data = preprocess_data(
            rainfall_data=data_meta['rainfall']['data'],
            centralbank_data=data_meta['centralbank']['data'],
            milkprice_data=data_meta['milkprice']['data']
        )

        model_pipe = load_pipeline(file_name=config.app_config.pipeline_save_file)
        results['predictions'] = model_pipe.predict(final_data[config.model_config.features])

    return results
    

