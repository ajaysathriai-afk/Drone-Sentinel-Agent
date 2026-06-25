from app.database import SessionLocal
from app.models import Incident


def get_recent_incidents(limit=5):

    db = SessionLocal()

    incidents = (
        db.query(Incident)
        .order_by(Incident.id.desc())
        .limit(limit)
        .all()
    )

    db.close()

    return incidents


def count_incidents():

    db = SessionLocal()

    count = (
        db.query(Incident)
        .count()
    )

    db.close()

    return count


def latest_incident():

    db = SessionLocal()

    incident = (
        db.query(Incident)
        .order_by(Incident.id.desc())
        .first()
    )

    db.close()

    return incident
