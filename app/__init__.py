from flask import Flask
from flask_bootstrap import Bootstrap
from .routes.rutes import app_router


def create_app():
    app = Flask(__name__)

    app.register_blueprint(app_router)

    Bootstrap(app)

    return app