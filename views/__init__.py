# https://flask.palletsprojects.com/en/1.1.x/api/
from app import app
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_user, login_required, logout_user
from models.module import UserTT, UserDN
from views.makeup_api import makeup_api_bp  # blueprint not a module
from views.easter_egg import easter_egg_bp
from views.database_items import database_items_bp
from views.easter_egg_college import easter_egg_college_bp
from views.time_to_thrift import time_to_thrift_bp

Bootstrap(app)
#  need login manager in the main file to allow for the login system to work for Time to Thrift
"""login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return UserTT.query.get(int(user_id))
"""
"""
@login_manager.user_loader
def load_user_DN(user_id):
    return UserDN.query.get(int(user_id))
"""
#  Defining routes
app.register_blueprint(makeup_api_bp, url_prefix='/makeup_api')
app.register_blueprint(easter_egg_bp, url_prefix='/easter_egg')
app.register_blueprint(database_items_bp, url_prefix='/database_items')
app.register_blueprint(easter_egg_college_bp, url_prefix='/easter_egg_college')
app.register_blueprint(time_to_thrift_bp, url_prefix='/time_to_thrift')

@app.route('/')
def index():
    return render_template("index.html")

