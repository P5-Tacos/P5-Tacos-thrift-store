"""__init.py__ has responsibility of defining interfaces for blueprint"""
from flask import Blueprint

database_items_bp = Blueprint('database_items_bp',__name__,
                          template_folder='templates',
                          static_folder='static'
                          )

from . import view #getting the rest of the routes into this file

