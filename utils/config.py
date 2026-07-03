import json
from pathlib import Path

CONFIG_PATH = Path("config/config.json")

with open(CONFIG_PATH, "r") as file:
    config = json.load(file)

ENV = config["environment"]
BASE_URL = config[ENV]["base_url"]
BROWSER = config["browser"]
HEADLESS = config["headless"]
VIEWPORT = config["viewport"]
TIMEOUT = config["timeout"]