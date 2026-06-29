import json
from pathlib import Path

import yaml


def parse(file_path):
    suffix = Path(file_path).suffix
    if suffix in (".yaml", ".yml"):
        with open(file_path) as f:
            data = yaml.safe_load(f)
        return data
    elif suffix == ".json":
        with open(file_path) as f:
            data = json.load(f)
        return data
