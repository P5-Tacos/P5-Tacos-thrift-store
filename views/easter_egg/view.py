#this is where all the routes will go

from views.easter_egg import easter_egg_bp
from flask import Flask, render_template
from views.easter_egg import model
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = ':)'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eggbase_user'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column('item_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(50))
    grade = db.Column(db.Integer())

def __init__(self, id, name, password, grade):
    self.name = name
    self.id = id
    self.password = password
    self.grade = grade

db.create_all()


@easter_egg_bp.route('/') #this is the home page of the makeup API page
def index():
    return render_template("easter_egg/home.html")

@easter_egg_bp.route('/theeastercontacts')
def eastercontactus():
    return render_template("easter_egg/newcontactus.html", images=model.infoforthecontactsineaster())

@easter_egg_bp.route('/image_map_dnhs')
def image_map():
    return render_template("easter_egg/image_map_dnhs.html", images=model.infoforthecontactsineaster())
