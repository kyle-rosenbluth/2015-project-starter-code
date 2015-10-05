from app import app
from app import db
from models import Coordinate
from flask import request
from flask_restful import Api, Resource
api = Api(app)

@app.route('/', methods=['GET'])
def index():
    return 'Hello world!'

class Health(Resource):
    def get(self):
        return 'Ok', 200

api.add_resource(Health, '/health')

class Coordinates(Resource):
    def post(self):
        coordinates = request.json["coordinates"]
        for coordinate in coordinates:
            latitude = coordinate["latitude"]
            longitude = coordinate["longitude"]
            notes = coordinate["notes"]
            db.session.add(Coordinate(latitude, longitude, notes))
        db.session.commit()
        print Coordinate.query.all()
api.add_resource(Coordinates, '/coordinates')
