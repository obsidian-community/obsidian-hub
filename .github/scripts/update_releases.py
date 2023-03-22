#!/usr/bin/env python3
import os
import sys
import argparse
from typing import Sequence

from authors import AllAuthors
from obsidian_releases import get_community_plugins
from plugins import PluginList
from sort_lists import sort_links_under_heading

from utils import (
    format_link,
    get_category_files,
    get_template,
    FileGroups,
    print_file_summary,
    print_progress_bar,
    write_template_file,
    add_file_group,
    get_output_path,
    get_output_dir,
    FileNameCaseCollisionsPreventer,
)
from themes import ThemeList, Theme, ThemeDownloadCount, get_community_themes


def process_released_plugins(overwrite: bool = False, verbose: bool = False) -> PluginList:
    print("-----\nProcessing plugins....\n")
    template = get_template("plugin")
    plugins_dir = get_output_dir(template)
    collision_preventer = FileNameCaseCollisionsPreventer(plugins_dir)
    plugin_list: PluginList = get_community_plugins()

    valid_plugins: PluginList = list()
    file_groups: FileGroups = dict()

    print_progress_bar(
        0, len(plugin_list),
    )
    for plugin in plugin_list:
        plugin_is_valid = plugin.collect_data_for_plugin(file_groups)

        if not plugin_is_valid:
            continue

        group = write_template_file(
            template, collision_preventer.get_name(plugin.id()), overwrite=overwrite, verbose=verbose, **plugin.data()
        )
        valid_plugins.append(plugin)

        add_file_group(file_groups, group, plugin.id())
        print_progress_bar(
            plugin_list.index(plugin) + 1, len(plugin_list),
        )

    print_file_summary(file_groups)

    return valid_plugins


def process_released_themes(overwrite: bool = False, verbose: bool = False) -> ThemeList:
    print("-----\nProcessing themes....\n")
    theme_list = get_community_themes()
    valid_themes: ThemeList = list()

    file_groups: FileGroups = dict()
    print_progress_bar(
        0, len(theme_list),
    )

    theme_downloads = ThemeDownloadCount.get_theme_downloads()

    themes_dir = get_output_dir(Theme.template)
    collision_preventer = FileNameCaseCollisionsPreventer(themes_dir)

    for index, theme in enumerate(theme_list):
        current_name, valid = theme.collect_data_for_theme(theme_downloads, file_groups)
        if not valid:
            continue

        # Prefer the existing capitalisation of any existing filename,
        # to prevent case-conflicts.
        current_name = collision_preventer.get_name(current_name)

        group = write_template_file(
            Theme.template, current_name, overwrite=overwrite, verbose=verbose, **theme.data()
        )
        valid_themes.append(theme)
        add_file_group(file_groups, group, current_name)
        print_progress_bar(
            index + 1, len(theme_list),
        )

    print_file_summary(file_groups)

    return valid_themes


def update_uncategorized_plugins(valid_plugins: PluginList, overwrite: bool = True) -> None:
    print("Finding uncategorized plugins....\n")
    UNCATEGORIZED = "Uncategorized plugins"

    plugin_ids = [p.id() for p in valid_plugins]
    categorized = set()

    file_list = get_category_files()

    for file in file_list:
        if UNCATEGORIZED in file:
            continue

        with open(file) as category_file:
            contents = category_file.read()
            for plugin in plugin_ids:
                link = f'[{plugin}|'
                if link in contents:
                    categorized.add(plugin)

    uncategorized = list()
    for p in valid_plugins:
        if p.id() in set(plugin_ids).difference(categorized):
            uncategorized.append(p.data())

    template = get_template("category")
    write_template_file(
        template,
        UNCATEGORIZED,
        name=UNCATEGORIZED,
        description="Plugins which have not yet been categorized by the community.",
        plugins=uncategorized,
        overwrite=overwrite,
        verbose=True,
    )

    # Alphabetize the plugin list
    file_path = get_output_path(template, UNCATEGORIZED)
    absolute_file_path = os.path.abspath(file_path)
    sort_links_under_heading(absolute_file_path)


def process_authors(themes: ThemeList,
                    plugins: PluginList,
                    overwrite: bool = False,
                    verbose: bool = False) -> None:
    print("-----\nProcessing authors....\n")
    template = get_template("author")
    authors_dir = get_output_dir(template)
    collision_preventer = FileNameCaseCollisionsPreventer(authors_dir)
    all_authors = collate_authors(themes, plugins)

    print("\nCreating author notes....\n")
    file_groups: FileGroups = dict()
    for user, author_info in all_authors.items():
        group = write_template_file(
            template, collision_preventer.get_name(user), overwrite=overwrite, verbose=verbose, **author_info
        )
        add_file_group(file_groups, group, user)

    print_file_summary(file_groups)


def collate_authors(themes: ThemeList, plugins: PluginList) -> AllAuthors:

    all_authors = AllAuthors()
    for theme in themes:
        author = theme.author()
        user = theme.user()
        theme_link = format_link(theme.name())
        all_authors.setdefault(user, dict()).update(author=author, user=user)
        all_authors[user].setdefault("themes", []).append(theme_link)

    # We process plugins after because they have richer info
    for plugin in plugins:
        author = plugin.author()
        user = plugin.user()
        plugin_link = format_link(plugin.id(), plugin.name())
        all_authors.setdefault(user, dict()).update(
            author=author, user=user, website=plugin.authorUrl()
        )
        all_authors[user].setdefault("plugins", []).append(plugin_link)

    return all_authors


def update_download_counts(verbose: bool = True) -> None:
    update_theme_download_counts(verbose)


def update_theme_download_counts(verbose: bool) -> None:
    print("-----\nUpdating theme download counts....\n")
    # This is so fast that there is no point showing the progress bar

    template = get_template("theme")
    theme_list = get_community_themes()

    theme_downloads = ThemeDownloadCount.get_theme_downloads()

    for theme in theme_list:
        current_name = theme.name()
        ThemeDownloadCount.update_theme_download_count(template, theme_downloads, current_name, verbose)


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

    plugins = list()
    themes = list()
    if args.all or args.plugins:
        plugins = process_released_plugins(args.overwrite, args.verbose)
        update_uncategorized_plugins(plugins)
    if args.all or args.themes:
        themes = process_released_themes(args.overwrite, args.verbose)
    if args.update_download_counts:
        update_download_counts(args.verbose)

    if args.all:
        process_authors(themes, plugins, args.overwrite, args.verbose)


if __name__ == "__main__":
    main()
