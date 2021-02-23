#this is where all the routes will go

from views.easter_egg import easter_egg_bp
from flask import Flask, render_template,redirect,url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, FileField, FloatField,PasswordField
from wtforms.validators import InputRequired, Length, NumberRange
from views.easter_egg import model
from views.easter_egg import food
from flask_login import UserMixin, LoginManager
from flask_login import UserMixin, LoginManager, login_required
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from views.easter_egg import db, User
from views.easter_egg import del_norte_buildings
import json

app = Flask(__name__)
Bootstrap(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class LoginForm(FlaskForm):
    username = StringField('username',validators=[InputRequired(), Length(min=1,max=15)])
    password = PasswordField('password',validators=[InputRequired(), Length(min=1,max=80)])

class RegisterForm(FlaskForm):
    username = StringField('username',validators=[InputRequired(), Length(min=1,max=15)])
    password = PasswordField('password',validators=[InputRequired(), Length(min=1,max=80)])
    grade = FloatField('grade',validators=[InputRequired()])
    id = FloatField('id',validators=[InputRequired()])

@easter_egg_bp.route('/') #this is the home page of the makeup API page
def index():
    return render_template("easter_egg/home.html")

@easter_egg_bp.route('/theeastercontacts')
def eastercontactus():
    return render_template("easter_egg/newcontactus.html", images=model.infoforthecontactsineaster())

@easter_egg_bp.route('/image_map_dnhs')
def image_map():
    return render_template("easter_egg/image_map_dnhs.html", images=model.infoforthecontactsineaster())

@easter_egg_bp.route('/Signup/',methods = ['GET','POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(name = form.username.data, Stu_id = form.id.data, password = form.password.data,grade = form.grade.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('easter_egg_bp.login'))

    return render_template("easter_egg/SU.html",form = form)

@easter_egg_bp.route('/Login', methods = ['GET', 'POST'])
def login():
    logform = LoginForm()

    if logform.validate_on_submit():
        #exists = db.session.query(
        #db.session.query(User).filter_by(username='AndrewZhang').exists()
        #).scalar()
        #if exists == True:
        #return "Exists"
        user = User.query.filter_by(username = logform.username.data).first()
        if user:
            if user.password == logform.password.data:
                return redirect(url_for('private'))

        return '<h1>Invalid username or password</h1>'

    return render_template("easter_egg/login.html",form = logform)

@easter_egg_bp.route('/auth_user', methods = ['GET','POST']) #this is the home page of the makeup API page
def private():
    return render_template("easter_egg/auth_user.html")

@login_required
@easter_egg_bp.route('/ordernow')
def timetoorder():
    return render_template("easter_egg/ordernow.html")

@easter_egg_bp.route('/multipage_form')
def multipage_from():
    return render_template("easter_egg/multipage_form.html", snack_list=food.inventory_stack())

#  from JSON to python
dict_buildings = json.loads(del_norte_buildings.json_all_building)
class_rooms = []
for i in dict_buildings:
    class_rooms.append(dict_buildings[i])

@easter_egg_bp.route('/singlepage_form')
def singlepage_form():
    return render_template("easter_egg/singlepage_form.html", snack_list=food.inventory_stack(), building_list=dict_buildings, class_rooms=class_rooms)

@easter_egg_bp.route('/after_form', methods = ['GET','POST'])
def after_form():
    if request.method == 'POST':
        total_cost = request.form['total_cost_input']
        building_group = request.form.get('buildings_group')
        all_rooms = []

        #  starting at 1 to ensure that we start at the correct value. This is because we have loop index define the name of the inputs
        b = 1
        for i in class_rooms:
            room_number = request.form.get('room'+str(b))
            all_rooms.append(room_number)
            b = b + 1

        #  getting the last number of the groups
        if len(building_group) == 5:
            #  form "room1" to "room9"
            last_char = building_group[-1]
        else:
            #  from "room10" to "room15"
            last_char = building_group[-2:]

        # decrement by one to select the correct group of numbers
        item_number = int(last_char) - 1
        # select the selected item for the hidden displays
        room = all_rooms[item_number]

        information = {"total cost": total_cost, "building group": building_group, "room number": room}
        return render_template("easter_egg/after_form.html", information=information)

