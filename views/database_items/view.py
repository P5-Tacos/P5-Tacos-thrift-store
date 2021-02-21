from views.database_items import database_items_bp
# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import FileField
import os
from wtforms import StringField
from wtforms.validators import InputRequired, Length
from sqlalchemy.dialects.sqlite import BLOB



records = []

#from models.__init__ import *
#from models.crud_items import *
#from views.app import shopping_cart_pass

# create a Flask instance
"Setting up the keys are needed for the database"
app = Flask(__name__)
#app.config['SECRET_KEY'] = ':)'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.sqlite3' #note this database is contianed within the UsersTT database
db = SQLAlchemy(app)

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

MYDIR = ("static\images\owner_upload")
CHECK_FOLDER = os.path.isdir(MYDIR)

# If folder doesn't exist, then create it.
if not CHECK_FOLDER:
    os.makedirs(MYDIR)
    print("created folder : ", MYDIR)

else:
    print(MYDIR, "folder already exists.")

#this is for the bootstrap forms
class ItemForm(FlaskForm):
    name = StringField('name', validators=[InputRequired(), Length(min=1, max=15)])
    type = StringField('type', validators=[InputRequired(), Length(min=1, max=80)])
    price = StringField('price', validators=[InputRequired()])
    image = FileField('image', validators=[FileRequired(),FileAllowed(['png', 'pdf', 'jpg'], "Nerd")])

"""@database_items_bp.route('/') #this is the home page of the makeup API page
def index():
    return render_template("database_items/index.html")"""

item = items.query.all()
for item in item:
    user_dict = {'id': item.id, 'name': item.name, 'type': item.type, 'price': item.price}
    records.append(user_dict)

#views/database_items/template/database_items/testing_hello.html

@database_items_bp.route('/')
def index():
    return render_template('database_items/index.html')

#@database_items_bp.route('/database', methods=['GET', 'POST'])  # contribution by Andrew
@database_items_bp.route('/testing_action', methods=['GET', 'POST'])  # contribution by Andrew
def shop_owner():
    form = ItemForm()
    "Validate the forms"
    print("arrived to items_bluprint")

    if form.validate_on_submit():  # adding in all
        #getting the information from the form, formating it in a way to pass into database
        new_item = items(type=form.type.data, name=form.name.data, price=form.price.data)
        #adding new row into database
        db.session.add(new_item)
        #commiting changes to database
        db.session.commit()
        print("completed creating to the database")

        #formating information for the front end
        user_dict = {'id': new_item.id, 'name': new_item.name, 'type': new_item.type, 'price': new_item.price}
        #appending information onto the front end data
        records.append(user_dict)
        print("completed updating front end")

        #abstracting the image that was passed through the form
        f = form.image.data
        #creating a name for the image
        filename = str(new_item.id) + ".jpg"
        #saving the image in the "MYDIR" location with the created filename
        f.save(os.path.join(MYDIR, filename))#the saving image is loading
        print("completed uploading image to correct folder")

    #renders the same page with updated front end information
    return render_template("database_items/database_items.html", form=form, table=records, gallery=records)#, display_cart=shopping_cart_pass.shopping_cart
    #return redirect(url_for('database_items_bp.index'))

@database_items_bp.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    # Appending app path to upload folder path within app root folder
    uploads = os.path.join(current_app.root_path, app.config['owner_upload'])
    # Returning file from appended path
    return send_from_directory(directory=uploads, filename=filename)


# CRUD delete
@database_items_bp.route('/delete/', methods=['GET', "POST"])
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
                #print("after delete")  # for debuggin in the terminla

            for i in range(len(records)):  # deleting the front end view of the data base
                if records[i]['id'] == float(userid):
                    del records[i]
                    break
    else:
        print("could not find the value")

    return redirect(url_for('database_items_bp.shop_owner'))
