import os
from pathlib import Path

from flask_hospital.utils import get_project_root

current_folder: Path = Path(__file__).resolve().parent
root_folder: str = get_project_root(current_folder)


class BasicConfig:
    SECRET_KEY: str | None = os.environ.get("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BasicConfig):
    DB_USER: str | None = os.environ.get("DB_USER")
    DB_PASSWORD: str | None = os.environ.get("DB_PASSWORD")
    DB_PORT: int = 3306
    DB_NAME: str = "flask_hospital_db"
    MYSQL_DATABASE_URI: str = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@localhost:{DB_PORT}/{DB_NAME}"


# --- INICIO DEL HACKEO INFALIBLE ---
# Forzamos a Python a mirar dentro de la carpeta 'src',
# sin importar desde dónde o cómo ejecutes el archivo.
# ruta_src = str(Path(__file__).resolve().parent.parent)
# if ruta_src not in sys.path:
#     sys.path.insert(0, ruta_src)
# --- FIN DEL HACKEO ---
