#!/usr/bin/env python3
"""
Parametrize templates
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

# Instantiate Babel object
babel = Babel(app)


# Config class for Flask app
class Config:
    """
    Configuration class for Flask app,
    Set Babel’s default locale ("en") and timezone ("UTC")
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Locale selector function for Babel.
    Determines the best-matching language based on the user's preferences.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    Render the index template with parametrized messages.
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
