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

user_type = 'user'

@easter_egg_bp.route('/') #this is the home page of the makeup API page
def index():
    #return render_template("easter_egg/home.html",user_type=user_type)
    user_type = 'user'
    return render_template('easter_egg/user_dashboard.html', user_type=user_type)

@easter_egg_bp.route('/image_map_dnhs')
def image_map():
    return render_template("easter_egg/image_map_dnhs.html", images=model.infoforthecontactsineaster(),user_type=user_type)

@easter_egg_bp.route('/image_map_dnhs2')
def image_map2():
    return render_template("easter_egg/image_map_dnhs2.html", images=model.infoforthecontactsineaster(),user_type=user_type)

"""@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = UserTT.query.filter_by(username = username).first()
        if user:
            if user.password == password:
                login_user(user)
                return redirect(url_for('logged_in'))

        return '<h1>Invalid username or password</h1>'

    return render_template("login.html")

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        new_user = UserTT(username = username, email = email, password = password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template("SU.html")"""

@easter_egg_bp.route('/auth_user', methods = ['GET','POST']) #this is the home page of the makeup API page
def private():
    return render_template("easter_egg/auth_user.html",user_type=user_type)

@login_required
@easter_egg_bp.route('/ordernow')
def timetoorder():
    return render_template("easter_egg/ordernow.html",user_type=user_type)

@easter_egg_bp.route('/multipage_form')
def multipage_from():
    return render_template("easter_egg/multipage_form.html", snack_list=food.inventory_stack(),user_type=user_type)

#  from JSON to python
dict_buildings = json.loads(del_norte_buildings.json_all_building)
class_rooms = []
for i in dict_buildings:
    class_rooms.append(dict_buildings[i])

@easter_egg_bp.route('/singlepage_form')
def singlepage_form():
    return render_template("easter_egg/singlepage_form.html", snack_list=food.inventory_stack(), building_list=dict_buildings, class_rooms=class_rooms, user_type=user_type)

@easter_egg_bp.route('/after_form', methods = ['GET','POST'])
def after_form():
    if request.method == 'POST':
        list_dict_food = food.inventory_stack()
        trash_quanities = []
        trash_items = []
        pass_info = []

        #print(food_items)
        b = 1
        for i in list_dict_food:
            food_name = request.form.get('food_item'+str(b))
            food_count = request.form.get('food_quantity'+str(b))
            if food_count == '0':
                trash_items.append(food_name)
                trash_quanities.append(food_count)
            else:
                pass_info.append(food_count) #pass the quanity of the item first
                pass_info.append(food_name) #pass the name of the item second
            b = b + 1

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
        return render_template("easter_egg/after_form.html", information=information, pass_info=pass_info, user_type=user_type)

@easter_egg_bp.route('/runner_dashboard')#  will eventually be post , methods = ['GET','POST']
def runner_dashboard():
    user_type = 'runner'
    return render_template('easter_egg/runner_dashboard.html', user_type=user_type)

@easter_egg_bp.route('/user_dashboard')#  will eventually be post , methods = ['GET','POST']
def user_dashboard():
    user_type = 'user'
    return render_template('easter_egg/user_dashboard.html', user_type=user_type)


"""@easter_egg_bp.route('/theeastercontacts')
def eastercontactus():
    return render_template("easter_egg/newcontactus.html", images=model.infoforthecontactsineaster(),user_type=user_type)
"""