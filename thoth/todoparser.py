import datetime


class TodoParser:
    def __init__(self, todo_str):
        self.todo_str = todo_str
        self.todo = self.parse(todo_str)

    def example_todo(self):
        examples = [
            'x (A) 2024-01-31 2024-01-01 todo text and information +my_tags @home due:2024-03-31'
        ]
        return examples

    def _priority_convert_char_to_int(self, char):
        value = ord(char) - 41 - 24
        if value > 25 or value < 0:
            raise SyntaxError('Priority syntax has to be A-Z')

    def _is_date(self):
        pass

    def _extract_date(self, date_str):
        # date format: aaaa-mm-dd
        date_str = date_str.strip()

        if len(date_str) != 10:
            raise SyntaxError('Date syntax has to be AAAA-MM-DD')

        date_split = date_str.split('-')

        year = date_split[0]
        month = date_split[1]
        day = date_split[2]

        return f'{year}/{month}/{day}'

    def parse(self, txt):
        completion = False
        priority = -1
        completion_date = None  # datetime.datetime()
        creation_date = None    # datetime.datetime()
        text = ''
        project_tag = ''
        context_tag = ''
        due_date = None         # datetime.datetime()

        # 'x (A) 2024-01-31 2024-01-01 todo text and information +my_tags @home due:2024-03-31'
        
        # preparation
        txt = txt.strip()

        # completion
        if txt[0]== 'x':
            completion = True
            txt = txt[1:]
        txt = txt.strip()

        # priority
        priority = -1
        if txt[0] == '(':
            if not txt[2] == ')':
                raise SyntaxError('Watch for priority.')
            else:
                priority = self._priority_convert_char_to_int(txt[1])
            txt = txt[3:]
            txt = txt.strip()

        # date
        date = ''
        if txt[4] == '-' and txt[7] == '-':
            str_date = txt[0:3]
            all_int = True
            for char in str_date:
                try:
                    temp = int(char)
                except ValueError:
                    all_int = False
            if all_int:
                year = txt[0:4]
                month = txt[5:7]
                day = txt[8:10]
                date = year + '/' + month + '/' + day

                txt = txt[10:]
                txt = txt.strip()

        # date (cration | completion)
        if txt[4] == '-' and txt[7] == '-':
            str_date = txt[0:3]
            all_int = True
            for char in str_date:
                try:
                    temp = int(char)
                except ValueError:
                    all_int = False
            if all_int:
                completion_date = date
                year = txt[0:4]
                month = txt[5:7]
                day = txt[8:10]
                creation_date = year + '/' + month + '/' + day

                txt = txt[10:]
                txt = txt.strip()
        else:
            if date != '':
                creation_date = date 

        # due date
        due_date_str = txt.split('due:')
        if len(due_date_str) > 1:
            date_str = due_date_str[-1]
            due_date = self._extract_date(date_str)

            txt = due_date_str[0]
            txt = txt.strip()

        # project tag
        context_tag_split = txt.split('@')
        if len(context_tag_split) > 1:
            context_tag = context_tag_split[-1].strip()

            txt = context_tag_split[0]
            txt = txt.strip()

        project_tag_split = txt.split('+')
        if len(project_tag_split) > 1:
            project_tag = project_tag_split[-1].strip()

            txt = project_tag_split[0]
            txt = txt.strip()

        todo = {
            'completion': completion,
            'priority': priority,
            'completion_date': completion_date,
            'creation_date': creation_date,
            'text': txt,
            'project_tag': project_tag,
            'context_tag': context_tag,
            'due_date': due_date
        }
        return todo


class TodoTxt:
    pass
