#!/usr/bin/env python3
"""Flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel


# create configuration object
class Config:
    """class to configure languages in the app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# create a flask instance
app = Flask(__name__)

# configure flask app
app.config.from_object(Config)

# instantiate babel
babel = Babel()


def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


# route for index page
@app.route("/")
def index():
    """index page"""
    return render_template('2-index.html')


if __name__ == "__main__":
    """run app when executed directly"""
    app.run(host="127.0.0.1", port=5000, debug=True)
