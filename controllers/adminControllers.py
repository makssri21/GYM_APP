import os
from flask import jsonify, render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required
from datetime import datetime
from werkzeug.utils import secure_filename
import config
from models.Users import Users
from flask import request, jsonify

@login_required
def admin_dashboard():
    if not current_user.is_authenticated:
        flash('Molimo prijavite se da biste pristupili ovoj stranici.', category='error')
        return redirect(url_for('auth.login'))

    return render_template('pages/admin_dashboard.html')
