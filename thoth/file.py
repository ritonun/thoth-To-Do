import os

import click

from thoth.settings import settings


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
