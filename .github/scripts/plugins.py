#!/usr/bin/env python3

from typing import Union, Any, Dict, List

from authors import update_author_name_for_manual_exceptions
from utils import get_plugin_manifest, FileGroups, add_file_group

# Type aliases:
PluginStorage = Dict[str, Any]
PluginList = List["Plugin"]
PluginManifest = Dict[str, Union[str, bool]]

MOBILE_COMPATIBLE = "[[Mobile-compatible plugins|Yes]]"
DESKTOP_ONLY = "[[Desktop-only plugins|No]]"


class Plugin(PluginStorage):

    def collect_data_for_plugin(self, file_groups: FileGroups) -> bool:
        """
        Take raw plugin data from a community plugin, and add information to it,
        typically from its manifest file.

        :param plugin: A dict with data about the plugin, to be updated by this function
        :param file_groups: Place to store error message if the plugin is invalid
        :return: Whether the plugin is valid, and is OK to be added to the Hub
        """
        repo = self.get("repo")
        branch = self.get("branch", "master")
        current_name = str(self.get("name"))

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
        repo = str(self.get("repo"))
        plugin_is_valid = Plugin.validate_plugin(self, manifest, repo, file_groups)

        user = repo.split("/")[0]
        if manifest.get("isDesktopOnly"):
            mobile = DESKTOP_ONLY
        else:
            mobile = MOBILE_COMPATIBLE

        self.update(mobile=mobile, user=user, **manifest)
        update_author_name_for_manual_exceptions(self)

        return plugin_is_valid

    @staticmethod
    def validate_plugin(plugin: "Plugin", manifest: PluginManifest, repo: str, file_groups: FileGroups) -> bool:
        return Plugin.validate_plugin_ids(plugin, manifest, repo, file_groups)

    @staticmethod
    def validate_plugin_ids(plugin: "Plugin", manifest: PluginManifest, repo: str, file_groups: FileGroups) -> bool:
        ids_match = True
        releases_id = plugin.get('id')
        manifest_id = manifest.get('id')
        if releases_id != manifest_id:
            print(
                f"ERROR repo:{repo} ID {releases_id} does not match ID in manifest: {manifest_id}")
            add_file_group(file_groups, "error", f"{releases_id}/{manifest_id}")
            ids_match = False
        return ids_match
