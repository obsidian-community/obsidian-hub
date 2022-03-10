#!/usr/bin/env python3

import os
import re
import sys
from typing import Sequence

from utils import get_template

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
        "id": "editor-status",
        "name": "Editor status",
        "description": "Adds a status bar item to show and change the current editor mode."
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
        "description": "Publish your notes through [[Obsidian Publish]]",
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


def main(argv: Sequence[str] = sys.argv[1:]) -> None:
    get_core_plugins()


if __name__ == "__main__":
    main()
