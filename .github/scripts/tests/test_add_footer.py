from approvaltests.approvals import verify

import add_footer
import utils

from test_templates import JINJA_TEMPLATES_DIR, approval_test_options


# TODO
# Test rewriting
# Test that file is not changed if it already has the header
# Test that the footer finds the template
# Test that footer is not added twice
# Test that footer is updated if content differs
# Test behaviour if no EOL at end of content

def test_footer_added_if_missing():
    relative_path = '04 - Guides, Workflows, & Courses/for Plugin Developers.md'
    contents = \
        f"""Sample note content.
Path used for this test: `{relative_path}`
If the above file still exists in the vault, then the generated links
should still work.
CHECK that path in URLs has been encoded.
"""
    comment = add_footer.get_footer_comment_regex()
    template = utils.get_template_from_directory(JINJA_TEMPLATES_DIR, "footer.md.jinja")
    debug = False
    result = add_footer.add_footer_to_markdown(relative_path, contents, comment, template, debug)
    text_to_verify = f"""
INPUT:

---
{contents}
---

OUTPUT:

---
{result}
---
"""
    verify(text_to_verify, options=approval_test_options())
