from flask import Flask, render_template, request, redirect, url_for, send_from_directory, current_app
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

# create a Flask instance
"Setting up the keys are needed for the database"
app = Flask(__name__)
#app.config['SECRET_KEY'] = ':)'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///models/items.sqlite3'
db = SQLAlchemy(app)

class items(db.Model):
    id = db.Column('item_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    type = db.Column(db.String(50))
    price = db.Column(db.String(200))

def __init__(self, id, name, type, price):
    self.name = name
    self.id = id
    self.type = type
    self.price = price

#db.create_all()


