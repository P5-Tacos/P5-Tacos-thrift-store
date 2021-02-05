#this is where all the routes will go

from views.easter_egg import easter_egg_bp
from flask import Flask, render_template,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField, FileField, FloatField,PasswordField
from wtforms.validators import InputRequired, Length, NumberRange
from views.easter_egg import model
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

from flask_bootstrap import Bootstrap



app = Flask(__name__)
Bootstrap(app)

app.config['SECRET_KEY'] = ':)'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eggbase_user.db' #path from repository root: views/easter_egg/eggbase_user.db
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



class LoginForm(FlaskForm):
    username = StringField('username',validators=[InputRequired(), Length(min=4,max=15)])
    password = PasswordField('password',validators=[InputRequired(), Length(min=8,max=80)])




@easter_egg_bp.route('/') #this is the home page of the makeup API page
def index():
    return render_template("easter_egg/home.html")

@easter_egg_bp.route('/theeastercontacts')
def eastercontactus():
    return render_template("easter_egg/newcontactus.html", images=model.infoforthecontactsineaster())

@easter_egg_bp.route('/image_map_dnhs')
def image_map():
    return render_template("easter_egg/image_map_dnhs.html", images=model.infoforthecontactsineaster())

@easter_egg_bp.route('/college_board_requirements')
def college_req():
    return render_template("easter_egg/college_board_requirements.html", images=model.infoforthecontactsineaster())

@easter_egg_bp.route('/Login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user:
            if user.password == form.password.data:
                return redirect(url_for('easter_egg/login.html'))

        return '<h1>Invalid username or password</h1>'

    return render_template("easter_egg/login.html",form = form)

