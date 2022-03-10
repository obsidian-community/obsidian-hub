from plugins import PluginList, Plugin
from utils import get_json_from_github

PLUGINS_JSON_FILE = "https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/community-plugins.json"
THEMES_JSON_FILE = "https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/community-css-themes.json"


def get_community_plugins() -> PluginList:
    raw_data = get_json_from_github(PLUGINS_JSON_FILE)
    plugin_list = list()
    for el in raw_data:
        plugin_list.append(Plugin(el))
    return plugin_list
