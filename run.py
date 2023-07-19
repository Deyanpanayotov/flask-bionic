from flask import Flask, render_template
from app import server

app = Flask(__name__)

@app.route('/')
def render_dash_app():
    from app import app as dash_app
    return render_template('index.html', dash_app=dash_app.layout)

if __name__ == '__main__':
    app.run(debug=True)
