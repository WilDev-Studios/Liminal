from termcolor import colored
from typing import Callable

import json
import sys
import os

def executor(args:list[str], config:dict[str], projects:dict[str], dir:str, commands:dict[str]) -> None:
    os.startfile(config["projects_directory"])

data:dict[str, str | Callable] = {
    "description": "Open the project folder in File Explorer",
    "usage": "explore",
    "executor": executor
}