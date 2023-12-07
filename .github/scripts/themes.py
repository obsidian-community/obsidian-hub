import yaml
import os
import re
import requests
import typing
from typing import Optional, Union, Dict, List
from jinja2.environment import Template

from hub_types import ThemeDownloads, ThemeSettings, ThemePluginSupport, ThemeStorage
from obsidian_releases import get_community_plugins, THEMES_JSON_FILE
from core_plugins import CORE_PLUGINS
from utils import (
    THEME_CSS_FILE,
    THEME_LEGACY_CSS_FILE,
    get_output_path,
    get_theme_css,
    FileGroups,
    add_file_group, get_template, get_json_from_github
)

# enquote Theme so that it can be used before it is declared
ThemeList = List["Theme"]

CommunityPluginsIDAndName = Dict[str, str]

settings_regex = r"\/\*!?\s*@settings[\r\n]+?([\s\S]+?)\*\/"
plugins_regex = r"\/\*!?\s*@plugins[\r\n]+?([\s\S]+?)\*\/"

DOWNLOAD_COUNT_SHIELDS_URL_PREFIX = 'https://img.shields.io/badge/downloads-'
DOWNLOAD_COUNT_SEARCH = re.compile(DOWNLOAD_COUNT_SHIELDS_URL_PREFIX + r"(\d+)-")

DARK_MODE_THEMES = "[[Dark-mode themes|dark]]"
LIGHT_MODE_THEMES = "[[Light-mode themes|light]]"


class Theme:
    # will be shared between all instances, so only created once
    template = get_template("theme")

    def __init__(self, data: ThemeStorage):
        self.__data = data

    def name(self) -> str:
        return str(self.__data.get("name"))

    def author(self) -> str:
        return str(self.__data.get("author"))

    def user(self) -> str:
        return str(self.__data.get("user"))

    def repo(self) -> str:
        return str(self.__data.get("repo"))

    def branch(self) -> str:
        return str(self.__data.get("branch", "HEAD"))

    def modes(self) -> List[str]:
        return typing.cast(typing.List[str], self.__data.get("modes"))

    def data(self) -> ThemeStorage:
        return self.__data

    @staticmethod
    def get_theme_settings(theme_css: str) -> Optional[ThemeSettings]:
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

        return None

    @staticmethod
    def get_theme_plugin_support(
            theme_css: str,
            comm_plugins: Optional[CommunityPluginsIDAndName] = None) -> Optional[ThemePluginSupport]:
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
                plugin_list = get_community_plugins()
                comm_plugins = {n.id(): n.name() for n in plugin_list}

            supported_comm_plugins = list()
            for p in plugins.get("community", list()):
                plugin_name = comm_plugins.get(p, p)
                supported_comm_plugins.append("{}|{}".format(p, plugin_name))

            plugins["community"] = supported_comm_plugins

            return plugins

        return None

    def collect_data_for_theme(self, theme_downloads: ThemeDownloads, file_groups: FileGroups) -> typing.Tuple[
        str, bool]:
        """
        Take raw theme data from a community theme, and add information to it.

        :param theme_downloads: The download count of all themes
        :param file_groups:  Place to store error message if the theme is invalid
        :return: The name of the theme, and whether it is valid
        """
        repo = self.repo()
        branch = self.branch()
        # we check for the new `theme.css` first, and if that doesn't exist, we check for the legacy `obsidian.css`
        css_file = get_theme_css(THEME_CSS_FILE.format(repo, branch))
        if css_file == "404: Not Found":
            css_file = get_theme_css(THEME_LEGACY_CSS_FILE.format(repo, branch))

        return self.collect_data_for_theme_and_css(css_file, theme_downloads, file_groups)

    def collect_data_for_theme_and_css(self, css_file: str, theme_downloads: ThemeDownloads,
                                       file_groups: FileGroups) -> typing.Tuple[str, bool]:
        valid = True
        current_name = self.name()

        try:
            repo = self.repo()
            branch = self.branch()
            user = repo.split("/")[0]
            raw_modes = self.modes()
            assert raw_modes
            modes = (
                ", ".join(raw_modes)
                    .replace("dark", DARK_MODE_THEMES)
                    .replace("light", LIGHT_MODE_THEMES)
            )
            settings = Theme.get_theme_settings(css_file)
            plugin_support = Theme.get_theme_plugin_support(css_file)

            download_count = ThemeDownloadCount.get_theme_download_count_preferring_previous(Theme.template,
                                                                                             theme_downloads,
                                                                                             current_name)

            self.__data.update(
                user=user,
                modes=modes,
                branch=branch,
                settings=settings,
                plugins=plugin_support,
                download_count=download_count,
            )
        except Exception as err:
            print(f'ERROR processing theme {current_name}. Error message: {err}')
            add_file_group(file_groups, "error", f"{current_name}")
            valid = False

        return current_name, valid


class ThemeDownloadCount:

    @staticmethod
    def get_theme_download_count_preferring_previous(template: Template, theme_downloads: ThemeDownloads,
                                                     current_name: str) -> int:
        previous_download_count = ThemeDownloadCount.get_theme_previous_download_count_or_none(template, current_name)
        if previous_download_count:
            return previous_download_count

        return ThemeDownloadCount.get_theme_current_download_count(theme_downloads, current_name)

    @staticmethod
    def get_theme_current_download_count(theme_downloads: ThemeDownloads, current_name: str) -> int:
        return int(theme_downloads[current_name]["download"])

    @staticmethod
    def get_theme_previous_download_count_or_none(template: Template, current_name: str) -> Union[int, None]:
        """
        Read the theme file from disk, and return the previously-saved download count
        :return: The saved theme download count, or None if this could not be obtained
        """
        file_name = get_output_path(template, current_name)
        if not os.path.exists(file_name):
            # This is a new theme, so we don't yet have a previous download count:
            return None

        with open(file_name) as file:
            contents = file.read()
            result = DOWNLOAD_COUNT_SEARCH.search(contents)
            if not result:
                # We could not extract the previous download count.
                # Perhaps the URL in the theme template has been modified?
                return None
            return int(result.group(1))

    @staticmethod
    def set_theme_download_count(template: Template, current_name: str, new_download_count: int, verbose: bool) -> None:
        file_name = get_output_path(template, current_name)

        if not os.path.exists(file_name):
            if verbose:
                print("No note for theme            {}".format(file_name))
            return

        previous_download_count = ThemeDownloadCount.get_theme_previous_download_count_or_none(template, current_name)
        if not previous_download_count:
            if verbose:
                print("Cannot read download count   {}".format(file_name))
            return

        # If the download count has decreased, there is something gone fundamentally wrong:
        # assert new_download_count >= previous_download_count

        if new_download_count == previous_download_count:
            if verbose:
                print("Download count unchanged     {}".format(file_name))
            return

        # This is a bit hacky, as the call to get_previous_download_count_or_none()
        # already read the file. However, this code is so very fast to run
        # that, for simplicity, it's easier to just re-read the file for now.
        with open(file_name) as file:
            old_contents = file.read()

        old_text = ThemeDownloadCount.get_url_pattern_for_downloads_shield(previous_download_count)
        new_text = ThemeDownloadCount.get_url_pattern_for_downloads_shield(new_download_count)
        new_contents = old_contents.replace(old_text, new_text)
        assert new_contents != old_contents

        with open(file_name, 'w') as file:
            file.write(new_contents)

        if verbose:
            print(
                "Download count updated       {} - {} -> {}".format(file_name, previous_download_count,
                                                                    new_download_count))

    @staticmethod
    def update_theme_download_count(template: Template, theme_downloads: ThemeDownloads, current_name: str,
                                    verbose: bool) -> None:
        download_count = ThemeDownloadCount.get_theme_current_download_count(theme_downloads, current_name)
        ThemeDownloadCount.set_theme_download_count(template, current_name, download_count, verbose)

    @staticmethod
    def get_theme_downloads() -> ThemeDownloads:
        # Example content:
        # {
        #     "80s Neon": {
        #         "download": 9271,
        #         "id": "80s Neon"
        #     },
        #     "Agora": {
        #         "download": 1824,
        #         "id": "Agora"
        #     },
        return requests.get('https://releases.obsidian.md/stats/theme').json()

    @staticmethod
    def get_url_pattern_for_downloads_shield(placeholder_for_download_count: int) -> str:
        old_text = f"{DOWNLOAD_COUNT_SHIELDS_URL_PREFIX}{placeholder_for_download_count}-"
        return old_text


def get_community_themes() -> ThemeList:
    raw_data = get_json_from_github(THEMES_JSON_FILE)
    theme_list = list()
    for el in raw_data:
        theme_list.append(Theme(el))
    return theme_list
