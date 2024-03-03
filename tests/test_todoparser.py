# content of test_todoparser.py
import pytest

import thoth.todoparser

def generate_todo():
    todos = [
        {
            'completion': 'x',
            'priority': '(A)',
            'completion_date': '2024-01-31',
            'creation_date': '2024-01-01',
            'text': 'todo text and information',
            'project_tag': '+my_tags',
            'context_tag': '@home',
            'due_date': 'due:2024-03-31'
        },
        {
            'priority': '(T)',
            'text': 'color terminal !!',
            'project_tag': '+new_tag'
        },
        {
            'completion': 'a',
            'dued_date': 'due:2024'
        }
    ]

    examples = []
    for todo in todos:
        string = ''
        for key in todo:
            string += todo[key] + ' '
        examples.append(string.strip())
    return examples, todos


class TestTodoParser:
    def test_parser(self):
        examples_str, examples_dict = generate_todo()

        for index in range(len(examples_str)):
            td_str = examples_str[index]
            td_dict = examples_dict[index]

            parser = thoth.todoparser.TodoParser(td_str)
            td = parser.todo

            for key in td_dict:
                if key in td:
                    assert str(td[key]).strip() == str(td_dict[key]).strip()