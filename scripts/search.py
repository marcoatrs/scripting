import signal
import sys
from argparse import ArgumentParser
from pathlib import Path

signal.signal(signal.SIGINT, lambda s, f: sys.exit(0))

parser = ArgumentParser()
parser.add_argument("--item", "-i", help="search pattern", type=str)
parser.add_argument("--path", "-p", help="search folder", type=str, default=".")
args = parser.parse_args()
path = Path(args.path)

if not path.exists():
    print("Folder not found")

for file in path.rglob(args.item):
    print(file)
