#!/usr/bin/env python3

import sys
import argparse
import glob
from themes import get_theme_plugin_support, get_theme_settings
import requests

from utils import (
    THEME_CSS_FILE,
    format_link,
    get_category_files,
    get_template,
    get_theme_css,
    print_file_summary,
    print_progress_bar,
    write_file,
    get_json_from_github,
    get_plugin_manifest,
)
from utils import PLUGINS_JSON_FILE, THEMES_JSON_FILE, OUTPUT_DIR


MOBILE_COMPATIBLE = "[[Mobile-compatible plugins|Yes]]"
DESKTOP_ONLY = "[[Desktop-only plugins|No]]"

DARK_MODE_THEMES = "[[Dark-mode themes|dark]]"
LIGHT_MODE_THEMES = "[[Light-mode themes|light]]"


def process_released_plugins(overwrite=False, verbose=False):
    print("-----\nProcessing plugins....\n")
    template = get_template("plugin")
    plugin_list = get_json_from_github(PLUGINS_JSON_FILE)

    devs = list()
    file_groups = dict()

    print_progress_bar(
        0, len(plugin_list),
    )
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
        group = write_file(
            template, plugin.get("id"), overwrite=overwrite, verbose=verbose, **plugin
        )
        devs.append(plugin)

        file_groups.setdefault(group, list()).append(plugin.get("id"))
        print_progress_bar(
            plugin_list.index(plugin) + 1, len(plugin_list),
        )

    print_file_summary(file_groups)

    return devs


def process_released_themes(overwrite=False, verbose=False):
    print("-----\nProcessing themes....\n")
    template = get_template("theme")
    theme_list = get_json_from_github(THEMES_JSON_FILE)
    designers = list()

    file_groups = dict()
    print_progress_bar(
        0, len(theme_list),
    )

    theme_downloads: dict = requests.get('https://releases.obsidian.md/stats/theme').json()

    for theme in theme_list:
        repo = theme.get("repo")
        user = repo.split("/")[0]
        modes = (
            ", ".join(theme.get("modes"))
            .replace("dark", DARK_MODE_THEMES)
            .replace("light", LIGHT_MODE_THEMES)
        )
        branch = theme.get("branch", "master")
        css_file = get_theme_css(THEME_CSS_FILE.format(repo, branch))
        settings = get_theme_settings(css_file)
        plugin_support = get_theme_plugin_support(css_file)

        current_name = theme.get("name")
        download_count = theme_downloads[current_name]["download"]

        theme.update(
            user=user,
            modes=modes,
            branch=branch,
            settings=settings,
            plugins=plugin_support,
            download_count= download_count,
        )
        group = write_file(
            template, theme.get("name"), overwrite=overwrite, verbose=verbose, **theme
        )
        designers.append(theme)
        file_groups.setdefault(group, list()).append(theme.get("name"))
        print_progress_bar(
            theme_list.index(theme) + 1, len(theme_list),
        )

    print_file_summary(file_groups)

    return designers


def get_uncategorized_plugins(overwrite=True, verbose=False):
    print("Finding uncategorized plugins....\n")
    template = get_template("category")
    UNCATEGORIZED = "Uncategorized plugins"

    released_plugins = get_json_from_github(PLUGINS_JSON_FILE)
    plugin_list = [p.get("id") for p in released_plugins]
    categorized = set()

    file_list = get_category_files()

    for file in file_list:
        if UNCATEGORIZED in file:
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

    group = write_file(
        template,
        UNCATEGORIZED,
        name=UNCATEGORIZED,
        description="Plugins which have not yet been categorized by the community.",
        plugins=uncategorized,
        overwrite=overwrite,
        verbose=True,
    )


def process_authors(theme_designers, plugin_devs, overwrite=False, verbose=False):
    print("-----\nProcessing authors....\n")
    template = get_template("author")
    total = len(theme_designers) + len(plugin_devs)

    print_progress_bar(0, total)
    all_authors = dict()
    for designer in theme_designers:
        author = designer.get("author")
        user = designer.get("user")
        theme_link = format_link(designer.get("name"))
        all_authors.setdefault(user, dict()).update(author=author, user=user)
        all_authors[user].setdefault("themes", []).append(theme_link)
        print_progress_bar(
            theme_designers.index(designer) + 1, total,
        )

    # We process plugins after because they have richer info
    for dev in plugin_devs:
        author = dev.get("author")
        user = dev.get("user")
        plugin_link = format_link(dev.get("id"), dev.get("name"))
        all_authors.setdefault(user, dict()).update(
            author=author, user=user, website=dev.get("authorUrl", "")
        )
        all_authors[user].setdefault("plugins", []).append(plugin_link)
        print_progress_bar(
            len(theme_designers) + plugin_devs.index(dev) + 1, total,
        )

    print("\nCreating author notes....\n")
    file_groups = dict()
    for user, author_info in all_authors.items():
        group = write_file(
            template, user, overwrite=overwrite, verbose=verbose, **author_info
        )
        file_groups.setdefault(group, list()).append(user)

    print_file_summary(file_groups)


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser(
        description="Create notes based on the obsidian-releases repo"
    )
    parser.add_argument(
        "--overwrite", action="store_true", help="Overwrite existing files."
    )
    parser.add_argument("-v", "--verbose", action="store_true", default=False)

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--all", action="store_true", help="Process plugins, themes and authors."
    )
    group.add_argument(
        "--themes",
        action="store_true",
        help="Only process themes (authors won't be updated).",
    )
    group.add_argument(
        "--plugins",
        action="store_true",
        help="Only process plugins (authors won't be updated)",
    )

    args = parser.parse_args(argv)

    devs = list()
    designers = list()
    if args.all or args.plugins:
        devs = process_released_plugins(args.overwrite, args.verbose)
        get_uncategorized_plugins()
    if args.all or args.themes:
        designers = process_released_themes(args.overwrite, args.verbose)

    if args.all:
        process_authors(designers, devs, args.overwrite, args.verbose)


if __name__ == "__main__":
    main()
