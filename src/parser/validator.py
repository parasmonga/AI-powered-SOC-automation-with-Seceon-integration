import ipaddress

from src.models.alert import Alert
from src.utils.logger import get_logger

logger = get_logger("VALIDATOR")


class AlertValidator:
    """
    Validates Alert objects before processing.
    """

    VALID_SEVERITIES = {
        "Low",
        "Medium",
        "High",
        "Critical",
    }

    def validate(self, alert: Alert) -> bool:

        logger.info("Validating alert...")

        # Validate severity
        if alert.metadata.severity not in self.VALID_SEVERITIES:
            logger.error(
                f"Invalid severity: {alert.metadata.severity}"
            )
            return False

        # Validate source IP
        if alert.network.source_ip:
            try:
                ipaddress.ip_address(alert.network.source_ip)
            except ValueError:
                logger.error(
                    f"Invalid source IP: {alert.network.source_ip}"
                )
                return False

        # Validate destination IP
        if alert.network.destination_ip:
            try:
                ipaddress.ip_address(alert.network.destination_ip)
            except ValueError:
                logger.error(
                    f"Invalid destination IP: {alert.network.destination_ip}"
                )
                return False

        logger.info("Alert validation successful.")

        return True