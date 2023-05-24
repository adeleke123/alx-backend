#!/usr/bin/env python3
"""Get locale from request"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

# Instantiate Babel object
babel = Babel(app)


class Config:
    """
    Configuration class for Flask app,
    Set Babel’s default locale ("en") and timezone ("UTC")
    """
    LANGUAGES = ["en", "fr"]

    # Babel configuration
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Locale selector function for Babel.
    Determines the best-matching language based on user's preferences.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Route handler for the root URL.
    Renders the index.html template.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
