from mlProject import logger
from mlProject.components.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "01 Data Ingestion"

try:
    logger.info(f">>>>>> Stage: {STAGE_NAME} has started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> Stage: {STAGE_NAME} has finished <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e