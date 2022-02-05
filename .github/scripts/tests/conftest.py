import pytest

from approvaltests import set_default_reporter
from approvaltests.reporters import GenericDiffReporterFactory


def configure_approvaltests() -> None:
    # The supported tool names are listed in:
    #   https://github.com/approvals/ApprovalTests.Python/blob/master/approvaltests/reporters/reporters.json
    #
    # Uncomment these 3 lines to turn on a different reporter, if you don't like the default one found:
    # diff_tool_name = "AraxisMergeMac"
    # diff_tool = GenericDiffReporterFactory().get(diff_tool_name)
    # set_default_reporter(diff_tool)
    pass


# For how this works, see:
# https://github.com/approvals/ApprovalTests.Python/blob/main/docs/configuration.md#how-to-configure-a-default-reporter-for-your-system
@pytest.fixture(scope="session", autouse=True)  # type: ignore # Untyped decorator makes function "set_default_reporter_for_all_tests" untyped
def set_default_reporter_for_all_tests() -> None:
    configure_approvaltests()
