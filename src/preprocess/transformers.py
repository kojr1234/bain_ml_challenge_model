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
    This class implements the transformer function for CentralBank PIB information,
    converting the values to integer
    """
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        def convert_int(x):
            return int(x.replace('.',''))
        
        X = X.copy()
        pib_columns = [c for c in X.columns if c.startswith('PIB')]
        X.dropna(subset=pib_columns, how='any', axis=0, inplace=True)
        for c in pib_columns:
            X[c] = X[c].apply(convert_int)

        return X

class CentralBankIMACECPreprocess(BaseEstimator, TransformerMixin):
    """
    This class implements the transformer function for CentralBank IMACEC
    infromation, converting the values to float and correcting the 
    scale of the values
    """
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        def to_100(x): 
            x = x.split('.')
            if x[0].startswith('1'):
                if len(x[0]) >2:
                    return float(x[0] + '.' + x[1])
                else:
                    x = x[0]+x[1]
                    return float(x[0:3] + '.' + x[3:])
            else:
                if len(x[0])>2:
                    return float(x[0][0:2] + '.' + x[0][-1])
                else:
                    x = x[0] + x[1]
                    return float(x[0:2] + '.' + x[2:])
        
        X = X.copy()
        imacec_iv_columns = [c for c in X.columns if c.lower().startswith('imacec')] + \
            ['Indice_de_ventas_comercio_real_no_durables_IVCM']
        X.dropna(subset=imacec_iv_columns, how='any', axis=0, inplace=True)
        for c in imacec_iv_columns:
            X[c] = X[c].apply(to_100)

        return X