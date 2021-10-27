import yaml
import re

from plugins import CORE_PLUGINS
from utils import PLUGINS_JSON_FILE, get_json_from_github

settings_regex = r"\/\*\s*@settings[\r\n]+?([\s\S]+?)\*\/"
plugins_regex = r"\/\*\s*@plugins[\r\n]+?([\s\S]+?)\*\/"


def get_theme_settings(theme_css):
    """
    Based on the style settings plugin: https://github.com/mgmeyers/obsidian-style-settings/blob/main/src/main.ts
    
    Example with Yin and Yang settings: https://regex101.com/r/ZAQcf6/1
    """
    match = re.search(settings_regex, theme_css, re.MULTILINE)
    if match:
        settings_str = match[1]
        settings = yaml.load(settings_str.replace("\t", "    "), Loader=yaml.FullLoader)

        start_h = None

        markdown_settings = list()

        tab_level = 0
        last_h = None
        content = True

        for setting in settings.get("settings", list()):
            if setting is None or setting.get("hub") == "ignore":
                continue

            if setting.get("type") == "heading":
                title = setting.get("title")
                description = setting.get("description", "")
                last_h = setting.get("level")
                content = False

                if start_h is None:
                    start_h = setting.get("level")

                if setting.get("level") == start_h:
                    markdown_settings.append(
                        {
                            "header": "**{}**: {}".format(title, description),
                            "type": setting.get("type"),
                        }
                    )
                    tab_level = 0

                else:
                    tab_level = setting.get("level") - start_h - 1

                    markdown_settings.append(
                        {
                            "title": "{}- **{}**: {}".format(
                                "    " * tab_level, title, description,
                            ),
                        }
                    )
            else:
                if last_h is None:
                    tab_level = 0
                elif not content and last_h != start_h:
                    tab_level = tab_level + 1

                if setting.get("description"):
                    description = ": {}".format(setting.get("description"))
                else:
                    description = ""

                markdown_settings.append(
                    {
                        "title": "{}- {}{}".format(
                            "    " * tab_level, setting.get("title"), description
                        ),
                        "type": setting.get("type"),
                    }
                )

                content = True
        return markdown_settings


def get_theme_plugin_support(theme_css, comm_plugins=None):
    match = re.search(plugins_regex, theme_css, re.MULTILINE)
    if match:
        plugin_str = match[1]
        plugins = yaml.load(plugin_str.replace("\t", "    "), Loader=yaml.FullLoader)

        core_plugins = {n.get("id"): n.get("name") for n in CORE_PLUGINS}
        supported_core_plugins = list()
        for p in plugins.get("core", list()):
            plugin_name = core_plugins.get(p)
            supported_core_plugins.append(
                "Obsidian Core Plugins#{}|{}".format(plugin_name, plugin_name)
            )
        plugins["core"] = supported_core_plugins

        if comm_plugins is None:
            plugin_list = get_json_from_github(PLUGINS_JSON_FILE)
            comm_plugins = {n.get("id"): n.get("name") for n in plugin_list}

        supported_comm_plugins = list()
        for p in plugins.get("community", list()):
            plugin_name = comm_plugins.get(p, p)
            supported_comm_plugins.append("{}|{}".format(p, plugin_name))

        plugins["community"] = supported_comm_plugins

        return plugins
