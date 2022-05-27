import argparse
import os.path
import re
import sys
from os import walk
from typing import Sequence, List

# This code is for validating the **Content** of the Hub, such as file names,
# as opposed to validating the Python code and other infrastructure.

from make_mocs import MocFileAndDirectoryFilter
from utils import get_root_of_vault


class ErrorLogger:
    def __init__(self) -> None:
        self.error_count = 0

    def log_error(self, relative_path: str, message: str) -> None:
        """
        Log an error. Errors are treated as failures, giving a non-zero exit code from the script.
        """
        print(f'\nError:\n  {message}:\n  {relative_path} ')
        self.error_count += 1

    def log_warning(self, relative_path: str, message: str) -> None:
        """
        Log a warning. These will not cause the script to fail.
        """
        print(f'\nWarning:\n  {message}:\n  {relative_path} ')


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
        return

    if '.' not in file:
        logger.log_error(relative_path, 'This file has no extension: consider adding ".md" to its name')

    check_file_markdown_content(relative_path)


def get_internal_links(content: str) -> List[str]:
    regex = r'\[\[[^[]*]]'
    return re.findall(regex, content)


def check_file_markdown_content(file: str) -> None:
    if not file.endswith('.md'):
        return
    with open(file) as f:
        content = f.read()

        internal_links = get_internal_links(content)
        for link in internal_links:
            check_link(file, link)


def check_link(file: str, link: str) -> None:
    number_of_pipes = link.count('|')
    if number_of_pipes > 1:
        allowed_links_with_pipes = [
            '[[obsidian-plugin-todo|Obsidian TODO | Text-based GTD]]'
        ]
        if link not in allowed_links_with_pipes:
            logger.log_warning(file, f"Too many aliases in wiki link: {link}")


def check_content_of_vault() -> None:
    os.chdir(get_root_of_vault())
    check_content_of_working_directory()


def main(argv: Sequence[str] = sys.argv[1:]) -> None:
    parser = argparse.ArgumentParser(
        description="Check for issues with the content of the Hub vault (such as errors in file names)."
    )
    args = parser.parse_args(argv)

    check_content_of_vault()


if __name__ == "__main__":
    main()
    exit(logger.error_count)
