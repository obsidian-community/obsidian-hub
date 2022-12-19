import re
from os.path import basename, dirname
from tempfile import TemporaryFile, TemporaryDirectory
from pathlib import Path

import add_footer
import utils

from helpers_for_testing import verify_as_markdown
from test_templates import JINJA_TEMPLATES_DIR


# Test that the footer finds the template
def test_consistency_that_search_expression_matches_template() -> None:
    relative_path = 'Any old file.md'
    empty_input = ''
    output = add_footer_to_markdown_test(empty_input, relative_path)

    explanation = """

ERROR.
If this test fails, the search expression in add_footer.py does not find the footer template.
They need to be consistent, to prevent multiple footer accumulating.
"""
    comment = add_footer.get_footer_comment_regex()
    # Make sure that the regex comment finds the text added from the footer template
    assert re.search(comment, output), explanation


# Simple test, that footer is added if not present.
def test_footer_added_if_missing() -> None:
    relative_path = '04 - Guides, Workflows, & Courses/for Plugin Developers.md'
    input = \
        f"""# Sample note content.
Path used for this test: `{relative_path}`
If the above file still exists in the vault, then the generated links
should still work.
CHECK that path in URLs has been encoded.
"""
    output = add_footer_to_markdown_test(input, relative_path)
    verify_footer_addition(input, output)

# Ensure eol is added before footer, if missing from input file
def test_end_of_line_added_if_missing() -> None:
    relative_path = '04 - Guides, Workflows, & Courses/for Plugin Developers.md'
    input = \
        f"""# Sample note content.
Path used for this test: `{relative_path}`
I do not have a line-ending at end of file. A blank line should be added."""
    output = add_footer_to_markdown_test(input, relative_path)
    verify_footer_addition(input, output)


# Test that footer is not added twice
# Test that footer is updated if content differs
def test_footer_updated_if_present() -> None:
    relative_path = '04 - Guides, Workflows, & Courses/for Plugin Developers.md'
    text_to_be_overwritten = 'CHECK THAT I AM NOT PRESENT IN FINAL OUTPUT'
    raw_content = \
        f"""# Sample note content.
Path used for this test: `{relative_path}`
CHECK that the footer is only present once in the output.
CHECK that UPPER-CASE of this text is not present: '{text_to_be_overwritten.lower()}'
"""
    content_with_footer_added = add_footer_to_markdown_test(raw_content, relative_path)
    input = content_with_footer_added + '\n' + text_to_be_overwritten
    assert text_to_be_overwritten in input

    output = add_footer_to_markdown_test(input, relative_path)
    assert not text_to_be_overwritten in output

    verify_footer_addition(input, output)


def add_footer_to_markdown_test(input: str, relative_path:str) -> str:
    """
    Convenience wrapper for calling add_footer.add_footer_to_markdown()

    :param input: Simulated content of a markdown note
    :param relative_path: The path to use, to represent the location of input
    :return: The result of adding or updating the footer in input
    """
    comment = add_footer.get_footer_comment_regex()

    with TemporaryDirectory() as tmproot:
        absolute_path = f"{tmproot}/{relative_path}"
        Path(dirname(absolute_path)).mkdir(parents=True, exist_ok=True)
        utils.write_file(absolute_path, input)

        add_footer.ensure_footer_in_file(absolute_path, relative_path)

        return str(utils.read_file(absolute_path))

def verify_footer_addition(input: str, output: str) -> None:

    check_output_has_eol_on_last_line(output)

    text_to_verify = f"""
INPUT:

---
{input}
---

OUTPUT:

---
{output}
"""
    verify_as_markdown(text_to_verify)


def check_output_has_eol_on_last_line(output: str) -> None:
    # First make sure that the output has a finely end-of-line character.
    explanation = """
    ERROR.
    The generated footer does not have an end-of-line character on the last line.
    """
    assert output[-1] == '\n', explanation
