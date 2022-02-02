from typing import Any

from approvaltests import verify, verify_as_json, Options


def verify_as_markdown(data: Any):
    """
    A convenience wrapper around approvaltests.verify(), that saves the outputs with .md file extension
    """
    options = Options().for_file.with_extension(".md")
    verify(data, options=options)


def verify_in_json_format_to_markdown(data: Any):
    """
    A convenience wrapper around approvaltests.verify_as_json(), that saves the outputs with .md file extension
    """
    options = Options().for_file.with_extension(".md")
    verify_as_json(data, options=options)
