#!/usr/bin/env python3

# module to use flask web framework

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def greeting():
    """ greet """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def console():
    """ Thr console prompt """
    return "HBNB"

if __name__ == "__main__":
    app.run(host='0.0.0.0')