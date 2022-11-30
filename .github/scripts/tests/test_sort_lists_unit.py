import sort_lists

def test_extract_list() -> None:
    markdown_text = """
# Heading 1

## Heading 2

- [[item1|alias1]]
- [[item2|alias2]]: desc
- [[item3|alias3]] - OTHER ALT
- [[item4|alias4]] 

## Heading 3
"""
    expected_list_text = """- [[item1|alias1]]
- [[item2|alias2]]: desc
- [[item3|alias3]] - OTHER ALT
- [[item4|alias4]] 
"""

    [start_pos, end_pos] = sort_lists.extract_list_pos(markdown_text, "## Heading 2")
    assert start_pos == 28
    assert end_pos == 123
    assert markdown_text[start_pos:end_pos] == expected_list_text[:]

def test_extract_alias() -> None:
    link = "- [[item1|alias1]]: desc"
    alias = sort_lists.extract_alias(link)
    assert alias == "alias1"

def test_extract_alias_no_alias() -> None:
    link = "- [[item1]]: desc"
    alias = sort_lists.extract_alias(link)
    assert alias == "item1"

def test_sort_list() -> None:
    unsorted_md = """- [[item1|alias4]]
- [[item2|alias2]]: desc
- [[item3|alias3]] - OTHER ALT
- [[item4|alias1]] """

    expected_md = """- [[item4|alias1]] 
- [[item2|alias2]]: desc
- [[item3|alias3]] - OTHER ALT
- [[item1|alias4]]
"""

    sorted_md = sort_lists.sort_list(unsorted_md)
    assert sorted_md == expected_md
