# commands.py
import os

import click

@click.command(help='Test hello world')
def hello():
    click.echo('Hello, World!\n')
