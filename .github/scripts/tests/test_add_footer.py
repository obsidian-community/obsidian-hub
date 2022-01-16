from approvaltests.approvals import verify

import add_footer
import utils

from test_templates import JINJA_TEMPLATES_DIR, approval_test_options


# TODO
# Test rewriting
# Test that file is not changed if it already has the header
# Test that the footer finds the template
# Test behaviour if no EOL at end of content

# Simple test, that footer is added if not present.
def test_footer_added_if_missing():
    relative_path = '04 - Guides, Workflows, & Courses/for Plugin Developers.md'
    input = \
        f"""Sample note content.
Path used for this test: `{relative_path}`
If the above file still exists in the vault, then the generated links
should still work.
CHECK that path in URLs has been encoded.
"""
    output = add_footer_to_markdown_test(input, relative_path)
    verify_footer_addition(input, output)


# Test that footer is not added twice
# Test that footer is updated if content differs
def test_footer_updated_if_present():
    relative_path = '04 - Guides, Workflows, & Courses/for Plugin Developers.md'
    text_to_be_overwritten = 'CHECK THAT I AM NOT PRESENT IN FINAL OUTPUT'
    raw_content = \
        f"""Sample note content.
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
    template = utils.get_template_from_directory(JINJA_TEMPLATES_DIR, "footer.md.jinja")
    debug = False
    output = add_footer.add_footer_to_markdown(relative_path, input, comment, template, debug)
    return output


def verify_footer_addition(input, output):
    text_to_verify = f"""
INPUT:

---
{input}
---

OUTPUT:

---
{output}
---
"""
    verify(text_to_verify, options=approval_test_options())
