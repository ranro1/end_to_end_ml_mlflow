###################################################
# stage_01_data_ingestion.py:
# Prediction pipeline 
###################################################
import joblib
import numpy as np
import pandas as pd
from pathlib import Path


class PredictionPipeline:
    def __init__(self):
        # loads the model
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))


    def predict(self, data):
        prediction = self.model.predict(data)

        return prediction