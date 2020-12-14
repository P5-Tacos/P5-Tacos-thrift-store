# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template

#create a Flask instance
app = Flask(__name__)

#InfoDb = []

#connects default URL of server to a python function
@app.route('/')
def home():
    return render_template("test.html")#home has to be under templates

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True)