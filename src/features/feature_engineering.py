import ipaddress

from src.models.alert import Alert
from src.utils.logger import get_logger

logger = get_logger("FEATURES")


class FeatureEngineer:
    """
    Extracts ML-ready features from an Alert object.
    """

    SEVERITY_MAP = {
        "Low": 1,
        "Medium": 2,
        "High": 3,
        "Critical": 4,
    }

    def extract(self, alert: Alert) -> dict:

        logger.info("Extracting alert features...")

        features = {}

        # Severity
        features["severity_score"] = self.SEVERITY_MAP.get(
            alert.metadata.severity,
            0
        )

        # Source IP
        if alert.network.source_ip:
            ip = ipaddress.ip_address(alert.network.source_ip)
            features["source_private"] = int(ip.is_private)
        else:
            features["source_private"] = 0

        # Destination IP
        if alert.network.destination_ip:
            ip = ipaddress.ip_address(alert.network.destination_ip)
            features["destination_private"] = int(ip.is_private)
        else:
            features["destination_private"] = 0

        # Protocol
        protocol = (alert.network.protocol or "").upper()

        features["is_tcp"] = int(protocol == "TCP")
        features["is_udp"] = int(protocol == "UDP")

        # Privileged user
        username = (alert.event.username or "").lower()

        features["privileged_user"] = int(
            username in {
                "administrator",
                "admin",
                "root"
            }
        )

        # PowerShell keyword
        description = (alert.event.description or "").lower()

        features["powershell_detected"] = int(
            "powershell" in description
        )

        logger.info("Feature extraction completed.")

        return features