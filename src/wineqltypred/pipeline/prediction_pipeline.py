import joblib
import numpy as np
import pandas as pd
from pathlib import Path
from src.wineqltypred.config.configuration import ConfigurationManager

class PredictionPipeline:
    def __init__(self):
        config = ConfigurationManager().get_model_evaluation_config()
        model_path = config.model_path
        self.model = joblib.load(Path(model_path))

    def predict(self, data):
        prediction = self.model.predict(data)
        return prediction