from datetime import datetime
from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class AlertMetadata(BaseModel):
    """Basic alert information."""

    alert_id: str = Field(..., description="Unique alert identifier")
    alert_name: str = Field(..., description="Alert name")
    severity: str = Field(..., description="Alert severity")
    timestamp: datetime = Field(..., description="Alert timestamp")


class NetworkInfo(BaseModel):
    """Network-related information."""

    source_ip: Optional[str] = None
    destination_ip: Optional[str] = None
    source_port: Optional[int] = None
    destination_port: Optional[int] = None
    protocol: Optional[str] = None


class EventInfo(BaseModel):
    """Event-related information."""

    username: Optional[str] = None
    hostname: Optional[str] = None
    description: Optional[str] = None
    process_name: Optional[str] = None
    file_hash: Optional[str] = None


class Alert(BaseModel):
    """Complete Seceon alert."""

    metadata: AlertMetadata

    network: NetworkInfo = NetworkInfo()

    event: EventInfo = EventInfo()

    raw_data: Dict[str, Any] = Field(default_factory=dict)