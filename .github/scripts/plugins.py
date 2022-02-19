#!/usr/bin/env python3

import re
import os
import sys
from typing import Union, Any, Dict, List, Sequence

from authors import update_author_name_for_manual_exceptions
from utils import get_template, get_plugin_manifest, FileGroups, add_file_group

# Type aliases:
Plugin = Dict[str, Any]
PluginList = List[Plugin]
PluginManifest = Dict[str, Union[str, bool]]

MOBILE_COMPATIBLE = "[[Mobile-compatible plugins|Yes]]"
DESKTOP_ONLY = "[[Desktop-only plugins|No]]"

CORE_PLUGINS = [
    {
        "id": "audio-recorder",
        "name": "Audio recorder",
        "description": "Record audio and save as attachment.",
    },
    {
        "id": "backlink",
        "name": "Backlinks",
        "description": "Show the number of backlinks in the status bar, and display backlinks and unlinked mentions in a sidebar tab.",
    },
    {
        "id": "command-palette",
        "name": "Command palette",
        "description": "Use Cmd/Ctrl+P and begin typing to invoke a command.",
    },
    {
        "id": "daily-notes",
        "name": "Daily notes",
        "description": "Create or open today’s daily note.",
    },
    {
        "id": "file-explorer",
        "name": "File explorer",
        "description": "See the files and folders in your vault.",
    },
    {
        "id": "file-recovery",
        "name": "File recovery",
        "description": "Let you restore recent snapshots to recover from accidental data loss. Snapshots are only saved for Markdown files.",
    },
    {
        "id": "global-search",
        "name": "Search",
        "description": "Search for a keyword in all the notes.",
    },
    {
        "id": "graph",
        "name": "Graph view",
        "description": "View a graph that displays links between your notes.",
    },
    {
        "id": "markdown-importer",
        "name": "Markdown format converter",
        "description": "Convert Markdown from other apps to Obsidian format.",
    },
    {
        "id": "note-composer",
        "name": "Note composer",
        "description": "Merge, split, and refactor notes.",
    },
    {
        "id": "open-with-default-app",
        "name": "Open in default app",
        "description": "Add a button to open the current file in its default app.",
    },
    {
        "id": "outgoing-link",
        "name": "Outgoing Links",
        "description": "Show outgoing links and detect unlinked mentions of other notes in the current note.",
    },
    {
        "id": "outline",
        "name": "Outline",
        "description": "Display the outline of the current file or linked pane.",
    },
    {
        "id": "page-preview",
        "name": "Page preview",
        "description": "Hover an internal link to preview its content. In editor mode, press Ctrl/Cmd while hovering.",
    },
    {
        "id": "publish",
        "name": "Publish",
        "description": "Publish your notes through [[Obsidian Publish.]]",
    },
    {
        "id": "random-note",
        "name": "Random note",
        "description": "Open a random note to rediscover or review.",
    },
    {
        "id": "slash-commands",
        "name": "Slash commands",
        "description": "Enable the ability to trigger slash commands in the editor by typing the forward slash.",
    },
    {
        "id": "slides",
        "name": "Slides",
        "description": "Present from Markdown. Use '---' to separate slides.",
    },
    {
        "id": "starred",
        "name": "Starred notes",
        "description": "Star frequently used files and searches.",
    },
    {
        "id": "switcher",
        "name": "Quick switcher",
        "description": "Use Ctrl/Cmd+O to jump to other files with your keyboard.",
    },
    {
        "id": "sync",
        "name": "Sync",
        "description": "Synchronize your files through [[Obsidian Sync]].",
    },
    {
        "id": "tag-pane",
        "name": "Tag pane",
        "description": "Display your tags and their number of occurrences.",
    },
    {
        "id": "templates",
        "name": "Templates",
        "description": "Insert template content from a folder of template files.",
    },
    {
        "id": "word-count",
        "name": "Word count",
        "description": "Show word count in the status bar.",
    },
    {
        "id": "workspaces",
        "name": "Workspaces",
        "description": "Save and load workspace layout.",
    },
    {
        "id": "zk-prefixer",
        "name": "Zettelkasten prefixer",
        "description": "Create a note with a 12-digit Zettelkasten ID (YYYYMMDDHHII).",
    },
]


def get_core_plugins() -> None:
    template = get_template("core_plugin")
    file_path = os.path.join("../..", "05 - Concepts/Obsidian Core Plugins.md")
    with open(file_path, "r") as md_file:
        contents = md_file.read()

    match = re.search(
        r"%% Begin Hub: Core Plugins %%[\r\n]+?([\s\S]+?)%% End Hub: Core Plugins %%",
        contents,
        re.MULTILINE,
    )

    for plugin in CORE_PLUGINS:
        plugin["slug"] = "Plugins/" + plugin["name"].replace(" ", "+")

    assert match # Needed to stop match[1] giving 'error: Value of type "Optional[Match[str]]" is not indexable'
    new_contents = contents.replace(match[1], template.render(plugins=CORE_PLUGINS))

    with open(file_path, "w") as md_file:
        md_file.write(new_contents)


def collect_data_for_plugin(plugin: Plugin, file_groups: FileGroups) -> bool:
    """
    Take raw plugin data from a community plugin, and add information to it,
    typically from its manifest file.

    :param plugin: A dict with data about the plugin, to be updated by this function
    :param file_groups: Place to store error message if the plugin is invalid
    :return: Whether the plugin is valid, and is OK to be added to the Hub
    """
    repo = plugin.get("repo")
    branch = plugin.get("branch", "master")
    current_name = str(plugin.get("name"))

    try:
        manifest = get_plugin_manifest(repo, branch)
        return collect_data_for_plugin_and_manifest(plugin, manifest, file_groups)

    except Exception as err:
        print(f'ERROR processing plugin {current_name}. Error message: {err}')
        plugin_is_valid = False
        add_file_group(file_groups, "error", f"{current_name}")
        return plugin_is_valid


def collect_data_for_plugin_and_manifest(plugin: Plugin, manifest: PluginManifest, file_groups: FileGroups) -> bool:
    # the cast to str is to silence: error: Item "None" of "Optional[Any]" has no attribute "split"
    repo = str(plugin.get("repo"))
    plugin_is_valid = validate_plugin(plugin, manifest, repo, file_groups)

    user = repo.split("/")[0]
    if manifest.get("isDesktopOnly"):
        mobile = DESKTOP_ONLY
    else:
        mobile = MOBILE_COMPATIBLE

    plugin.update(mobile=mobile, user=user, **manifest)
    update_author_name_for_manual_exceptions(plugin)

    return plugin_is_valid


def validate_plugin(plugin: Plugin, manifest: PluginManifest, repo: str, file_groups: FileGroups) -> bool:
    return validate_plugin_ids(plugin, manifest, repo, file_groups)


def validate_plugin_ids(plugin: Plugin, manifest: PluginManifest, repo: str, file_groups: FileGroups) -> bool:
    ids_match = True
    releases_id = plugin.get('id')
    manifest_id = manifest.get('id')
    if releases_id != manifest_id:
        print(
            f"ERROR repo:{repo} ID {releases_id} does not match ID in manifest: {manifest_id}")
        add_file_group(file_groups, "error", f"{releases_id}/{manifest_id}")
        ids_match = False
    return ids_match


def main(argv: Sequence[str] = sys.argv[1:]) -> None:
    get_core_plugins()


if __name__ == "__main__":
    main()
