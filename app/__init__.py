from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(app.config.from_object(config['development']))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coordinate.db'
db = SQLAlchemy(app)

from app import views, models
db.create_all()
