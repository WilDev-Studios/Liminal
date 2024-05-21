from termcolor import colored
from typing import Callable

import json
import sys
import os

def executor(args:list[str], config:dict[str], projects:dict[str], dir:str, commands:dict[str]) -> None:
    while True:
        chosenDirectory:str = input(colored("New Projects Directory: ", "light_green"))

        if os.path.exists(chosenDirectory):
            config["projects_directory"] = chosenDirectory

            with open(f"{dir}/config.json", 'w') as file:
                json.dump(config, file, indent=4)

            break

        print(colored("Sorry, that directory doesn't exist. Please try again.", "red"))

data:dict[str, str | Callable] = {
    "description": "Set/reset the projects directory path",
    "usage": "set",
    "executor": executor
}