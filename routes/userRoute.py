from flask import Blueprint
from controllers.userControllers import home, successSubmit

user = Blueprint('user', __name__)

user.route('/')(home)   # HOME
