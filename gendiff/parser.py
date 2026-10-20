import json
from pathlib import Path

import yaml

PARSERS = {
    ".json": json.load,
    ".yaml": yaml.safe_load,
    ".yml": yaml.safe_load,
}


def parse(file_path):
    path = Path(file_path)
    extension = path.suffix.lower()

    with open(file_path) as f:
        return PARSERS[extension](f)
