from typing import TypedDict

class DroneState(TypedDict):
    image_bytes: bytes
    image_path: str
    analysis: dict
    objects: list
    object_counts: dict
    risk_score: int
    threat_level: str
    summary: str
    alert_message: str
    incident_id: int
    zone: str
