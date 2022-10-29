import pandas as pd
from src.config import core
from src.config.core import config
from functools import reduce
from multiprocessing.connection import Pipe
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.feature_selection import SelectKBest, mutual_info_regression
from src.preprocess.transformers import (RainfallInitialPreprocess, 
                                        CentralBankInitialPreprocess,
                                        CentralBankPIBPreprocess,
                                        CentralBankIMACECPreprocess,
                                        MilkPricePreprocess)

pipeline_rainfall = Pipeline(
    [
        ('RainfallInitialPreprocess', RainfallInitialPreprocess())
    ]
)

pipeline_cb = Pipeline([
        ('CentralBankInitialPreprocess', CentralBankInitialPreprocess()),
        ('CentralBankPIBPreprocess',CentralBankPIBPreprocess()),
        ('CentralBankIMACECPreprocess', CentralBankIMACECPreprocess())
    ]
)

pipeline_milk = Pipeline(
    [
        ('MilkPricePreprocess', MilkPricePreprocess())
    ]
)

pipeline_final_data = Pipeline([('scale', StandardScaler()),
                 ('selector', SelectKBest(mutual_info_regression)),
                 ('poly', PolynomialFeatures()),
                 ('model', Ridge())])

def preprocess_data(*,
    rainfall_data: pd.DataFrame,
    centralbank_data: pd.DataFrame,
    milkprice_data: pd.DataFrame
    ) -> pd.DataFrame:
    """
    Preprocess raw data to be used as input for the model
    """

    rainfall_data = pipeline_rainfall.transform(rainfall_data)
    centralbank_data = pipeline_cb.transform(centralbank_data)
    milkprice_data = pipeline_milk.transform(milkprice_data)

    final_data = reduce(lambda l, r: pd.merge(l, r, on=['mes','ano'], how='inner'),
                        [rainfall_data, centralbank_data, milkprice_data])

    feature_columns = config.model_config.features
    target_column = [config.model_config.target]
    final_data = final_data[feature_columns + target_column]

    return final_data