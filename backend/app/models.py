from sqlalchemy import Column, Integer, String, Text
from app.database import Base


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)

    image_name = Column(String, nullable=False)

    timestamp = Column(String)

    event = Column(Text)

    detected_objects = Column(Text)

    threat_level = Column(String)

    zone = Column(String, default="Unknown")


class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)

    severity = Column(String)

    message = Column(Text)
