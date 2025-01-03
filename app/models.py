from app import db
from datetime import datetime

class Flight(db.Model):
    __tablename__ = 'flight'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    date = db.Column(db.Date, nullable=False)
    takeoff_time = db.Column(db.Time, nullable=False)
    landing_time = db.Column(db.Time)
    duration = db.Column(db.Integer)  # minutes
    takeoff_location = db.Column(db.String(100), nullable=False)
    landing_location = db.Column(db.String(100), nullable=False)
    takeoff_altitude = db.Column(db.Float)  # meters
    max_altitude = db.Column(db.Float)  # meters
    distance_covered = db.Column(db.Float)  # kilometers
    temperature = db.Column(db.Integer)  # celsius
    wind_speed = db.Column(db.Float)  # km/h
    wind_direction = db.Column(db.String(50))
    weather_conditions = db.Column(db.Text)
    equipment_used = db.Column(db.String(200))
    notes = db.Column(db.Text)
    gps_track = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def distance(self):
        return self.distance_covered

    def __repr__(self):
        return f'<Flight {self.date} from {self.takeoff_location}>'

    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date.isoformat() if self.date else None,
            'takeoff_time': self.takeoff_time.isoformat() if self.takeoff_time else None,
            'landing_time': self.landing_time.isoformat() if self.landing_time else None,
            'duration': self.duration,
            'takeoff_location': self.takeoff_location,
            'landing_location': self.landing_location,
            'takeoff_altitude': self.takeoff_altitude,
            'max_altitude': self.max_altitude,
            'distance_covered': self.distance_covered,
            'temperature': self.temperature,
            'wind_speed': self.wind_speed,
            'wind_direction': self.wind_direction,
            'weather_conditions': self.weather_conditions,
            'equipment_used': self.equipment_used,
            'notes': self.notes,
            'gps_track': self.gps_track,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }