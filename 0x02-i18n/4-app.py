#!/usr/bin/env python3
"""
A basic flask app to configure babel
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
app.template_folder = 'templates'
babel = Babel(app)


class Config(object):
    """
    The config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    The locale selector
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    The index page
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
