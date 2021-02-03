# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, current_app
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, FileField, FloatField
from wtforms.validators import InputRequired, Length, NumberRange
import os
from sqlalchemy.dialects.sqlite import BLOB
from wtforms import StringField
from wtforms.validators import InputRequired, Length
from views.makeup_api import makeup_api_bp  # blueprint not a module
from views.easter_egg import easter_egg_bp
from views.database import database_bp


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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.sqlite3'
Bootstrap(app)
db = SQLAlchemy(app)
records = []

"Initialize Database with specific Items"


class items(db.Model):
    id = db.Column('item_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    type = db.Column(db.String(50))
    price = db.Column(db.Float(200))


def __init__(self, id, name, type, price, image):
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
    price = StringField('price', validators=[InputRequired(), NumberRange(min = 0.01, max = 100000,message = "Please enter a proper price")])
    image = FileField('image', validators=[InputRequired()])


"""Defining routes"""
app.register_blueprint(makeup_api_bp, url_prefix='/makeup_api')
app.register_blueprint(easter_egg_bp, url_prefix='/easter_egg')
app.register_blueprint(database_bp, url_prefix='/database')


#  connects default URL of server to a python function
@app.route('/')
def index():
    #  function use Flask import (Jinga) to render an HTML template
    return render_template("home.html", inventory_list1=thriftythreadsdata.inventory_itemsTT(),
                           inventory_list2=barbarelladata.inventory_itemsBB())


@app.route('/storefront')
def storefront():
    return render_template("storefront.html", cards=websitecards.CardsForStores())


@app.route('/contactus')
def contactus():
    return render_template("contactus.html",
                           images=contactimages.grouppictures())  # this is the app route to the contact us page


#  displaying all the current items in the data bases

def list_map():  # mapping the front end to the backend, put in the function so we don't have to copy and paste this all the time
    item = items.query.all()
    for item in item:
        user_dict = {'id': item.id, 'name': item.name, 'type': item.type, 'price': item.price}
        records.append(user_dict)


list_map()  # running once, appends database items into list user sees


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
    return render_template("Database test.html", form=form, table=records)

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
    return render_template("login.html")


@app.route('/thriftythreads')
def thriftythreads():
    return render_template("gallery.html", inventory_list=thriftythreadsdata.inventory_itemsTT(),
                           Store_Title="Thrifty Threads")  # this is the app route to the ThriftTHreads's page


@app.route('/barbarella')
def barbarella():
    return render_template("gallery.html", inventory_list=barbarelladata.inventory_itemsBB(),
                           Store_Title="Barbarella")  # this is the app route to Barbarella's page


if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True, host='192.168.0.12', port='5000')
