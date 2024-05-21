from termcolor import colored
from typing import Callable

import json
import sys
import os

def executor(args:list[str], config:dict[str], projects:dict[str], dir:str, commands:dict[str]) -> None:
    if len(args) < 2:
        os.startfile(config["projects_directory"])
        return
    
    index:str = args[1]

    if index not in projects:
        print(colored(f"File index {index} doesn't exist.", "red"))
        return
    
    projectsDir:str = config["projects_directory"]
    folderName:str = projects[index]["name"]

    os.startfile(f"{projectsDir}/{folderName}")

data:dict[str, str | Callable] = {
    "description": "Open the project folder in File Explorer (optionally a specific project folder)",
    "usage": "explore [index]",
    "executor": executor
}