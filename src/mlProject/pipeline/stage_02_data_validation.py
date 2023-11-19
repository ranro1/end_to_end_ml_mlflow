###################################################
# stage_02_data_validation.py:
# Data valdiation pipeline
###################################################
from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_validation import DataValidation
from mlProject import logger

STAGE_NAME = "02 Data Validation"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        """
        Function that runs the data validation pipeline.
        """
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()

        

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage: {STAGE_NAME} has started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Stage: {STAGE_NAME} has finished <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e