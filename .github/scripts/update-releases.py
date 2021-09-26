import sys
import argparse
import glob

from utils import (
    get_category_files,
    get_template,
    write_file,
    get_json_from_github,
    get_plugin_manifest,
)
from utils import PLUGINS_JSON_FILE, THEMES_JSON_FILE, OUTPUT_DIR


MOBILE_COMPATIBLE = "[[Mobile-compatible plugins|Yes]]"
DESKTOP_ONLY = "[[Desktop-only plugins|No]]"

DARK_MODE_THEMES = "[[Dark-mode themes|dark]]"
LIGHT_MODE_THEMES = "[[Light-mode themes|light]]"


def process_released_plugins(overwrite=False):
    template = get_template("plugin")
    plugin_list = get_json_from_github(PLUGINS_JSON_FILE)
    for plugin in plugin_list:
        repo = plugin.get("repo")
        branch = plugin.get("branch", "master")
        manifest = get_plugin_manifest(repo, branch)
        user = repo.split("/")[0]
        if manifest.get("isDesktopOnly"):
            mobile = DESKTOP_ONLY
        else:
            mobile = MOBILE_COMPATIBLE

        plugin.update(mobile=mobile, user=user, **manifest)
        write_file(template, plugin.get("id"), overwrite=overwrite, **plugin)


def process_released_themes(overwrite=False):
    print("-----\nProcessing themes....\n")
    template = get_template("theme")
    theme_list = get_json_from_github(THEMES_JSON_FILE)
    for theme in theme_list:
        repo = theme.get("repo")
        user = repo.split("/")[0]
        modes = (
            ", ".join(theme.get("modes"))
            .replace("dark", DARK_MODE_THEMES)
            .replace("light", LIGHT_MODE_THEMES)
        )
        branch = theme.get("branch", "master")
        theme.update(user=user, modes=modes, branch=branch)
        write_file(template, theme.get("name"), overwrite=overwrite, **theme)


def get_uncategorized_plugins(overwrite=False):
    template = get_template("category")

    released_plugins = get_json_from_github(PLUGINS_JSON_FILE)
    plugin_list = [p.get("id") for p in released_plugins]
    categorized = set()

    file_list = get_category_files()

    for file in file_list:
        if "Uncategorized plugins" in file:
            continue

        with open(file) as category_file:
            contents = category_file.read()
            for plugin in plugin_list:
                if plugin in contents:
                    categorized.add(plugin)

    uncategorized = list()
    for p in released_plugins:
        if p.get("id") in set(plugin_list).difference(categorized):
            uncategorized.append(p)

    write_file(
        template,
        "Uncategorized plugins",
        name="Uncategorized plugins",
        description="Plugins which have not yet been categorized by the community.",
        plugins=uncategorized,
        overwrite=overwrite,
    )


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser(
        description="Create notes based on the obsidian-releases repo"
    )
    parser.add_argument(
        "--overwrite", action="store_true", help="Overwrite existing files."
    )
    args = parser.parse_args(argv)

    process_released_plugins(args.overwrite)
    process_released_themes(args.overwrite)
    get_uncategorized_plugins(args.overwrite)


if __name__ == "__main__":
    main()
