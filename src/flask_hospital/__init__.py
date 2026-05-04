from typing import TYPE_CHECKING

from flask import Flask

from flask_hospital.config import DevelopmentConfig
from flask_hospital.db import create_db
from flask_hospital.routes.index.routes import index_bp

if TYPE_CHECKING:
    from flask_sqlalchemy import SQLAlchemy


def create_app() -> Flask:
    app = Flask(__name__)

    app.config.from_object(DevelopmentConfig)

    db: SQLAlchemy = create_db()
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(index_bp)

    return app
