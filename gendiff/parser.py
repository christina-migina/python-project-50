import json
from pathlib import Path

import yaml

PARSERS = {
    ".json": json.load,
    ".yaml": yaml.safe_load,
    ".yml": yaml.safe_load,
}


def parse(file_path):
    path = Path(file_path).resolve()

    if not path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")

    extension = path.suffix.lower()

    with open(path, encoding="utf-8") as f:
        return PARSERS[extension](f)
