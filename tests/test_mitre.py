from src.parser.parser import AlertParser
from src.mitre.mapper import MitreMapper

parser = AlertParser()
mapper = MitreMapper()

sample_alert = {

    "alert_id": "ALT-900",

    "alert_name": "PowerShell Execution",

    "severity": "High",

    "timestamp": "2026-07-08T18:00:00",

    "source_ip": "10.10.10.5",

    "destination_ip": "8.8.8.8",

    "protocol": "TCP",

    "username": "administrator",

    "hostname": "SERVER-01",

    "description": "Suspicious PowerShell execution"

}

alert = parser.parse(sample_alert)

print(mapper.map(alert))