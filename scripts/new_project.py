import os
import sys
from argparse import ArgumentParser
from pathlib import Path

parser = ArgumentParser(0)

parser.add_argument("--name", "-n", type=str, help="Nombre del proyecto")
parser.add_argument("--path", "-p", type=str, help="Dirección de creación", default=".")


def create_new_prokect(name: str, path: str):
    if name is None:
        name = ""
        while name == "":
            name = input("Project name: ")
    _path = Path(path) / name
    if _path.exists():
        print(f'This folder "{name}" exist')
        sys.exit(0)
    _path.mkdir()

    (_path / name).mkdir()
    (_path / "test").mkdir()
    (_path / "app.py").touch()
    (_path / "README.md").touch()
    (_path / "CHANGELOG.md").touch()
    (_path / ".gitignore").touch()

    os.chdir(_path)
    os.system("git init")


args = parser.parse_args()
create_new_prokect(args.name, args.path)
