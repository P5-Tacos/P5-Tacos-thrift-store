#this is where all the routes will go

from views.makeup_api import makeup_api_bp
from flask import Flask, render_template, request
import requests
import json
from views.makeup_api import model

app = Flask(__name__)

@makeup_api_bp.route('/') #this is the home page of the makeup API page
def index():
    return render_template("makeup_api/home.html")

@makeup_api_bp.route('/makeup_landing', methods=['GET', 'POST'])
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
            return render_template("makeup_api/makeup_landing.html", error_message=fail_response, link_list=model.makeup_redirects())
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
            return render_template("makeup_api/makeup_landing.html", imageUrlList=display_list, count=data_dict, link_list=model.makeup_redirects())
    test_list = []
    testing_text = ""
    # imageUrlList=test_list, text=testing_text, count=test_list,
    return render_template("makeup_api/makeup_landing.html", link_list=model.makeup_redirects())  # imageUrlList=display_list, text=response.text, count=data_dict  # Needs to be connected with jinja options
