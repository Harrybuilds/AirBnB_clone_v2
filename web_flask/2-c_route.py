#!/usr/bin/python3
""" module to use flask web framework """

from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def greeting():
    """ greet """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def console():
    """ the console """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def handletext(text):
    """ handle  user input """
    if "_" in text:
        text = text.replace("_", " ")
    return f"{escape(text)}"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
