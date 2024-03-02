import datetime

"""
todo_b = {
    'completion': bool
    'priority': int
    'completion_date': datetime
    'cretion_date': datetime
    'text': str
    'project_tag': str
    'context_tag': str
    'due_date': datetime
}
"""
todo = {
    'completion': '',
    'priority': '',
    'completion_date': '',
    'cretion_date': '',
    'text': '',
    'project_tag': '',
    'context_tag': '',
    'due_date': ''
}


class TodoParser:
    def __init__(self, todo_str):
        self.todo_str = todo_str
        self.parse(todo_str)

    def example_todo(self):
        examples = [
            'x (A) 2024-01-31 2024-01-01 todo text and information +my_tags @home due:2024-03-31'
        ]
        return examples

    def _priority_convert_char_to_int(self, char):
        value = ord(char) - 41 - 24
        if value > 25 or value < 0:
            raise SyntaxError('Priority syntax has to be A-Z')

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
        print(f'Strip:\n{txt}')

        # completion
        if txt[0]== 'x':
            completion = True
            txt = txt[1:-1]
        txt = txt.strip()

        # priority
        if txt[0] == '(':
            if not txt[2] == ')':
                raise SyntaxError('Watch for priority.')
            else:
                priority = self._priority_convert_char_to_int(txt[1])
            txt = txt[3:-1]
            txt = txt.strip()

        # date
        if txt[4] == '-' and txt[7] == '-':
            date = txt[0:3]
            all_int = True
            for char in date:
                try:
                    temp = int(char)
                except ValueError:
                    all_int = False
            if all_int:
                year = txt[0:4]
                month = txt[5:7]
                day = txt[8:10]
                txt = txt[10:-1]
                txt = txt.strip()


class TodoTxt:
    pass
