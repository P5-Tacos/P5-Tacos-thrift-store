# this is where all the routes will go

from views.easter_egg import easter_egg_bp
from flask import Flask, render_template, redirect, url_for, request
from views.easter_egg.model import food, del_norte_buildings, model

from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_user, login_required, current_user
import json

# importing databases form the module.py file
app = Flask(__name__)
from models.module import db, userEE, orderEE, userDN, userRR
from models.login import load_user_DN, model_logout_all

from datetime import datetime
from sqlalchemy import func
import time

db.init_app(app)

#  for the login page
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return userDN.query.get(user_id)


user_type = 'user'

everybody = []
user_records = []
runner_records = []


def everbody_append():
    # mapping the backend to the front end, of all of the users in the login database
    user = userDN.query.all()
    for user in user:
        user_dn_dict = {'id': user.id, 'username': user.username, 'email': user.email, 'password': user.password,
                        'program': user.program}
        everybody.append(user_dn_dict)

def list_user_map():
    #  mapping the backend to the front end, for the users of del norte eats
    user = userEE.query.all()
    for user in user:
        user_dn_dict = {'id': user.id, 'username': user.username, 'email': user.email, 'password': user.password}
        user_records.append(user_dn_dict)

def list_runner_map():
    #  mapping the backend to the front end, for the runners of del norte eats in database
    runners = userRR.query.all()
    for user in runners:
        runner_dn_dict = {'id': user.id, 'username': user.username, 'email': user.email, 'password': user.password}
        runner_records.append(runner_dn_dict)

def order_map():
    #  mapping the backend end to the frontend, for the orders of the users
    order_records = []
    orders = orderEE.query.all()
    for order in orders:
        order_dn_dict = {'id': order.id,'username': order.username, 'price': order.price, 'order contents': order.order_contents,
                         'time': order.time, 'picked up': order.picked_up, 'delivered': order.delivered}
        order_records.append(order_dn_dict)
    return order_records

# running once, appends database items into list user sees
list_user_map()
list_runner_map()
everbody_append()
order_records = order_map()

def per_user():
    if current_user.is_anonymous:
        username = 'Guest'
    else:
        username = current_user.username
    order_user = []
    orders = orderEE.query.filter_by(username=username).all()
    for order in orders:
        order_dn_dict = {'id': order.id,'username': order.username, 'price': order.price, 'order contents': order.order_contents,
                         'time': order.time, 'picked up': order.picked_up, 'delivered': order.picked_up}
        order_user.append(order_dn_dict)
    return order_user

def dash_handel():
    # to redirect the user to the user to logged in or guest dashboard

    # always getting the user orders based on the username of the current user
    # username = current_user.username
    order_user = per_user()
    if current_user.is_anonymous:
        return render_template('easter_egg/user_dashboard_guest.html', user_type=user_type, order_table=order_user)
    else:
        return render_template('easter_egg/user_dashboard_authen.html', user_type=user_type, order_table=order_user)

#  redirecting the user to the guest dashboard, the route for home int he user dashboard
@easter_egg_bp.route('/')
def index():
    user_type = 'user'
    result = dash_handel()
    return result

#  static image map
@easter_egg_bp.route('/image_map_dnhs')
def image_map():
    return render_template("easter_egg/unused_templates/image_map_dnhs.html", images=model.infoforthecontactsineaster(),
                           user_type=user_type)

# image map that resizes with the window size
@easter_egg_bp.route('/image_map_dnhs2')
def image_map2():
    return render_template("easter_egg/unused_templates/image_map_dnhs2.html", images=model.infoforthecontactsineaster(),
                           user_type=user_type)


@easter_egg_bp.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        form_username = request.form['username']
        form_password = request.form['password']
        form_program = request.form['program']
        #  print("this is the login page"+  str(form_program))
        #  program = 'del_norte_eats'
        program = form_program
        #  print(program)
        form_user = [form_username, form_password]
        #  collecting all of the people with the program 'time_to_thrift'
        all_user_list = userDN.query.all()
        users_in_data = []

        # user = all_user.query.filter_by(program=program)
        # itterates through all of the data within user database
        id = []
        all_user_info = []
        for user in all_user_list:

            # this loop is to display all the users within the system
            user_info = {'id': user.id, 'username': user.username, 'email': user.email, 'password': user.password,
                         'program': user.program}
            users_in_data.append(user_info)

            #  to find which users are corresponding to the system
            if user.program == program:
                id.append(user.id)

                user_cred = [user.username, user.password]
                all_user_info.append(user_cred)
        #  print(all_user_info)
        for user in all_user_info:
            # print(user)
            # if the information from the login matches the information that was sttored in the data base
            if form_user == user:

                #  gets credentials of the user
                user_in_db = userDN.query.filter_by(username=form_username).first()
                #  logs in the user with their credentials
                login_user(user_in_db)
                print("redirecting")
                #  redirects the user to their specific dashboard
                if program == 'del_norte_eats_runner':
                    #  redirecting to the runner dashboard
                    print('runner')
                    return redirect(url_for('easter_egg_bp.runner_dashboard'))
                    #return render_template('easter_egg/runner/runner_dashboard.html', user_type=user_type, order_table=order_records)
                else:
                    print('user')
                    if program == 'del_norte_eats':
                        #  redirecting for the user dashboard
                        order_user = per_user()
                        return render_template('easter_egg/user_dashboard_authen.html', user_type=user_type, order_table=order_user)
                    else:
                        #  there should never be a redirect to this, all the programs should correspond
                        return render_template("easter_egg/after_login.html", user_type=user_type)

        # if there was a problem with the login
        return render_template("easter_egg/after_login.html", user_type=user_type)

    #  default of what the user intially sees when selecting the login button
    return render_template("easter_egg/login.html", user_type=user_type)

@easter_egg_bp.route('/logged_in')
def logged_in():
    result = dash_handel()
    return result

#  sign up of users, creating the user into the main database and user database
@easter_egg_bp.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        program = request.form['program']

        #  print(str(email) + " " + str(username) + " " + str(password) + " " + str(program))

        #  adding user into the all_user database
        new_user = userDN(username=username, email=email, password=password, program=program)
        db.session.add(new_user)
        db.session.commit()

        # adding user into the userEE database
        new_user_2 = userEE(username=username, email=email, password=password)
        db.session.add(new_user_2)
        db.session.commit()

        #  redirecting to the login logic
        return redirect(url_for('easter_egg_bp.login'))

    return render_template("easter_egg/SU.html", user_type=user_type)  # form = form,

#  sign up of runners, creating the user into the main database and runner database
@easter_egg_bp.route('/signup_runner', methods=["GET", "POST"])
def signup_runner():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        program = request.form['program']

        #  print(str(email) + " " + str(username) + " " + str(password) + " " + str(program))

        #  adding user into the all_user database
        new_user = userDN(username=username, email=email, password=password, program=program)
        db.session.add(new_user)
        db.session.commit()

        # adding user into the userEE database
        new_user_2 = userRR(username=username, email=email, password=password)
        db.session.add(new_user_2)
        db.session.commit()

        #  redirecting to the login logic
        return redirect(url_for('easter_egg_bp.login'))

    return render_template("easter_egg/runner/SU.html", user_type=user_type)

#  currently unused
@easter_egg_bp.route('/auth_user', methods=['GET', 'POST'])
def private():
    return render_template("easter_egg/auth_user.html", user_type=user_type)


#  from JSON to python
dict_buildings = json.loads(del_norte_buildings.json_all_building)
#  setting up list to use data in after_form function
class_rooms = []
for i in dict_buildings:
    class_rooms.append(dict_buildings[i])

#  the form using java script to progress the user through each section of the form rather than having all of the
#  inputs on one page currently not used
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

        # starting at 1 to ensure that we start at the correct value. This is because we have loop index define the
        # name of the inputs
        b = 1
        for i in class_rooms:
            room_number = request.form.get('room' + str(b))
            all_rooms.append(room_number)
            b = b + 1

        #  getting the last number of the groups
        if len(building_group) == 5:
            #  from "room1" to "room9"
            last_char = building_group[-1]
        else:
            #  from "room10" to "room15"
            last_char = building_group[-2:]

        # decrement by one to select the correct group of numbers
        item_number = int(last_char) - 1
        # select the selected item for the hidden displays
        room = all_rooms[item_number]

        information = {"total cost": total_cost, "building group": building_group, "room number": room}

        # the information that will be stored into the database
        into_json = {"total cost": total_cost, "building group": building_group, "room number": room,
                     "order_contents": pass_info}
        order_json = json.dumps(into_json)
        #print(order_json)

        only_food_json = json.dumps(pass_info)
        #print(only_food_json)
        #  if the user is not logged in when submitting the form the username is defualted to guest

        if current_user.is_anonymous:
            username = 'Guest'
        else:
            username = current_user.username

        #  getting the time of the submit

        now = datetime.now()
        default = datetime.now()
        #  id = db.session.query(func.max(orderEE.id))
        #  print(id)
        #  orderEE.query.all()
        #  1 interger is a dummy variable
        order_info = orderEE(username=username, price=float(total_cost), order_contents=only_food_json, time=now, picked_up=default, delivered=default)
        db.session.add(order_info)
        db.session.commit()

    return render_template("easter_egg/after_form.html", information=information, pass_info=pass_info,
                           user_type=user_type)


@easter_egg_bp.route('/runner_dashboard')
def runner_dashboard():
    user_type = 'Runner'
    order_user = per_user()

    # list to determine which button will show
    button_logic_pickup = []
    button_logic_delivered = []

    order_records = []
    orders = orderEE.query.all()
    for order in orders:
        #print(order.id)
        if order.time != order.picked_up:
            #print("has been picked up")
            button_logic_pickup.append(1)
            pickup_value = 1
        else:
            #print("has not been picked up")
            button_logic_pickup.append(0)
            pickup_value = 0
        if order.time != order.delivered:
            #print("has been delivered")
            button_logic_delivered.append(1)
            delivered_value = 1

            #  assumming that the order has been picked up previously
            total_time = order.delivered - order.time
            print(total_time)
        else:
            #print("has not been delivered")
            button_logic_delivered.append(0)
            delivered_value = 0

        order_dn_dict = {'id': order.id,
                         'username': order.username,
                         'price': order.price,
                         'order contents': order.order_contents,
                         'time': order.time,
                         'picked up': order.picked_up,
                         'delivered': order.delivered,
                         'button_logic_pickup': pickup_value,
                         'button_logic_delivered': delivered_value,
                         'total_time': total_time
                         }
        order_records.append(order_dn_dict)
    return render_template('easter_egg/runner/runner_dashboard.html', user_type=user_type, order_table=order_records)


@easter_egg_bp.route('/user_dashboard')
def user_dashboard():
    #  the redirect to the dashboard when user clicks the home button in nav bar of Del Norte eats
    user_type = 'user'
    result = dash_handel()
    return result


@easter_egg_bp.route('/admin')
def admin_page():
    # admin page showing all of the data within Del Norte Eats
    return render_template('easter_egg/admin_page.html', user_table=user_records, all_table=everybody, order_table=order_records, runner_table = runner_records)


@easter_egg_bp.route('/logout_return')
def home():
    #  logging out the user in Del Norte Eats and redirecting the user to the home page
    if current_user.is_authenticated:
        model_logout_all()
        return render_template("index.html")
    else:
        return render_template("index.html")

@easter_egg_bp.route('/port_runner')
def runner_nav():
    if current_user.is_authenticated:
        #  if the user is logged in as a customer, they will be logged out
        #  redirected to the login page of the runner page
        model_logout_all()
        return render_template("easter_egg/runner/login_runner.html")
    else:
        #  if the user is not logged in as a customer, they will be redirected to the login runner page
        return render_template("easter_egg/runner/login_runner.html")

@easter_egg_bp.route('/port_user')
def user_nav():
    if current_user.is_authenticated:
        #  if the runner is logged in as a customer, they will be logged out
        #  redirected to the login page of the user page
        model_logout_all()
        return redirect(url_for('easter_egg_bp.index'))
    else:
        #  if the runner is not logged in they will be redirected to the login runner page
        return redirect(url_for('easter_egg_bp.index'))

@easter_egg_bp.route('/logout', methods=["GET", "POST"])
@login_required
def logout():
    #  logging out the user and redirect the user back tot he user dashboard
    if request.method == "POST":
        model_logout_all()
        result = dash_handel()
        return result

    # if the input type was not a post form, if the logout was in the nav bar
    model_logout_all()
    result = dash_handel()
    return result

@easter_egg_bp.route('/logout_rr', methods=["GET", "POST"])
@login_required
def logout_rr():
    #  this is the route on the runner dashboard to reroute the runner back to the runner login
    if request.method == "POST":
        model_logout_all()
        return render_template("easter_egg/runner/login_runner.html")

@easter_egg_bp.route('/picked_up/', methods=['GET', "POST"])
def picked_up():
    if request.method == "POST":  # we know the item id
        order_id = request.form["order_id"]
        now = datetime.now()

        order_dict = {'picked_up': now}
        db.session.query(orderEE).filter_by(id=order_id).update(order_dict)
        db.session.commit()

        #return render_template('easter_egg/runner/runner_dashboard.html', user_type=user_type, order_table=order_records)
        return redirect(url_for('easter_egg_bp.runner_dashboard'))

# dilivered_button

@easter_egg_bp.route('/delivered/', methods=['GET', "POST"])
def delivered():
    if request.method == "POST":  # we know the item id
        order_id = request.form["order_id"]
        now = datetime.now()

        order_dict = {'delivered': now}
        db.session.query(orderEE).filter_by(id=order_id).update(order_dict)
        db.session.commit()

        #return render_template('easter_egg/runner/runner_dashboard.html', user_type=user_type, order_table=order_records)
        return redirect(url_for('easter_egg_bp.runner_dashboard'))
