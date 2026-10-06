import json
from pathlib import Path

file_path = Path("data/type_chart.json")

with open(file_path, "r", encoding="utf-8") as file:
	data = json.load(file)