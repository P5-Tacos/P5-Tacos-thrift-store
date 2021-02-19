# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, current_app
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from wtforms import StringField, FileField, FloatField, PasswordField
from wtforms.validators import InputRequired, Length, NumberRange
import os
from sqlalchemy.dialects.sqlite import BLOB
from wtforms import StringField
from wtforms.validators import InputRequired, Length, Email
from views.makeup_api import makeup_api_bp  # blueprint not a module
from views.easter_egg import easter_egg_bp
from views.database import database_bp
from views.easter_egg_college import easter_egg_college_bp
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

import thriftythreadsdata
import barbarelladata
import contactimages
import websitecards
import gallery_form

# create a Flask instance
"Setting up the keys are needed for the database"
app = Flask(__name__)
app.config['SECRET_KEY'] = ':)'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///UsersTT.db'
Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
records = []
shopping_cart = [] #list to append values for each item to display on the user dashboard

#to ensure that the directory is made each time the program is run
MYDIR = ("static\images\owner_upload")
CHECK_FOLDER = os.path.isdir(MYDIR)

# If folder doesn't exist, then create it.
if not CHECK_FOLDER:
    os.makedirs(MYDIR)
    print("created folder : ", MYDIR)

else:
    print(MYDIR, "folder already exists.")


class UserTT(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15))
    email = db.Column(db.String(50))
    password = db.Column(db.String(80))

@login_manager.user_loader
def load_user(user_id):
    return UserTT.query.get(int(user_id))

class items(db.Model):
    id = db.Column('item_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    type = db.Column(db.String(50))
    price = db.Column(db.String(200))


def __init__(self, id, name, type, price):
    self.name = name
    self.id = id
    self.type = type
    self.price = price

"Create Database"
db.create_all()

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

"""Defining routes"""
app.register_blueprint(makeup_api_bp, url_prefix='/makeup_api')
app.register_blueprint(easter_egg_bp, url_prefix='/easter_egg')
app.register_blueprint(database_bp, url_prefix='/database')
app.register_blueprint(easter_egg_college_bp, url_prefix='/easter_egg_college')

#  displaying all the current items in the data bases

def list_map():  # mapping the front end to the backend, put in the function so we don't have to copy and paste this all the time
    item = items.query.all()
    for item in item:
        user_dict = {'id': item.id, 'name': item.name, 'type': item.type, 'price': item.price}
        records.append(user_dict)

user_records= []
def list_user_map():  # mapping the front end to the backend, put in the function so we don't have to copy and paste this all the time
    user = UserTT.query.all()
    for user in user:
        user_tt_dict = {'id': user.id, 'username': user.username, 'email': user.email, 'password': user.password}
        user_records.append(user_tt_dict)


list_map()  # running once, appends database items into list user sees
list_user_map()

#  connects default URL of server to a python function
@app.route('/')
def index():
    #  function use Flask import (Jinga) to render an HTML template
    return render_template("home.html", inventory_list1=thriftythreadsdata.inventory_itemsTT(),
                           inventory_list2=barbarelladata.inventory_itemsBB())

@app.route('/storefront')
def storefront():
    return render_template("storefront.html", cards=websitecards.CardsForStores())

@app.route('/reactiontest')
def reactiontest():
    return render_template("reactiontest.html")


@app.route('/contactus')
def contactus():
    return render_template("contactus.html", images=contactimages.grouppictures())  # this is the app route to the contact us page

@app.route('/database', methods=['GET', 'POST'])  # contribution by Andrew
def shopowner():
    form = ItemForm()
    "Validate the forms"

    if form.validate_on_submit():  # adding in all
        new_item = items(type=form.type.data, name=form.name.data, price=form.price.data)
        db.session.add(new_item)
        db.session.commit()
        user_dict = {'id': new_item.id, 'name': new_item.name, 'type': new_item.type, 'price': new_item.price}
        records.append(user_dict)
        f = form.image.data
        filename = str(new_item.id) + ".jpg"
        f.save(os.path.join(MYDIR, filename))

    return render_template("Database test.html", form=form, table=records, gallery=records)

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    # Appending app path to upload folder path within app root folder
    uploads = os.path.join(current_app.root_path, app.config['owner_upload'])
    # Returning file from appended path
    return send_from_directory(directory=uploads, filename=filename)


# CRUD delete
@app.route('/delete/', methods=['GET', "POST"])
def delete():
    # print("arrived to delete")  # for debugging in the terminal

    if request.method == "POST":  # we know the item id
        userid = request.form["item_id"]
        found_values = []
        for dictionary in records:  # deleteing items from the data base
            if (dictionary["id"] == float(userid)):
                # print("we found it")  # for debugging in the terminal
                found_values.append(dictionary)
                delete = items.query.filter_by(id=float(userid)).first()
                db.session.delete(delete)
                db.session.commit()
                print("after delete")  # for debuggin in the terminla

            for i in range(len(records)):  # deleting the front end view of the data base
                if records[i]['id'] == float(userid):
                    del records[i]
                    break
                """for index in range(len(records)):  # this prints all values in the data base
                    print("---------")
                    for key in records[index]:
                        print(records[index][key])"""
            """else:
                print("we could not find it", end="")"""
        print("this is the row contents" + str(found_values))

    else:
        print("could not find the value")

    return redirect(url_for('shopowner'))


@app.route('/database_form', methods=['GET', 'POST'])
def database_forms():
    return render_template("database_form.html", tag_list=gallery_form.gallery_tags())


@app.route('/login', methods=["GET", "POST"])
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

@app.route('/logged_in', methods=["GET", "POST"])
@login_required
def logged_in():
    return render_template("logged_in.html", name = current_user.username, display_cart=shopping_cart)

@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = UserTT(username = form.username.data, email = form.email.data, password = form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template("SU.html", form = form)



@app.route('/thriftythreads')
def thriftythreads():
    return render_template("gallery.html", inventory_list=thriftythreadsdata.inventory_itemsTT(),
                           Store_Title="Thrifty Threads", route="/thriftythreads")  # this is the app route to the ThriftTHreads's page


@app.route('/barbarella')
def barbarella():
    return render_template("gallery.html", inventory_list=barbarelladata.inventory_itemsBB(),
                           Store_Title="Barbarella", route="/barbarella")  # this is the app route to Barbarella's page

@app.route('/logout', methods=["GET", "POST"])
@login_required
def logout():
    if request.method == "POST" :
        logout_user()
        return redirect(url_for('login'))
@app.route('/admin')
def admin_display():
    return render_template("admin_page.html", table=user_records)

@app.route('/purchase', methods=["GET", "POST"])
def purchase():
    if request.method == 'POST':
        store_route = request.form['store_route']
        item_name = request.form['item_name']
        item_price = request.form['item_price']
        item_location = request.form['item_location']

        print(store_route)
        store_route = str(store_route)
        """print("theses were the hidden values:") #testing pourposes
        print(item_name)
        print(item_price)
        print(item_location)"""

        pass_info = {"item_name": item_name, "item_price": item_price, "item_location": item_location}
        shopping_cart.append(pass_info)
        #get the id of the item (done)
            #get the page of the item
            #append the id of the item into the shopping cart
            #redirect user to the page that they were just at

        return redirect(store_route)

if __name__ == "__main__":
    user1 = UserTT(username = "John",password = "111111", email = "John@gmail.com")
    db.session.add(user1)
    db.session.commit()
    # runs the application on the repl development server
    app.run(debug=True, host='192.168.0.12', port='5000')
