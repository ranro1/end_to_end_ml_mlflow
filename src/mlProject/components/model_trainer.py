###########################################################
# model_trainer.py:
# Contains a class called ModelTrainer that represents
# a model trainer object, which traines a model on data# 
###########################################################

import pandas as pd
import os
from mlProject import logger
from sklearn.linear_model import ElasticNet
import joblib
from mlProject.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        """
        Trains the model.
        """

        # reads train and test data
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        # defines X & y for both train and test
        X_train = train_data.drop([self.config.target_column], axis=1)
        y_train = train_data[[self.config.target_column]]
        X_test = test_data.drop([self.config.target_column], axis=1)
        y_test = test_data[[self.config.target_column]]

        # initializes the model
        elasticNet_model = ElasticNet(alpha=self.config.alpha,
                                     l1_ratio=self.config.l1,
                                     random_state=42)

        # fir the model to the data
        elasticNet_model.fit(X_train, y_train)

        # save the model
        joblib.dump(elasticNet_model, os.path.join(self.config.root_dir, self.config.model_name))