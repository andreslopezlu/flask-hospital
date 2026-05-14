from flask import Flask

from flask_hospital.config import DevelopmentConfig
from flask_hospital.db import db
from flask_hospital.routes.index.routes import index_bp


def create_app() -> Flask:
    app: Flask = Flask(__name__)

    app.config.from_object(DevelopmentConfig)

    db.init_app(app)

    with app.app_context():
        from flask_hospital import models  # type: ignore[import-untyped]  # noqa: F401, PLC0415

        db.create_all()

    app.register_blueprint(index_bp)

    return app
