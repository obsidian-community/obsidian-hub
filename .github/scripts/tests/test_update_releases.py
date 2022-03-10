from update_releases import process_authors
from tests.helpers_for_testing import verify_as_markdown, get_saved_sample_data_for_theme, \
    get_saved_sample_data_for_plugin


def test_process_authors() -> None:
    theme, css_file, theme_downloads = get_saved_sample_data_for_theme("Christmas")
    themes = [theme]
    plugin = get_saved_sample_data_for_plugin("nldates-obsidian")
    plugins = [plugin]
    process_authors(themes, plugins, overwrite=True, verbose=False)
