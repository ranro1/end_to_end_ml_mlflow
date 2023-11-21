###################################################
# stage_05_model_evaluation.py:
# Model evalutaion pipeline
###################################################
from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_evaluation import ModelEvaluation
from mlProject import logger
from pathlib import Path

STAGE_NAME = "05 Model Training"

class ModelEvaluationPipeline:
    """
    Class that represents and performs data transformation pipeline.
    """
    def __init__(self):
        pass

    def main(self):
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
            model_evaluation_config.log_to_mlflow()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage: {STAGE_NAME} has started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> Stage: {STAGE_NAME} has finished <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
