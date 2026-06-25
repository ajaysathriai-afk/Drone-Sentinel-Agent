from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Incident

router = APIRouter()

@router.get("/")
def get_incidents(
    db: Session = Depends(get_db)
):
    incidents = db.query(
        Incident
    ).all()

    return [
        {
            "id": incident.id,
            "timestamp": incident.timestamp,
            "event": incident.event,
        }
        for incident in incidents
    ]
