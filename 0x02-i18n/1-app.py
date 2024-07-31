#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, render_template
from flask_babel import Babel

# create a flask instance
app = Flask(__name__)

# instantiate babel
babel = Babel(app)


# create configuration object
class Config:
    """class to configure languages in the app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# configure flask app
app.config.from_object(Config)


# route for index page
@app.route("/")
def index():
    """index page"""
    return render_template('0-index.html')


if __name__ == "__main__":
    """run app when executed directly"""
    app.run(host="127.0.0.1", port=5000, debug=True)
