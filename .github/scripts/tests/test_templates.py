# Run tests with:
#   ./run_tests.py

# -------------------------------------------------------------------------------------------------------------
# For how to use and maintain these tests, please see:
#       https://publish.obsidian.md/hub/00+-+Contribute+to+the+Obsidian+Hub/03+Contributor+Notes/03.03+Scripts+and+Automation/Testing+Python+Code+with+Approval+Tests
# -------------------------------------------------------------------------------------------------------------
import glob
from pathlib import Path

import utils

from helpers_for_testing import verify_as_markdown, get_processed_saved_sample_data_for_plugin, \
    get_processed_saved_sample_data_for_theme
from update_releases import collate_authors

JINJA_TEMPLATES_DIR = str(Path(__file__).parent.parent.absolute() / 'templates')
OBSIDIAN_TEMPLATES_DIR = str(Path(__file__).parent.parent.parent.parent / "00 - Contribute to the Obsidian Hub/01 Templates/")


# It's tempting to copy template text between the Jinja templates (JINJA_TEMPLATES_DIR)
# and the Obsidian templates (CONTRIB_TEMPLATES_DIR). This helps with keeping consistency
# between pairs of templates for the same type of content.
#
# Lots of the Jinja templates put spaces in the variables, e.g. '{{ user }}'.
# Unfortunately, Obsidian requires the spaces to be removed: '{{user}}.
#
# This means that there is a weakness in this file's use of Jinja to test the output
# of the Obsidian templates, as variables with spaces will work fine via Jijna,
# but will not work when used in Obsidian by Hub maintainers.
#
# This test therefore inspects all the Obsidian templates, and fails if
# any of them have Jinja-style variables with spaces in.
def test_all_template_variables_are_valid() -> None:
    error_message = check_for_invalid_spaces_in_templates()
    assert '' == error_message


def check_for_invalid_spaces_in_templates() -> str:
    error_message = ''
    for template_file in glob.glob(OBSIDIAN_TEMPLATES_DIR + '*.md'):
        # print(template_file)
        with open(template_file) as template_text:
            text = template_text.read()
            for problem_text in ['{{ ', ' }}']:
                if problem_text in text:
                    error_message += f'  Illegal string "{problem_text}" in "{template_file}"\n'
    if error_message != '':
        error_message = \
            'ERROR: At least one template has variables with spaces, that Obsidian will not recognise.\n' + \
            'Please remove all spaces in any special text such as "{{ title }}".\n' + \
            'The files with problems are:\n' + \
            error_message
    return error_message


def test_author_from_jinja() -> None:
    template = utils.get_template_from_directory(JINJA_TEMPLATES_DIR, "author.md.jinja")
    new_content = template.render(user="test-user", author="Test User", website="https://mysite.com",
                                  plugins=[
                                      "[[my-plugin1]]",
                                      "[[my-plugin2]]",
                                  ],
                                  themes=[
                                      "[[my-theme1]]",
                                      "[[my-theme2]]",
                                  ],
                                  file_path="Some%20Encoded%20Path.md")

    verify_as_markdown(new_content)


def test_author_from_jinja_minimal() -> None:
    template = utils.get_template_from_directory(JINJA_TEMPLATES_DIR, "author.md.jinja")
    new_content = template.render(user="test-user", author="test-user", file_path="Some%20Encoded%20Path.md")

    verify_as_markdown(new_content)


def test_author_from_templates() -> None:
    template = utils.get_template_from_directory(OBSIDIAN_TEMPLATES_DIR, 'T - Author.md')
    new_content = template.render(title="test-user")

    verify_as_markdown(new_content)


def test_real_data_in_plugin_template() -> None:
    plugin = get_processed_saved_sample_data_for_plugin("nldates-obsidian")

    template = utils.get_template_from_directory(JINJA_TEMPLATES_DIR, "plugin.md.jinja")
    new_content = template.render(**plugin.data())

    verify_as_markdown(new_content)


def test_real_data_in_theme_template() -> None:
    theme = get_processed_saved_sample_data_for_theme("Christmas")

    template = utils.get_template_from_directory(JINJA_TEMPLATES_DIR, "theme.md.jinja")
    new_content = template.render(**theme.data())

    verify_as_markdown(new_content)


def test_real_data_in_author_template() -> None:
    # A plugin and theme written by the same author, deathau
    plugin = get_processed_saved_sample_data_for_plugin("cooklang-obsidian")
    theme = get_processed_saved_sample_data_for_theme("Christmas")

    all_authors = collate_authors([theme], [plugin])
    assert len(all_authors) == 1
    author = all_authors['deathau']

    template = utils.get_template_from_directory(JINJA_TEMPLATES_DIR, "author.md.jinja")
    new_content = template.render(**author)

    verify_as_markdown(new_content)
