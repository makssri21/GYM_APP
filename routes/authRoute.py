from flask import Blueprint
from controllers.authControllers import login, logout

auth = Blueprint('auth', __name__)

auth.route('/login', methods=['GET','POST'])(login)
auth.route('/logout')(logout)
