import ipaddress

from src.utils.logger import get_logger

logger = get_logger("THREAT_INTEL")


class ThreatIntel:

    """
    Simple Threat Intelligence module.
    """

    BLACKLIST = {

        "185.220.101.15",
        "45.95.147.236",
        "103.25.59.200",
        "1.2.3.4"

    }

    def lookup(self, ip: str):

        logger.info(f"Checking reputation of {ip}")

        if not ip:

            return {
                "ip": None,
                "reputation": "Unknown",
                "blacklisted": False
            }

        obj = ipaddress.ip_address(ip)

        if obj.is_private:

            return {
                "ip": ip,
                "reputation": "Internal",
                "blacklisted": False
            }

        if ip in self.BLACKLIST:

            return {
                "ip": ip,
                "reputation": "Malicious",
                "blacklisted": True
            }

        return {
            "ip": ip,
            "reputation": "Trusted",
            "blacklisted": False
        }