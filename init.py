from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    from models.Roles import Roles
    from models.Users import Users
    from models.RequestStatuses import RequestStatuses

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(Users, int(user_id))

    # Import tek nakon što je db inicijalizovan
    from routes.authRoute import auth
    from routes.userRoute import user
    from routes.adminRoute import admin

    app.register_blueprint(auth)
    app.register_blueprint(user)
    app.register_blueprint(admin)
    
    return app
