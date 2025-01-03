# app/routes.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Flight
from app import db
from datetime import datetime
from collections import defaultdict

# Crear el Blueprint
bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/records')
def flight_records():
    flights = Flight.query.order_by(Flight.date.desc()).all()
    return render_template('flight_records.html', flights=flights)

@bp.route('/flight/new', methods=['GET', 'POST'])
def new_flight():
    if request.method == 'POST':
        flight = Flight(
            title=request.form['title'],
            date=datetime.strptime(request.form['date'], '%Y-%m-%d'),
            takeoff_time=datetime.strptime(request.form['takeoff_time'], '%H:%M').time(),
            landing_time=datetime.strptime(request.form['landing_time'], '%H:%M').time(),
            duration=int(request.form['duration']) if request.form['duration'] else None,
            takeoff_location=request.form['takeoff_location'],
            landing_location=request.form['landing_location'],
            takeoff_altitude=float(request.form['takeoff_altitude']),
            max_altitude=float(request.form['max_altitude']),
            distance_covered=float(request.form['distance_covered']),
            temperature=int(request.form['temperature']) if request.form['temperature'] else None,
            wind_speed=float(request.form['wind_speed']) if request.form['wind_speed'] else None,
            wind_direction=request.form['wind_direction'],
            weather_conditions=request.form['weather_conditions'],
            equipment_used=request.form['equipment_used'],
            notes=request.form['notes'],
            gps_track=request.form['gps_track']
        )
        db.session.add(flight)
        db.session.commit()
        flash('Flight successfully recorded!', 'success')
        return redirect(url_for('main.index'))
    return render_template('new_flight.html')

@bp.route('/flight/<int:id>')
def flight_detail(id):
    flight = Flight.query.get_or_404(id)
    return render_template('flight_detail.html', flight=flight)

@bp.route('/flight/<int:id>/edit', methods=['GET', 'POST'])
def edit_flight(id):
    flight = Flight.query.get_or_404(id)
    if request.method == 'POST':
        flight.title = request.form['title']
        flight.date = datetime.strptime(request.form['date'], '%Y-%m-%d')
        flight.takeoff_time = datetime.strptime(request.form['takeoff_time'], '%H:%M').time()
        flight.landing_time = datetime.strptime(request.form['landing_time'], '%H:%M').time()
        flight.duration = int(request.form['duration']) if request.form['duration'] else None
        flight.takeoff_location = request.form['takeoff_location']
        flight.landing_location = request.form['landing_location']
        flight.takeoff_altitude = float(request.form['takeoff_altitude'])
        flight.max_altitude = float(request.form['max_altitude'])
        flight.distance_covered = float(request.form['distance_covered'])
        flight.temperature = int(request.form['temperature']) if request.form['temperature'] else None
        flight.wind_speed = float(request.form['wind_speed']) if request.form['wind_speed'] else None
        flight.wind_direction = request.form['wind_direction']
        flight.weather_conditions = request.form['weather_conditions']
        flight.equipment_used = request.form['equipment_used']
        flight.notes = request.form['notes']
        flight.gps_track = request.form['gps_track']
        
        db.session.commit()
        flash('Flight successfully updated!', 'success')
        return redirect(url_for('main.flight_detail', id=flight.id))
    return render_template('edit_flight.html', flight=flight)

@bp.route('/flight/<int:id>/delete', methods=['POST'])
def delete_flight(id):
    flight = Flight.query.get_or_404(id)
    db.session.delete(flight)
    db.session.commit()
    flash('Flight successfully deleted!', 'success')
    return redirect(url_for('main.index'))

@bp.route('/stats')
def stats():
    flights = Flight.query.all()
    total_flights = len(flights)
    
    if total_flights > 0:
        # Totales
        total_distance = sum(flight.distance_covered for flight in flights)
        total_duration = sum(flight.duration for flight in flights)
        max_altitude = max(flight.max_altitude for flight in flights)
        
        # Acumulados (media de los totales)
        cumulative_distance = total_distance / total_flights
        cumulative_duration = total_duration / total_flights
        cumulative_altitude = sum(flight.max_altitude for flight in flights) / total_flights
        
        stats = {
            'total_flights': total_flights,
            'total_distance': total_distance,
            'total_duration': total_duration,
            'max_altitude': max_altitude,
            'cumulative_distance': cumulative_distance,
            'cumulative_duration': cumulative_duration,
            'cumulative_altitude': cumulative_altitude
        }
    else:
        stats = {
            'total_flights': 0,
            'total_distance': 0,
            'total_duration': 0,
            'max_altitude': 0,
            'cumulative_distance': 0,
            'cumulative_duration': 0,
            'cumulative_altitude': 0
        }
    
    return render_template('stats.html', stats=stats)

@bp.route('/advanced-stats')
def advanced_stats():
    flights = Flight.query.order_by(Flight.date).all()
    
    dates = []
    durations = []
    distance_altitude = []
    
    for flight in flights:
        # Datos para la tendencia de duración
        dates.append(flight.date.strftime('%Y-%m-%d'))
        durations.append(flight.duration)
        
        # Datos de distancia vs altitud
        distance_altitude.append({
            'x': flight.distance_covered,
            'y': flight.max_altitude
        })
    
    flight_data = {
        'dates': dates,
        'durations': durations,
        'distance_altitude': distance_altitude
    }
    
    return render_template('advanced_stats.html', flight_data=flight_data)

@bp.route('/guide')
def guide():
    return render_template('guide.html')