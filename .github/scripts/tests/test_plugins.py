import json

import plugins

from approvaltests.approvals import verify_as_json

from test_make_mocs import approval_test_options


# Names that are currently manually edited when update-releases.py is run:
#  "Andrew Brown & Tim Hor" -> "Tim Hor",
#  "bicarlsen" -> "Brian Carlsen",
#       https://github.com/bicarlsen/obsidian_image_caption/pull/7
#  "Chetachi" -> "Chetachi E.",
#  "ryanjamurphy" -> "Ryan J. A. Murphy"


def test_author_augmented_for_ryanjamurphy():
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

    plugin = json.loads(plugin_as_json)
    file_groups = dict()
    result = plugins.collect_data_for_plugin(plugin, file_groups)
    verify_as_json(plugin, options=approval_test_options())
