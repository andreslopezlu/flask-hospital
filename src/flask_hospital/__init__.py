import os

from flask import Flask

from flask_hospital import config
from flask_hospital.extensions import db, login, migrate
from flask_hospital.routes.index.routes import index_bp

configuration: type[config.BasicConfig | config.DevConfig | config.TestConfig | config.ProdConfig] | None = None
ENVIRONMENT_TYPE: str | None = os.getenv("ENV")

if ENVIRONMENT_TYPE == "BASIC":
    configuration = config.BasicConfig
elif ENVIRONMENT_TYPE == "DEV":
    configuration = config.DevConfig
elif ENVIRONMENT_TYPE == "TEST":
    configuration = config.TestConfig
elif ENVIRONMENT_TYPE == "PROD":
    configuration = config.ProdConfig


def create_app(
    config_class: type[config.BasicConfig | config.DevConfig | config.TestConfig | config.ProdConfig]
    | None = configuration,
) -> Flask:
    app: Flask = Flask(__name__)

    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)  # type: ignore

    with app.app_context():
        from flask_hospital import models  # noqa: F401, PLC0415

    app.register_blueprint(index_bp)

    return app
