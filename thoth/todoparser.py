import datetime

from thoth.validator import Validators


class TodoParser:
    def __init__(self, todo_string):
        self.todo_string = todo_string
        self.todo_dict_value, self.todo_dict_str = self.parse(todo_string)

    def _precheck(self, todo_string):
        if todo_string.count('+') > 1:
            raise SyntaxError('Only 1 project tag ("+") per todo')
        if todo_string.count('@') > 1:
            raise SyntaxError('Only 1 context tag ("@") per todo')

    def _priority_convert_char_to_int(self, char):
        value = ord(char) - 41 - 24
        if value > 25 or value < 0:
            raise SyntaxError('Priority syntax has to be A-Z')
        return value

    def _str_to_timestamp(self, date_str):
        time = datetime.datetime.strptime(date_str, "%Y-%M-%d")
        time = datetime.datetime.timestamp(time)
        return time

    def _timestamp_to_str(self, time):
        date = datetime.datetime.fromtimestamp(time).strftime('%Y-%M-%d')
        return date

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
        self._precheck(txt)

        # completion
        if Validators.completion(txt[0]):
            todo_str['completion'] = 'x'
            todo_value['completion'] = True
            txt = txt[1:].strip()

        # priority
        if Validators.priority(txt[0:3]):
            todo_str['priority'] = txt[1]
            todo_value['priority'] = self._priority_convert_char_to_int(txt[1])
            txt = txt[3:].strip()

        # date
        date = ''
        date_str = ''
        if Validators.date(txt[0:10]):
            date = self._str_to_timestamp(txt[0:10])
            txt = txt[10:].strip()
        if Validators.date(txt[0:10]):
            todo_value['creation_date'] = self._str_to_timestamp(txt[0:10])
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
                todo_value['due_date'] = self._str_to_timestamp(date)

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


class TodoTxt:
    pass
