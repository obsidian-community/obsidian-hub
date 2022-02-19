#!/usr/bin/env python3

import sys
import argparse
from typing import Any, Dict, Sequence

from plugins import collect_data_for_plugin, PluginList

from utils import (
    format_link,
    get_category_files,
    get_template,
    FileGroups,
    print_file_summary,
    print_progress_bar,
    write_file,
    get_json_from_github,
    add_file_group,
)
from utils import PLUGINS_JSON_FILE, THEMES_JSON_FILE
from themes import get_theme_downloads, update_theme_download_count, collect_data_for_theme, ThemeList


def process_released_plugins(overwrite: bool = False, verbose: bool = False) -> PluginList:
    print("-----\nProcessing plugins....\n")
    template = get_template("plugin")
    plugin_list: PluginList = get_json_from_github(PLUGINS_JSON_FILE)

    devs: PluginList = list()
    file_groups: FileGroups = dict()

    print_progress_bar(
        0, len(plugin_list),
    )
    for plugin in plugin_list:
        plugin_is_valid = collect_data_for_plugin(plugin, file_groups)

        if not plugin_is_valid:
            continue

        group = write_file(
            template, plugin.get("id"), overwrite=overwrite, verbose=verbose, **plugin
        )
        devs.append(plugin)

        add_file_group(file_groups, group, plugin.get("id"))
        print_progress_bar(
            plugin_list.index(plugin) + 1, len(plugin_list),
        )

    print_file_summary(file_groups)

    return devs


def process_released_themes(overwrite: bool = False, verbose: bool = False) -> ThemeList:
    print("-----\nProcessing themes....\n")
    template = get_template("theme")
    theme_list: ThemeList = get_json_from_github(THEMES_JSON_FILE)
    designers: ThemeList = list()

    file_groups: FileGroups = dict()
    print_progress_bar(
        0, len(theme_list),
    )

    theme_downloads = get_theme_downloads()

    for theme in theme_list:
        current_name, valid = collect_data_for_theme(theme, theme_downloads, template, file_groups)
        if not valid:
            continue

        group = write_file(
            template, current_name, overwrite=overwrite, verbose=verbose, **theme
        )
        designers.append(theme)
        add_file_group(file_groups, group, current_name)
        print_progress_bar(
            theme_list.index(theme) + 1, len(theme_list),
        )

    print_file_summary(file_groups)

    return designers


def get_uncategorized_plugins(overwrite: bool = True, verbose: bool = False) -> None:
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
                link = f'[{plugin}|'
                if link in contents:
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


def process_authors(theme_designers: ThemeList,
                    plugin_devs: PluginList,
                    overwrite: bool = False,
                    verbose: bool = False) -> None:
    print("-----\nProcessing authors....\n")
    template = get_template("author")
    total = len(theme_designers) + len(plugin_devs)

    print_progress_bar(0, total)
    AllAuthors = Dict[str, Dict[str, Any]]
    all_authors: AllAuthors = dict()
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
    file_groups: FileGroups = dict()
    for user, author_info in all_authors.items():
        group = write_file(
            template, user, overwrite=overwrite, verbose=verbose, **author_info
        )
        add_file_group(file_groups, group, user)

    print_file_summary(file_groups)


def update_download_counts(verbose: bool = True) -> None:
    update_theme_download_counts(verbose)


def update_theme_download_counts(verbose: bool) -> None:
    print("-----\nUpdating theme download counts....\n")
    # This is so fast that there is no point showing the progress bar

    template = get_template("theme")
    theme_list = get_json_from_github(THEMES_JSON_FILE)

    theme_downloads = get_theme_downloads()

    for theme in theme_list:
        current_name = theme.get("name")
        update_theme_download_count(template, theme_downloads, current_name, verbose)


def main(argv: Sequence[str] = sys.argv[1:]) -> None:
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
    group.add_argument(
        "--update-download-counts",
        action="store_true",
        help="Only update the download counts in existing themes. "
             "This ignores the overwrite argument, and always updates.",
    )

    args = parser.parse_args(argv)

    devs = list()
    designers = list()
    if args.all or args.plugins:
        devs = process_released_plugins(args.overwrite, args.verbose)
        get_uncategorized_plugins()
    if args.all or args.themes:
        designers = process_released_themes(args.overwrite, args.verbose)
    if args.update_download_counts:
        update_download_counts(args.verbose)

    if args.all:
        process_authors(designers, devs, args.overwrite, args.verbose)


if __name__ == "__main__":
    main()
