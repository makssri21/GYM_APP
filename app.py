from flask import render_template
from init import create_app, db

app = create_app()

@app.route('/')
def index():
    return render_template('pages/home.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)