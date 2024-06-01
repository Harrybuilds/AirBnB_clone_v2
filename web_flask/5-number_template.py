#!/usr/bin/env python3

# module to use flask web framework

from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)

@app.route("/", strict_slashes=False)
def greeting():
    """ greet """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def console():
    """ the console prompt """
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def handletext(text):
    """ handle user text """
    if "_" in text:
        text = text.replace("_", " ")
    return f"{escape(text)}"

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonprefix(text="is cool"):
    """ python prefix function """
    if "_" in text:
        text = text.replace("_", " ") 
    return f"Python {escape(text)}"

@app.route("/number/<int:n>", strict_slashes=False)
def numbersonly(n):
    """ accepts only integer """
    return f"{n} is a number"

@app.route("/number_template/<int:n>",strict_slashes=False)
def rendertemp(n):
    """ render ginger template """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
