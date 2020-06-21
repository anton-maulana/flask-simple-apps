import sys

from flask import Flask
from flask_cors import CORS

from controllers import *

def create_app():
    app = Flask('fraud_detection')
    app.config.from_pyfile('./app.cfg')

    app.register_blueprint(HomeController)
    CORS(app)
    return app