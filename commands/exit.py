from termcolor import colored
from typing import Callable

import json
import sys
import os

def executor(args:list[str], config:dict[str], projects:dict[str], dir:str, commands:dict[str]) -> None:
    sys.exit(0)

data:dict[str, str | Callable] = {
    "description": "Closes the application",
    "usage": "exit",
    "executor": executor
}