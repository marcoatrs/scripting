import json
import sys
from argparse import ArgumentParser
from pathlib import Path

parser = ArgumentParser()
parser.add_argument("--input", "-i", help="Json file path")
args = parser.parse_args()

json_path = Path(args.input)

if not json_path.exists():
    print("JSON not found")
    sys.exit()

try:
    with open(json_path, "r") as json_file:
        json_obj = json.load(json_file)
except Exception:
    print("No valid JSON")
    sys.exit()

print("Valid JSON!")
