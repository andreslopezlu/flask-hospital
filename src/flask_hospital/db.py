from flask_sqlalchemy import SQLAlchemy


def create_db() -> SQLAlchemy:
    return SQLAlchemy()
