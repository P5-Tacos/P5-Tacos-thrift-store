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

@easter_egg_college_bp.route('/AP_CSP_Requirements')
def AP_CSP_requirements():
    return render_template("easter_egg_college/AP CSP Requirements Reflection.html")

@easter_egg_college_bp.route('/who_am_i')
def who_am_i():
    return render_template("easter_egg_college/who_am_i.html")

