import os.path

from utils import get_template
from typing import Any, List, Union
from argparse import Namespace


class VaultMoc:
    """
    Top-level class, to manage MOCs for all the directories in an entire vault.

    For now, the path to the vault is hard-coded, as there is some code
    in make_mocs.py that knows that the root of the vault is in a parent of the
    directory containing this script.
    """

    def update_all_mocs(self, args: Namespace) -> None:
        directory = '../..'  # Note: use forward slash on all platforms, for consistent output across platforms
        moc_filter = MocFileAndDirectoryFilter()
        for root, dirs, files in os.walk(directory):
            moc_filter.filter_directories(dirs)
            dirs.sort()
            directory_moc = DirectoryMoc(root, dirs, files)
            directory_moc.generate_moc()


class DirectoryMoc:
    """Class to create or update the MOC file for a single directory"""

    def __init__(self, directory: str, sub_directories: List[str], files: List[str]) -> None:
        """
        
        :param directory: name of the directory, such as '../..', 'Directory 1' or 'Directory 1/Sub-directory'
        :param sub_directories: List of names of sub-directories in directory
        :param files: List of names of files in directory
        :return: None
        """
        self.directory = directory
        self.namer = MocFileNamer()
        self.moc_file_path = self.namer.moc_file_path_for_directory(directory)
        self.sub_directories = sub_directories
        self.files = files

    def generate_moc(self) -> None:
        """
        Currently, it either updates the list of files in an existing MOC,
        or if none is present, it creates a new MOC file, using the template file
        .github/scripts/templates/directory_moc.md.jinja

        Later, it may be updated to streamline renaming of existing directories
        that already had a MOC file, named after the previous directory name.

        :return: Nothing
        """
        moc_maker = MocMaker()
        new_moc_content_with_delimiters = moc_maker.make_moc_for_directory_with_delimiters(self.directory,
                                                                                           self.sub_directories,
                                                                                           self.files)
        if os.path.exists(self.moc_file_path):
            self.rewrite_existing_moc_file(new_moc_content_with_delimiters)
        else:
            self.write_new_moc_file(new_moc_content_with_delimiters)

    def rewrite_existing_moc_file(self, new_moc_content_with_delimiters: str) -> None:
        with open(self.moc_file_path, 'r') as input:
            initial_content = input.readlines()
        with open(self.moc_file_path, 'w') as output:
            moc_maker = MocMaker()
            output.write(moc_maker.update_existing_moc(initial_content, new_moc_content_with_delimiters))

    def write_new_moc_file(self, new_moc_content_with_delimiters: str) -> None:
        template = get_template("directory_moc")
        moc_base_name = self.namer.moc_base_name_for_directory(self.directory)
        new_content = template.render(title=moc_base_name, list_of_files_and_dirs=new_moc_content_with_delimiters)
        with open(self.moc_file_path, 'w') as output:
            output.write(new_content)


class MocMaker:
    """
    Class that generates the content of a MOC file
    
    That is, it generates a Markdown list of links to files and directories
    """

    def make_moc_for_files(self, directory: str, files: List[str]) -> str:
        output = ''
        moc_filter = MocFileAndDirectoryFilter()
        for file in files:
            if not moc_filter.include_file_in_moc(directory, file):
                continue
            output += self.make_line_for_file(directory, file)
        return output

    def make_moc_for_sub_directories(self, directory: str, sub_directories: List[str]) -> str:
        output = ''
        moc_filter = MocFileAndDirectoryFilter()
        for sub_directory in sub_directories:
            if not moc_filter.include_directory_in_moc(sub_directory):
                continue
            output += self.make_line_for_sub_directory(directory, sub_directory)
        return output

    def make_moc_for_directory(self, directory: str, dirs: List[str], files: List[str]) -> str:
        result = ''

        sorted_dirs = sorted(dirs, key=str.casefold)
        result += self.make_moc_for_sub_directories(directory, sorted_dirs)

        sorted_files = sorted(files, key=str.casefold)
        result += self.make_moc_for_files(directory, sorted_files)

        if not result:
            result = '\n'
        return result

    def make_moc_for_directory_with_delimiters(self, directory: str, dirs: List[str], files: List[str]) -> str:
        result = ''
        result += MocDelimiter().initial_delimiter()
        result += self.make_moc_for_directory(directory, dirs, files)
        result += MocDelimiter().final_delimiter()
        return result

    def update_existing_moc(self, initial_content: List[str], new_moc_content_with_delimiters: str) -> str:
        inside_old_index = False
        index_written = False
        result = ''
        for line in initial_content:

            if MocDelimiter.whole_line_is_initial_delimiter(line):
                inside_old_index = True
                result += new_moc_content_with_delimiters
                index_written = True
                continue

            if MocDelimiter().whole_line_is_final_delimiter(line):
                inside_old_index = False
                continue

            if not inside_old_index:
                result += line
        if not index_written:
            result += new_moc_content_with_delimiters

        return result

    def make_line_for_file(self, directory: str, file: str) -> str:
        link_name, extension = os.path.splitext(file)
        if extension != '.md':
            link_name += extension
        return self.make_link_line(directory, link_name)

    def make_line_for_sub_directory(self, directory: str, sub_directory: str) -> str:
        path = directory + '/' + sub_directory
        namer = MocFileNamer()
        file = namer.moc_name_for_sub_directory(sub_directory)
        return self.make_link_line(path, file)

    def strip_parent_directories_from_directory(self, directory: str) -> str:
        # Ugly hack because all directory names start with '../../'
        # Note: use forward slash on all platforms, for consistent output across platforms
        result = directory.replace('../', '')
        if result == '..':  # Even more horrible hack for files in root of repo
            result = ''
        return result

    def make_link_line(self, directory: str, link_name: str) -> str:
        adjusted_directory = self.strip_parent_directories_from_directory(directory)
        if len(adjusted_directory) > 0:
            adjusted_directory += '/'
        result = f'-  [[{adjusted_directory}{link_name}|{link_name}]]\n'
        # print(f'directory={directory}\nadjusted_directory={adjusted_directory}\nlink_name={link_name}\n=> {result}')
        return result


class MocFileAndDirectoryFilter:
    """Various filtering functions, to determine what is included in the generated MOC"""

    def __init__(self) -> None:
        self.DIRECTORIES_TO_EXCLUDE = ['venv', 'DO NOT COMMIT']  # Directories beginning '.' are also excluded
        self.FILES_TO_EXCLUDE = ['logo.svg', 'publish.css']  # MOC files, and files beginning '.' are also excluded

    def include_directory_in_moc(self, directory: str) -> bool:
        if directory[0] == '.':
            return False
        return directory not in self.DIRECTORIES_TO_EXCLUDE

    def include_file_in_moc(self, directory: str, file: str) -> bool:
        if self.file_is_moc_for_directory(directory, file):
            return False
        if file in self.FILES_TO_EXCLUDE:
            return False
        return file[0] != '.'

    def file_is_moc_for_directory(self, directory: str, file: str) -> bool:
        namer = MocFileNamer()
        return file == namer.moc_file_name_for_directory(directory)

    def filter_directories(self, dirs: List[str]) -> None:
        dirs[:] = [d for d in dirs if self.include_directory_in_moc(d)]


class MocFileNamer:
    """
    Various naming functions, to determine the name and location of MOC files.

    Currently, it is hard-coded that the Moc file for a directory
    will be called the directory name, with a 🗂️ prefix.

    This matches the configuration of the Zoottelkeeper plugin as of November 2021.
    """

    def moc_name_for_sub_directory(self, sub_directory: str) -> str:
        name = sub_directory
        if name == '..':
            name = 'hub'
        return '🗂️ ' + name

    def moc_base_name_for_directory(self, directory: str) -> str:
        directory_name = os.path.basename(directory)
        return self.moc_name_for_sub_directory(directory_name)

    def moc_file_name_for_directory(self, directory: str) -> str:
        return self.moc_base_name_for_directory(directory) + ".md"

    def moc_file_path_for_directory(self, directory: str) -> str:
        moc_file_basename = self.moc_file_name_for_directory(directory)
        return os.path.join(directory, moc_file_basename)


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
    def whole_line_is_initial_delimiter(line: str) -> bool:
        return line in MocDelimiter().all_known_initial_delimiters()

    @staticmethod
    def whole_line_is_final_delimiter(line: str) -> bool:
        return line in MocDelimiter().all_known_final_delimiters()

    @staticmethod
    def all_known_initial_delimiters() -> List[str]:
        return [
            # From oldest to newest: the last one is the current one
            '%% Zoottelkeeper: Beginning of the autogenerated index file list  %%\n',
            '%% Hub MOCs: Don’t edit below  %%\n',
        ]

    @staticmethod
    def all_known_final_delimiters() -> List[str]:
        return [
            # From oldest to newest: the last one is the current one
            '%% Zoottelkeeper: End of the autogenerated index file list  %%\n',
            '%% Hub MOCs: Don’t edit above  %%\n',
        ]

    @staticmethod
    def initial_delimiter() -> str:
        return MocDelimiter.all_known_initial_delimiters()[-1]

    @staticmethod
    def final_delimiter() -> str:
        return MocDelimiter.all_known_final_delimiters()[-1]
