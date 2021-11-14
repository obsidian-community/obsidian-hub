# Run tests with:
#   ./run_tests.py

# -------------------------------------------------------------------------------------------------------------
# For how to use and maintain these tests, please see:
#       https://github.com/obsidian-community/obsidian-hub/wiki/Testing-Python-Code-with-Approval-Tests
# -------------------------------------------------------------------------------------------------------------
import os

import utils

from approvaltests.approvals import verify, verify_all

from test_make_mocs import approval_test_options

JINJA_TEMPLATES_DIR = "../templates"
CONTRIB_TEMPLATES_DIR = "../../../00 - Contribute to the Obsidian Hub/01 Templates/"


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
                                  ], )

    verify(new_content, options=approval_test_options())


def test_author_from_jinja_minimal():
    template = utils.get_template_from_directory(JINJA_TEMPLATES_DIR, "author.md.jinja")
    new_content = template.render(user="test-user", author="Test User")

    verify(new_content, options=approval_test_options())


def test_author_from_templater():
    template = utils.get_template_from_directory(CONTRIB_TEMPLATES_DIR, 'T - Author.md')
    new_content = template.render(title="test-user")

    verify(new_content, options=approval_test_options())
