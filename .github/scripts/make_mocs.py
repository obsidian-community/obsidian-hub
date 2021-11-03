import os.path


def make_moc(directory, files):
    output = ''
    for file in files:
        name, extension = os.path.splitext(file)
        if extension == '.md':
            link_name = name
        else:
            link_name = file # include extension
        output += f'- [[{directory}/{link_name}|{link_name}]]\n'
    return output
