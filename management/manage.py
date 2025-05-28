"""To run typer commands

$ python manage.py <command> <subcommand> <options>
    - command: name of the file in management/commands
    - subcommand: name of the function in the command file
    - options: arguments and flags for the subcommand
"""
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import typer
from commands import migrate

app = typer.Typer()
app.add_typer(migrate.app)


if __name__ == "__main__":
    app()
