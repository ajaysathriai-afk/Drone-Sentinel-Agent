from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database import get_db
from app.models import Incident

router = APIRouter()

@router.get("/")
def get_zone_analytics(db: Session = Depends(get_db)):
    results = (
        db.query(Incident.zone, func.count(Incident.id).label("count"))
        .filter(Incident.zone != None)
        .group_by(Incident.zone)
        .all()
    )
    return [{"zone": zone, "count": count} for zone, count in results]

@router.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    from app.models import Alert
    incident_count = db.query(func.count(Incident.id)).scalar()
    alert_count = db.query(func.count(Alert.id)).scalar()
    
    latest = (
        db.query(Incident.threat_level)
        .order_by(Incident.id.desc())
        .first()
    )
    threat = latest[0] if latest else "LOW"
    
    return {
        "incidents": incident_count,
        "alerts": alert_count,
        "threat_level": threat
    }
