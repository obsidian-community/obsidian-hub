from pathlib import Path
from typing import Any, Tuple, List

from approvaltests import verify, verify_as_json, Options

import utils
from plugins import Plugin
from themes import Theme, ThemeList
from hub_types import ThemeDownloads, ThemeStorage, PluginStorage, PluginManifest


def verify_as_markdown(data: Any, options: Options = Options()) -> None:
    """
    A convenience wrapper around approvaltests.verify(), that saves the outputs with .md file extension
    """
    verify(data, options=options.for_file.with_extension(".md"))


def verify_in_json_format_to_markdown(data: Any, options: Options = Options()) -> None:
    """
    A convenience wrapper around approvaltests.verify_as_json(), that saves the outputs with .md file extension
    """
    verify_as_json(data, options=options.for_file.with_extension(".md"))


def get_raw_saved_sample_data_for_theme(theme_name: str) -> Tuple[Theme, str, ThemeDownloads]:
    """
    A convenience function to load raw data for a theme that has previous been saved
    to .github/scripts/tests/sample_data/themes

    This allows for tests to be written using data stored in this repo, instead of
    having to download real themes and community release information, whose contents will
    change over time, likely causing random test failures and maintenance pain in the future.

    This returns the data from raw the community themes file, the CSS and the download count.

    See also get_processed_saved_sample_data_for_theme() which collates data from those
    two files together.
    """
    sample_data_for_theme = Path(__file__).parent.absolute() / 'sample_data/themes' / theme_name
    assert sample_data_for_theme.exists()

    theme_downloads = utils.get_json_from_file(str(sample_data_for_theme / 'stats-theme.json'))
    theme_list: List[ThemeStorage] = utils.get_json_from_file(str(sample_data_for_theme / 'community-css-themes.json'))
    theme = Theme(theme_list[0])

    with open(sample_data_for_theme / 'obsidian.css') as f:
        css_file = f.read()

    return theme, css_file, theme_downloads


def get_processed_saved_sample_data_for_theme(theme_name: str) -> Theme:
    """
    A convenience function to load processed/collated data for a theme that has previous been saved
    to .github/scripts/tests/sample_data/themes
    """

    theme, css_file, theme_downloads = get_raw_saved_sample_data_for_theme(theme_name)
    theme_file_groups: utils.FileGroups = dict()
    theme.collect_data_for_theme_and_css(css_file, theme_downloads, theme_file_groups)
    return theme


def get_raw_saved_sample_data_for_plugin(plugin_id: str) -> Tuple[Plugin, PluginManifest]:
    """
    A convenience function to load raw data for a plugin that has previous been saved
    to .github/scripts/tests/sample_data/plugins

    This allows for tests to be written using data stored in this repo, instead of
    having to download real plugins and community release information, whose contents will
    change over time, likely causing random test failures and maintenance pain in the future.

    This returns the data from raw Plugin and Manifest json files.

    See also get_processed_saved_sample_data_for_plugin() which collates data from those
    two files together.
    """
    sample_data_for_plugin = Path(__file__).parent.absolute() / 'sample_data/plugins' / plugin_id
    assert sample_data_for_plugin.exists()

    plugin_list: List[PluginStorage] = utils.get_json_from_file(str(sample_data_for_plugin / 'community-plugins.json'))
    plugin = Plugin(plugin_list[0])

    manifest = utils.get_json_from_file(str(sample_data_for_plugin / 'manifest.json'))

    return plugin, manifest


def get_processed_saved_sample_data_for_plugin(plugin_id: str) -> Plugin:
    """
    A convenience function to load processed/collated data for a plugin that has previous been saved
    to .github/scripts/tests/sample_data/plugins
    """
    plugin, manifest = get_raw_saved_sample_data_for_plugin(plugin_id)
    plugin_file_groups: utils.FileGroups = dict()
    plugin.collect_data_for_plugin_and_manifest(manifest, plugin_file_groups)
    return plugin
