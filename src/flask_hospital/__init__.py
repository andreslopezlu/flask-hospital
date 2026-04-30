from flask import Flask

from flask_hospital.config import DevelopmentConfig
from flask_hospital.routes.index.routes import index_bp


def create_app() -> Flask:
    app = Flask(__name__)

    app.config.from_object(DevelopmentConfig)

    app.register_blueprint(index_bp)

    return app
