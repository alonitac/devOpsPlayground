from flask import Flask

app = Flask(__name__)

"""
ngnix1 (8080)       nginx2 (8081)
private-nginx       private-nginx
"""


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/<name>")
def hello(name):
    return f"Hello, {name}!"


app.run(host='0.0.0.0', port=8080)

