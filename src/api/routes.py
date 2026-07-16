from fastapi import APIRouter
from src.services.alert_service import AlertProcessingService

router = APIRouter()

service = AlertProcessingService()


@router.get("/")
def home():
    return {"message": "AI SOC Decision Engine Running"}


@router.post("/alerts")
def receive_alert(alert: dict):
    return service.process(alert)