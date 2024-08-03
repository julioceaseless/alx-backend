#!/usr/bin/env python3
"""Flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


# create configuration object
class Config:
    """class to configure languages in the app"""
    LANGUAGES = ["de", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# language selector
def get_locale() -> str:
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False


babel = Babel(app, locale_selector=get_locale)


# route for index page
@app.route("/")
def index() -> str:
    """index page"""
    return render_template('3-index.html')


if __name__ == "__main__":
    """run app when executed directly"""
    app.run(host="0.0.0.0", port=5000, debug=True)
