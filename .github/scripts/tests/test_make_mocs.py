# Run tests with:
#   ./run_tests.py
import os

from approvaltests import Options
from approvaltests.approvals import verify, verify_all
from approvaltests.reporters import GenericDiffReporterFactory

# TODO Figure out how to make this import work within Pycharm.
#      (It does run from ./run_tests.py)
import make_mocs


def make_default_reporter():
    return Options().with_reporter(GenericDiffReporterFactory().get("AraxisMergeMac"))


def test_moc_name_for_directory():
    alist = ['..', 'Events']
    verify_all(
        "moc_name_for_directory", alist,
        lambda x: "{0} => {1}".format(x, make_mocs.moc_name_for_sub_directory(x)), options=make_default_reporter())


def test_output_for_files():
    directory = '01 - Topic 1/01.02 Subtopic'
    files = ['README.md', 'publish.css', 'logo.svg', 'File 1.md', 'File 2.md']
    result = make_mocs.make_moc_for_files(directory, files)
    verify(result)


def test_output_for_sub_directories():
    directory = '01 - Community'
    sub_directories = ['Authors - Persons', 'Events', 'Obsidian Roundup', 'Video Channels']
    result = make_mocs.make_moc_for_sub_directories(directory, sub_directories)
    verify(result, options=make_default_reporter())


def test_moc_for_empty_directory():
    result = make_mocs.moc_content_for_directory('../..', [], [])
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
    result = make_mocs.moc_content_for_directory('../..', directories, files)
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
    new_index_with_delimiters = make_mocs.moc_content_for_directory('test', directories, files)

    result = make_mocs.update_existing_moc(initial_content, new_index_with_delimiters)
    verify(result, options=make_default_reporter())