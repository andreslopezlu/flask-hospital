from typing import Any

import click
import mysql.connector
from flask import current_app, g
from mysql.connector.abstracts import MySQLConnectionAbstract, MySQLCursorAbstract
from mysql.connector.pooling import PooledMySQLConnection


def get_db() -> PooledMySQLConnection | MySQLConnectionAbstract | Any:

    if "db" not in g:
        g.db = mysql.connector.connect(
            host=current_app.config["MYSQL_HOST"],
            user=current_app.config["MYSQL_USER"],
            password=current_app.config["MYSQL_PASSWORD"],
            database=current_app.config["MYSQL_DATABASE"],
        )

    return g.db


def close_db() -> None:
    db: PooledMySQLConnection | MySQLConnectionAbstract | Any = g.pop("bd", None)

    if db is not None:
        db.close()


def init_db():
    db: PooledMySQLConnection | MySQLConnectionAbstract | Any = get_db()
    cursor: MySQLCursorAbstract | Any = db.cursor()

    with current_app.open_resource("schema.sql") as f:
        sql_commands: Any = f.read().decode("utf-8")

        for i in cursor.execute(sql_commands, multi=True):
            pass

    db.commit()
    cursor.close()


@click.command("init-db")
def init_db_command() -> None:
    init_db()
    click.echo("Database initialized")


def init_app(app) -> None:
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
