from approvaltests import verify_as_json

from update_releases import collate_authors
from tests.helpers_for_testing import \
    get_processed_saved_sample_data_for_plugin, get_processed_saved_sample_data_for_theme


def test_process_authors() -> None:
    theme = get_processed_saved_sample_data_for_theme("Christmas")
    themes = [theme]

    plugin = get_processed_saved_sample_data_for_plugin("nldates-obsidian")
    plugins = [plugin]

    all_authors = collate_authors(themes, plugins)
    verify_as_json(all_authors)
