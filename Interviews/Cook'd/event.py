from sqlalchemy import Column, Integer, String, DateTime, Float
from geoalchemy2 import Geography
from app.db.base_class import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    creator_id = Column(String, index=True)
    capacity = Column(Integer)
    start_time = Column(DateTime, index=True)
    location = Column(Geography(geometry_type='POINT', srid=4326))
    lat = Column(Float)
    lng = Column(Float)

