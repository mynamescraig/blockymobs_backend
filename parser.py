import json
from pathlib import Path
from typing import Any

def parse_json(json_file_path) -> Any:
    file_path = Path(json_file_path)
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data