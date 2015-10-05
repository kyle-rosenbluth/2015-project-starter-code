from app import db

class Coordinate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    notes = db.Column(db.String(250))

    def __init__(self, latitude, longitude, notes):
        self.latitude = latitude
        self.longitude = longitude
        self.notes = notes
