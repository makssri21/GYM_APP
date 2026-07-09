import os
from flask import jsonify, render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required
from datetime import datetime
from werkzeug.utils import secure_filename
import config
from models.Users import Users
from flask import request, jsonify
def login_page():
    return render_template('/pages/login.html')

def home():
    return render_template('pages/home.html')

def successSubmit():
    return "Success"
    