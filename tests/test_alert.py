from src.models.alert import (
    Alert,
    AlertMetadata,
    EventInfo,
    NetworkInfo,
)

alert = Alert(
    metadata=AlertMetadata(
        alert_id="ALT-1001",
        alert_name="Brute Force",
        severity="High",
        timestamp="2026-07-08T12:00:00",
    ),
    network=NetworkInfo(
        source_ip="10.10.10.5",
        destination_ip="8.8.8.8",
        protocol="TCP",
    ),
    event=EventInfo(
        username="admin",
        hostname="DC-01",
        description="Multiple failed login attempts",
    ),
)

print(alert.model_dump())