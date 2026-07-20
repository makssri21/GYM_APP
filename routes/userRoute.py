from flask import Blueprint
from controllers.userControllers import home, successSubmit, submit_request

user = Blueprint('user', __name__)

user.route('/home', methods=["GET"])(home)
user.route('/submit_request', methods=["POST"])(submit_request)