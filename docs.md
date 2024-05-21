# Documentation
Liminal allows users to customize their experience with the application (exactly why it's open-source).
Here's how to use Liminal to it's fullest potential.

## Commands
If the basic commands aren't enough for users, Liminal makes it very easy to make custom commands.

### How to create a new command
Commands are designed to be simple. They are made of 4 parts.
- The name (defined by the filename of the command. Can only be 1 word long).
- The imports (what's needed to function).
- The executing function (what's called when the command is used).
- The metadata (all necessary info for the command to run properly).
  
Command files must end in `.py`, signifying to Liminal that the file is a command and is to be ran and imported in Python. No other languages are supported for commands.
Every command must be under the `commands` folder, as Liminal loops through each command file and loads it into the program.
These are further explained below along with details on how to make them.

**Imports** - 
Usually, we don't need a lot of imports. But the basics are these (note, if a command needs more, make sure to note the other dependencies so other users using your command, if applicable, don't have import errors):
```python
from termcolor import colored
from typing import Callable

import json
import sys
import os
```
- `colored` is the function used to make the printed console text a different color
- `Callable` is there for typing annotations (I find it to be good practice)
- `json` is there so if files need to be accessed and read in a `dict`
- `sys` is there to call system-functions (like exits and calls)
- `os` is there for operating system functions (like clears and calls)

**Executing Function** - 
This is the function that will be called when your command is used. It's defined like below:
```python
def executor(args:list[str], config:dict[str], projects:dict[str], dir:str, commands:dict[str]) -> None:
  ...
```
- `executor` is the function name. This can be called anything, as long as the `executor` key's value in the command metadata is this function's name.
- `args` is always the first parameter. This is the command entered by the user, but split between each word (a list of words used. Index 0 is the command name, indexes 1+ are the arguments).
- `config` is Liminal's config file. It contains the parent directory of all projects under the `projects_directory` key, while the `version` key is used for automatic updates. Usage for this parameter can be seen in the basic command set.
- `projects` are all of the projects and their data used when listed in the Liminal app. It contains the indexes of each project, and further defines the name, type, and size of the project as it's value.
- `dir` is the main directory of Liminal. It's the access point for all Liminal functions, and may be used in place of relative directories for guaranteed file accessibility.
- `commands` is a list of all commands currently registered in Liminal, along with their metadata (of which you are reading about right now). This list is only refreshed when Liminal restarts. Further details about metadata is below.
- `None` is the return type. All Liminal functions return `None`, as no data passed from commands is used in the main program.

**Metadata** - 
This data is used by Liminal to index each command and load it properly. Some of this metadata is used when users use the `help` command, while other data is used in the actual usage of the command.
```python
data:dict[str, str | Callable] = {
  "description": "...",
  "usage": "...",
  "executor": ...
}
```
- `data` is the name of the metadata object. It must always be called `data`.
- `description` is the description of the command you are making. This is shown when listed as a command when a user uses the `help` command.
- `usage` is the way the command is intended on being used. It defines all of the arguments taken. Mandatory arguments should be noted with `<` and `>`, while optional should be noted with `[` and `]` (while also being after all mandatory args).
- `executor` is the function to be called when the command is invoked. Usually, by Liminal convention, the executor should just be called `executor` (like in the example above), but it may be called anything else (as long as the actual function and this value are the same).

### Command Examples
This one will print `Hello world` when the `hellowrld` command is used.
```python
# commands/hellowrld.py
from termcolor import colored
from typing import Callable

import json
import sys
import os

# The function name `executor` can be changed, as long as the value of "executor" in `data` is changed to the same
def executor(args:list[str], config:dict[str], projects:dict[str], dir:str, commands:dict[str]) -> None:
  print("Hello world")

data:dict[str, str | Callable] = {
  "description": "Prints \"Hello world\" to the console",
  "usage": "hellowrld",
  "executor": executor
}
```
```cmd
>>> hellowrld
Hello world
```
<br><br>
This one will print `Hello world` `x` many times when the `hellowrld` command is used.
```python
# commands/hellowrld.py
from termcolor import colored
from typing import Callable

import json
import sys
import os

def different_executor_name(args:list[str], config:dict[str], projects:dict[str], dir:str, commands:dict[str]) -> None:
  if len(args) != 2: # command name and 1 argument
    print(colored("hellowrld command requires one argument", "red"))
    return

  try:
    amount:int = int(args[1])
  except:
    print(colored("hellowrld command argument must be of type int", "red"))
    return

  for i in range(amount):
    print("Hello world")

data:dict[str, str | Callable] = {
  "description": "Prints \"Hello world\" x amount of times",
  "usage": "hellowrld <amount>",
  "executor": different_executor_name
}
```
```cmd
>>> hellowrld 5
Hello world
Hello world
Hello world
Hello world
Hello world
```

Now obviously the point of commands isn't for printing `Hello world` to the console. Commands are here to make workflows and tasks easier for developers. Ones that automatically compile C or C++ code, or open the projects in Windows Explorer, etc. are good examples of commands that would work well.
