# this is where all the routes will go

from views.easter_egg import easter_egg_bp
from flask import Flask, render_template, redirect, url_for, request
from views.easter_egg.model import food, del_norte_buildings, model

from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_user, login_required,current_user
import json

# importing databases form the module.py file
app = Flask(__name__)
from models.module import db, userEE, OrderEE, userDN
from models.login import load_user_DN, model_logout_all

db.init_app(app)

#  for the login page
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return userEE.query.get(user_id)

user_type = 'user'


user_records = []
order_records = []

def list_user_map():  # mapping the front end to the backend, put in the function so we don't have to copy and paste
    user = userEE.query.all()
    for user in user:
        user_dn_dict = {'id': user.id,'user id': user.user_id,  'username': user.username, 'email': user.email, 'password': user.password}
        user_records.append(user_dn_dict)

def order_map():  # mapping the front end to the backend, put in the function so we don't have to copy and paste
    orders = OrderEE.query.all()
    for order in orders:
        order_dn_dict = {'user id': order.user_id,'price': order.price,  'order contents': order.order_contents, 'time': order.time}
        order_records.append(order_dn_dict)

# running once, appends database items into list user sees
list_user_map()
order_map()

@easter_egg_bp.route('/')  # this is the home page of the makeup API page
def index():
    # return render_template("easter_egg/home.html",user_type=user_type)
    user_type = 'user'
    return render_template('easter_egg/user_dashboard.html', user_type=user_type)


@easter_egg_bp.route('/image_map_dnhs')
def image_map():
    return render_template("easter_egg/image_map_dnhs.html", images=model.infoforthecontactsineaster(),
                           user_type=user_type)


@easter_egg_bp.route('/image_map_dnhs2')
def image_map2():
    return render_template("easter_egg/image_map_dnhs2.html", images=model.infoforthecontactsineaster(),
                           user_type=user_type)


@easter_egg_bp.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username)
        print(password)
        user = userEE.query.filter_by(username=username).first()
        print(user)
        if user:
            if user.password == password:
                login_user(user)
                return redirect(url_for('easter_egg_bp.logged_in'))

        return '<h1>Invalid username or password</h1>'  # this should be replaced with a page instead of just a message

    return render_template("easter_egg/login.html")

@easter_egg_bp.route('/logged_in')
def logged_in():
    return render_template("easter_egg/user_dashboard.html")

@easter_egg_bp.route('/signup', methods=["GET", "POST"])
def signup():
    # on submit
    if request.method == 'POST':
        # getting information from the form
        email = request.form['email']
        user_id = request.form['user_id']
        username = request.form['username']
        password = request.form['password']
        #user_id = int(user_id)
        # user_id = int(user_id) #ensure that user id is within the correct form (type int)
        """print(email)
         print(user_id)
         print(username)
         print(password)"""

        new_user = userEE(username = username, user_id = user_id, email = email, password = password)
        #new_user = userEE(username='billy', user_id=1111111, email='123@gmail.com', password='password')
        # adding information into the database
        db.session.add(new_user)
        db.session.commit()

        # redirecting the user to the login page
        return redirect(url_for('easter_egg_bp.login'))

    # default will be rendering the page
    return render_template("easter_egg/sign_up.html")


@easter_egg_bp.route('/auth_user', methods=['GET', 'POST'])  # this is the home page of the makeup API page
def private():
    return render_template("easter_egg/auth_user.html", user_type=user_type)


#  from JSON to python
dict_buildings = json.loads(del_norte_buildings.json_all_building)
class_rooms = []
for i in dict_buildings:
    class_rooms.append(dict_buildings[i])


@easter_egg_bp.route('/singlepage_form')
def singlepage_form():
    return render_template("easter_egg/singlepage_form.html", snack_list=food.inventory_stack(),
                           building_list=dict_buildings, class_rooms=class_rooms, user_type=user_type)


@easter_egg_bp.route('/after_form', methods=['GET', 'POST'])
def after_form():
    if request.method == 'POST':
        list_dict_food = food.inventory_stack()
        trash_quanities = []
        trash_items = []
        pass_info = []

        # print(food_items)
        b = 1
        for i in list_dict_food:
            food_name = request.form.get('food_item' + str(b))
            food_count = request.form.get('food_quantity' + str(b))
            if food_count == '0':
                trash_items.append(food_name)
                trash_quanities.append(food_count)
            else:
                pass_info.append(food_count)  # pass the quanity of the item first
                pass_info.append(food_name)  # pass the name of the item second
            b = b + 1

        total_cost = request.form['total_cost_input']
        building_group = request.form.get('buildings_group')
        all_rooms = []

        #  starting at 1 to ensure that we start at the correct value. This is because we have loop index define the name of the inputs
        b = 1
        for i in class_rooms:
            room_number = request.form.get('room' + str(b))
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

        #the information that will be stored into the database
        into_json = {"total cost": total_cost, "building group": building_group, "room number": room, "order_contents": pass_info}
        order_json = json.dumps(into_json)
        #print(order_json)

        #formating into the database
        #need user id
        #price
        #order contents
        #order time
        return render_template("easter_egg/after_form.html", information=information, pass_info=pass_info,
                               user_type=user_type)


@easter_egg_bp.route('/runner_dashboard')  # will eventually be post , methods = ['GET','POST']
def runner_dashboard():
    user_type = 'runner'
    return render_template('easter_egg/runner_dashboard.html', user_type=user_type)


@easter_egg_bp.route('/user_dashboard')  # will eventually be post , methods = ['GET','POST']
def user_dashboard():
    user_type = 'user'
    return render_template('easter_egg/user_dashboard.html', user_type=user_type)

@easter_egg_bp.route('/admin')
def admin_page():
    #user_dn_dict = {'id': user.ID,'user id': user.user_id,  'username': user.username, 'email': user.email, 'password': user.password}
    #counter for user Admin
    #b = 0

    """print(user_records)
    for i in user_records:
        for v in i:
            print(str(v))"""

    return render_template('easter_egg/admin_page.html',table=user_records)#, user_quanity=b

@easter_egg_bp.route('/logout_return')
def home():
    if current_user.is_authenticated:
        model_logout_all()
        return render_template("index.html")
    else:
        return render_template("index.html")


@easter_egg_bp.route('/logout', methods=["GET", "POST"])
@login_required
def logout():
    if request.method == "POST":
        model_logout_all()
        #logout_user()
        return redirect(url_for('easter_egg_bp.login'))

