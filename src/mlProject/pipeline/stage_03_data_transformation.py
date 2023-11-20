###################################################
# stage_03_data_transformation.py:
# Data transformation pipeline
###################################################
from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_transformation import DataTransformation
from mlProject import logger
from pathlib import Path

STAGE_NAME = "03 Data Transformation"

class DataTranformationTrainingPipeline:
    """
    Class that represents and performs data transformation pipeline.
    """
    def __init__(self):
        pass

    def main(self):
        try:
            # Checking if the last work in status.txt is "Valid"
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
              status = f.read().split("\n")[-1]
            
            # If the data is valid according to the scema.yaml, perform data transformation pipeline
            if status == 'Valid':
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()

            else:
                raise Exception("The data schema is not valid")

        except Exception as e:
            print(e)

    
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage: {STAGE_NAME} has started <<<<<<")
        obj = DataTranformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Stage: {STAGE_NAME} has finished <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e