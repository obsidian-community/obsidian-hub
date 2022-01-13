#!/usr/bin/env python3

from os import walk
from os.path import join, relpath
from utils import get_template
from re import sub, search
from urllib.parse import quote

from utils import get_root_of_vault

# These are directories and files to exclude
# By adding a dir/file, this script will ignore them and never change them!
DIRECTORIES_TO_EXCLUDE = ['.git', '.github', '.idea', 'venv', 'DO NOT COMMIT']
FILES_TO_EXCLUDE = ['.DS_Store', '.gitignore']


def add_footer(root: str, debug: bool = True):
    """
    Walks through the filetree rooted at `root`.
    For each markdown file that it finds, it replaces a particular comment line with the corresponding template.

    Parameters:
        root: path from which this method should run. Generally: root of the hub.
        debug: boolean that indicates wether or not to print logging statements
    """
    # Grab the template
    template = get_template("footer")

    # This is the regex to search for
    # Note that we select the comment itself, and then ANYTHING afterwards
    # This requires the "DOTALL" (?s) and "MULTILINE" (?m) flags to be set
    comment = r"(?sm)%% Hub footer: Please don't edit anything below this line %%.*"

    # Loop through the files
    for root, dirs, files in walk(root, topdown=True):
        # Exclude directories and files
        dirs[:] = [d for d in dirs if d not in DIRECTORIES_TO_EXCLUDE]
        files[:] = [f for f in files if f not in FILES_TO_EXCLUDE]

        # Loop through the files
        for file in files:
            # We only care about markdown files
            # Note: Alternative implementation is to use os.splitext;
            # both work for this usecase
            if file.endswith(".md"):

                # Get the ABSOLUTE filepath
                the_file = join(root, file)

                if debug:
                    print(f"Processing '{relpath(the_file, root)}'...")

                # Get the rendered template (file => relative path => html encoded)
                render = template.render(
                    file_path=quote(relpath(the_file, root)))

                # Open the (ABSOLUTE) file in read/write mode
                with open(the_file, "r+") as f:
                    # Read the file contents
                    contents = f.read()

                    # Check if our particular comment is present
                    if search(comment, contents):
                        replacement = sub(comment, render, contents)
                        if debug:
                            print(
                                f"\t=> Replacing everything below the line with the template for '{file}'.")
                    # If it's not there: Add it
                    else:
                        replacement = contents + "\n" + render

                        if debug:
                            print(f"\t=> Adding the template for '{file}'.")

                    # Actually write
                    # This is done by seeking to the beginning of the file
                    f.seek(0)
                    # Then writing the replacement string
                    f.write(replacement)
                    # And finally truncating the file to close it
                    f.truncate()


def main():
    # Grab the root folder to run in.
    # Uses the utility method to get root of the vault.
    root = get_root_of_vault()

    # Set debug to whichever you'd like; true by default
    add_footer(root)


if __name__ == "__main__":
    main()
