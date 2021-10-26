import yaml
import re

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
                    h_diff = 3 - start_h

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

                markdown_settings.append(
                    {
                        "title": "{}- {}".format(
                            "    " * tab_level, setting.get("title")
                        ),
                        "type": setting.get("type"),
                    }
                )

                content = True
        return markdown_settings


def get_theme_plugin_support(theme_css):
    match = re.search(plugins_regex, theme_css, re.MULTILINE)
    if match:
        plugin_str = match[1]
        plugins = yaml.load(plugin_str.replace("\t", "    "), Loader=yaml.FullLoader)
        return plugins
