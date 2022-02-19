import os
import json
import glob
from typing import Dict, List, Union, Any

import requests

from urllib.request import urlopen
from jinja2 import FileSystemLoader, Environment, DebugUndefined
from jinja2.environment import Template

PLUGIN_MANIFEST = "https://raw.githubusercontent.com/{}/{}/manifest.json"
PLUGINS_JSON_FILE = "https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/community-plugins.json"
THEMES_JSON_FILE = "https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/community-css-themes.json"
THEME_CSS_FILE = "https://raw.githubusercontent.com/{}/{}/obsidian.css"

OUTPUT_DIR = {
    "plugin": "02 - Community Expansions/02.05 All Community Expansions/Plugins",
    "category": "02 - Community Expansions/02.01 Plugins by Category",
    "theme": "02 - Community Expansions/02.05 All Community Expansions/Themes",
    "author": "01 - Community/People",
    "plugin_issues": "01 - Community/Contributing to the Community"
}

# Type aliases:
FileGroups = Dict[str, List[str]]
# JSONType is from https://stackoverflow.com/a/58405201/104370
JSONType = Union[str, int, float, bool, None, Dict[str, Any], List[Any]]


# For performance reasons, we check the environment only once, and cache the value.
# Doing it on every call to print_progress_bar() added 45 seconds to one 
# GitHub Actions workflow
running_in_continuous_integration = os.environ.get('GITHUB_ACTIONS') != None


def get_template(template_name: str) -> Template:
    directory = "./templates"
    template_file_name = "{}.md.jinja".format(template_name)
    return get_template_from_directory(directory, template_file_name)


def get_template_from_directory(directory: str, template_name_with_extensions: str) -> Template:
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


def get_output_dir(template: Template, file_name: str) -> str:
    template_name, _, _ = template.name.split(".")
    return os.path.join(
        "../..",
        OUTPUT_DIR.get(template_name, "08 - Seedbox"),
        "{}.md".format(file_name),
    )


def write_file(template: Template,
               file_name: str,
               overwrite: bool = False,
               verbose: bool = False,
               **kwargs: Any) -> str:
    file_path = get_output_dir(template, file_name)
    absolute_file_path = os.path.abspath(file_path)

    file_content = render_template_for_file(template, absolute_file_path, **kwargs)

    # Check if file exists
    if os.path.exists(file_path) and not overwrite:
        group = "modified"
        modified = "File contents don't match template."

        if have_same_contents(file_path, file_content):
            modified = ""
            group = "exists"

        if verbose:
            print("{} exists. {}".format(file_name, modified))
    elif os.path.exists(file_path) and overwrite:
        if not have_same_contents(file_path, file_content):
            open(file_path, 'w').write(file_content)
            group = "overwritten"
            if verbose:
                print("Overwriting {}".format(file_name))
        else:
            group = "exists"
    else:
        # Create file
        if verbose:
            print("Creating {}".format(file_name))
        open(file_path, 'w').write(file_content)
        group = "new"

    return group


def render_template_for_file(template: Template, absolute_file_path: str, **kwargs: Any) -> Any:
    # This add_footer function cannot be imported at top of this file,
    # as this would cause a cyclic reference:
    from add_footer import encode_absolute_path_for_footer
    encoded_path = encode_absolute_path_for_footer(absolute_file_path)

    file_content = template.render(file_path=encoded_path, **kwargs)
    file_content = ensure_last_line_has_eol(file_content)
    return file_content


def have_same_contents(file_path: str, rendered_template: str) -> bool:
    # Compare filled-out template against contents of an existing file
    with open(file_path) as file:
        contents = file.read()

    if contents == rendered_template:
        return True

    return False


def get_json_from_github(url: str) -> JSONType:
    with urlopen(url) as response:
        json_file = json.loads(response.read())

    return json_file


def get_json_from_file(file_path: str) -> JSONType:
    with open(file_path) as f:
        json_file = json.loads(f.read())

    return json_file


def get_theme_css(url: str) -> str:
    with requests.get(url) as response:
        return response.text


def get_plugin_manifest(repository: str, branch: str) -> JSONType:
    manifest = get_json_from_github(PLUGIN_MANIFEST.format(repository, branch))
    return manifest


def get_category_files() -> List[str]:
    return glob.glob(
        os.path.abspath(os.path.join(
            "../..", OUTPUT_DIR["category"])) + "/*.md"
    )


def format_link(note_name: str, alias: Union[str, None] = None) -> str:
    if alias is None:
        return "[[{}]]".format(note_name)
    else:
        return "[[{}|{}]]".format(note_name, alias)


def add_file_group(file_groups: FileGroups, category: str, file_name_or_id: str) -> None:
    file_groups.setdefault(category, list()).append(file_name_or_id)


def print_file_summary(file_groups: FileGroups, verbose: bool = False) -> None:
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


# Print iterations progress, unless running in CI build
def print_progress_bar(
    iteration: int,
    total: int,
    prefix: str = "",
    suffix: str = "",
    decimals: int = 1,
    length: int = 100,
    fill: str = "█",
    printEnd: str = "\r",
) -> None:
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

    # Don't clutter the CI logs up with progress bar:
    if running_in_continuous_integration:
        return

    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + "-" * (length - filledLength)
    print(f"\r{prefix} |{bar}| {percent}% {suffix}", end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


def get_root_of_vault() -> str:
    """
    Helper method that returns the root directory of the vault.
    """
    dir_path = os.path.dirname(os.path.realpath(__file__))
    up1 = os.path.dirname(dir_path)
    up2 = os.path.dirname(up1)
    return up2


def ensure_last_line_has_eol(contents: str) -> str:
    """
    Ensure that the given string ends with an end-of-line character.
    :param contents: The string to check
    :return: The supplied string, with a `\n` added, if needed
    """
    eol = '\n'
    if len(contents) == 0 or contents[-1] != eol:
        contents += eol
    return contents
