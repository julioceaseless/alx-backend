#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, render_template

# create a flask instance
app = Flask(__name__)


# route for index page
@app.route("/")
def index():
    """index page"""
    return render_template('0-index.html')


if __name__ == "__main__":
    """run app when executed directly"""
    app.run(host="127.0.0.1", port=5000, debug=True)
