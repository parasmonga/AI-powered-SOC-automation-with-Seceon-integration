import joblib

model = joblib.load(
    "src/ml/models/xgboost_model.pkl"
)


class RiskPredictor:

    def predict(self, features: dict):

        X = [[

            features["severity_score"],

            features["source_private"],

            features["is_tcp"],

            features["privileged_user"],

            features["powershell_detected"],

            features["blacklisted"],

            features["mitre_match"]

        ]]

        prediction = model.predict(X)[0]

        probability = model.predict_proba(X)[0][1]

        return {

            "prediction": int(prediction),

            "probability": float(probability)

        }