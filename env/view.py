# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Length
import thriftythreadsdata
import barbarelladata

#create a Flask instance
"Setting up the keys are needed for the database"
app = Flask(__name__)
app.config['SECRET_KEY'] = ':)'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.sqlite3'
Bootstrap(app)
db = SQLAlchemy(app)
"Initialize Database with specific Items"
class items(db.Model):
    id = db.Column('item_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    type = db.Column(db.String(50))
    price = db.Column(db.Float(200))

def __init__(self, id, name, type, price):
    self.name = name
    self.id = id
    self.type = type
    self.price = price
"Create Database"
db.create_all()

"Initialize the form that will retrieve data from the HTML page,flaskwtf form"
class ItemForm(FlaskForm):
    name = StringField('name',validators=[InputRequired(), Length(min=1,max=15)])
    type = StringField('type',validators=[InputRequired(), Length(min=1,max=80)])
    price = StringField('price',validators=[InputRequired(), Length(min=1,max=80)])
#connects default URL of server to a python function

"""@app.route('/')
def index():
    return render_template("inventory.html") #this the the first landing page that the user enters"""

@app.route('/')
def index():
    #function use Flask import (Jinga) to render an HTML template
    return render_template("home.html", inventory_list=thriftythreadsdata.inventory_itemsTT())

@app.route('/contactus')
def contactus():
    return render_template("contactus.html") #this is the app route to the contact us page

@app.route('/database', methods = ['GET','POST']) #contribution by Andrew
def signup():
    form = ItemForm()
    "Validate the forms"
    if form.validate_on_submit():
        new_item = items(type = form.type.data, name = form.name.data, price = form.price.data)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('contactus'))
    return render_template("Database test.html", form = form)

@app.route('/thriftythreads')
def thriftythreads():
    return render_template("gallery.html", inventory_list=thriftythreadsdata.inventory_itemsTT(), Store_Title="Thrifty Threads") #this is the app route to the ThriftTHreads's page

@app.route('/barbarella')
def barbarella():
    return render_template("gallery.html", inventory_list=barbarelladata.inventory_itemsBB(), Store_Title="Barbarella") #this is the app route to Barbarella's page

@app.route('/TT1')
def TT1():
    return render_template("clothes_info.html", data = thriftythreadsdata.TT1()) #takes the variables and sticks it in to the template

@app.route('/TT2')
def TT2():
    return render_template("clothes_info.html", data = thriftythreadsdata.TT2())

@app.route('/TT3')
def TT3():
    return render_template("clothes_info.html", data = thriftythreadsdata.TT3())

@app.route('/TT4')
def TT4():
    return render_template("clothes_info.html", data = thriftythreadsdata.TT4())


if __name__ == "__main__":
    app.run(debug=True)