import os
from logging import *
from pathlib import Path

# basic logging on terminal
basicConfig(level = INFO, format =  "[%(asctime)s]: %(message)s")

project_name = "Audio_Vision"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/entity/__init__.py",
    "dvc.yaml",
    "params.yaml",
    "config/config.yaml",
    "setup.py",
    "requirements.txt",
    "research/experiments.ipynb",
    "templates/index.html"
]

# creating files and folders
for file in list_of_files:
    filepath = Path(file)
    dirname, filename = os.path.split(filepath) 

    if dirname != "":
        os.makedirs(dirname, exist_ok=True)
        info(f"Creating directory: {dirname} for file: {filename}.")

    if filename != "":
        if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
            with open(filepath, "w") as f:
                pass
            info(f"Creating file: {filename} in directory: {dirname}.")

        else:
            info(f"file: {filename} already exists.")
