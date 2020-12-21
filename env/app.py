# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import  BooleanField, StringField, PasswordField
from wtforms.validators import InputRequired,Email,Length



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
def home():
    return render_template("test.html")#home has to be under templates
"""

@app.route('/')
def index():
    return render_template("inventory.html") #this is a navbar for socks, shirts, shorts

@app.route('/contactus')
def contactus():
    return render_template("contactus.html") #this is the app route to the contact us page


@app.route('/database')
def signup():
    form = ItemForm()
    "Validate the forms"
    if form.validate_on_submit():
        new_item = items(type = form.type.data, name = form.name.data, price = form.price.data)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('contactus'))


    return render_template("Database test.html", form = form)

@app.route('/men')
def men():
    return render_template("men.html") #this is the app route to the men's page

@app.route('/women')
def women():
    items = [{"product":"t-shirt", "price":10},]
    return render_template("women.html", items = items) #this is the app route to the women's page


@app.route('/inventory')
def inventory():
    return render_template("inventory.html") #this is the app route to home page


if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True)