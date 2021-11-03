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
    return make_link_line(directory, link_name)


def make_link_line(directory, link_name):
    return f'-  [[{directory}/{link_name}|{link_name}]]\n'


def make_moc_for_sub_directories(directory, sub_directories):
    output = ''
    for sub_directory in sub_directories:
        output += make_line_for_sub_directory(directory, sub_directory)
    return output


def moc_name_for_directory(sub_directory):
    name = sub_directory
    if name == '..':
        name = 'hub'
    return '🗂️ ' + name


def make_line_for_sub_directory(directory, sub_directory):
    path = directory + '/' + sub_directory
    file = moc_name_for_directory(sub_directory)
    return make_link_line(path, file)
