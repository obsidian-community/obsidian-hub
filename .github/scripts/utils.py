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
    "author": "01 - Community/Authors - Persons",
}


def get_template(template_name):
    file_loader = FileSystemLoader("./templates")
    env = Environment(
        loader=file_loader,
        trim_blocks=True,
        lstrip_blocks=True,
        # undefined=DebugUndefined,
    )
    return env.get_template("{}.md.jinja".format(template_name))


def get_output_dir(template, file_name):
    template_name, _, _ = template.name.split(".")
    return os.path.join(
        "../..",
        OUTPUT_DIR.get(template_name, "08 - Seedbox"),
        "{}.md".format(file_name),
    )


def write_file(template, file_name, overwrite=False, **kwargs):
    file_path = get_output_dir(template, file_name)

    # Check if file exists
    if os.path.exists(file_path) and not overwrite:
        # Compare filled-out template against contents
        with open(file_path) as file:
            contents = file.read()

        modified = "File contents don't match template."
        if contents == template.render(**kwargs):
            modified = ""

        print("{} exists. {}".format(file_name, modified))
    elif os.path.exists(file_path) and overwrite:
        print("Overwriting {}".format(file_name))
        template.stream(**kwargs).dump(file_path)
    else:
        # Create file
        print("Creating {}".format(file_name))
        template.stream(**kwargs).dump(file_path)


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
        os.path.abspath(os.path.join("../..", OUTPUT_DIR["category"])) + "/*.md"
    )


def format_link(note_name, alias=None):
    if alias is None:
        return "[[{}]]".format(note_name)
    else:
        return "[[{}|{}]]".format(note_name, alias)
