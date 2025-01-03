from app import create_app, db
from app.models import Flight
from datetime import datetime, time

def test_create_flight():
    app = create_app()
    
    with app.app_context():
        # Create test flight
        new_flight = Flight(
            date=datetime.now().date(),
            start_time=time(10, 30),
            end_time=time(11, 45),
            duration=75,
            takeoff_location="Monte Test",
            landing_location="Valle Test",
            max_altitude=1200.5,
            distance_covered=15.3,
            temperature=22,
            wind_speed=12.5,
            wind_direction="NE",
            weather_conditions="Sunny, light clouds",
            equipment_used="Test Wing v1",
            notes="Test flight"
        )
        
        # Save to database
        db.session.add(new_flight)
        db.session.commit()
        
        # Query and verify
        flight = Flight.query.first()
        print(f"Created flight: {flight.to_dict()}")
        
        # Clean up
        db.session.delete(flight)
        db.session.commit()

if __name__ == "__main__":
    test_create_flight()