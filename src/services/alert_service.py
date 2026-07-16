from src.parser.parser import AlertParser
from src.parser.validator import AlertValidator

from src.features.feature_engineering import FeatureEngineer
from src.mitre.mapper import MitreMapper
from src.threat_intel.reputation import ThreatIntel

from src.decision.engine import DecisionEngine
from src.llm.explainer import AlertExplainer

from src.utils.logger import get_logger

import traceback

logger = get_logger("SERVICE")


class AlertProcessingService:

    def __init__(self):

        self.parser = AlertParser()

        self.validator = AlertValidator()

        self.features = FeatureEngineer()

        self.mitre = MitreMapper()

        self.threat = ThreatIntel()

        self.decision = DecisionEngine()

        self.explainer = AlertExplainer()

    def process(self, raw_alert: dict):

        try:

            logger.info("Received new alert.")

            # Parse Alert
            alert = self.parser.parse(raw_alert)

            # Validate Alert
            if not self.validator.validate(alert):

                logger.error("Alert validation failed.")

                return {
                    "status": "failed",
                    "reason": "Validation Failed"
                }

            logger.info("Alert validation successful.")

            # Feature Engineering
            features = self.features.extract(alert)

            # MITRE Mapping
            mitre = self.mitre.map(alert)

            # Threat Intelligence
            threat = self.threat.lookup(
                alert.network.source_ip
            )

            # Add ML Features
            features["blacklisted"] = int(
                threat["blacklisted"]
            )

            features["mitre_match"] = int(
                mitre["technique_id"] != "Unknown"
            )

            # AI Decision
            decision = self.decision.decide(
                features
            )

            # AI Explanation
            explanation = self.explainer.explain(
                alert=alert,
                features=features,
                mitre=mitre,
                threat=threat,
                decision=decision
            )

            logger.info("Alert processed successfully.")

            return {

                "status": "success",

                "alert": alert.model_dump(),

                "features": features,

                "mitre": mitre,

                "threat": threat,

                "decision": decision,

                "explanation": explanation

            }

        except Exception as e:

            traceback.print_exc()

            logger.exception("Alert Processing Failed")

            return {

                "status": "error",

                "message": str(e)

            }