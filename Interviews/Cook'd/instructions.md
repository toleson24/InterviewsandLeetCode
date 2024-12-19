# Add Event Model and API Endpoint

This PR implements a new endpoint for discovering nearby in-person events based on user location. The feature aims to encourage spontaneous real-world meetups by showing events happening within walking distance (<=1 mile radius).

## Context

Average response time: 2.3s (target <500ms)  
Active daily events: ~5000 across major cities  
Peak usage: 6-8 PM local time  
Mobile usage: 95% of requests  
Battery drain complaints: 32% of recent support tickets  

## Recent User Feedback

"Battery dies quickly when looking for events"  
"Shows events that already started"  
"Sometimes diesplays events 5+ miles away"  
"Same events keep showing up even after I've declined them"  

## Changes: 

Add FastAPI endpoint for proximity-based event discovery  
Implement PostGIS spatial  queries  
Add Redis caching layer  
Handle real-time event capacity updates  

## Performance Requirements  

Max response time: 500ms  
Battery impact: <5% per hour  
Location accuracy: +-100m  
Support 100 concurrent requests/second  
Real-time capacity updates  

## Instructions

Welcome to the bug bash, try to catch all the bugs before times runs out!  

You can catdh bugs by leaving comments calling  out the fauly behavior.  

As you catch bugs you'll get points for each one. The more bugs you catch, the more points you get!  

## Time

30:00 minutes  

