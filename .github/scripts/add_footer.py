#!/usr/bin/env python3

from os import walk
from os.path import join, relpath, dirname
from utils import get_template, regex_replace_in_file, append_to_file
from re import sub, search
from urllib.parse import quote

from utils import ensure_last_line_has_eol, get_root_of_vault
from jinja2.environment import Template

# These are directories and files to exclude
# By adding a dir/file, this script will ignore them and never change them!
DIRECTORIES_TO_EXCLUDE = ['.git', '.github', '.idea', 'venv', '01 Templates', 'DO NOT COMMIT']
FILES_TO_EXCLUDE = ['.DS_Store', '.gitignore', 'Hub Tree Structure.md']


def add_footer(top_directory: str, debug: bool = True) -> None:
    """
    Walks through the filetree rooted at `root`.
    For each markdown file that it finds, it replaces a particular comment line with the corresponding template.

    Parameters:
        top_directory: path from which this method should run. Generally: root of the hub.
        debug: boolean that indicates whether or not to print logging statements
    """
    # Grab the template
    template = get_template("footer")

    # This is the regex to search for
    comment = get_footer_comment_regex()

    # Loop through the files
    for root, dirs, files in walk(top_directory, topdown=True):
        # Exclude directories and files
        dirs[:] = [d for d in dirs if d not in DIRECTORIES_TO_EXCLUDE]
        dirs.sort()
        files[:] = [f for f in files if f not in FILES_TO_EXCLUDE]
        files.sort()

        # Loop through the files
        for file in files:
            # We only care about markdown files
            # Note: Alternative implementation is to use os.splitext;
            # both work for this usecase
            if file.endswith(".md"):
                absolute_path = join(root, file)
                relative_path = relpath(absolute_path, top_directory)
                ensure_footer_in_file(absolute_path, relative_path)


def ensure_footer_in_file(absolute_path: str, relative_path: str) -> None:
    """
    Will replace corrupted footers, and add missing footers.
    """
    footer_contents = render_footer(relative_path)
    footer_comment_regex = get_footer_comment_regex()

    # None if no match.
    # True if replacement changed the file
    # False if replacement left the file unchanged.
    result = regex_replace_in_file(absolute_path, footer_comment_regex, footer_contents)


    log_fmt = "[%-10s] - \"%s\""
    if result is None:
        append_to_file(absolute_path, footer_contents)
        print(log_fmt % ('ADDED', relative_path))
    elif result:
        print(log_fmt % ('REPLACED', relative_path))
    # else:
    #     # Unchanged.
    #     print(log_fmt % ('UNCHANGED', relative_path))


def get_footer_comment_regex() -> str:
    # This is the regex to search for
    # Note that we select the comment itself, and then ANYTHING afterwards
    # This requires the "DOTALL" (?s) and "MULTILINE" (?m) flags to be set
    return r"(?sm)%% Hub footer: Please don't edit anything below this line %%.*"


def encode_absolute_path_for_footer(absolute_path: str) -> str:
    relative_path = relpath(absolute_path, get_root_of_vault())
    encoded_path = quote(relative_path)
    return encoded_path

def render_footer(relative_path: str) -> str:
    # Get the rendered template (file => relative path => html encoded)
    render = get_template("footer").render(
        file_path=quote(relative_path))
    render = ensure_last_line_has_eol(render)
    return str(render)

def main() -> None:
    # Grab the root folder to run in.
    # Uses the utility method to get root of the vault.
    root = get_root_of_vault()

    # Set debug to whichever you'd like; true by default
    add_footer(root)


if __name__ == "__main__":
    main()
