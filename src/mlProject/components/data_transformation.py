##############################################################
# data_transformation.py:
# Contains a class called DataTransformation that represents
# a data transformation object, which splits the data.
# NOTE: Preprocessing techniques such as PCA, EDA, missing 
# value handling and so on should come here if neccesary.
##############################################################s

import os
from mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from mlProject.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        

    def train_test_splitting(self) -> None:
        """
        Splitting train and test with 0.25 test size,
        logging and printing the shape of both train and test.

        Args:
            None
        
        Returns:
            None
        """
        data = pd.read_csv(self.config.data_path)

        train, test = train_test_split(data, test_size=0.25)

        # saves both train and test into .csv files
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        # logs the process and shapes
        logger.info(f"Splitted data into train and test with 0.25% test size")
        logger.info(f"Train shape: {train.shape}")
        logger.info(f"Test shape: {test.shape}")

        print(f"Train shape: {train.shape}")
        print(f"Test shape: {test.shape}")