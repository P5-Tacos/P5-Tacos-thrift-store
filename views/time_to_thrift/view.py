from views.time_to_thrift import time_to_thrift_bp
from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import FileField, PasswordField
from wtforms import StringField
from wtforms.validators import InputRequired, Length, Email
from models import thriftythreadsdata, barbarelladata, contactimages, websitecards
shopping_cart = []
#app = Flask(__name__)
#  connects default URL of server to a python function

app = Flask(__name__)

@time_to_thrift_bp.route('/')
def index():
    #  function use Flask import (Jinga) to render an HTML template
    # print("from the home page" +str(shopping_cart))
    return render_template("home.html", inventory_list1=thriftythreadsdata.inventory_itemsTT(),
                           inventory_list2=barbarelladata.inventory_itemsBB(), display_cart=shopping_cart)

@time_to_thrift_bp.route('/storefront')
def storefront():
    return render_template("storefront.html", cards=websitecards.CardsForStores(), display_cart=shopping_cart)

@time_to_thrift_bp.route('/reactiontest')
def reactiontest():
    return render_template("reactiontest.html")


@time_to_thrift_bp.route('/contactus')
def contactus():
    return render_template("contactus.html", images=contactimages.grouppictures(), display_cart=shopping_cart)  # this is the app route to the contact us page

@time_to_thrift_bp.route('/login', methods=["GET", "POST"])
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

    return render_template("login.html", display_cart=shopping_cart)

@time_to_thrift_bp.route('/logged_in', methods=["GET", "POST"])
#@login_required
def logged_in():
    #print(current_user.username)
    return render_template("logged_in.html", display_cart=shopping_cart)

@time_to_thrift_bp.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        new_user = UserTT(username = username, email = email, password = password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template("SU.html", display_cart=shopping_cart)#form = form,

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

        return redirect(store_route)

@time_to_thrift_bp.route('/shopping_cart_remove', methods=["GET", "POST"])
def shopping_cart_remove():
    if request.method == 'POST':
        #takes the postiion of the item within the list
        item_pos_list = request.form['item_pos_list']
        #pops out the list in the corresponding postition
        shopping_cart.pop(int(item_pos_list))
        return redirect(url_for('logged_in'))

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

        return redirect(url_for('logged_in'))

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
        return redirect(url_for('logged_in'))

@time_to_thrift_bp.route('/thriftythreads')
def thriftythreads():
    return render_template("gallery.html", inventory_list=thriftythreadsdata.inventory_itemsTT(),
                           Store_Title="Thrifty Threads", route="/thriftythreads", window_y_value=json.dumps(window_y_value), display_cart=shopping_cart)  # this is the app route to the ThriftTHreads's page


@time_to_thrift_bp.route('/barbarella')
def barbarella():
    return render_template("gallery.html", inventory_list=barbarelladata.inventory_itemsBB(),
                           Store_Title="Barbarella", route="/barbarella", window_y_value=json.dumps(window_y_value), display_cart=shopping_cart)  # this is the app route to Barbarella's page

@time_to_thrift_bp.route('/clothes_info', methods=["GET", "POST"])
def clothes_info():
    if request.method == 'POST':
        store_route = request.form['store_route']
        item_name = request.form['item_name']
        item_price = request.form['item_price']
        item_location = request.form['item_location']

        pass_info = {"item_name": item_name, "item_price": item_price, "item_location": item_location}

        return render_template("clothes_info.html", pass_info=pass_info)  # this is the app route to Barbarella's page


@time_to_thrift_bp.route('/logout', methods=["GET", "POST"])
@login_required
def logout():
    if request.method == "POST" :
        logout_user()
        return redirect(url_for('login'))

@time_to_thrift_bp.route('/admin')
def admin_display():
    return render_template("admin_page.html", table=user_records, display_cart=shopping_cart)

@time_to_thrift_bp.route('/testing_home')
def testing_home():
    return render_template("testing_home.html")
