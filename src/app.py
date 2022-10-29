from typing import Any
import pandas as pd
import numpy as np

from fastapi import APIRouter, FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.encoders import jsonable_encoder

from src.preprocess.data_validation import (MultipleRainfallDataInputs,
                                 MultipleCentralBankDataInputs,
                                 MultipleMilkPriceDataInputs)
from src.predict import make_prediction
from src.config import core
import json
import logging

FORMAT = "%(asctime)s %(filename)s %(message)s"
logging.basicConfig(filename=core.LOGS_DIR / 'app_logs', level=logging.INFO, format=FORMAT)
logger = logging.getLogger(__name__)

app = FastAPI(
    title='Bain ML Challenge', openapi_url="/api/v1/openapi.json"
)

root_router = APIRouter()

@root_router.get("/")
def index(request: Request):
    """basic html response"""
    body = """
    <html>
    <body style='padding: 10px;'>
    <h1>Bain ML Challenge API</h1>
    Check the docs: <a href='/docs'>here</a>
    </body>
    </html>
    """

    return HTMLResponse(content=body)

@root_router.post("/predict", status_code=200)
def predict(*, 
    rainfall_data: MultipleRainfallDataInputs,
    centralbank_data: MultipleCentralBankDataInputs,
    milkprice_data: MultipleMilkPriceDataInputs) -> Any:

    rainfall_data = pd.DataFrame(jsonable_encoder(rainfall_data.inputs)).replace(
        {np.nan: None}
    )

    centralbank_data = pd.DataFrame(jsonable_encoder(centralbank_data.inputs)).replace(
        {np.nan: None}
    )

    milkprice_data = pd.DataFrame(jsonable_encoder(milkprice_data.inputs)).replace(
        {np.nan: None}
    )

    results = make_prediction(
            rainfall_data=rainfall_data,
            centralbank_data=centralbank_data,
            milkprice_data=milkprice_data
    )
    results["predictions"] = results["predictions"].astype(float).tolist()

    no_errors = True
    errors = {}
    for k, v in results['errors'].items():
        if v:
            no_errors = False
            errors[k] = v

    if not no_errors:
        logger.warning(f"Prediction validation error: {results.get('errors')}")
        raise HTTPException(status_code=400, detail=json.loads(errors))

    logger.info(f"Prediction results: {results.get('predictions')}")

    return results

app.include_router(root_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3400",
        "http://localhost:8400",
        "https://localhost:3400",
        "https://localhost:8400"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8881, log_level="debug")
