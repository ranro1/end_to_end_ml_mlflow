###################################################
# stage_01_data_ingestion.py:
# Data ingestion pipeline
###################################################

from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_ingestion import DataIngestion
from mlProject import logger

STAGE_NAME = "01 Data Ingestion"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        """
        Function that runs the data ingestion pipeline.
        """
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise e
        

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage: {STAGE_NAME} has started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Stage: {STAGE_NAME} has finished <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e