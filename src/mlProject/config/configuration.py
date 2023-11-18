###################################################
# configuration.py:
# Contains a class that represents configuration
# manager.
###################################################

from mlProject.constants import *
from mlProject.utils.common import read_yaml, create_dirs
from mlProject.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    """
    Class to represent a configuration manager for initialize
    configurations from config.yaml.
    """
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            params_filepath = PARAMS_FILE_PATH,
            schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_dirs([self.config.artifacts_root])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Get data ingestion configurations.

        Args:
            None
        
        Returns: 
            DataIngestionConfig object that contains the configs from config.yaml

        """
        config = self.config.data_ingestion

        create_dirs([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    