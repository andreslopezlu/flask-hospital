from flask import Blueprint

index_bp = Blueprint("index", __name__)


@index_bp.route("/")
def home() -> str:
    return "Hola inmundo animal"
