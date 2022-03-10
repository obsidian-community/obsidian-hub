import json

import plugins

from helpers_for_testing import verify_in_json_format_to_markdown
from utils import FileGroups


def verify_plugin(manifest_as_json: str, plugin_as_json: str) -> None:
    plugin = plugins.Plugin(json.loads(plugin_as_json))
    manifest = json.loads(manifest_as_json)
    file_groups: FileGroups = dict()
    result = plugin.collect_data_for_plugin_and_manifest(manifest, file_groups)
    verify_in_json_format_to_markdown(plugin.data())


def test_author_augmented_for_ryanjamurphy() -> None:
    # Copied from https://github.com/obsidianmd/obsidian-releases/blob/30b6c827db345e92ce62d50c431878b80ede9d17/community-plugins.json
    plugin_as_json = '''
    {
        "id": "DEVONlink-obsidian",
        "name": "DEVONlink - Open or reveal notes in DEVONthink",
        "description": "Open or reveal the current note in DEVONthink.",
        "author": "ryanjamurphy",
        "repo": "ryanjamurphy/DEVONlink-obsidian"
    }
    '''

    manifest_as_json = '''
    {
        "id": "DEVONlink-obsidian",
        "name": "DEVONlink",
        "version": "2.2.1",
        "minAppVersion": "0.9.12",
        "description": "Open or reveal the current note in DEVONthink.",
        "author": "ryanjamurphy",
        "authorUrl": "https://axle.design",
        "isDesktopOnly": true
    }
    '''
    verify_plugin(manifest_as_json, plugin_as_json)


def test_author_missing_from_manifest() -> None:
    # This plugin has the author name in the community plugins file, but not in its own manifest.json
    # This test verifies that this situation is handled correctly.
    plugin_as_json = '''
    {
        "id": "obsidian-git",
        "name": "Obsidian Git",
        "author": "Denis Olehov",
        "description": "Backup your vault with git.",
        "repo": "denolehov/obsidian-git"
    }
    '''

    manifest_as_json = '''
    {
        "id": "obsidian-git",
        "name": "Obsidian Git",
        "description": "Backup your vault with git.",
        "isDesktopOnly": true,
        "js": "main.js",
        "version": "1.19.0"
    }
    '''
    verify_plugin(manifest_as_json, plugin_as_json)
