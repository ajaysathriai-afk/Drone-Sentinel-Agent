from sqlalchemy import func

from app.database import SessionLocal
from app.models import Incident


def sql_investigate(question: str):

    db = SessionLocal()

    q = question.lower()

    # Which zone had the most incidents?
    if "zone" in q and "most" in q:

        result = (
            db.query(
                Incident.zone,
                func.count(Incident.id)
            )
            .group_by(Incident.zone)
            .order_by(
                func.count(Incident.id).desc()
            )
            .first()
        )

        db.close()

        if result:
            return (
                f"The zone with the most incidents is "
                f"{result[0]} "
                f"with {result[1]} incidents."
            )

        return "No incidents found."

    # Summarize parking incidents
    if "parking" in q:

        incidents = (
            db.query(Incident)
            .filter(
                Incident.zone == "Parking"
            )
            .all()
        )

        db.close()

        if not incidents:
            return "No parking incidents found."

        summary = []

        for incident in incidents:

            summary.append(
                f"- {incident.timestamp}: "
                f"{incident.event} "
                f"({incident.threat_level})"
            )

        return "\n".join(summary)

    db.close()

    return "SQL agent could not answer this question."
