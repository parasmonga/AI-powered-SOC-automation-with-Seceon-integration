from src.models.alert import (
    Alert,
    AlertMetadata,
    NetworkInfo,
    EventInfo,
)

from src.utils.logger import get_logger

logger = get_logger("PARSER")


class AlertParser:
    """
    Converts raw Seceon JSON into an Alert object.
    """

    def parse(self, data: dict) -> Alert:

        logger.info("Parsing incoming alert...")

        alert = Alert(

            metadata=AlertMetadata(
                alert_id=data.get("alert_id", "UNKNOWN"),
                alert_name=data.get("alert_name", "Unknown Alert"),
                severity=data.get("severity", "Low"),
                timestamp=data.get("timestamp"),
            ),

            network=NetworkInfo(
                source_ip=data.get("source_ip"),
                destination_ip=data.get("destination_ip"),
                source_port=data.get("source_port"),
                destination_port=data.get("destination_port"),
                protocol=data.get("protocol"),
            ),

            event=EventInfo(
                username=data.get("username"),
                hostname=data.get("hostname"),
                description=data.get("description"),
                process_name=data.get("process_name"),
                file_hash=data.get("file_hash"),
            ),

            raw_data=data,
        )

        logger.info("Alert parsed successfully.")

        return alert