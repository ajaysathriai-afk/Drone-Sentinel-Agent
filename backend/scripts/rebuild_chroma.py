from app.database import SessionLocal
from app.models import Incident

from app.vectorstore.chroma_db import (
    collection
)

db = SessionLocal()

incidents = db.query(
    Incident
).all()

for incident in incidents:

    collection.add(
        documents=[
            incident.event
        ],
        ids=[
            str(incident.id)
        ]
    )

print(
    f"Indexed {len(incidents)} incidents"
)

db.close()
