from typing import Any

from approvaltests import verify, verify_as_json, Options


def verify_as_markdown(data: Any, options: Options = Options()) -> None:
    """
    A convenience wrapper around approvaltests.verify(), that saves the outputs with .md file extension
    """
    verify(data, options=options.for_file.with_extension(".md"))


def verify_in_json_format_to_markdown(data: Any, options: Options = Options()) -> None:
    """
    A convenience wrapper around approvaltests.verify_as_json(), that saves the outputs with .md file extension
    """
    verify_as_json(data, options=options.for_file.with_extension(".md"))
