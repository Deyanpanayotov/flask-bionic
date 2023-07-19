from flask import Flask, render_template
from app import app

application = Flask(__name__)

@application.route('/')
def render_dash_app():
    return render_template('index.html', dash_app=app.layout)

if __name__ == '__main__':
    application.run(debug=True)
