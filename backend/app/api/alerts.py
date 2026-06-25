from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Alert

router = APIRouter()

@router.get("/")
def get_alerts(
    db: Session = Depends(get_db)
):
    alerts = db.query(Alert).all()

    return [
        {
            "id": alert.id,
            "severity": alert.severity,
            "message": alert.message,
        }
        for alert in alerts
    ]
