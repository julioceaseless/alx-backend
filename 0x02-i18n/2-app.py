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


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """get locale"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# route for index page
@app.route("/")
def index():
    """index page"""
    print(request.headers)
    return render_template('3-index.html')


if __name__ == "__main__":
    """run app when executed directly"""
    app.run(host="127.0.0.1", port=5000, debug=True)
