from src.parser.parser import AlertParser
from src.features.feature_engineering import FeatureEngineer

parser = AlertParser()
engineer = FeatureEngineer()

sample_alert = {
    "alert_id": "ALT-101",
    "alert_name": "PowerShell Execution",
    "severity": "High",
    "timestamp": "2026-07-08T15:00:00",
    "source_ip": "192.168.10.5",
    "destination_ip": "8.8.8.8",
    "protocol": "TCP",
    "username": "administrator",
    "hostname": "SERVER-01",
    "description": "Suspicious PowerShell execution"
}

alert = parser.parse(sample_alert)

features = engineer.extract(alert)

print(features)