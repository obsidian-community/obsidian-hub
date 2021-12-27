import os
import json
import glob
import requests

from urllib.request import urlopen
from jinja2 import FileSystemLoader, Environment, DebugUndefined

PLUGIN_MANIFEST = "https://raw.githubusercontent.com/{}/{}/manifest.json"
PLUGINS_JSON_FILE = "https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/community-plugins.json"
THEMES_JSON_FILE = "https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/community-css-themes.json"
THEME_CSS_FILE = "https://raw.githubusercontent.com/{}/{}/obsidian.css"

OUTPUT_DIR = {
    "plugin": "02 - Community Expansions/02.05 All Community Expansions/Plugins",
    "category": "02 - Community Expansions/02.01 Plugins by Category",
    "theme": "02 - Community Expansions/02.05 All Community Expansions/Themes",
    "author": "01 - Community/People",
}


def get_template(template_name: str):
    """
    Gets a particular template with template_name as name.
    """
    # Default templates directory
    directory = "./templates"

    # Grab the current working directory to figure out where the template dir is.
    cwd = os.getcwd()
    if cwd.endswith("obsidian-hub"):
        # We're in root. Need to go down into .github/scripts/templates
        directory = os.path.join(cwd, ".github", "scripts", "templates")
    if cwd.endswith("github"):
        # We're in .github. Need to do down into scripts/templates
        directory = os.path.join(cwd, "scripts", "templates")
    if cwd.endswith("scripts"):
        # We're in scripts. Need to go down into templates
        directory = os.path.join(cwd, "templates")
    if cwd.endswith("templates"):
        # We're already there. Current directory.
        directory = cwd

    # Construct the filename and return the template
    template_file_name = f"{template_name}.md.jinja"
    return get_template_from_directory(directory, template_file_name)


def get_template_from_directory(directory: str, template_name_with_extensions: str):
    file_loader = FileSystemLoader(directory)
    # A note on writing templates...
    # trim_blocks and lstrip_blocks remove a lot of whitespace.
    # If you find yourself needing to prevent an end-of-line character
    # being swallowed, see these docs:
    #     https://jinja.palletsprojects.com/en/3.0.x/templates/#whitespace-control
    env = Environment(
        loader=file_loader,
        trim_blocks=True,
        lstrip_blocks=True,
        # undefined=DebugUndefined,
    )
    return env.get_template(template_name_with_extensions)


def get_output_dir(template, file_name):
    template_name, _, _ = template.name.split(".")
    return os.path.join(
        "../..",
        OUTPUT_DIR.get(template_name, "08 - Seedbox"),
        "{}.md".format(file_name),
    )


def write_file(template, file_name, overwrite=False, verbose=False, **kwargs):
    file_path = get_output_dir(template, file_name)

    # Check if file exists
    if os.path.exists(file_path) and not overwrite:
        group = "modified"
        modified = "File contents don't match template."

        if have_same_contents(file_path, template.render(**kwargs)):
            modified = ""
            group = "exists"

        if verbose:
            print("{} exists. {}".format(file_name, modified))
    elif os.path.exists(file_path) and overwrite:
        if not have_same_contents(file_path, template.render(**kwargs)):
            template.stream(**kwargs).dump(file_path)
            group = "overwritten"
            if verbose:
                print("Overwriting {}".format(file_name))
        else:
            group = "exists"
    else:
        # Create file
        if verbose:
            print("Creating {}".format(file_name))
        template.stream(**kwargs).dump(file_path)
        group = "new"

    return group


def have_same_contents(file_path, rendered_template):
    # Compare filled-out template against contents of an existing file
    with open(file_path) as file:
        contents = file.read()

    if contents == rendered_template:
        return True

    return False


def get_json_from_github(url):
    with urlopen(url) as response:
        json_file = json.loads(response.read())

    return json_file


def get_theme_css(url):
    with requests.get(url) as response:
        return response.text


def get_plugin_manifest(repository, branch):
    manifest = get_json_from_github(PLUGIN_MANIFEST.format(repository, branch))
    return manifest


def get_category_files():
    return glob.glob(
        os.path.abspath(os.path.join(
            "../..", OUTPUT_DIR["category"])) + "/*.md"
    )


def format_link(note_name, alias=None):
    if alias is None:
        return "[[{}]]".format(note_name)
    else:
        return "[[{}|{}]]".format(note_name, alias)


def print_file_summary(file_groups, verbose=False):
    messages = {
        "error": "has an error, so was ignored.",
        "exists": "exist but no changes were detected.",
        "modified": "exist, but file contents and filled out template don't match.",
        "new": "were newly created.",
        "overwritten": "were overwritten.",
    }
    for g, files in file_groups.items():
        print("{} files {}".format(len(files), messages.get(g)))
        if g not in ["exists"] or verbose:
            for f in files:
                print("\t- {}".format(f))


# Print iterations progress
def print_progress_bar(
    iteration,
    total,
    prefix="",
    suffix="",
    decimals=1,
    length=100,
    fill="█",
    printEnd="\r",
):
    """
    Call in a loop to create terminal progress bar

    Source: https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console

    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + "-" * (length - filledLength)
    print(f"\r{prefix} |{bar}| {percent}% {suffix}", end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()
