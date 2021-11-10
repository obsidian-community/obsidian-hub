# Run tests with:
#   ./run_tests.py
import os

# -----------------------------------------------------------------------------
# ABOUT THESE TESTS
#
# The tests below that use verify() and verify_all() use ApprovalTests.Python
# to write out some output (called "received") and compare it with
# previously-accepted output (called "approved").
#
# If the received differs from the approved, or if the approved does not
# exist yet, then the framework searches for a diff-tool on your machine,
# and uses it to show you the differences - with:
# - received on the left
# - approved on the right
#
# You can then either:
# 1. Fix the code, if the differences show an unwanted change
# 2. Use the diff tool to copy the changes over from received to approved,
#    if the changes are intentional.
#
# Reference material:
# 1. Clare's talks on Approval Tests:
#       - https://claremacrae.co.uk/conferences/presentations_by_topic.html#testing-legacy-c-code-with-approval-tests
#       - The start of the 2019-02-05 video is probably the best introduction.
# 2. Python ApprovalTests library:
#       - https://github.com/approvals/ApprovalTests.Python
# -----------------------------------------------------------------------------

from approvaltests import Options
from approvaltests.approvals import verify, verify_all
from approvaltests.reporters import GenericDiffReporterFactory

# TODO Figure out how to make this import work within Pycharm.
#      (It does run from ./run_tests.py)
import make_mocs


def verify_moc_for_directory_with_delimiters(directory, sub_directories, files):
    """
    Generate the MOC output for given directory and its contents, and save it disk,
    verifying that the output is unchanged since the previous approved output,
    by calling the ApprovalTests method verify()

    For more info, see https://github.com/obsidian-community/obsidian-hub/wiki/Testing-Python-Code-with-Approval-Tests

    :param directory: name of the directory, such as '../..', 'Directory 1' or 'Directory 1/Sub-directory'
    :param sub_directories: List of names of sub-directories in the given directory
    :param files: List of names of files in the given directory
    :return: None
    """
    moc_maker = make_mocs.MocMaker()
    result = moc_maker.make_moc_for_directory_with_delimiters(directory, sub_directories, files)
    verify(result, options=approval_test_options())


def approval_test_options():
    options = Options().for_file.with_extension(".md")

    # Remainder here is specific to Clare's machine
    #
    # The supported tool names are listed in:
    #   https://github.com/approvals/ApprovalTests.Python/blob/master/approvaltests/reporters/reporters.json
    #
    diff_tool_name = "AraxisMergeMac"
    diff_tool = GenericDiffReporterFactory().get(diff_tool_name)
    options = options.with_reporter(diff_tool)

    return options


def test_moc_name_for_directory():
    namer = make_mocs.MocFileNamer()

    # Test that the prefix is correctly added to a directory name:
    assert namer.moc_name_for_sub_directory('Events') == '🗂️ Events'

    # Test that the top-level directory gets a special-case name of "hub":
    assert namer.moc_name_for_sub_directory('..') == '🗂️ hub'


def test_moc_for_empty_directory():
    # This tests that a blank line is inserted between the delimiters,
    # if the directory is empty.
    verify_moc_for_directory_with_delimiters('../..', [], [])


def test_moc_for_root_directory():
    directory = '../..'
    directories = [
        # Directories that should not be included
        '.this_hidden_directory_should_not_be_included_in_file_list',

        # Check the directory names are sorted
        '02 - This directory should be listed after directory 01 ...',
        '01 - This directory should be listed before directory 02...',

        # Python virtual environment directory should also not be included
        '03 - There should not be a directory called "venv" in the output',
        'venv',
    ]
    files = [
        # Files that should not be included
        '.this_hidden_file_should_not_be_included_in_file_list',

        # Check the file names are sorted
        '01 - all files should be listed after all folders',
        '03 - This file should be listed after file 02 ...',
        '02 - This file should be listed before file 03...',
        'ZZ - This file should be listed after file YY ...',
        'YY - This file should be listed before file ZZ...',

        # Confirm whether some non .md files are included
        'svg-files-are-currently-included.svg',
        'css-files-are-currently-included.css',

        '00 - there should not be a link to a file called 🗂️ hub',
        '🗂️ hub.md',
    ]

    verify_moc_for_directory_with_delimiters(directory, directories, files)

def test_updating_existing_moc():
    input_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(input_dir, 'sample-existing-moc.md')
    with open(input_file) as input:
        initial_content = input.readlines()

    directories = [
        'dir 1',
        'Dir 2',
    ]
    files = [
        'File 1.md',
        'File 2.md',
    ]
    moc_maker = make_mocs.MocMaker()
    new_moc_content_with_delimiters = moc_maker.make_moc_for_directory_with_delimiters('test', directories, files)

    result = moc_maker.update_existing_moc(initial_content, new_moc_content_with_delimiters)
    verify(result, options=approval_test_options())
