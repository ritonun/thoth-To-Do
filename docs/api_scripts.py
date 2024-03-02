import os


package_name = 'thoth'

def get_python_file_path(package_path):
    package_file = os.listdir(package_path)
    package_files = []
    for file in package_file:
        ext = file.split('.')[-1]
        if ext == 'py':
            package_files.append(package_path + file)
    return package_files


def read_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '')

    return lines


def get_func_name(py_lines):
    functions = []

    func_line = []
    for line in py_lines:
        if 'def' in line:
            if '    def' in line:
                continue
            func_line.append(line)

    for line in func_line:
        func_name = line.replace('def ', '').strip()
        func_name = func_name.split('(')[0]
        functions.append(func_name)
    return functions


def generate_md_line(package_name, file_name, function_name):
    line = f'::: {package_name}.{file_name}.{function_name}\n\t:docstring:\n\n'
    return line


def generate_md_line_file(package_name, file_name):
    line = f'::: {package_name}.{file_name}\n\n'
    return line


def generate_api_md_function():
    package_name = 'thoth'

    md_lines = []

    path = '../thoth/'
    files = get_python_file_path(path)
    for file in files:
        file_name = file.split('/')[-1]
        file_name = file_name.split('.')[0]
        if file_name in ['__init__', '__main__']:
            continue
        lines = read_file(file)
        functions_names = get_func_name(lines)
        if not functions_names:
            continue
        md_lines.append(f'## {file_name.capitalize()}\n')
        for f in functions_names:
            md_line = generate_md_line(package_name, file_name, f)
            md_lines.append(md_line)

    with open('api.md', 'w') as f:
        f.write('# API\n\n')
        for line in md_lines:
            f.write(line + '\n')


def generate_api_md_file():
    package_name = 'thoth'

    md_lines = []

    path = '../thoth/'
    files = get_python_file_path(path)
    for file in files:
        file_name = file.split('/')[-1]
        file_name = file_name.split('.')[0]
        if file_name in ['__init__', '__main__']:
            continue

        md_lines.append(f'**{file_name}.py**\n')
        md_line = generate_md_line_file(package_name, file_name)
        md_lines.append(md_line)

    with open('api.md', 'w') as f:
        f.write('# API\n\n')
        for line in md_lines:
            f.write(line + '\n')


if __name__ == '__main__':
    generate_api_md_file()
