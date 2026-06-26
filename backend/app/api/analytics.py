from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db
from app.models import Incident, Alert

router = APIRouter()


@router.get("/")
def get_zone_analytics(db: Session = Depends(get_db)):

    results = (
        db.query(
            Incident.zone,
            func.count(Incident.id).label("count")
        )
        .filter(Incident.zone != None)
        .group_by(Incident.zone)
        .all()
    )

    return [
        {
            "zone": zone,
            "count": count,
        }
        for zone, count in results
    ]


@router.get("/stats")
def get_stats(db: Session = Depends(get_db)):

    incident_count = db.query(
        func.count(Incident.id)
    ).scalar()

    alert_count = db.query(
        func.count(Alert.id)
    ).scalar()

    high = (
        db.query(func.count(Incident.id))
        .filter(
            Incident.threat_level == "HIGH"
        )
        .scalar()
    )

    medium = (
        db.query(func.count(Incident.id))
        .filter(
            Incident.threat_level == "MEDIUM"
        )
        .scalar()
    )

    low = (
        db.query(func.count(Incident.id))
        .filter(
            Incident.threat_level == "LOW"
        )
        .scalar()
    )

    zones = db.query(
        func.count(
            func.distinct(
                Incident.zone
            )
        )
    ).scalar()

    latest = (
        db.query(
            Incident.threat_level
        )
        .order_by(
            Incident.id.desc()
        )
        .first()
    )

    threat = latest[0] if latest else "LOW"

    return {

        "incidents": incident_count,

        "alerts": alert_count,

        "high": high,

        "medium": medium,

        "low": low,

        "zones": zones,

        "threat_level": threat,
    }