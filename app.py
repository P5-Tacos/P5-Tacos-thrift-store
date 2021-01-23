# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Length
import requests
import json

import thriftythreadsdata
import barbarelladata
import contactimages
import websitecards
import makeupdata

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
    price = StringField('price', validators=[InputRequired(), Length(min=1, max=80)])


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


list_map()


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


# CRUD delete
@app.route('/delete/', methods=['GET', "POST"])
def delete():
    # print("arrived to delete")

    if request.method == "POST":  # we know the item id
        userid = request.form["item_id"]
        found_values = []
        for dictionary in records:
            if (dictionary["id"] == float(userid)):
                # print("we found it")
                found_values.append(dictionary)
                delete = items.query.filter_by(id=float(userid)).first()
                db.session.delete(delete)
                db.session.commit()
                print("after delete")

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

@app.route('/amazon_api',  methods=['GET', 'POST'])
def amazon():
    #imageUrlList = "this represents the data from the API" #
    url = "http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline"

    querystring = {"product_category":"lipstick","brand":"colourpop"}

    headers = {
        'x-rapidapi-key': "5d6a7f4252msh63f17827aaa3826p1cce67jsn7ced6dd4e974",
        'x-rapidapi-host': "makeup.p.rapidapi.com"
    }
    data_JSON = requests.request("GET", url, headers=headers, params=querystring)
    response = requests.request("GET", url, headers=headers)
    print(response.text)
    response_list = response.text
    #print(response[0])
    #print(response.text[])

    data_dict = json.loads(str(response.text))
    print(data_dict)
    """b = 0
    #id = response.json().get('id')
    print(response[0])
    print("all the dictonaries in a new line") #from this test we understand that we are printing all the characters shown in the json file
    for x in range(len(response.text)):  # this prints all values in the data base
        print(response.text[b])
        b = b+1
    print(b)"""

    display_list = [] #this is the list that is passed to the template
    b = 0
    for item in data_dict:
        id = str(response.json()[b]['id'])
        brand = response.json()[b]['brand']
        name = response.json()[b]['name']
        price = response.json()[b]['price']
        image_link = response.json()[b]['image_link']
        product_link = response.json()[b]['product_link']
        website_link = response.json()[b]['website_link']
        description = response.json()[b]['description']
        rating = response.json()[b]['rating']
        category = response.json()[b]['category']
        product_type = response.json()[b]['product_type']
        tag_list = response.json()[b]['tag_list']
        info = {"id":id, "tag_list": tag_list, "product_type": product_type, "category":category, "rating": rating, "website_link": website_link, "product_link": product_link, "image_link":image_link,"name": name, "brand":brand, "description": description,"price": price}
        display_list.append(info)
        b = b + 1

    test = [{},{},{}]
    id = response.json()[0]['product_type']
    print("printing id " + str(id))
    return render_template("gallery_makeup.html", imageUrlList=display_list, text=response.text, count=data_dict)


@app.route('/makeup_landing', methods=['GET', 'POST'])
def makeup_landing():
    url = "http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline" #default
    if request.method == 'POST':
        option = request.form['makup_options']
        url = "http://makeup-api.herokuapp.com/api/v1/products.json?brand=" + str(option)

        querystring = {"product_category":"lipstick","brand":"colourpop"}

        headers = {
            'x-rapidapi-key': "5d6a7f4252msh63f17827aaa3826p1cce67jsn7ced6dd4e974",
            'x-rapidapi-host': "makeup.p.rapidapi.com"
        }
        #data_JSON = requests.request("GET", url, headers=headers, params=querystring)
        response = requests.request("GET", url, headers=headers)
        print(response.text)
        fail_condition ="[]" #this represents an empty json
        fail_response = "the json file requested is empty"

        if response.text == fail_condition:
            return render_template("makeup_landing.html", error_message=fail_response, link_list=makeupdata.makeup_redirects())
        else:

            data_dict = json.loads(str(response.text))
            print(data_dict)

            display_list = []  # this is the list that is passed to the template
            b = 0
            for item in data_dict:
                id = str(response.json()[b]['id'])
                brand = response.json()[b]['brand']
                name = response.json()[b]['name']
                price = response.json()[b]['price']
                image_link = response.json()[b]['image_link']
                product_link = response.json()[b]['product_link']
                website_link = response.json()[b]['website_link']
                description = response.json()[b]['description']
                rating = response.json()[b]['rating']
                category = response.json()[b]['category']
                product_type = response.json()[b]['product_type']
                tag_list = response.json()[b]['tag_list']
                info = {"id":id, "tag_list": tag_list, "product_type": product_type, "category":category, "rating": rating, "website_link": website_link, "product_link": product_link, "image_link":image_link,"name": name, "brand":brand, "description": description,"price": price}
                display_list.append(info)
                b = b + 1

            id = response.json()[0]['product_type']
            print("printing id " + str(id))
            return render_template("makeup_landing.html", imageUrlList=display_list, count=data_dict, link_list=makeupdata.makeup_redirects())
    test_list = []
    testing_text = ""
    # imageUrlList=test_list, text=testing_text, count=test_list,
    return render_template("makeup_landing.html", link_list=makeupdata.makeup_redirects())  # imageUrlList=display_list, text=response.text, count=data_dict  # Needs to be connected with jinja options


@app.route('/thriftythreads')
def thriftythreads():
    return render_template("gallery.html", inventory_list=thriftythreadsdata.inventory_itemsTT(),
                           Store_Title="Thrifty Threads")  # this is the app route to the ThriftTHreads's page


@app.route('/barbarella')
def barbarella():
    return render_template("gallery.html", inventory_list=barbarelladata.inventory_itemsBB(),
                           Store_Title="Barbarella")  # this is the app route to Barbarella's page


@app.route('/TT1')
def TT1():
    return render_template("clothes_info.html",
                           data=thriftythreadsdata.TT1())  # takes the variables and sticks it in to the template


@app.route('/TT2')
def TT2():
    return render_template("clothes_info.html", data=thriftythreadsdata.TT2())


@app.route('/TT3')
def TT3():
    return render_template("clothes_info.html", data=thriftythreadsdata.TT3())


@app.route('/TT4')
def TT4():
    return render_template("clothes_info.html", data=thriftythreadsdata.TT4())

if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True, host='192.168.0.12', port='5000')

