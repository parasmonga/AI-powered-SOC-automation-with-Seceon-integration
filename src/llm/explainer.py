from src.utils.logger import get_logger

logger = get_logger("EXPLAINER")


class AlertExplainer:

    def explain(
        self,
        alert,
        features,
        mitre,
        threat,
        decision
    ):

        explanation = []

        explanation.append(
            f"Alert severity is {alert.metadata.severity}."
        )

        if features["powershell_detected"]:
            explanation.append(
                "PowerShell execution was detected."
            )

        if features["privileged_user"]:
            explanation.append(
                "A privileged account was involved."
            )

        if threat["blacklisted"]:
            explanation.append(
                "Source IP is blacklisted."
            )

        if mitre["technique_id"] != "Unknown":
            explanation.append(
                f"Activity matches MITRE ATT&CK {mitre['technique_id']} ({mitre['technique']})."
            )

        explanation.append(
            f"ML predicted {decision['probability']*100:.2f}% probability of malicious activity."
        )

        if decision["decision"] == "Escalate":
            explanation.append(
                "Recommendation: Escalate immediately to SOC analyst."
            )

        elif decision["decision"] == "Investigate":
            explanation.append(
                "Recommendation: Perform additional investigation."
            )

        else:
            explanation.append(
                "Recommendation: Alert can be closed."
            )

        logger.info("Explanation generated.")

        return explanation