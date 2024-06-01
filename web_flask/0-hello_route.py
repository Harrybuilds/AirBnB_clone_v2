#!/usr/bin/python3
# module to use flask web framework

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/")
def greeting():
    """ greet """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
