import os
import sys
import argparse

DIRECTORIES_TO_EXCLUDE = ['.git', '.github', '.idea', '.obsidian', 'meta-notes', 'venv']


def process_all_directories(directory, args):
    for root, dirs, files in os.walk(directory):
        filter_directories(dirs)
        dirs.sort()
        process_directory(root, files)


def filter_directories(dirs):
    dirs[:] = [d for d in dirs if d not in DIRECTORIES_TO_EXCLUDE]


def process_directory(root, files):
    path = root.split(os.sep)
    print((len(path) - 1) * '---', os.path.basename(root) + '/')


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser(
        description="Create and update MOCs, mimicking Zoottelkeeper output"
    )
    parser.add_argument("-v", "--verbose", action="store_true", default=False)

    args = parser.parse_args(argv)

    process_all_directories('../..', args)


if __name__ == "__main__":
    main()
