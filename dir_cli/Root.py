import click
import os
from .Command import Command
from .Group import Group


class Root:
    def __init__(self, base_dir="cli"):
        self.base_dir = base_dir
        self.base_path = os.path.join(os.getcwd(), base_dir)

        root = self.root
        self._load_commands(root)
        root()

    @click.group()
    def root():
        """Base cli"""

    def _load_commands(self, root: click.Group):
        for item in os.listdir(self.base_dir):

            if Group.is_valid(item, self.base_dir):
                group = Group(item, self.base_dir)
                root.add_command(group.get())

            if Command.is_valid(item, self.base_dir):
                command = Command(item, self.base_dir)
                root.add_command(command.get())
