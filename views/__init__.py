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
from models.module import UserTT
from app import app
Bootstrap(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return UserTT.query.get(int(user_id))
"""login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'"""

from models import thriftythreadsdata, barbarelladata, contactimages, websitecards


"""Defining routes"""
app.register_blueprint(makeup_api_bp, url_prefix='/makeup_api')
app.register_blueprint(easter_egg_bp, url_prefix='/easter_egg')
app.register_blueprint(database_items_bp, url_prefix='/database_items')
app.register_blueprint(easter_egg_college_bp, url_prefix='/easter_egg_college')
app.register_blueprint(time_to_thrift_bp, url_prefix='/time_to_thrift')


#  displaying all the current items in the data bases
"""
def list_map():  # mapping the front end to the backend, put in the function so we don't have to copy and paste this all the time
    item = items.query.all()
    for item in item:
        user_dict = {'id': item.id, 'name': item.name, 'type': item.type, 'price': item.price}
        records.append(user_dict)
"""

#  connects default URL of server to a python function

@app.route('/')
def index():
    #  function use Flask import (Jinga) to render an HTML template
    # print("from the home page" +str(shopping_cart))
    return render_template("index.html")
