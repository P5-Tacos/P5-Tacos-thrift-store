from views.time_to_thrift import time_to_thrift_bp
from flask import Flask
#app = Flask(__name__)
#  connects default URL of server to a python function
app = Flask(__name__)

@time_to_thrift_bp.route('/')
def index():
    print("you have found the college board home page")
