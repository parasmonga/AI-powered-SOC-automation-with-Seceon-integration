from src.parser.parser import AlertParser
from src.parser.validator import AlertValidator

parser = AlertParser()
validator = AlertValidator()

sample_alert = {

    "alert_id": "ALT-101",

    "alert_name": "Brute Force",

    "severity": "High",

    "timestamp": "2026-07-08T15:00:00",

    "source_ip": "10.10.10.5",

    "destination_ip": "8.8.8.8",

    "protocol": "TCP",

    "username": "admin",

    "hostname": "DC-01",

    "description": "Multiple failed logins"

}

alert = parser.parse(sample_alert)

print(validator.validate(alert))