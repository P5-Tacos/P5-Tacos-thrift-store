#this is where all the routes will go

from views.easter_egg import easter_egg_bp
from flask import Flask, render_template

app = Flask(__name__)

@easter_egg_bp.route('/') #this is the home page of the makeup API page
def index():
    return render_template("easter_egg/home.html")
