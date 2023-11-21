###########################################################
# model_evaluation.py:
# Contains a class called ModelEvaluation that represents
# a model evaluation object, which evaluates the model's
# perfomarnce and logs the predefined metrics both locally
# and remotly to MLFlow
###########################################################

import os
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from mlProject.entity.config_entity import ModelEvaluationConfig
from mlProject.utils.common import save_to_json
from pathlib import Path


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, preds):
        """
        Calculates and returns the following metrics:
            - Mean Squared Error
            - Mean Absolute Error
            - R^2

        Args:
            actual - contains the true values
            pred - contains the predicted values from the model

        Returns:
            rmse - double, root mean squeared error
            mae - double, mean absolute error
            r2 - double, r^2 metric
        """
        rmse = np.sqrt(mean_squared_error(actual, preds))
        mae = mean_absolute_error(actual, preds)
        r2 = r2_score(actual, preds)

        return rmse, mae, r2
    
    def log_to_mlflow(self):
        """
        Logs the metrics, parametrs and model to MLFlow
        """
        
        # loads test data and model
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        # defines X_test and y_test
        X_test = test_data.drop([self.config.target_column], axis=1)
        y_test = test_data[[self.config.target_column]]

        # sets tracking uri
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        # starts mlflow tracking
        with mlflow.start_run():
            # calculate scores
            preds = model.predict(X_test)
            (rmse, mae, r2) = self.eval_metrics(y_test, preds)

            # saves metrics locally
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_to_json(path=Path(self.config.metric_file_name), data=scores)

            # logs parameters to mlflow
            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)
            
            # logs model to mlflow
            mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticNet")
           

