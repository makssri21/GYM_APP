import os
from flask import jsonify, render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required
from datetime import datetime
from werkzeug.utils import secure_filename
import config
from models.Users import Users
from models.Requests import Requests
from models.RequestStatuses import RequestStatuses
from flask import request, jsonify
from init import db
def login_page():
    return render_template('/pages/login.html')

def home():
    return render_template("pages/home.html")

@login_required
def submit_request():

    request_title = request.form.get("RequestTitle")
    date_of_birth = request.form.get("DateOfBirth")
    place = request.form.get("Place")
    comment = request.form.get("Comment")

    new_request = Requests(
        RequestTitle=request_title,
        DateOfBirth=datetime.strptime(date_of_birth, "%Y-%m-%d").date(),
        Place=place,
        Comment=comment,
        CreatedBy=current_user.Username,
        RequestStatusId=1
    )

    db.session.add(new_request)
    db.session.commit()

    flash("Zahtjev je uspješno poslan.", "success")
    return redirect(url_for("user.home"))

def successSubmit():
    return "Success"
    