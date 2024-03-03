# commands.py
import os

import click

from thoth import file, todoparser


@click.command(help='Add a new todo')
@click.argument('todo_string')
def a(todo_string):
    example_todo = 'x (A) 2024-01-31 2024-01-01 todo text  +my_tags @home due:2024-03-31'
    click.echo('Example todo:')
    click.echo(example_todo)
    click.echo('')
    t = todoparser.TodoParser(example_todo)

    for key in t.todo_dict_value:
        val = t.todo_dict_value[key]
        string = t.todo_dict_str[key]
        click.echo(f'{key}: {string} | {val}')


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
