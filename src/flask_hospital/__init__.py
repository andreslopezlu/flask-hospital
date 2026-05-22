from flask import Flask

from flask_hospital import config
from flask_hospital.extensions import db
from flask_hospital.routes.index.routes import index_bp


def create_app(config_class: type[config.DevelopmentConfig] = config.DevelopmentConfig) -> Flask:
    app: Flask = Flask(__name__)

    app.config.from_object(config_class)

    db.init_app(app)

    with app.app_context():
        from flask_hospital import models  # noqa: F401, PLC0415

        db.create_all()

    app.register_blueprint(index_bp)

    return app
