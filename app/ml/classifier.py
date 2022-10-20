import pickle
import pandas as pd
from xgboost import Booster, DMatrix

import warnings
warnings.filterwarnings('ignore')


class Classifier:
    def __init__(self, model_path='app/ml/phishing_model.json', scaler_path='app/ml/phishing_scaler.pkl'):
        self.model = Booster()
        self.model.load_model(model_path)
        with open(scaler_path, 'rb') as f:
            self.scaler = pickle.load(f)
    
    def predict(self, url_features: dict) -> dict:
        url_features = pd.DataFrame.from_dict(url_features)
        url_features_scaled = self.scaler.transform(url_features)
        pred = self.model.predict(DMatrix(url_features_scaled))
        return {
            "class": "phishing" if pred[0] >= 0.5 else "legit",
            "probabilities": {
                "legit": str(round(1 - pred[0], 4)),
                "phishing": str(round(pred[0], 4))
            }
        }

