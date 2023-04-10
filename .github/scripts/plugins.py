#!/usr/bin/env python3

from typing import List

from authors import update_author_name_for_manual_exceptions
from hub_types import PluginStorage, PluginManifest
from utils import get_plugin_manifest, FileGroups, add_file_group

# Type aliases:
PluginList = List["Plugin"]

MOBILE_COMPATIBLE = "[[Mobile-compatible plugins|Yes]]"
DESKTOP_ONLY = "[[Desktop-only plugins|No]]"


class Plugin:

    def __init__(self, data: PluginStorage):
        self.__data = data

    def repo(self) -> str:
        return str(self.__data.get("repo"))

    def branch(self) -> str:
        return str(self.__data.get("branch", "HEAD"))

    def name(self) -> str:
        return str(self.__data.get("name"))

    def id(self) -> str:
        return str(self.__data.get("id"))

    def author(self) -> str:
        return str(self.__data.get("author"))

    def user(self) -> str:
        return str(self.__data.get("user"))

    def authorUrl(self) -> str:
        return str(self.__data.get("authorUrl", ""))

    def data(self) -> PluginStorage:
        return self.__data

    def collect_data_for_plugin(self, file_groups: FileGroups) -> bool:
        """
        Take raw plugin data from a community plugin, and add information to it,
        typically from its manifest file.

        :param file_groups: Place to store error message if the plugin is invalid
        :return: Whether the plugin is valid, and is OK to be added to the Hub
        """
        repo = self.repo()
        branch = self.branch()
        current_name = self.name()

        try:
            manifest = get_plugin_manifest(repo, branch)
            return self.collect_data_for_plugin_and_manifest(manifest, file_groups)

        except Exception as err:
            print(f'ERROR processing plugin {current_name}. Error message: {err}')
            plugin_is_valid = False
            add_file_group(file_groups, "error", f"{current_name}")
            return plugin_is_valid

    def collect_data_for_plugin_and_manifest(self, manifest: PluginManifest, file_groups: FileGroups) -> bool:
        # the cast to str is to silence: error: Item "None" of "Optional[Any]" has no attribute "split"
        repo = self.repo()
        plugin_is_valid = self.validate_plugin(manifest, repo, file_groups)

        user = repo.split("/")[0]
        if manifest.get("isDesktopOnly"):
            mobile = DESKTOP_ONLY
        else:
            mobile = MOBILE_COMPATIBLE

        self.__data.update(mobile=mobile, user=user, **manifest)
        update_author_name_for_manual_exceptions(self.__data)

        return plugin_is_valid

    def validate_plugin(self, manifest: PluginManifest, repo: str, file_groups: FileGroups) -> bool:
        return self.validate_plugin_ids(manifest, repo, file_groups)

    def validate_plugin_ids(self, manifest: PluginManifest, repo: str, file_groups: FileGroups) -> bool:
        ids_match = True
        releases_id = self.id()
        manifest_id = manifest.get('id')
        if releases_id != manifest_id:
            print(
                f"ERROR repo:{repo} ID {releases_id} does not match ID in manifest: {manifest_id}")
            add_file_group(file_groups, "error", f"{releases_id}/{manifest_id}")
            ids_match = False
        return ids_match
