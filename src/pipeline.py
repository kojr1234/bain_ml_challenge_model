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