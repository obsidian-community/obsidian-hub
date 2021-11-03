# Run tests with:
#   ./run_tests.py

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
        lambda x: "{0} => {1}".format(x, make_mocs.moc_name_for_directory(x)), options=make_default_reporter())


def test_output_for_files():
    directory = '01 - Topic 1/01.02 Subtopic'
    files = ['README.md', 'publish.css', 'logo.svg', 'File 1.md', 'File 2.md']
    result = make_mocs.make_moc_for_directory(directory, files)
    verify(result)


def test_output_for_sub_directories():
    directory = '01 - Community'
    sub_directories = ['Authors - Persons', 'Events', 'Obsidian Roundup', 'Video Channels']
    result = make_mocs.make_moc_for_sub_directories(directory, sub_directories)
    verify(result, options=make_default_reporter())
