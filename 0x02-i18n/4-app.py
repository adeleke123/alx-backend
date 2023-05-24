#!/usr/bin/env python3
"""
Force locale with URL parameter
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Configuration class for the Flask app.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Determine the best match with the supported languages
    if locale parameter is present in the request & supported locale,
    return it.
    """
    locale = request.args.get('locale')
    if locale:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Render the index template with parametrized messages.
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
