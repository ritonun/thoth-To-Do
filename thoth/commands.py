# commands.py
import os

import click

from thoth import file


@click.command(help='Add a new todo')
def a():
    click.echo('Add todo\n')


@click.command(help='Remove a todo')
def rm():
    click.echo('Remove todo\n')


@click.command(help='List all todo')
def ls():
    click.echo('List todo\n')


@click.command(help='Search for a todo')
def s():
    click.echo('Search todo\n')


@click.command(help='Init the application')
def init():
    click.echo('Init app\n')
    file.init_paths()
