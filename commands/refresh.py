from termcolor import colored
from typing import Callable

import json
import sys
import os

def executor(args:list[str], config:dict[str], projects:dict[str], dir:str, commands:dict[str]) -> None:
    os.system(f"python {dir}/main.py")
    sys.exit(0)

data:dict[str, str | Callable] = {
    "description": "Refreshes the application to display any new change manually",
    "usage": "refresh",
    "executor": executor
}