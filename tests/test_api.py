import pandas as pd
import numpy as np
import logging
from src.config import core
from fastapi.testclient import TestClient

FORMAT = "%(asctime)s %(filename)s %(message)s"
logging.basicConfig(filename=core.LOGS_DIR / 'api_logs', level=logging.INFO, format=FORMAT)
logger = logging.getLogger(__name__)

def test_api_prediction(
        client: TestClient,
        rainfall_data: pd.DataFrame,
        cb_data: pd.DataFrame,
        milk_price_data: pd.DataFrame):

    payload = {
        "rainfall_data": {"inputs": rainfall_data.replace({np.nan: None}).to_dict(orient="records")},
        "centralbank_data": {"inputs": cb_data.replace({np.nan: None}).to_dict(orient="records")},
        "milkprice_data":{"inputs": milk_price_data.replace({np.nan: None}).to_dict(orient="records")}
    }

    logger.debug(payload)

    response = client.post("http://localhost:8881/predict", json=payload)

    response_dict = response.json()
    assert response.status_code == 200
    for _, v in response_dict['errors'].items():
        assert not v

    for pred in response_dict['predictions']:
        assert type(pred) == float
