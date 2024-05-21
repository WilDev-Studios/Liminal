from termcolor import colored
from typing import Callable

import json
import sys
import os

def executor(args:list[str], config:dict[str], projects:dict[str], _:str, commands:dict[str]) -> None:
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

    if not os.path.exists(f"{projectsDir}/{folderName}/launch.json"):
        print(colored(f"No launch.json file was found. Cannot launch program at index {index}", "red"))
        return

    with open(f"{projectsDir}/{folderName}/launch.json") as file:
        launchConfig:dict[str] = json.load(file)
    
    if "entrypoint" not in launchConfig:
        print(colored(f"Launch.json \"entrypoint\" was not configured. Cannot launch program at index {index}.", "red"))
        return

    if "language" not in launchConfig:
        print(colored(f"Launch.json \"language\" was not configured. Cannot launch program at index {index}.", "red"))
        return

    entrypoint:str = launchConfig["entrypoint"]

    if not os.path.exists(f"{projectsDir}/{folderName}/{entrypoint}"):
        print(colored(f"Entrypoint \"{entrypoint}\" could not be found. Cannot launch program at index {index}.", "red"))
        return

    language:str = launchConfig["language"]

    match language:
        case "python":
            os.system(f"start cmd.exe /k \"python {projectsDir}/{folderName}/{entrypoint}\"")
        case _:
            print(colored(f"Language \"{language}\" is not recognized by Liminal. Cannot launch program at index {index}.", "red"))

data:dict[str, str | Callable] = {
    "description": "Launches a program via an index with a lookup to a specified entrypoint file and language",
    "usage": "launch <index>",
    "executor": executor
}