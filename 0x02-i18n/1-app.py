#!/usr/bin/env python3
"""Basic Babel setup"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)

# Instantiate Babel object
babel = Babel(app)


class Config:
    """
    Configuration class for Flask app,
    Set Babel’s default locale ("en") and timezone ("UTC")
    """
    # Available languages
    LANGUAGES = ["en", "fr"]

    # Babel configuration
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index():
    """
    Route handler for the root URL.
    Renders the index.html template.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
