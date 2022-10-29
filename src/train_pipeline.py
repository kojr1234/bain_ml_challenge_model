import logging
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score

from src.config.core import config
from src.pipeline import pipeline_final_data, preprocess_data

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_training() -> None:
    """
    Function to train the model
    """

    rainfall_data = pd.read_csv(core.DATASET_DIR / 'precipitaciones.csv')
    cb_data = pd.read_csv(core.DATASET_DIR / 'banco_central.csv')
    milk_data = pd.read_csv(core.DATASET_DIR / 'precio_leche.csv')

    training_dataset = preprocess_data(
        rainfall_data=rainfall_data,
        cb_data=cb_data,
        milk_data=milk_data
    )

    X = training_dataset[config.model_config.features]
    y = training_dataset[config.model_config.target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, 
        y,
        test_size=config.model_config.test_size,
        random_state=config.model_config.random_state
    )

    grid = GridSearchCV(
        estimator=pipeline_final_data,
        param_grid=config.model_config.gridsearch,
        cv = 3,
        scoring = 'r2'
    )
    grid.fit(X_train, y_train)
    y_predicted = grid.predict(X_test)

    rmse = mean_squared_error(y_test, y_predicted)
    r2 = r2_score(y_test, y_predicted)

    print('RMSE: ', rmse)
    print('R2: ', r2)


if __name__ == "__main__":
    np.random.seed(0)
    run_training()