from src.ml.predictor import RiskPredictor

predictor = RiskPredictor()

features = {

    "severity_score": 3,

    "source_private": 1,

    "is_tcp": 1,

    "privileged_user": 1,

    "powershell_detected": 1,

    "blacklisted": 0,

    "mitre_match": 1

}

print(
    predictor.predict(features)
)