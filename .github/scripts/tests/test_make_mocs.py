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


def make_default_reporter():
    # Don't customise the diff-tool
    return Options()

    # Remainder here is specific to Clare's machine
    #
    # The supported tool names are listed in:
    #   https://github.com/approvals/ApprovalTests.Python/blob/master/approvaltests/reporters/reporters.json
    #
    # diff_tool = "AraxisMergeMac"
    # return Options().with_reporter(GenericDiffReporterFactory().get(diff_tool))


def test_moc_name_for_directory():
    alist = ['..', 'Events']
    namer = make_mocs.MocFileNamer()
    verify_all(
        "base-name of moc in directory", alist,
        lambda x: "{0} => {1}".format(x, namer.moc_name_for_sub_directory(x)), options=make_default_reporter())


def test_output_for_files():
    directory = '01 - Topic 1/01.02 Subtopic'
    files = ['README.md', 'publish.css', 'logo.svg', 'File 1.md', 'File 2.md']
    moc_maker = make_mocs.MocMaker()
    result = moc_maker.make_moc_for_files(directory, files)
    verify(result)


def test_output_for_sub_directories():
    directory = '01 - Community'
    sub_directories = ['Authors - Persons', 'Events', 'Obsidian Roundup', 'Video Channels']
    moc_maker = make_mocs.MocMaker()
    result = moc_maker.make_moc_for_sub_directories(directory, sub_directories)
    verify(result, options=make_default_reporter())


def test_moc_for_empty_directory():
    moc_maker = make_mocs.MocMaker()
    result = moc_maker.make_moc_for_directory_with_delimiters('../..', [], [])
    verify(result, options=make_default_reporter())


def test_moc_for_root_directory():
    directories = [
        '.git',
        '.github',
        '.idea',
        '.obsidian',
        '00 - Contribute to the Obsidian Hub',
        '01 - Community',
        '02 - Community Expansions',
        '03 - Showcases & Templates',
        '04 - Guides, Workflows, & Courses',
        '05 - Concepts',
        '06 - Inbox',
        'venv',
    ]
    files = [
        '.DS_Store',
        '.gitignore',
        '00 - Start here.md',
        'CONTRIBUTING.md',
        'README.md',
        'logo.svg',
        'publish.css',
        '🗂️ hub.md',
    ]
    moc_maker = make_mocs.MocMaker()
    result = moc_maker.make_moc_for_directory_with_delimiters('../..', directories, files)
    verify(result, options=make_default_reporter())


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
    verify(result, options=make_default_reporter())
