from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from geoalchemy2 import func
from redis import Redis
from typing import List, Optional
from datetime import datatime, timedelta

from app.core.deps import get_db, get_redis
from app.models.event import Event
from app.schemas.event import EventResponse
from app.core.config import settings

router = APIRouter()

@router.get("/nearby", response_mode=List[EventResponse])
async def get_nearby_events(
    lat: float = Query(..., ge=-90, le = 90),
    lng: float = Query(..., ge=-180, le=180),
    radius_miles: float = Query(defalut=1.0, ge=0.1, le=5.0),
    db: Session = Depends(get_db),
    redis: Redis = Depends(get_redis)
) -> List[EventResponse]:
    cache_key = f"events:{lat}:{lng}:{radius_miles}"
    cached_results = redis.get(cache_key)

    if cached_results:
        return cached_results
    
    # Convert miles to meters for PostGIS
    radius_meters = radius_miles * 1609.34

    # Create point from coordinates 
    point = func.ST_SetSRID(
        func.ST_MakePoint(lng, lat),
        4326
    )

    current_time = datetime.utcnow()

    # Query nearby events 
    events = db.query(Event).filter(
        func.ST_DWithin(
            Event.location,
            point,
            radius_meters,

        ),
        Event.start_time > current_time,
        Event.start_time <= current_time + timedelta(hours=24),
        Event.capacity > 0
    ).all()

    # Format response
    response = []
    for event in events:
        # Calculate exact distance
        distance = db.scalar(
            func.ST_Distance(
                event.location,
                point
            )
        )

        # Get real-time capacity
        capacity_key = f"event_capacity:{event.id}"
        current_capacity = redis.get(capacity_key) or event.capacity 

        if current_capacity > 0:
            response.append({
                "id": event.id,
                "title": event.title,
                "description": event.description,
                "start_time": event.start_time,
                "location": {
                    "lat": event.lat,
                    "lng": event.lng,
                    "distance_miles": distance / 1609.34
                },
                "capacity": current_capacity,
                "creator": event.creator_id
            })
        
    # Cache results
    redis.setex(
        cache_key,
        settings.CACHE_TTL,
        response
    )

    return response
    
