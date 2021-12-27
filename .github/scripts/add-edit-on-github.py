from os import walk, getcwd
from os.path import join
from utils import get_template
from re import sub

# The path to the vault. For now set to current working directory, as I assume all scripts are ran from the root path by default
VAULT_PATH = getcwd()

# Set to False to disable informational logging
LOG = True


def add_edit_on_github():
    """
    Walks through the filetree rooted at VAULT_PATH.
    For each markdown file that it finds, it replaces a particular comment line with the corresponding template.
    """
    # Grab the template
    template = get_template("footer")

    # This is the line to search for
    comment = r"%% Hub footer: Please don't edit anything below this line %%"

    # Loop through the files
    for root, _, files in walk(VAULT_PATH, topdown=True):
        for file in files:
            # We only care about markdown files
            # Note: Alternative implementation is to use os.splitext;
            # both work for this usecase
            if file.endswith(".md"):
                # Get the full filepath
                the_file = join(root, file)

                if LOG:
                    print(f"Processing '{the_file}'...")

                # Get the rendered template
                render = template.render(file_path=the_file)

                # Open the file in read/write mode
                with open(the_file, "r+") as f:
                    # Read the file contents
                    contents = f.read()

                    # Create variable holding the replacement text
                    # By default, don't replace anything
                    replacement = contents

                    # If the comment is found
                    if comment in contents:
                        # And we don't have the entire template yet
                        if render not in contents:
                            replacement = sub(comment, render, contents)

                            if LOG:
                                print("\t=> Replacing the line with the template.")

                    else:
                        # Comment not found!
                        replacement = contents + "\n" + render

                        if LOG:
                            print("\t=> Adding the template.")

                    # Actually write
                    # This is done by seeking to the beginning of the file
                    f.seek(0)
                    # Then writing the replacement string
                    f.write(replacement)
                    # And finally truncating the file to close it, and remove possible dangling information (e.g. if replacement is shorter than original contents)
                    f.truncate()


def main():
    add_edit_on_github()


if __name__ == "__main__":
    main()
