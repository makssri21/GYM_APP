from flask import render_template
from init import create_app, db
from flask_migrate import Migrate

app = create_app()
app.config.from_object('config')

migrate = Migrate(app, db)

# blueprints (ako postoje importi)
# from routes import user, auth, admin
# app.register_blueprint(user, url_prefix='/')
# app.register_blueprint(auth, url_prefix='/')
# app.register_blueprint(admin, url_prefix='/')

@app.route('/')
def index():
    return render_template('pages/home.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)