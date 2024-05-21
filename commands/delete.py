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

    #TODO: Fix this...permission errors for some reason?
    print(colored("Warning: This command may not work depending on system setup. Permission errors may occur, so deleting this project manually may be necessary. In that case, use the \"explore\" command.", "yellow"))

    print(colored("To delete this project/folder, please type the full name of the folder you wish to delete", "light_red"))
    inputName:str = input(colored("CONFIRM FOLDER NAME: ", "red"))

    if inputName != folderName:
        print(colored("Folder name does not match. Project deletion has been cancelled.", "light_red"))
        return

    os.remove(f"{projectsDir}/{folderName}")

    os.system(f"python {dir}/main.py")
    sys.exit(0)

data:dict[str, str | Callable] = {
    "description": "Delete a project/folder",
    "usage": "delete <index>",
    "executor": executor
}