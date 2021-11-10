import os.path

from utils import get_template


class VaultMoc:
    """
    Top-level class, to manage MOCs for all the directories in an entire vault.

    For now, the path to the vault is hard-coded, as there is some code
    in make_mocs.py that knows that the root of the vault is in a parent of the
    directory containing this script.
    """

    def update_all_mocs(self, args):
        directory = '../..'
        moc_filter = MocFileAndDirectoryFilter()
        for root, dirs, files in os.walk(directory):
            moc_filter.filter_directories(dirs)
            dirs.sort()
            directory_moc = DirectoryMoc(root, dirs, files)
            directory_moc.generate_moc()


class DirectoryMoc:
    """Class to write the MOC for a single directory"""

    def __init__(self, root, dirs, files):
        self.root = root
        self.namer = MocFileNamer()
        self.moc_file_path = self.namer.moc_file_path_for_directory(root)
        self.dirs = dirs
        self.files = files

    def generate_moc(self):
        """
        Currently, it either updates the list of files in an existing MOC,
        or if none is present, it creates a new MOC file, using the template file
        .github/scripts/templates/directory_moc.md.jinja

        Later, it may be updated to streamline renaming of existing directories
        that already had a MOC file, named after the previous directory name.

        :return: Nothing
        """
        moc_maker = MocMaker()
        new_moc_content_with_delimiters = moc_maker.make_moc_for_directory_with_delimiters(self.root, self.dirs,
                                                                                           self.files)
        if os.path.exists(self.moc_file_path):
            self.rewrite_existing_moc_file(new_moc_content_with_delimiters)
        else:
            self.write_new_moc_file(new_moc_content_with_delimiters)

    def rewrite_existing_moc_file(self, new_moc_content_with_delimiters):
        with open(self.moc_file_path, 'r') as input:
            initial_content = input.readlines()
        with open(self.moc_file_path, 'w') as output:
            moc_maker = MocMaker()
            output.write(moc_maker.update_existing_moc(initial_content, new_moc_content_with_delimiters))

    def write_new_moc_file(self, new_moc_content_with_delimiters):
        template = get_template("directory_moc")
        moc_base_name = self.namer.moc_base_name_for_directory(self.root)
        new_content = template.render(title=moc_base_name, list_of_files_and_dirs=new_moc_content_with_delimiters)
        with open(self.moc_file_path, 'w') as output:
            output.write(new_content)


class MocMaker:
    """
    Class that generates the content of a MOC file
    
    That is, it generates a Markdown list of links to files and directories
    """
    def make_moc_for_files(self, directory, files):
        output = ''
        moc_filter = MocFileAndDirectoryFilter()
        for file in files:
            if not moc_filter.include_file_in_moc(directory, file):
                continue
            output += self.make_line_for_file(directory, file)
        return output

    def make_moc_for_sub_directories(self, directory, sub_directories):
        output = ''
        moc_filter = MocFileAndDirectoryFilter()
        for sub_directory in sub_directories:
            if not moc_filter.include_directory_in_moc(sub_directory):
                continue
            output += self.make_line_for_sub_directory(directory, sub_directory)
        return output

    def make_moc_for_directory(self, root, dirs, files):
        result = ''

        sorted_dirs = sorted(dirs, key=str.casefold)
        result += self.make_moc_for_sub_directories(root, sorted_dirs)

        sorted_files = sorted(files, key=str.casefold)
        result += self.make_moc_for_files(root, sorted_files)

        if not result:
            result = '\n'
        return result

    def make_moc_for_directory_with_delimiters(self, root, dirs, files):
        result = ''
        result += MocDelimiter().initial_delimiter()
        result += self.make_moc_for_directory(root, dirs, files)
        result += MocDelimiter().final_delimiter()
        return result

    def update_existing_moc(self, initial_content, new_moc_content_with_delimiters):
        inside_old_index = False
        index_written = False
        result = ''
        for line in initial_content:

            if line == MocDelimiter().initial_delimiter():
                inside_old_index = True
                result += new_moc_content_with_delimiters
                index_written = True
                continue

            if line == MocDelimiter().final_delimiter():
                inside_old_index = False
                continue

            if not inside_old_index:
                result += line
        if not index_written:
            result += new_moc_content_with_delimiters

        return result

    def make_line_for_file(self, directory, file):
        link_name, extension = os.path.splitext(file)
        if extension != '.md':
            link_name += extension
        return self.make_link_line(directory, link_name)

    def make_line_for_sub_directory(self, directory, sub_directory):
        path = directory + '/' + sub_directory
        namer = MocFileNamer()
        file = namer.moc_name_for_sub_directory(sub_directory)
        return self.make_link_line(path, file)

    def strip_parent_directories_from_directory(self, directory):
        # Ugly hack because all directory names start with '../../'
        result = directory.replace('../', '')
        if result == '..':  # Even more horrible hack for files in root of repo
            result = ''
        return result

    def make_link_line(self, directory, link_name):
        adjusted_directory = self.strip_parent_directories_from_directory(directory)
        if len(adjusted_directory) > 0:
            adjusted_directory += '/'
        result = f'-  [[{adjusted_directory}{link_name}|{link_name}]]\n'
        # print(f'directory={directory}\nadjusted_directory={adjusted_directory}\nlink_name={link_name}\n=> {result}')
        return result


class MocFileAndDirectoryFilter:
    """Various filtering functions, to determine what is included in the generated MOC"""

    def __init__(self):
        self.DIRECTORIES_TO_EXCLUDE = ['venv']  # Directories beginning '.' are also excluded

    def include_directory_in_moc(self, directory):
        if directory[0] == '.':
            return False
        return directory not in self.DIRECTORIES_TO_EXCLUDE

    def include_file_in_moc(self, directory, file):
        if self.file_is_moc_for_directory(directory, file):
            return False
        return file[0] != '.'

    def file_is_moc_for_directory(self, directory, file):
        namer = MocFileNamer()
        return file == namer.moc_file_name_for_directory(directory)

    def filter_directories(self, dirs):
        dirs[:] = [d for d in dirs if self.include_directory_in_moc(d)]


class MocFileNamer:
    """
    Various naming functions, to determine the name and location of MOC files.

    Currently, it is hard-coded that the Moc file for a directory
    will be called the directory name, with a 🗂️ prefix.

    This matches the configuration of the Zoottelkeeper plugin as of November 2021.
    """

    def moc_name_for_sub_directory(self, sub_directory):
        name = sub_directory
        if name == '..':
            name = 'hub'
        return '🗂️ ' + name

    def moc_base_name_for_directory(self, root):
        directory_name = os.path.basename(root)
        return self.moc_name_for_sub_directory(directory_name)

    def moc_file_name_for_directory(self, root):
        return self.moc_base_name_for_directory(root) + ".md"

    def moc_file_path_for_directory(self, root):
        moc_file_basename = self.moc_file_name_for_directory(root)
        return os.path.join(root, moc_file_basename)


class MocDelimiter:
    """
    Class providing the markers that are used to mark the beginning and end
    of the machine-generated links to a directory's contents.

    In this first version, we use the same strings as the Zoottelkeeper plugin,
    to enable almost identical MOCs to be generated by both update-mocs.py
    and Zoottelkeeper.

    Later, these may be replaced by strings specific to the Obsidian Hub.
    """
    @staticmethod
    def initial_delimiter():
        return '%% Zoottelkeeper: Beginning of the autogenerated index file list  %%\n'

    @staticmethod
    def final_delimiter():
        return '%% Zoottelkeeper: End of the autogenerated index file list  %%\n'
