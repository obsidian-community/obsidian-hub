# Run tests with:
#   ./run_tests.py

# -------------------------------------------------------------------------------------------------------------
# For how to use and maintain these tests, please see:
#       https://publish.obsidian.md/hub/00+-+Contribute+to+the+Obsidian+Hub/03+Contributor+Notes/03.03+Scripts+and+Automation/Testing+Python+Code+with+Approval+Tests
# -------------------------------------------------------------------------------------------------------------
import glob

import utils

from helpers_for_testing import verify_as_markdown

JINJA_TEMPLATES_DIR = "../templates"
OBSIDIAN_TEMPLATES_DIR = "../../../00 - Contribute to the Obsidian Hub/01 Templates/"


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
def test_all_template_variables_are_valid():
    error_message = check_for_invalid_spaces_in_templates()
    assert '' == error_message


def check_for_invalid_spaces_in_templates():
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


def test_author_from_jinja():
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


def test_author_from_jinja_minimal():
    template = utils.get_template_from_directory(JINJA_TEMPLATES_DIR, "author.md.jinja")
    new_content = template.render(user="test-user", author="test-user", file_path="Some%20Encoded%20Path.md")

    verify_as_markdown(new_content)


def test_author_from_templates():
    template = utils.get_template_from_directory(OBSIDIAN_TEMPLATES_DIR, 'T - Author.md')
    new_content = template.render(title="test-user")

    verify_as_markdown(new_content)
