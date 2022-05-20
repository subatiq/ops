import json
from ipaddress import IPv4Address
from pathlib import Path
from typing import Any, Optional

import requests

CURRENT_PATH = Path.home() / ".ops"
CURRENT_PATH.mkdir(parents=True, exist_ok=True)


def get_fleet(host: IPv4Address, port: int) -> list:
    """
    Get a list of all machines in the fleet
    """
    url = f"http://{host}:{port}/api/fleet"

    response = requests.get(url)
    return response.json().get("machines", [])


def load_config() -> Optional[dict[str, Any]]:
    path = CURRENT_PATH / "config.json"
    if not path.exists():
        print("No config file found. Please run ops setup")
        return

    return json.loads(path.read_text())


def set_config(config: dict[str, Any]) -> None:
    path = CURRENT_PATH / "config.json"
    path.write_text(json.dumps(config))


def get_machines_with_state(state: str) -> list[dict[str, Any]]:
    config = load_config()
    if not config:
        return []
    fleet = get_fleet(config["host"], config["port"])
    return [machine for machine in fleet if machine["state"] == state]
