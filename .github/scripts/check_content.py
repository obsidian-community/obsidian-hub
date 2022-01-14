import argparse
import os.path
import sys
from os import walk

# This code is for validating the **Content** of the Hub, such as file names,
# as opposed to validating the Python code and other infrastructure.

from make_mocs import MocFileAndDirectoryFilter
from utils import get_root_of_vault


class ErrorLogger:
    def __init__(self):
        self.error_count = 0

    def log_error(self, relative_path, message):
        print(f'Error:\n  {message}:\n  {relative_path} ')
        self.error_count += 1


logger = ErrorLogger()


def check_content_of_working_directory() -> None:
    """
    Walks through the filetree rooted at the current working directory.
    For each file that it finds, it validates the file
    """
    moc_filter = MocFileAndDirectoryFilter()
    for root, dirs, files in walk('.', topdown=True):
        moc_filter.filter_directories(dirs)
        for file in files:
            relative_path = os.path.join(root, file)
            check_file(relative_path, file)


def check_file(relative_path: str, file: str) -> None:
    """
    Check the given file for any issues.

    Writes error messages to the console, and returns the number of errors found.

    'dot' files are ignored.

    :param relative_path: The path of the file, including the directory, relative to the vault's root
    :param file: The name of the file, without any directory
    :return: The number of errors found in the given file
    """
    # Ignore 'dot' files, such as '.gitignore'
    if file[0] == '.':
        return 0

    if '.' not in file:
        logger.log_error(relative_path, 'This file has no extension: consider adding ".md" to its name')

    # Other checks may be added here in future


def check_content_of_vault() -> None:
    os.chdir(get_root_of_vault())
    check_content_of_working_directory()


def main(argv=sys.argv[1:]) -> None:
    parser = argparse.ArgumentParser(
        description="Check for issues with the content of the Hub vault (such as errors in file names)."
    )
    args = parser.parse_args(argv)

    check_content_of_vault()


if __name__ == "__main__":
    main()
    exit(logger.error_count)
