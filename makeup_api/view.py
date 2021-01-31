#this is where all the routes will go

from makeup_api import makeup_api_bp
from flask import Flask, render_template
#from makeup_api.model import test_list

app = Flask(__name__)

@makeup_api_bp.route('/') #this is the home page of the makeup API page
def index():
    return render_template("makeup_api/home.html")