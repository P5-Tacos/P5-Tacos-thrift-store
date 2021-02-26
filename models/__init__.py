"""import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

"""
"""from flask import Flask
app = Flask(__name__)

dbURI = 'sqlite:///models/myDB.db'

#database setup to support db examples
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SECRET_KEY'] = 'SECRET_KEY'
db = SQLAlchemy(app)"""
"""
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
"""
"""
#db.create_all()

######################################
#### SET UP OUR SQLite DATABASE #####
####################################

# This grabs our directory
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data_food.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#OMG SO IMPORTANT TO INCLUDE THIS ABOVE! Warnings up the wazoo if not here on a develoment server.

db = SQLAlchemy(app)

class UserDN(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, user_id, username, email, password):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"{self.user_id},{self.username}, {self.email}, {self.password}"

class OrderEE(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=True)
    price = db.Column(db.Integer, unique=False, nullable=False)
    order_contents = db.Column(db.String(1000), unique=False, nullable=False)
    time = db.Column(db.DateTime, primary_key=True)

    def __init__(self, user_id, price, order_contents, time):
        self.user_id = user_id
        self.price = price
        self.order_contents = order_contents
        self.time = time

    def __repr__(self):
        return f"{self.user_id},{self.price}, {self.order_contents}, {self.time}"
"""
"""
class Score(db.Model):
    __tablename__ = 'scores'
    id = db.Column(db.Integer, primary_key=True)
    # not planning to delete scores, but still a good practice
    p_name = db.Column(db.String(10), unique=False, nullable=False)
    p_score = db.Column(db.Integer, unique=False, nullable=False) # want score as int so we can sort by it easily.
    p_game = db.Column(db.String(10), unique=False, nullable=False)

    def __init__(self, p_name, p_score, p_game):
        self.p_name = p_name
        self.p_score = p_score
        self.p_game = p_game

    def __repr__(self):
        return f"{self.p_name},{self.p_score}, {self.p_game}"
"""
#must go after 'models'
#db.create_all();
