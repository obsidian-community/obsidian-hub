import os

import approvaltests
from approvaltests import verify_as_json, verify, Options
from approvaltests.scrubbers import create_regex_scrubber, Scrubber
from approvaltests.storyboard import StoryBoard
from jinja2 import Template

import utils
from tests.helpers_for_testing import verify_as_markdown, get_saved_sample_data_for_theme
from tests.test_templates import JINJA_TEMPLATES_DIR
from themes import get_theme_downloads, ThemeList, collect_data_for_theme_and_css
from utils import THEMES_JSON_FILE, get_json_from_github


# TODO  Several of these tests download data from GitHub.
#       This makes the tests slow and prone to failure when data changes.
#       Change them to read test data files from the repo.


def test_get_community_themes() -> None:
    theme_list: ThemeList = get_json_from_github(THEMES_JSON_FILE)
    assert len(theme_list) >= 115, len(theme_list)

    first_theme = theme_list[0]
    assert len(first_theme["modes"]) > 0
    assert first_theme["author"] != ""
    assert first_theme["name"] != ""
    assert first_theme["screenshot"] != ""

    # TODO Don't add new themes - maybe get a fixed revision
    verify_as_json(theme_list)


def test_collect_data_for_theme_with_settings() -> None:
    theme_name = "Minimal"
    verify_theme_data(theme_name)


def test_collect_data_for_theme_without_settings() -> None:
    theme_name = "Christmas"
    verify_theme_data(theme_name)


def test_rendering_of_theme() -> None:
    theme_name = "Minimal"

    template = get_template_for_theme()

    theme, css_file, theme_downloads = get_saved_sample_data_for_theme(theme_name)

    name = collect_data_for_theme_and_css(theme, css_file, theme_downloads, template)
    assert name == theme_name

    file_path = "delete_me.md"
    absolute_file_path = os.path.abspath(file_path)
    file_content = utils.render_template_for_file(template, absolute_file_path, **theme)

    assert len(file_content) > 0

    verify_as_markdown(file_content)


def get_template_for_theme() -> Template:
    template = utils.get_template_from_directory(JINJA_TEMPLATES_DIR, "theme.md.jinja")
    return template


def verify_theme_data(theme_name: str) -> None:
    s = StoryBoard()

    template = get_template_for_theme()

    theme, css_file, theme_downloads = get_saved_sample_data_for_theme(theme_name)

    assert theme
    assert theme["name"] == theme_name
    assert len(theme["modes"]) > 0
    assert theme["author"] != ""

    s.add_frame(approvaltests.utils.to_json(theme))

    name = collect_data_for_theme_and_css(theme, css_file, theme_downloads, template)
    assert name == theme_name
    assert theme["user"] != ""
    s.add_frame(approvaltests.utils.to_json(theme))

    verify(s)
