# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import FileField, PasswordField
from wtforms import StringField
from wtforms.validators import InputRequired, Length, Email
from views.makeup_api import makeup_api_bp  # blueprint not a module
from views.easter_egg import easter_egg_bp
from views.database_items import database_items_bp
from views.easter_egg_college import easter_egg_college_bp
from views.time_to_thrift import time_to_thrift_bp
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import json

from models import thriftythreadsdata, barbarelladata, contactimages, websitecards
from app import app

# create a Flask instance
"Setting up the keys are needed for the database"

app.config['SECRET_KEY'] = ':)'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///UsersTT.db'
Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
records = []
shopping_cart = [] #list to append values for each item to display on the user dashboard
window_y_value = 0
#print(window_y_value)

class UserTT(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50))
    password = db.Column(db.String(80))
    shopping_cart_column = db.Column(db.String(8000))

@login_manager.user_loader
def load_user(user_id):
    return UserTT.query.get(int(user_id))

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

class UserDN(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, user_id, username, email, password):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"{self.user_id},{self.username}, {self.email}, {self.password}"

class OrderEE(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=True)
    price = db.Column(db.Integer, unique=False, nullable=False)
    order_contents = db.Column(db.String(1000), unique=False, nullable=False)
    time = db.Column(db.DateTime, primary_key=True)

    def __init__(self, user_id, price, order_contents, time):
        self.user_id = user_id
        self.price = price
        self.order_contents = order_contents
        self.time = time

    def __repr__(self):
        return f"{self.user_id},{self.price}, {self.order_contents}, {self.time}"
"Create Database"
db.create_all()

"Initialize the form that will retrieve data from the HTML page,flaskwtf form"

class ItemForm(FlaskForm):
    name = StringField('name', validators=[InputRequired(), Length(min=1, max=15)])
    type = StringField('type', validators=[InputRequired(), Length(min=1, max=80)])
    price = StringField('price', validators=[InputRequired()])
    image = FileField('image', validators=[FileRequired(),FileAllowed(['png', 'pdf', 'jpg'], "Nerd")])

class LoginForm(FlaskForm):
    username = StringField('username',validators=[InputRequired(), Length(min=1,max=15)])
    password = PasswordField('password',validators=[InputRequired(), Length(min=1,max=80)])
    email = StringField('email',validator=[InputRequired(), Length(min = 1, max = 100)])

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid Email'),Length(max=50)])
    username = StringField('username',validators=[InputRequired(), Length(min=4,max=15)])
    password = PasswordField('password',validators=[InputRequired(), Length(min=8,max=80)])

"""Defining routes"""
app.register_blueprint(makeup_api_bp, url_prefix='/makeup_api')
app.register_blueprint(easter_egg_bp, url_prefix='/easter_egg')
app.register_blueprint(database_items_bp, url_prefix='/database_items')
app.register_blueprint(easter_egg_college_bp, url_prefix='/easter_egg_college')
app.register_blueprint(easter_egg_college_bp, url_prefix='/time_to_thrift')


#  displaying all the current items in the data bases
"""
def list_map():  # mapping the front end to the backend, put in the function so we don't have to copy and paste this all the time
    item = items.query.all()
    for item in item:
        user_dict = {'id': item.id, 'name': item.name, 'type': item.type, 'price': item.price}
        records.append(user_dict)
"""
user_records= []
def list_user_map():  # mapping the front end to the backend, put in the function so we don't have to copy and paste this all the time
    user = UserTT.query.all()
    for user in user:
        user_tt_dict = {'id': user.id, 'username': user.username, 'email': user.email, 'password': user.password, 'shopping_cart_column':user.shopping_cart_column}
        user_records.append(user_tt_dict)


#list_map()  # running once, appends database items into list user sees
list_user_map()

#  connects default URL of server to a python function

@app.route('/')
def index():
    #  function use Flask import (Jinga) to render an HTML template
    # print("from the home page" +str(shopping_cart))
    return render_template("index.html")
