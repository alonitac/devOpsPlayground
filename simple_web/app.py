import time
from flask import Flask

# fore reference https://flask.palletsprojects.com/en/2.0.x/quickstart/#a-minimal-application
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


app.run(host='0.0.0.0', port=5000)


















