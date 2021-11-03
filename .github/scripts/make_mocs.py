import os.path


def make_moc(directory, files):
    output = ''
    for file in files:
        name = os.path.splitext(file)[0]
        output += f'- [[{directory}/{name}|{name}]]\n'
    return output
