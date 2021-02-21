from views.database_items import database_items_bp
from flask import Flask, render_template, request

@database_items_bp.route('/') #this is the home page of the makeup API page
def index():
    return render_template("database_items/index.html")

#views/database_items/template/database_items/testing_hello.html