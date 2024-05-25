# Liminal
Simple Console Application to Make Managing Projects Easy

Liminal is a new, modern project management console application that aims for simplicity in it's aesthetic and functionality.
I've had firsthand experience with Command Prompt on Windows and Terminal on Ubuntu, and I dislike how commands are named.
Liminal is focused on English commands that make sense and are organized in such a way to make them easy to read and understand.

This application has a few basic commands set up. If you run the program after setup and use the "help" command, these will be shown.
Part of Liminal's simplicity and scalability is it's ability to allow users to create their own commands easily without touching the main source of the program (assuming programming experience in Python).
More details about creating more commands down below.

Liminal was originally created as a project management application designed for absolutely no mouse-usage (strictly keyboard).

**Please Note:**
Liminal works for Windows only (hasn't been tested in Linux-based operating systems or MacOS). If you'd like to test or help in this regard, please contact WilDev Studios via [Discord](https://www.discord.gg/4Ggybyy87d).

## Getting Started
- Ensure you have any [Python 3](https://www.python.org/downloads/) version installed on your computer and in your PATH variables (as well as their package installer, PIP)
- Run the main.py file you downloaded. This will run the program like usual, but take you through steps for setup. __Note:__ Liminal will automatically install the dependencies listed in dependencies.txt.
- Make sure all of the projects you want to manage under Liminal are located in one main parent directory, and set that directory path as the projects directory in the application when it asks.
- After initial setup, you should be able to use the commands listed under the "help" command to get started.

## Scalability
Liminal allows for users to create their own commands. In the future, WilDev Studios plans on creating a library-like website where users can publish their own commands (maybe plugins) to further enhance Liminal's functionality.

## Command Usage
Basic commands include:
- Create:
  - Allows you to make a new project folder.
- Delete:
  - Allows you to delete a project folder via it's index listed.
- Exit:
  - Hassle-free exiting of the program.
- Explore:
  - Opens the projects folder in Windows File Explorer (optionally a specific project folder).
  ![Explore Example](https://github.com/WilDev-Studios/Liminal/blob/main/media/example-1.png)
- Help:
  - Displays a list of all commands (even ones created by users).
  ![Help Example](https://github.com/WilDev-Studios/Liminal/blob/main/media/example-2.png)
- Launch:
  - Depending on system setup, this allows projects to be run through a simple command rather than executing complicated compiler/interpreter commands.
  - Requires further setup below.
  - Currently only supports [Python](https://www.python.org/), but [Java](https://www.java.com/en/), C++, C, JavaScript, and C# are planned.
- Refresh:
  - Restarts the Liminal application. Useful for getting rid of cluttered text or applying changes to source code (if edited).
- Set:
  - In case the projects directory needs to be reset or moved, this command allows you to change that configuration without editing manually in the config file.
- Terminal:
  - Opens a new Command Prompt window and changes it's directory to the given project's folder
- VSC:
  - For machines with [Visual Studio Code](https://code.visualstudio.com/), this command allows the folder selected to be opened in VSCode without hassle.

**More commands may be added in the future** - 
Plans for [Visual Studio](https://visualstudio.microsoft.com/), [Sublime Text](https://www.sublimetext.com/), [IntelliJ](https://www.jetbrains.com/idea/), etc. may be implemented.

### Launch Command
In order for the "launch" command to be used, the projects in question should have a "launch.json" file present.

Internals of the "launch.json" file:
```json
{
  "entrypoint": "...",
  "language": "..."
}
```

- `entrypoint` is the path to the file relative to the launch.json file in which Liminal should start the project from. Usually this is the main entry file for the program.
- `language` is the programming language that the entrypoint file is written. This is used so that Liminal knows what command to execute the entrypoint with.

**Project Folder Examples:**
```yaml
# Entrypoint file is in the same directory as `launch.json`
project_folder:
- launch.json
- main.py
```
```json
# Internals of launch.json
{
  "entrypoint": "main.py",
  "language": "python"
}
```
<br><br>
```yaml
# Entrypoint file is in a subdirectory from `launch.json`
project_folder:
- src:
  / main.py
  / ...
- launch.json
```
```json
# Internals of launch.json
{
  "entrypoint": "src/main.py",
  "language": "python"
}
```
