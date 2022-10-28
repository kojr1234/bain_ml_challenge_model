import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class RainfallInitialPreprocess(BaseEstimator, TransformerMixin):
    """
    Initial preprocess step necessary for rainfall data.
    This class transforms date into datetime and extracts month and year from
    the date.
    """
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        X['date'] = pd.to_datetime(X['date'], format = '%Y-%m-%d')
        X = X.sort_values(by='date', ascending=True).reset_index(drop=True)
        X['mes'] = X.date.apply(lambda x: x.month)
        X['ano'] = X.date.apply(lambda x: x.year)
        return X

class CentralBankInitialPreprocess(BaseEstimator, TransformerMixin):
    """
    Initial preprocess step necessary for central bank data.
    This class transforms Periodo into datetime and removes duplicates
    and null values.
    """
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        X['Periodo'] = X['Periodo'].apply(lambda x: x[0:10])
        X['Periodo'] = pd.to_datetime(X['Periodo'], format='%Y-%m-%d', errors='coerce')
        X.drop_duplicates(subset='Periodo', inplace=True)
        X.dropna(subset='Periodo', inplace=True)
        return X

class CentralBankPIBPreprocess(BaseEstimator, TransformerMixin):
    """
    This class implements the transformer class for CentralBank PIB information,
    converting the values to integer
    """
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        def convert_int(x):
            return int(x.replace('.',''))
        
        X = X.copy()
        cols_pib = [c for c in X.columns if c.startswith('PIB')]
        X.dropna(subset=cols_pib, how='any', axis=0, inplace=True)
        for c in cols_pib:
            X[c] = X[c].apply(convert_int)

        return X