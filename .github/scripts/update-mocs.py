import os
import sys
import argparse

from make_mocs import moc_file_path_for_directory, index_content_for_directory

DIRECTORIES_TO_EXCLUDE = ['.git', '.github', '.idea', '.obsidian', 'meta-notes', 'venv']


def process_all_directories(directory, args):
    print("CAUTION - overwriting MOCs - DO NOT COMMIT")
    for root, dirs, files in os.walk(directory):
        filter_directories(dirs)
        dirs.sort()
        process_directory(root, dirs, files)


def filter_directories(dirs):
    dirs[:] = [d for d in dirs if d not in DIRECTORIES_TO_EXCLUDE]


def process_directory(root, dirs, files):
    moc_file_path = moc_file_path_for_directory(root)
    with open(moc_file_path, 'w') as output:
        output.write(index_content_for_directory(root, dirs, files))


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser(
        description="Create and update MOCs, mimicking Zoottelkeeper output"
    )
    parser.add_argument("-v", "--verbose", action="store_true", default=False)

    args = parser.parse_args(argv)

    process_all_directories('../..', args)


if __name__ == "__main__":
    main()
