import shutil
import sys
from argparse import ArgumentParser
from pathlib import Path


def get_downloads_path():
    downloads_path = Path.home() / 'Downloads'
    if downloads_path.exists():
        return downloads_path
    return Path('.')


parser = ArgumentParser()
parser.add_argument('--path',
                    '-p',
                    help='Source folder',
                    default=get_downloads_path())
args = parser.parse_args()

folder = Path(args.path)
if not folder.exists():
    print('Folder not exist')
    sys.exit()

for path in folder.glob('*'):
    if path.is_dir():
        continue
    if path.name == 'desktop.ini':
        continue
    ext = path.name.split('.')[-1].lower()
    dst = (folder / ext)
    dst.mkdir(exist_ok=True)
    shutil.move(path, dst / path.name)
