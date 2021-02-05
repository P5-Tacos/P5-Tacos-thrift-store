#this is where all the routes will go

from views.easter_egg_college import easter_egg_college_bp
from flask import Flask, render_template

app = Flask(__name__)

@easter_egg_college_bp.route('/')
def index():
    print("you have found the college board home page")
    return render_template("easter_egg_college/home.html")

@easter_egg_college_bp.route('/college_board_requirements')
def college_req():
    return render_template("easter_egg_college/college_board_requirements.html")
