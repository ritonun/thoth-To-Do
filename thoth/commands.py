# commands.py
import os

import click

from thoth import file, todo


@click.command(help='Add a new todo')
@click.argument('todo_string')
def a(todo_string):
    example_todo = 'x (A) 2024-01-31 2024-01-01 todo text and information +my_tags @home due:2024-03-31'
    click.echo('Example todo:')
    click.echo(example_todo)
    click.echo('')
    todo.TodoParser(example_todo)


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
