from plugins import PluginList
from utils import get_json_from_github

PLUGINS_JSON_FILE = "https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/community-plugins.json"
THEMES_JSON_FILE = "https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/community-css-themes.json"


def get_community_plugins() -> PluginList:
    return get_json_from_github(PLUGINS_JSON_FILE)
