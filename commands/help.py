from termcolor import colored
from typing import Callable

import json
import sys
import os

def executor(args:list[str], config:dict[str], projects:dict[str], dir:str, commands:dict[str]) -> None:
    for cmd, cmdData in commands.items():
        print('- ' + colored(cmd, "light_cyan") + ': ' + colored(cmdData["usage"], "light_blue") + ' / ' + cmdData["description"])

data:dict[str, str | Callable] = {
    "description": "A full list of all supported commands",
    "usage": "help",
    "executor": executor
}