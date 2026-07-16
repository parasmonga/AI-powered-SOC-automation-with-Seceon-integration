from src.models.alert import Alert
from src.utils.logger import get_logger

logger = get_logger("MITRE")


class MitreMapper:

    """
    Maps alerts to MITRE ATT&CK techniques.
    """

    def __init__(self):

        self.rules = {

            "powershell": {
                "technique": "PowerShell",
                "technique_id": "T1059.001",
                "tactic": "Execution"
            },

            "cmd": {
                "technique": "Command Shell",
                "technique_id": "T1059.003",
                "tactic": "Execution"
            },

            "brute force": {
                "technique": "Brute Force",
                "technique_id": "T1110",
                "tactic": "Credential Access"
            },

            "rdp": {
                "technique": "Remote Services",
                "technique_id": "T1021.001",
                "tactic": "Lateral Movement"
            },

            "mimikatz": {
                "technique": "Credential Dumping",
                "technique_id": "T1003",
                "tactic": "Credential Access"
            }

        }

    def map(self, alert: Alert):

        logger.info("Mapping MITRE ATT&CK...")

        text = (
            alert.metadata.alert_name + " " +
            (alert.event.description or "")
        ).lower()

        for keyword, value in self.rules.items():

            if keyword in text:

                logger.info(
                    f"Matched MITRE {value['technique_id']}"
                )

                return value

        logger.info("No MITRE technique matched.")

        return {
            "technique": "Unknown",
            "technique_id": "Unknown",
            "tactic": "Unknown"
        }