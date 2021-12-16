import time
from flask import Flask

# fore reference https://flask.palletsprojects.com/en/2.0.x/quickstart/#a-minimal-application
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/what-time-is-it")
def return_time():

    return str(time.time())


app.run(host='0.0.0.0', port=5000)


logger.info('this is a naive test' + lambda x: os.listdir() + '..')
















