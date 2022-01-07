import os.path
from os import walk


def check_content() -> int:
    """
    Walks through the filetree rooted at the current working directory.
    For each file that it finds, it validates the file
    """
    error_count = 0
    DIRECTORIES_TO_EXCLUDE = ['.git', '.github', '.idea', 'venv', 'DO NOT COMMIT']
    FILES_TO_EXCLUDE = ['.DS_Store', '.gitignore']

    for root, dirs, files in walk('.', topdown=True):
        dirs[:] = [d for d in dirs if d not in DIRECTORIES_TO_EXCLUDE]
        files[:] = [f for f in files if f not in FILES_TO_EXCLUDE]
        for file in files:
            relative_path = os.path.join(root, file)
            error = check_file(relative_path, file)
            error_count += error
    return error_count


def check_file(relative_path: str, file: str) -> int:
    error = 0
    if '.' not in file:
        print(f'Error:\n  This file has no extension: consider adding ".md" to its name:\n  {relative_path} ')
        error = 1
    return error


def main() -> int:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    up1 = os.path.dirname(dir_path)
    up2 = os.path.dirname(up1)
    os.chdir(up2)
    return check_content()


if __name__ == "__main__":
    result = main()
    exit(result)
