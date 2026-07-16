from src.services.alert_service import AlertProcessingService

service = AlertProcessingService()

sample_alert = {
    "alert_id": "ALT-500",
    "alert_name": "PowerShell Execution",
    "severity": "High",
    "timestamp": "2026-07-08T16:00:00",
    "source_ip": "192.168.1.5",
    "destination_ip": "8.8.8.8",
    "protocol": "TCP",
    "username": "administrator",
    "hostname": "SERVER-01",
    "description": "Suspicious PowerShell command"
}

result = service.process(sample_alert)

print(result)