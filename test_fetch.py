from src.services.seceon_client import SeceonClient

client = SeceonClient()

alerts = client.fetch_alerts()

print(type(alerts))

print(alerts)