from flask_login import LoginManager  # type: ignore
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db: SQLAlchemy = SQLAlchemy()
migrate: Migrate = Migrate()
login = LoginManager()
login.login_view = "login"  # type: ignore
