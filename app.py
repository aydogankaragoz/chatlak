from flask import Flask, request
from models import db, Station, Measurement
import os

from flask import jsonify

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

db.init_app(app)

@app.route("/")
def main():

    return "Hello World!"

@app.route('/station', methods=['POST'])
def station():

    station = Station(request.form['name'],
                      request.form['lat'],
                      request.form['lng'])
    
    db.session.add(station)
    db.session.commit()

    return jsonify(Station.query.get(station.id).json())

@app.route("/stations")
def stations():
    stations = Station.query.all()
    return jsonify([station.json() for station in stations])

@app.route('/measurement', methods=['POST'])
def measurement():

    measurement = Measurement(request.form['sensor_id'],
                              request.form['temprature'],
                              request.form['humidity'],
                              request.form['distance'])
    
    db.session.add(measurement)
    db.session.commit()

    return jsonify(Measurement.query.get(measurement.id).json())

@app.route("/measurements")
def measurements():
    measurements = Measurement.query.all()
    return jsonify([measurement.json() for measurement in measurements])

if __name__ == '__main__':
    app.run()
