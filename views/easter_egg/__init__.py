"""__init.py__ has responsibility of defining interfaces for blueprint"""
from flask import Blueprint
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, inspect

app = Flask(__name__)
app.config['SECRET_KEY'] = ':)'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eggers.sqlite3'
db = SQLAlchemy(app)

class Order(db.Model):
    OrderID = db.Column('student_id', db.Integer, primary_key = True)
    Time = db.Column(db.DateTime, primary_key=True)
    Price = db.Column(db.Integer, unique=False, nullable=False)
    Feedback = db.Column(db.String(200), unique=False)

class User(db.Model):

    __tablename__ = 'Customer'
    id = db.Column('student_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(50))
    grade = db.Column(db.Integer)

    def __repr__(self):
        return '<User {}>'.format(self.name)


db.create_all()


easter_egg_bp = Blueprint('easter_egg_bp',__name__,
          template_folder='templates',
          static_folder='static'
          )

from . import view #getting the rest of the routes into this file

