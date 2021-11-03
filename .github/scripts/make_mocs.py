import os.path


def make_moc_for_directory(directory, files):
    output = ''
    for file in files:
        output += make_line_for_file(directory, file)
    return output


def make_line_for_file(directory, file):
    link_name, extension = os.path.splitext(file)
    if extension != '.md':
        link_name += extension
    return f'- [[{directory}/{link_name}|{link_name}]]\n'
