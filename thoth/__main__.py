# __main__.py

import click

from thoth import commands


@click.group()
def cli():
    pass


cli.add_command(commands.hello)
