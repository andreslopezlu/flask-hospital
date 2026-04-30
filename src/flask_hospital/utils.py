from pathlib import Path


def get_project_root(start: Path) -> str:
    default_files: list[str] = [".env", ".git", "pyproject.toml", "README.md", ".venv"]
    parents: list[Path] = [start, *start.parents]

    possible_root_folders: list[Path] = [
        (parent / file) for parent in parents for file in default_files if (parent / file).exists()
    ]

    root_folfer: str = str(possible_root_folders[0].parent) if possible_root_folders else ""

    return root_folfer
