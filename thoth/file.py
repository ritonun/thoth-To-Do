import os

import click

from thoth.settings import settings


def dump_todo(todo_string):
    with open(settings['todo_path'], 'a') as f:
        f.write(todo_string + '\n')


def load_todo(archive=False):
    if archive:
        path = settings['archive_path']
    else:
        path = settings['todo_path']

    with open(path, 'r') as f:
        lines = f.readlines()

    todos = []
    for line in lines:
        l = line.replace('\n', '').strip()
        todos.append(l)
    return todos


def create_folder(path):
    try:
        os.mkdir(path)
        return 0
    except FileExistsError:
        return 1


def create_file(path):
    try:
        open(path, 'x').close()
        return 0
    except FileExistsError:
        return 1


def init_paths():
    dirs = []
    files = []
    for key in settings:
        if 'path' in key:
            if os.path.isdir(settings[key]) or settings[key][-1] == '/':
                dirs.append(settings[key])
            else:
                files.append(settings[key])

    for directory in dirs:
        error = create_folder(directory)
        if error == 0:
            click.echo(f'mkdir "{directory}"')
        else:
            click.echo(f'Dir "{directory}" already exist!')
    for file in files:
        error = create_file(file)
        if error == 0:
            click.echo(f'created file "{file}"')
        else:
            click.echo(f'File "{file}" already exist!')
