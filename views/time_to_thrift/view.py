from views.time_to_thrift import time_to_thrift_bp
from flask import Flask, render_template, request, redirect, url_for
from models import thriftythreadsdata, barbarelladata, contactimages, websitecards
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import FileField, PasswordField
from wtforms import StringField
from wtforms.validators import InputRequired, Length, Email
import json

#from app import app
app = Flask(__name__)
from models.module import UserTT, db
db.init_app(app)

app.secret_key = 'xxxxyyyyyzzzzz'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

records = []
shopping_cart = [] #list to append values for each item to display on the user dashboard
window_y_value = 0
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

@login_manager.user_loader
def load_user(user_id):
    return UserTT.query.get(int(user_id))

user_records= []
def list_user_map():  # mapping the front end to the backend, put in the function so we don't have to copy and paste this all the time
    user = UserTT.query.all()
    for user in user:
        user_tt_dict = {'id': user.id, 'username': user.username, 'email': user.email, 'password': user.password, 'shopping_cart_column':user.shopping_cart_column}
        user_records.append(user_tt_dict)


#list_map()  # running once, appends database items into list user sees
list_user_map()

@time_to_thrift_bp.route('/')
def index_TT():
    #  function use Flask import (Jinga) to render an HTML template
    # print("from the home page" +str(shopping_cart))
    return render_template("time_to_thrift/home.html", inventory_list1=thriftythreadsdata.inventory_itemsTT(),
                           inventory_list2=barbarelladata.inventory_itemsBB(), display_cart=shopping_cart)

@time_to_thrift_bp.route('/storefront')
def storefront():
    return render_template("time_to_thrift/storefront.html", cards=websitecards.CardsForStores(), display_cart=shopping_cart)

@time_to_thrift_bp.route('/reactiontest')
def reactiontest():
    return render_template("reactiontest.html")


@time_to_thrift_bp.route('/contactus')
def contactus():
    return render_template("time_to_thrift/contactus.html", images=contactimages.grouppictures(), display_cart=shopping_cart)  # this is the app route to the contact us page

@time_to_thrift_bp.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = UserTT.query.filter_by(username = username).first()
        if user:
            if user.password == password:
                login_user(user)
                return redirect(url_for('time_to_thrift_bp.logged_in'))

        return '<h1>Invalid username or password</h1>'

    return render_template("time_to_thrift/login.html", display_cart=shopping_cart)

@time_to_thrift_bp.route('/logged_in', methods=["GET", "POST"])
#@login_required
def logged_in():
    #print(current_user.username)
    #views/time_to_thrift/templates/time_to_thrift/logged_in.html
    return render_template("time_to_thrift/logged_in.html", display_cart=shopping_cart)

@time_to_thrift_bp.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        new_user = UserTT(username = username, email = email, password = password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('time_to_thrift_bp.login'))

    return render_template("time_to_thrift/SU.html", display_cart=shopping_cart)#form = form,

@time_to_thrift_bp.route('/purchase', methods=["GET", "POST"])
def purchase():
    if request.method == 'POST':
        scroll_poss = request.form['scroll_poss']
        store_route = request.form['store_route']
        item_name = request.form['item_name']
        item_price = request.form['item_price']
        item_location = request.form['item_location']

        #print("scroll pos: "+str(scroll_poss))
        #print(scroll_poss)
        store_route = str(store_route)
        print(store_route)
        global window_y_value
        window_y_value = float(scroll_poss)


        """print("theses were the hidden values:") #testing pourposes
        print(item_name)
        print(item_price)
        print(item_location)"""

        pass_info = {"item_name": item_name, "item_price": item_price, "item_location": item_location}
        shopping_cart.append(pass_info)
        print("from the gallery page" +str(shopping_cart))
        #get the id of the item (Done)
        #get the page of the item (Done)
        #append the id of the item into the shopping cart (Done)
        #redirect user to the page that they were just at (Done)
        print(store_route)
        if store_route == '/thriftythreads':
            print('tt')
            return redirect(url_for('time_to_thrift_bp.thriftythreads'))
        if store_route == '/barbarella':
            print('bb')
            return redirect(url_for('time_to_thrift_bp.barbarella'))
        if store_route == '/logged_in':
            return redirect(url_for('time_to_thrift_bp.logged_in'))
        #erros out
        return redirect(store_route)

@time_to_thrift_bp.route('/shopping_cart_remove', methods=["GET", "POST"])
def shopping_cart_remove():
    if request.method == 'POST':
        #takes the postiion of the item within the list
        item_pos_list = request.form['item_pos_list']
        #pops out the list in the corresponding postition
        shopping_cart.pop(int(item_pos_list))
        return redirect(url_for('time_to_thrift_bp.logged_in'))

@time_to_thrift_bp.route('/shopping_cart_save', methods=["GET", "POST"])
def shopping_cart_save():
    if request.method == 'POST':
        username = request.form['username']
        #print(shopping_cart)
        jsonStr = json.dumps(shopping_cart)
        #print(jsonStr)

        db.session.query(UserTT).filter_by(username=username).update({"shopping_cart_column":jsonStr})
        db.session.commit()

        #records[1]['shopping_cart_column'] = str(jsonStr)
        for i in range(len(user_records)):  # updating the front end view of the data base
            if user_records[i]['username'] == username:
                user_records[i]['shopping_cart_column'] = str(jsonStr) #set the value of the json string to to the json file
                break

        return redirect(url_for('time_to_thrift_bp.logged_in'))

@time_to_thrift_bp.route('/shopping_cart_load', methods=["GET", "POST"])
def shopping_cart_load():
    if request.method == 'POST':
        #print("load my shopping cart from json")
        username = request.form['username']
        previous_list = db.session.query(UserTT).filter_by(username=username).first()
        #print(previous_list.shopping_cart_column)
        json_previous_list = previous_list.shopping_cart_column
        #converting from JSON to python
        loaded_list = json.loads(json_previous_list)
        #print("list of list" + str(loaded_list))
        for i in loaded_list:
            shopping_cart.append(i)
        return redirect(url_for('time_to_thrift_bp.logged_in'))

@time_to_thrift_bp.route('/thriftythreads')
def thriftythreads():
    return render_template("time_to_thrift/gallery.html", inventory_list=thriftythreadsdata.inventory_itemsTT(),
                           Store_Title="Thrifty Threads", route="/thriftythreads", window_y_value=json.dumps(window_y_value), display_cart=shopping_cart)  # this is the app route to the ThriftTHreads's page


@time_to_thrift_bp.route('/barbarella')
def barbarella():
    return render_template("time_to_thrift/gallery.html", inventory_list=barbarelladata.inventory_itemsBB(),
                           Store_Title="Barbarella", route="/barbarella", window_y_value=json.dumps(window_y_value), display_cart=shopping_cart)  # this is the app route to Barbarella's page

@time_to_thrift_bp.route('/clothes_info', methods=["GET", "POST"])
def clothes_info():
    if request.method == 'POST':
        store_route = request.form['store_route']
        item_name = request.form['item_name']
        item_price = request.form['item_price']
        item_location = request.form['item_location']

        pass_info = {"item_name": item_name, "item_price": item_price, "item_location": item_location}

        return render_template("time_to_thrift/clothes_info.html", pass_info=pass_info)  # this is the app route to Barbarella's page


@time_to_thrift_bp.route('/logout', methods=["GET", "POST"])
@login_required
def logout():
    if request.method == "POST" :
        logout_user()
        return redirect(url_for('time_to_thrift_bp.login'))

@time_to_thrift_bp.route('/admin')
def admin_display():
    return render_template("time_to_thrift/admin_page.html", table=user_records, display_cart=shopping_cart)

@time_to_thrift_bp.route('/testing_home')
def testing_home():
    return render_template("time_to_thrift/testing_home.html")