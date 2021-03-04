from flask_sqlalchemy import SQLAlchemy

# create a Flask instance
"Setting up the keys are needed for the database"
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from app import app

app.config['SECRET_KEY'] = ':)'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///UsersTT.db'
#Bootstrap(app)
db = SQLAlchemy(app)

class UserTT(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50))
    password = db.Column(db.String(80))
    shopping_cart_column = db.Column(db.String(8000), nullable=False)
    authen = db.Column(db.String(50))

    def __init__(self, username, email, password,authen, shopping_cart_column):
        self.username = username
        self.email = email
        self.password = password
        self.authen = authen
        self.shopping_cart_column = shopping_cart_column

    pass

class items(db.Model):
    id = db.Column('item_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    type = db.Column(db.String(50))
    price = db.Column(db.String(200))


    def __init__(self, name, type, price):
        self.name = name
        self.type = type
        self.price = price
    pass

class userDN(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50))
    password = db.Column(db.String(80))
    program = db.Column(db.String(50))

    def __init__(self, username, email, password, program):
        self.username = username
        self.email = email
        self.password = password
        self.program = program

    pass

class orderEE(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15))
    price = db.Column(db.Integer, unique=False, nullable=False)
    order_contents = db.Column(db.String(1000), unique=False, nullable=False)
    time = db.Column(db.DateTime, primary_key=True)

    def __init__(self, price,username, order_contents, time):
        self.username = username
        self.price = price
        self.order_contents = order_contents
        self.time = time
    pass

class userEE(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    pass

class userRR(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    pass

"Create Database"
db.create_all()
