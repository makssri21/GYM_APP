from flask import Blueprint
from controllers.adminControllers import admin_dashboard

admin = Blueprint('admin', __name__)


admin.route('/admin_dashboard')(admin_dashboard)