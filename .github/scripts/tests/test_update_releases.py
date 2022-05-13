from approvaltests import verify_as_json

from update_releases import collate_authors
from tests.helpers_for_testing import get_saved_sample_data_for_theme, \
    get_processed_saved_sample_data_for_plugin
from utils import FileGroups


def test_process_authors() -> None:
    theme, css_file, theme_downloads = get_saved_sample_data_for_theme("Christmas")
    theme_file_groups: FileGroups = dict()
    theme.collect_data_for_theme_and_css(css_file, theme_downloads, theme_file_groups)
    themes = [theme]

    plugin = get_processed_saved_sample_data_for_plugin("nldates-obsidian")
    plugins = [plugin]

    all_authors = collate_authors(themes, plugins)
    verify_as_json(all_authors)
