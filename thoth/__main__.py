# __main__.py

import click

from thoth import commands


@click.group()
def cli():
    pass


cli.add_command(commands.a)
cli.add_command(commands.rm)
cli.add_command(commands.ls)
cli.add_command(commands.s)
cli.add_command(commands.init)
