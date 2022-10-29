import logging
import numpy as np

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score

from src.config import core
from src.config.core import config
from src.preprocess.data_manager import load_dataset, save_pipeline
from src.pipeline import pipeline_final_data, preprocess_data

FORMAT = "%(asctime)s %(filename)s %(message)s"
logging.basicConfig(filename=core.LOGS_DIR / 'training_logs', level=logging.INFO, format=FORMAT)
logger = logging.getLogger(__name__)

def run_training() -> None:
    """
    Function to train the model
    """

    
    rainfall_data = load_dataset(file_name='precipitaciones.csv')
    cb_data = load_dataset(file_name='banco_central.csv')
    milk_data = load_dataset(file_name='precio_leche.csv')
    logging.info('Datasets successfully loaded!')

    training_dataset = preprocess_data(
        rainfall_data=rainfall_data,
        centralbank_data=cb_data,
        milkprice_data=milk_data
    )
    logging.info('Datasets successfully processed!')

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
    logging.info('Model successfully trained!')

    save_pipeline(pipeline_to_persist=grid)
    logging.info('Model successfully saved!')

    y_predicted = grid.predict(X_test)

    rmse = mean_squared_error(y_test, y_predicted)
    r2 = r2_score(y_test, y_predicted)
    
    print('RMSE: ', rmse)
    print('R2: ', r2)


if __name__ == "__main__":
    np.random.seed(0)
    run_training()