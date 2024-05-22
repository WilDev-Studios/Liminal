import os

os.system("cls")

DIRECTORY:str = os.path.dirname(__file__).replace('\\', '/')

with open(f"{DIRECTORY}/version.txt", "r") as file:
    VERSION:str = file.read()

try:
    from termcolor import colored
    from typing import Callable

    import importlib
    import colorama
    import requests
    import json
    import sys
except ImportError:
    with open(f"{DIRECTORY}/dependencies.txt") as file:
        dependencies:list[str] = file.read().split()

    for dependency in dependencies:
        os.system(f"pip install {dependency}")
    
    os.system(f"python {DIRECTORY}/main.py")

REPO_URL:str = "https://raw.githubusercontent.com/WilDev-Studios/Liminal/main"
API_URL:str  = "https://api.github.com/repos/WilDev-Studios/Liminal/contents"

response:requests.Response = requests.get(REPO_URL + "/version.txt")
version:str = json.loads(response.text)["version"]

colorama.init()

if version != VERSION:
    print(colored("A new update is available! Would you like to install it? [yes/no]", "light_cyan"))
    answer:str = input(colored("Update? ", "light_grey"))

    if answer.lower() == "yes":
        with open(f"{DIRECTORY}/main.py", "wb+") as file:
            if file.read() != (content := requests.get(REPO_URL + "/main.py").content):
                file.write(content)

        with open(f"{DIRECTORY}/dependencies.txt", "wb+") as file:
            if file.read() != (content := requests.get(REPO_URL + "/dependencies.txt").content):
                file.write(content)

        commandsRaw:list[dict[str]] = requests.get(API_URL + "/commands").json()
        
        for commandInfo in commandsRaw:
            filename:str = commandInfo["name"]

            with open(f"{DIRECTORY}/commands/{filename}", "wb+") as file:
                if file.read() != (content := requests.get(REPO_URL + "/commands/" + filename).content):
                    file.write(content)
        
        os.system(f"python {DIRECTORY}/main.py")
        sys.exit(0)

TOP_LEFT:str        = '┌'
TOP_RIGHT:str       = '┐'
BOTTOM_LEFT:str     = '└'
BOTTOM_RIGHT:str    = '┘'
VERTICAL:str        = '│'
HORIZONTAL:str      = '─'
HORIZONTAL_UP:str   = '┴'
HORIZONTAL_DOWN:str = '┬'
VERTICAL_LEFT:str   = '┤'
VERTICAL_RIGHT:str  = '├'
ALL:str             = '┼'

KILOBYTE:int = 1024
MEGABYTE:int = 1024**2
GIGABYTE:int = 1024**3
TERRABYTE:int = 1024**4
PETABYTE:int = 1024**5
EXABYTE:int = 1024**6

indexSection:str = '#'
nameSection:str  = "Name"
typeSection:str  = "Type"
sizeSection:str  = "Size"

longestIndex:int = len(indexSection)
longestName:int  = len(nameSection)
longestType:int  = len(typeSection)
longestSize:int  = len(sizeSection)

totalSize:int = 0
projects:dict[str, dict[str, str]] = {}
commands:dict[str, dict[str, str | Callable]] = {}

for filename in os.listdir(f"{DIRECTORY}/commands"):
    if not filename.endswith(".py"):
        continue

    commandName:str = filename[:-3]
    commandModule = importlib.import_module(f"commands.{commandName}")

    commands[commandName] = commandModule.data

config:dict[str] = {
    "projects_directory": None
}

if os.path.exists(f"{DIRECTORY}/config.json"):
    with open(f"{DIRECTORY}/config.json") as file:
        config = json.load(file)
else:
    with open(f"{DIRECTORY}/config.json", 'w') as file:
        json.dump(config, file, indent=4)

if config["projects_directory"] is None or not os.path.exists(config["projects_directory"]):
    if config["projects_directory"] is None:
        print(colored("Hello, this appears to be your first time using Liminal. Please set the directory in which all of your projects are (and will be) located below.", "light_cyan"))
    else:
        print(colored("Hello, it appears the project directory you had set was either moved or deleted. Please set a new one that is the location of your projects below.", "light_cyan"))

    while True:
        chosenDirectory:str = input(colored("Projects Directory: ", "light_green"))

        if os.path.exists(chosenDirectory):
            config["projects_directory"] = chosenDirectory

            with open(f"{DIRECTORY}/config.json", 'w') as file:
                json.dump(config, file, indent=4)

            break

        print(colored("Sorry, that directory doesn't exist. Please try again.", "red"))

def render_size(size:int) -> str:
    if size >= EXABYTE:
        return f"{'{:,}'.format(round(size / EXABYTE, 1))} EB"
    elif size >= PETABYTE:
        return f"{'{:,}'.format(round(size / PETABYTE, 1))} PB"
    elif size >= TERRABYTE:
        return f"{'{:,}'.format(round(size / TERRABYTE, 1))} TB"
    elif size >= GIGABYTE:
        return f"{'{:,}'.format(round(size / GIGABYTE, 1))} GB"
    elif size >= MEGABYTE:
        return f"{'{:,}'.format(round(size / MEGABYTE, 1))} MB"
    elif size >= KILOBYTE:
        return f"{'{:,}'.format(round(size / KILOBYTE, 1))} KB"
    else:
        return f"{'{:,}'.format(size)} B"

def add_project(index:int, name:str, type_:str, size:int) -> None:
    global longestIndex
    global longestName
    global longestType
    global longestSize
    global totalSize

    index:str = str(index)
    totalSize += size

    size:str = render_size(size)

    if (indexLen := len(index)) > longestIndex:
        longestIndex = indexLen
    
    if (nameLen := len(name)) > longestName:
        longestName = nameLen
    
    if (typeLen := len(type_)) > longestType:
        longestType = typeLen

    if (sizeLen := len(size)) > longestSize:
        longestSize = sizeLen
    
    projects[index] = {
        "name": name,
        "type": type_,
        "size": size
    }

def display_project(index:str, item:dict[str, str], defaultDisplay:bool=True) -> None:
    totalIndex:str = colored(index + (' ' * (longestIndex - len(index))) if defaultDisplay else "{:^{}}".format(index, longestIndex), "light_green")
    totalName:str = colored(item["name"] + (' ' * (longestName - len(item["name"]))) if defaultDisplay else "{:^{}}".format(item["name"], longestName), "light_red" if defaultDisplay else "light_green")
    totalType:str = colored(item["type"] + (' ' * (longestType - len(item["type"]))) if defaultDisplay else "{:^{}}".format(item["type"], longestType), "magenta" if defaultDisplay else "light_green")
    totalSize:str = colored(item["size"] + (' ' * (longestSize - len(item["size"]))) if defaultDisplay else "{:^{}}".format(item["size"], longestSize), "light_red" if defaultDisplay else "light_green")

    print(VERTICAL, totalIndex, VERTICAL, totalName, VERTICAL, totalType, VERTICAL, totalSize, VERTICAL)

index:int = 0

for filename in os.listdir(config["projects_directory"]):
    if os.path.isfile(f"{config['projects_directory']}/{filename}"):
        continue

    types:list[str] = []
    filesSize:int = 0

    for innerFilename in os.listdir(f"{config['projects_directory']}/{filename}"):
        filesSize += os.path.getsize(f"{config['projects_directory']}/{filename}/{innerFilename}")

        if innerFilename.endswith(".py"):
            if "Python" not in types:
                types.append("Python")

        if innerFilename.endswith(".js"):
            if "JavaScript" not in types:
                types.append("JavaScript")

        if innerFilename.endswith(".c"):
            if "C" not in types:
                types.append("C")

        if innerFilename.endswith(".cpp"):
            if "C++" not in types:
                types.append("C++")

        if innerFilename.endswith(".cs"):
            if "C#" not in types:
                types.append("C#")

        if innerFilename.endswith(".java"):
            if "Java" not in types:
                types.append("Java")
        
        if innerFilename.endswith(".html"):
            if "HTML" not in types:
                types.append("HTML")
    
        if innerFilename.endswith(".lua"):
            if "Lua" not in types:
                types.append("Lua")

    if len(types) < 1:
        type_:str = "---"
    else:
        type_:str = ", ".join(types)

    size:int = os.path.getsize(f"{config['projects_directory']}/{filename}") + filesSize

    add_project(index, filename, type_, size)
    index += 1

print(TOP_LEFT, HORIZONTAL * longestIndex, HORIZONTAL_DOWN, HORIZONTAL * longestName, HORIZONTAL_DOWN, HORIZONTAL * longestType, HORIZONTAL_DOWN, HORIZONTAL * longestSize, TOP_RIGHT)
display_project(indexSection, {
    "name": nameSection,
    "type": typeSection,
    "size": sizeSection,
}, False)
print(VERTICAL_RIGHT, HORIZONTAL * longestIndex, ALL, HORIZONTAL * longestName, ALL, HORIZONTAL * longestType, ALL, HORIZONTAL * longestSize, VERTICAL_LEFT)

for index, item in projects.items():
    display_project(index, item)

print(BOTTOM_LEFT, HORIZONTAL * longestIndex, HORIZONTAL_UP, HORIZONTAL * longestName, HORIZONTAL_UP, HORIZONTAL * longestType, HORIZONTAL_UP, HORIZONTAL * longestSize, BOTTOM_RIGHT)
print(colored(f"{len(projects)} Items" if len(projects) != 1 else f"1 Item", "light_yellow"), ' | ', colored(render_size(totalSize), "light_blue"), '\n')

while True:
    try:
        rawCommand:str = input(colored(">> ", "light_cyan"))
        command:list[str] = rawCommand.split()

        try:
            commands[command[0]]["executor"](command, config, projects, DIRECTORY, commands)
        except KeyError:
            print(colored(f"Command with name \"{command[0]}\" wasn't found. Try using \"help\" to find a list of commands.", "red"))
            continue
    except Exception as e:
        print(colored(e.__class__.__name__ + ": " + str(e), "red"))
