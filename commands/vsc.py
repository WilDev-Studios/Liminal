from termcolor import colored
from typing import Callable

import json
import sys
import os

def executor(args:list[str], config:dict[str], projects:dict[str], dir:str, commands:dict[str]) -> None:
    try:
        index:str = args[1]
    except IndexError:
        print(colored(f"File index wasn't entered.", "red"))
        return

    if index not in projects:
        print(colored(f"File index {index} doesn't exist.", "red"))
        return

    projectsDir:str = config["projects_directory"]
    folderName:str = projects[index]["name"]

    os.system(f"code -n \"{projectsDir}/{folderName}\"")

data:dict[str, str | Callable] = {
    "description": "Opens the provided index's file directory in Visual Studio Code (if installed)",
    "usage": "vsc <index>",
    "executor": executor
}