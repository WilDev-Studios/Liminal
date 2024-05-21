from termcolor import colored
from typing import Callable

import json
import sys
import os

def executor(args:list[str], config:dict[str], projects:dict[str], dir:str, commands:dict[str]) -> None:
    if len(args) < 2:
        print(colored("Create command requires more than 1 argument.", "red"))
        return
    
    name:str = ' '.join(args[1:])
    os.mkdir(f"{config['projects_directory']}/{name}", 0o777)

    os.system(f"python {dir}/main.py")
    sys.exit(0)

data:dict[str, str | Callable] = {
    "description": "Create a new project/folder",
    "usage": "create <folder_name>",
    "executor": executor
}
