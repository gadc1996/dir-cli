from importlib import import_module
import click
import os

class Command:
    def __init__(self, name: str, directory: str) -> None:
        # Remove .py from name
        self.name = name[:-3] if name.endswith('.py') else name
        self.directory = directory

    def get(self):
        # Dynamically import the module and return a Click command
        imported_module = import_module(f"{self.directory}.{self.name}")
        return click.command()(getattr(imported_module, self.name, None))
    
    @staticmethod
    def is_valid(item: str, path: str):
        return not item.startswith("__") and item.endswith('.py') and os.path.isfile(
            os.path.join(path, item)
        )

