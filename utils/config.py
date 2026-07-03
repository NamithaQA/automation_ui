import json
from pathlib import Path

CONFIG_PATH = Path("config/config.json")

def get_config(env: str):
    with open(CONFIG_PATH, "r") as file:
        config = json.load(file)

    return {
        "base_url": config[env]["base_url"],
        "browser": config["browser"],
        "headless": config["headless"],
        "viewport": config["viewport"],
        "timeout": config["timeout"]
    }