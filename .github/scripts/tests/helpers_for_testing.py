from pathlib import Path
from typing import Any, Tuple

from approvaltests import verify, verify_as_json, Options

import utils
from themes import Theme, ThemeDownloads, ThemeList


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


def get_saved_sample_data_for_theme(theme_name: str) -> Tuple[Theme, str, ThemeDownloads]:
    sample_data_for_theme = Path(__file__).parent.absolute() / 'sample_data/themes' / theme_name
    assert sample_data_for_theme.exists()

    theme_downloads = utils.get_json_from_file(str(sample_data_for_theme / 'stats-theme.json'))
    theme_list: ThemeList = utils.get_json_from_file(str(sample_data_for_theme / 'community-css-themes.json'))
    theme = theme_list[0]

    with open(sample_data_for_theme / 'obsidian.css') as f:
        css_file = f.read()

    return theme, css_file, theme_downloads
