import datetime

import click

from thoth import file, util
from thoth.validator import Validators
from thoth.settings import settings


class TodoTxt:
    def __init__(self):
        self.file = settings['todo_path']
        self.archive = settings['archive_path']

        self.todos_string, self.todos_parser = self.load_todos()

    def load_todos(self):
        todos_string = []
        todos_parser = []
        todos = file.load_todo(archive=False)

        for todo in todos:
            todos_string.append(todo)
            todos_parser.append(TodoParser(todo))

        return todos_string, todos_parser

    def write_todo(self, todo_string):
        file.dump_todo(todo_string)
        click.echo(f'>> Added to todo.txt: {todo_string}')

    def add_todo(self, todo_string):
        todo_parser = TodoParser(todo_string)
        if todo_parser.todo_dict_value['creation_date'] is None:
            if settings['auto_add_creation_time']:
                todo_parser.todo_dict_value['creation_date'] = util.get_date_str()
        todo_reconstruct_string = todo_parser.reconstruct()
        self.write_todo(todo_reconstruct_string)


class TodoParser:
    def __init__(self, todo_string):
        self.todo_string = todo_string
        self.todo_dict_value, self.todo_dict_str = self.parse(todo_string)

    def precheck(self, todo_string):
        if todo_string.count('+') > 1:
            raise SyntaxError('Only 1 project tag ("+") per todo')
        if todo_string.count('@') > 1:
            raise SyntaxError('Only 1 context tag ("@") per todo')

    def reconstruct(self, todo_dict=None):
        if todo_dict is None:
            todo_dict = self.todo_dict_value

        todo_string = ''

        for key in todo_dict:
            txt = ''
            if key == 'completion':
                if todo_dict[key]:
                    txt = 'x'

            elif key == 'priority':
                if isinstance(todo_dict[key], int):
                    txt = '(' + util.convert_priority_int_to_char(todo_dict[key]) + ')'

            elif 'date' in key:
                if todo_dict[key] is None:
                    txt = ''
                elif not isinstance(todo_dict[key], str):
                    txt = util.timestamp_to_str(todo_dict[key])

            elif key == 'project_tag':
                txt = '+' + todo_dict[key]
            elif key == 'context_tag':
                txt = '@' + todo_dict[key]

            else:
                txt = todo_dict[key]

            if txt != '':
                todo_string += txt + ' '

        todo_string = todo_string.strip()

        return todo_string

    def parse(self, txt):
        todo_str = {
            'completion': '',
            'priority': '',
            'completion_date': '',
            'creation_date': '',
            'text': '',
            'project_tag': '',
            'context_tag': '',
            'due_date': ''
        }

        todo_value = {
            'completion': False,
            'priority': -1,
            'completion_date': None,
            'creation_date': None,
            'text': '',
            'project_tag': '',
            'context_tag': '',
            'due_date': None
        }

        # preparation
        txt = txt.strip()

        # check any simple format error
        self.precheck(txt)

        # completion
        if Validators.completion(txt[0]):
            todo_str['completion'] = 'x'
            todo_value['completion'] = True
            txt = txt[1:].strip()

        # priority
        if Validators.priority(txt[0:3]):
            todo_str['priority'] = txt[1]
            todo_value['priority'] = util.convert_priority_char_to_int(txt[1])
            txt = txt[3:].strip()

        # date
        date = ''
        date_str = ''
        if Validators.date(txt[0:10]):
            date = util.str_to_timestamp(txt[0:10])
            txt = txt[10:].strip()
            if Validators.date(txt[0:10]):
                todo_value['creation_date'] = util.str_to_timestamp(txt[0:10])
                todo_str['creation_date'] = txt[0:10]
                todo_value['completion_date'] = date
                todo_str['completion_date'] = date_str
                txt = txt[10:].strip()
            else:
                todo_value['creation_date'] = date
                todo_str['creation_date'] = date_str
                txt = txt[10:].strip()

        # due date
        due_date_str = txt.split('due:')[-1]
        if len(due_date_str) > 1:
            date = due_date_str.replace('due:', '').strip()
            if Validators.date(date):
                todo_str['due_date'] = date
                todo_value['due_date'] = util.str_to_timestamp(date)

            txt = txt.split('due:')[0]
            txt = txt.strip()

        # project tag
        context_tag_split = txt.split('@')
        if len(context_tag_split) > 1:
            context_tag = context_tag_split[-1].strip()
            todo_value['context_tag'] = context_tag
            todo_str['context_tag'] = context_tag

            txt = context_tag_split[0]
            txt = txt.strip()

        project_tag_split = txt.split('+')
        if len(project_tag_split) > 1:
            project_tag = project_tag_split[-1].strip()

            todo_value['project_tag'] = project_tag
            todo_str['project_tag'] = project_tag

            txt = project_tag_split[0]
        txt = txt.strip()

        todo_value['text'] = txt
        todo_str['text'] = txt

        return todo_value, todo_str
