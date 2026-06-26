from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db
from app.models import Incident, Alert

router = APIRouter()


@router.get("/")
def get_zone_analytics(
    db: Session = Depends(get_db)
):

    results = (
        db.query(
            Incident.zone,
            func.count(Incident.id).label("count")
        )
        .group_by(Incident.zone)
        .all()
    )

    return [
        {
            "zone": zone or "Unknown",
            "count": count,
        }
        for zone, count in results
    ]


@router.get("/stats")
def get_stats(
    db: Session = Depends(get_db)
):

    incidents = db.query(
        func.count(Incident.id)
    ).scalar() or 0

    alerts = db.query(
        func.count(Alert.id)
    ).scalar() or 0

    high = db.query(
        func.count(Incident.id)
    ).filter(
        Incident.threat_level == "HIGH"
    ).scalar() or 0

    medium = db.query(
        func.count(Incident.id)
    ).filter(
        Incident.threat_level == "MEDIUM"
    ).scalar() or 0

    low = db.query(
        func.count(Incident.id)
    ).filter(
        Incident.threat_level == "LOW"
    ).scalar() or 0

    zones = db.query(
        func.count(
            func.distinct(
                Incident.zone
            )
        )
    ).scalar() or 0

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

        "incidents": incidents,

        "alerts": alerts,

        "threat_level": threat,

        "high": high,

        "medium": medium,

        "low": low,

        "zones": zones,

    }