from src.ml.predictor import RiskPredictor
from src.utils.logger import get_logger

logger = get_logger("DECISION")


class DecisionEngine:

    def __init__(self):

        self.predictor = RiskPredictor()

    def decide(self, features: dict):

        logger.info("Running XGBoost prediction...")

        result = self.predictor.predict(features)

        probability = result["probability"]

        risk_score = round(probability * 100)

        if risk_score >= 80:
            decision = "Escalate"

        elif risk_score >= 50:
            decision = "Investigate"

        else:
            decision = "Close"

        logger.info(
            f"Risk Score={risk_score}, Decision={decision}"
        )

        return {

            "prediction": result["prediction"],

            "probability": probability,

            "risk_score": risk_score,

            "decision": decision

        }