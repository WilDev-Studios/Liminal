from termcolor import colored
from typing import Callable

import json
import sys
import os

def executor(args:dict[str], config:dict[str], projects:dict[str], dir:str, commands:dict[str]) -> None:
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

    os.system(f"start cmd.exe /k \"cd /d {projectsDir}/{folderName}/&cls\"")

data:dict[str, str | Callable] = {
    "description": "Opens the provided index's file directory in a new Command Prompt instance",
    "usage": "terminal <index>",
    "executor": executor
}