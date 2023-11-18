###########################################################
# data_ingestion.py:
# Contains a class called DataIngestion that represents
# a data ingestion object, which deals with data.
###########################################################


import os
import urllib.request as request
import zipfile
from pathlib import Path
from mlProject import logger
from mlProject.utils.common import get_size
from mlProject.entity.config_entity import DataIngestionConfig

class DataIngestion:
    """
    Class that deals with data ingestion
    """
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    

    def download_file(self):
        """
        Downloads the data.

        Args:
            None
        
        Returns: 
            None

        """
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} downloaded successfully! additional info: {headers}")
        else:
            logger.info(f"File alrady exists, with size: {get_size(Path(self.config.local_data_file))}")


    def extract_zip_file(self):
        """
        Extracts a zip file into a directory.

        Args:
            None
        
        Returns: 
            DataIngestionConfig object that contains the configs from config.yaml

        """

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_f:
            zip_f.extractall(unzip_path)