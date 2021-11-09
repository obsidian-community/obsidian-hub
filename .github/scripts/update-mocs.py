import os
import sys
import argparse

from make_mocs import filter_directories, moc_file_path_for_directory, moc_base_name_for_directory, \
    make_moc_for_directory_with_delimiters, update_existing_moc
from utils import get_template


class VaultMoc:
    """
    Top-level class, to manage MOCs for all the directories in an entire vault.

    For now, the path to the vault is hard-coded, as there is some code
    in make_mocs.py that the root of the vault is in a parent of the
    directory containing this script.
    """
    def update_all_mocs(self, args):
        directory = '../..'
        for root, dirs, files in os.walk(directory):
            filter_directories(dirs)
            dirs.sort()
            directory_moc = DirectoryMoc()
            directory_moc.generate_moc(root, dirs, files)


class DirectoryMoc:
    """Class to manage the MOC for a single directory"""

    def generate_moc(self, root, dirs, files):
        process_directory(root, dirs, files)


def process_directory(root, dirs, files):
    moc_file_path = moc_file_path_for_directory(root)
    new_moc_content_with_delimiters = make_moc_for_directory_with_delimiters(root, dirs, files)
    if os.path.exists(moc_file_path):
        rewrite_existing_moc_file(moc_file_path, new_moc_content_with_delimiters)
    else:
        write_new_moc_file(root, moc_file_path, new_moc_content_with_delimiters)


def rewrite_existing_moc_file(moc_file_path, new_moc_content_with_delimiters):
    with open(moc_file_path, 'r') as input:
        initial_content = input.readlines()
    with open(moc_file_path, 'w') as output:
        output.write(update_existing_moc(initial_content, new_moc_content_with_delimiters))


def write_new_moc_file(root, moc_file_path, new_moc_content_with_delimiters):
    template = get_template("directory_moc")
    moc_base_name = moc_base_name_for_directory(root)
    new_content = template.render(title=moc_base_name, list_of_files_and_dirs=new_moc_content_with_delimiters)
    with open(moc_file_path, 'w') as output:
        output.write(new_content)


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser(
        description="Create and update MOCs, mimicking Zoottelkeeper output"
    )
    # parser.add_argument("-v", "--verbose", action="store_true", default=False)

    args = parser.parse_args(argv)

    vault_moc = VaultMoc()
    vault_moc.update_all_mocs(args)


if __name__ == "__main__":
    main()
