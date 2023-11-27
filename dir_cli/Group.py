import click
import os
from importlib import import_module
from .Command import Command

class Group:
    def __init__(self, name: str, directory: str) -> None:
        # Construct the module path and extract the name of the command
        self.module_name = f"{directory.replace('/', '.')}.{name}"
        self.module_path = os.path.join(directory, name)
        self.name = name

    def get(self):
        # Dynamically import the module and return a Click command
        imported_module = import_module(self.module_name)
        base_group = click.group()(getattr(imported_module, self.name, None))

        for item in os.listdir(self.module_path):
            if Group.is_valid(item, self.module_path):
                group = Group(item, self.module_path)
                base_group.add_command(group.get())
            
            if Command.is_valid(item, self.module_path):
                command = Command(item, self.module_name)
                base_group.add_command(command.get())

        return base_group

    @staticmethod
    def is_valid(item: str, path: str):
        return not item.startswith("__") and os.path.isdir(
            os.path.join(path, item)
        )

