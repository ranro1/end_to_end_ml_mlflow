from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline                                  

STAGE_NAME = "01 Data Ingestion"

try:
    logger.info(f">>>>>> Stage: {STAGE_NAME} has started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> Stage: {STAGE_NAME} has finished <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "02 Data Validation"
try:
    logger.info(f">>>>>> Stage: {STAGE_NAME} has started <<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> Stage: {STAGE_NAME} has finished <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e