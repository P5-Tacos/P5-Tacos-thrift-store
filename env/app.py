# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField
from wtforms.validators import InputRequired,Email,Length



#create a Flask instance
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.sqlite3'
db = SQLAlchemy(app)
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

db.create_all()

class ItemForm(FlaskForm):
    name = StringField('name',validators=[InputRequired(), Length(min=4,max=15)])
    type = StringField('type',validators=[InputRequired(), Length(min=8,max=80)])
    price = StringField('price',validators=[InputRequired(), Length(min=8,max=80)])
#connects default URL of server to a python function
"""@app.route('/')
def home():
    return render_template("test.html")#home has to be under templates
"""
@app.route('/')
def inv():
    return render_template("inventory.html") #this is a navbar for socks, shirts, shorts
def create():
    if request.form:
        """prepare data for primary table extracting from form"""
        user = Users(username=request.form.get("username"), password=request.form.get("password"))
        """add and commit data to user table"""
        db.session.add(user)
        db.session.commit()
        """prepare data for related tables extracting from form and using new UserID """
        userid = db.session.query(func.max(Users.UserID))
        email = Emails(email_address=request.form.get("email"), UserID=userid)
        phone_number = PhoneNumbers(phone_number=request.form.get("phone_number"), UserID=userid)
        """email table add and commit"""
        db.session.add(email)
        db.session.commit()
        """phone number table add and commit"""
        db.session.add(phone_number)
        db.session.commit()
    return redirect(url_for('pythondb_bp.databases'))
if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True)