import os.path

from utils import get_template

DIRECTORIES_TO_EXCLUDE = ['meta-notes', 'venv']  # Directories beginning '.' are also excluded


class VaultMoc:
    """
    Top-level class, to manage MOCs for all the directories in an entire vault.

    For now, the path to the vault is hard-coded, as there is some code
    in make_mocs.py that knows that the root of the vault is in a parent of the
    directory containing this script.
    """

    def update_all_mocs(self, args):
        directory = '../..'
        for root, dirs, files in os.walk(directory):
            filter_directories(dirs)
            dirs.sort()
            directory_moc = DirectoryMoc(root, dirs, files)
            directory_moc.generate_moc()


class DirectoryMoc:
    """Class to manage the MOC for a single directory"""

    def __init__(self, root, dirs, files):
        self.root = root
        self.moc_file_path = moc_file_path_for_directory(root)
        self.dirs = dirs
        self.files = files

    def generate_moc(self):
        new_moc_content_with_delimiters = make_moc_for_directory_with_delimiters(self.root, self.dirs, self.files)
        if os.path.exists(self.moc_file_path):
            self.rewrite_existing_moc_file(new_moc_content_with_delimiters)
        else:
            self.write_new_moc_file(new_moc_content_with_delimiters)

    def rewrite_existing_moc_file(self, new_moc_content_with_delimiters):
        with open(self.moc_file_path, 'r') as input:
            initial_content = input.readlines()
        with open(self.moc_file_path, 'w') as output:
            output.write(update_existing_moc(initial_content, new_moc_content_with_delimiters))

    def write_new_moc_file(self, new_moc_content_with_delimiters):
        template = get_template("directory_moc")
        moc_base_name = moc_base_name_for_directory(self.root)
        new_content = template.render(title=moc_base_name, list_of_files_and_dirs=new_moc_content_with_delimiters)
        with open(self.moc_file_path, 'w') as output:
            output.write(new_content)


class MocMaker:
    @staticmethod
    def make_moc_for_files(directory, files):
        return make_moc_for_files(directory, files)


def make_moc_for_files(directory, files):
    output = ''
    for file in files:
        if not include_file_in_moc(directory, file):
            continue
        output += make_line_for_file(directory, file)
    return output


def make_line_for_file(directory, file):
    link_name, extension = os.path.splitext(file)
    if extension != '.md':
        link_name += extension
    return make_link_line(directory, link_name)


def strip_parent_directories_from_directory(directory):
    # Ugly hack because all directory names start with '../../'
    result = directory.replace('../', '')
    if result == '..':  # Even more horrible hack for files in root of repo
        result = ''
    return result


def make_link_line(directory, link_name):
    adjusted_directory = strip_parent_directories_from_directory(directory)
    if len(adjusted_directory) > 0:
        adjusted_directory += '/'
    result = f'-  [[{adjusted_directory}{link_name}|{link_name}]]\n'
    # print(f'directory={directory}\nadjusted_directory={adjusted_directory}\nlink_name={link_name}\n=> {result}')
    return result


def include_directory_in_moc(directory):
    if directory[0] == '.':
        return False
    return directory not in DIRECTORIES_TO_EXCLUDE


def include_file_in_moc(directory, file):
    if file_is_moc_for_directory(directory, file):
        return False
    return file[0] != '.'


def file_is_moc_for_directory(directory, file):
    return file == moc_file_name_for_directory(directory)


def filter_directories(dirs):
    dirs[:] = [d for d in dirs if include_directory_in_moc(d)]


def make_moc_for_sub_directories(directory, sub_directories):
    output = ''
    for sub_directory in sub_directories:
        if not include_directory_in_moc(sub_directory):
            continue
        output += make_line_for_sub_directory(directory, sub_directory)
    return output


def moc_name_for_sub_directory(sub_directory):
    name = sub_directory
    if name == '..':
        name = 'hub'
    return '🗂️ ' + name


def moc_base_name_for_directory(root):
    directory_name = os.path.basename(root)
    return moc_name_for_sub_directory(directory_name)


def moc_file_name_for_directory(root):
    return moc_base_name_for_directory(root) + ".md"


def moc_file_path_for_directory(root):
    moc_file_basename = moc_file_name_for_directory(root)
    return os.path.join(root, moc_file_basename)


def make_line_for_sub_directory(directory, sub_directory):
    path = directory + '/' + sub_directory
    file = moc_name_for_sub_directory(sub_directory)
    return make_link_line(path, file)


def make_moc_for_directory_with_delimiters(root, dirs, files):
    result = ''
    result += moc_initial_delimiter()
    result += make_moc_for_directory(root, dirs, files)
    result += moc_final_delimiter()
    return result


def make_moc_for_directory(root, dirs, files):
    result = ''

    sorted_dirs = sorted(dirs, key=str.casefold)
    result += make_moc_for_sub_directories(root, sorted_dirs)

    sorted_files = sorted(files, key=str.casefold)
    result += make_moc_for_files(root, sorted_files)

    if not result:
        result = '\n'
    return result


def update_existing_moc(initial_content, new_moc_content_with_delimiters):
    inside_old_index = False
    index_written = False
    result = ''
    for line in initial_content:

        if line == moc_initial_delimiter():
            inside_old_index = True
            result += new_moc_content_with_delimiters
            index_written = True
            continue

        if line == moc_final_delimiter():
            inside_old_index = False
            continue

        if not inside_old_index:
            result += line
    if not index_written:
        result += new_moc_content_with_delimiters

    return result


def moc_initial_delimiter():
    return '%% Zoottelkeeper: Beginning of the autogenerated index file list  %%\n'


def moc_final_delimiter():
    return '%% Zoottelkeeper: End of the autogenerated index file list  %%\n'
