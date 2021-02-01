"""__init.py__ has responsibility of defining interfaces for blueprint"""
from flask import Blueprint

easter_egg_bp = Blueprint('easter_egg_bp',__name__,
template_folder='templates',
static_folder='static'
)

from . import view #getting the rest of the routes into this file

