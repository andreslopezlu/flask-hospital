from typing import Any

from flask_hospital import create_app

app: Any = create_app()


def main() -> None:
    app.run()


if __name__ == "__main__":
    main()
