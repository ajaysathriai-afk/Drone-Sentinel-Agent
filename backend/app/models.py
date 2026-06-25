from sqlalchemy import Column, Integer, String
from app.database import Base


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(String)
    event = Column(String)
    zone = Column(String, default="Unknown")
    threat_level = Column(String, default="LOW")


class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    severity = Column(String)
    message = Column(String)
