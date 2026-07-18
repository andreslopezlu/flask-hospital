import os
from pathlib import Path

from flask_hospital.utils import get_project_root

current_folder: Path = Path(__file__).resolve().parent
root_folder: str = get_project_root(current_folder)


class BasicConfig:
    SECRET_KEY: str | None = os.getenv("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(BasicConfig):
    DEBUG = True
    DEV_DB_PATH: Path = Path(root_folder) / "dev.db"
    SQLALCHEMY_DATABASE_URI: str = f"sqlite:///{DEV_DB_PATH}"


class TestConfig(BasicConfig):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///:memory:"
    WTF_CSRF_ENABLED = False


class ProdConfig(BasicConfig):
    DB_URL: str | None = os.getenv("DATABASE_URL")
