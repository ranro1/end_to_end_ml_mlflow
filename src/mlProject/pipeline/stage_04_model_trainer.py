###################################################
# stage_04_model_trainer.py:
# odel training pipeline
###################################################
from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_trainer import ModelTrainer
from mlProject import logger
from pathlib import Path

STAGE_NAME = "04 Model Training"

class ModelTrainerPipeline:
    """
    Class that represents and performs data transformation pipeline.
    """
    def __init__(self):
        pass

    def main(self):
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer_config = ModelTrainer(config=model_trainer_config)
            model_trainer_config.train()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage: {STAGE_NAME} has started <<<<<<")
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f">>>>>> Stage: {STAGE_NAME} has finished <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
