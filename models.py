from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True

    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        """Define a base way to print models"""
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })

    def json(self):
        """
                Define a base way to jsonify models, dealing with datetime objects
        """
        return {
            column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
            for column, value in self._to_dict().items()
        }


class Station(BaseModel, db.Model):
    """Model for the stations table"""
    __tablename__ = 'stations'

    id = db.Column(db.Integer, primary_key = True)
    createdAt = db.Column(db.DateTime, server_default=db.func.now())
    name = db.Column(db.String(100))
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)

    def __init__(self, name, lat, lng):
        self.name = name
        self.lat = lat
        self.lng = lng

    def _to_dict(self):
        return {'id' : self.id,
                'lat' : self.lat, 
                'lng' : self.lng,
                'name' : self.name,
                'createdAt' : self.createdAt}

class Measurement(BaseModel, db.Model):
    """Model for the stations table"""
    __tablename__ = 'measurements'

    id = db.Column(db.Integer, primary_key = True)
    createdAt = db.Column(db.DateTime, server_default=db.func.now())
    sensor_id = db.Column(db.Integer)
    temprature = db.Column(db.Float)
    humidity = db.Column(db.Float)
    distance = db.Column(db.Float)

    def __init__(self, sensor_id, temprature, humidity, distance):
        self.sensor_id = sensor_id
        self.temprature = temprature
        self.humidity = humidity
        self.distance = distance

    def _to_dict(self):
        return {'id' : self.id,
                'sensor_id' : self.sensor_id,
                'temprature' : self.temprature,
                'humidity' : self.humidity,
                'distance' : self.distance,
                'createdAt' : self.createdAt} 