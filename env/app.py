# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


#create a Flask instance
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.sqlite3'
db = SQLAlchemy(app)
class students(db.Model):
    id = db.Column('item_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    type = db.Column(db.String(50))
    price = db.Column(db.Float(200))

def __init__(self, name, city, addr,pin):
    self.name = name
    self.city = city
    self.addr = addr
    self.pin = pin

db.create_all()

#connects default URL of server to a python function
@app.route('/')
def home():
    return render_template("test.html")#home has to be under templates

@app.route('inventory')
def inv():
    return render_template("inventory.html") #this is a navbar for socks, shirts, shorts

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True)