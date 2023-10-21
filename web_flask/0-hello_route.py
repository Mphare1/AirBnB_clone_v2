#!/usr/bin/python3
from flask import Flask
"""
intialise flask web app to listen on 0.0.0.0:5000
"""
application = Flask(__name__)

@application.route('/', strict_slashes=False)
def hello_world():
    """
    display "Hello HBNB!"
    """
    return ('Hello HBNB!')


if __name__ == "__main__":
    application.run()
