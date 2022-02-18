import os

import approvaltests
from approvaltests import verify
from approvaltests.storyboard import StoryBoard
from jinja2 import Template

import utils
from tests.helpers_for_testing import verify_as_markdown, get_saved_sample_data_for_theme
from tests.test_templates import JINJA_TEMPLATES_DIR
from themes import collect_data_for_theme_and_css


def test_collect_data_for_theme_with_settings() -> None:
    theme_name = "Minimal"
    verify_theme_data(theme_name)


def test_collect_data_for_theme_without_settings() -> None:
    theme_name = "Christmas"
    verify_theme_data(theme_name)


def test_reading_theme__with_error_logs_error() -> None:
    theme_name = "InvalidSettingsData"
    template = get_template_for_theme()
    theme, css_file, theme_downloads = get_saved_sample_data_for_theme(theme_name)

    file_groups: utils.FileGroups = dict()
    name, valid = collect_data_for_theme_and_css(theme, css_file, theme_downloads, template, file_groups)

    assert name == theme_name
    assert valid == False
    # Check that an error has been logged for this theme
    assert 'error' in file_groups
    assert file_groups['error'][0] == name


def test_rendering_of_theme() -> None:
    theme_name = "Minimal"

    template = get_template_for_theme()

    theme, css_file, theme_downloads = get_saved_sample_data_for_theme(theme_name)

    file_groups: utils.FileGroups = dict()
    name, valid = collect_data_for_theme_and_css(theme, css_file, theme_downloads, template, file_groups)
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

    file_groups: utils.FileGroups = dict()
    name, valid = collect_data_for_theme_and_css(theme, css_file, theme_downloads, template, file_groups)
    assert name == theme_name
    assert theme["user"] != ""
    s.add_frame(approvaltests.utils.to_json(theme))

    verify(s)
