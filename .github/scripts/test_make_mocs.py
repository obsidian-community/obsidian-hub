# TODO Figure out how to move this to a tests directory, abd still import make_moc

from approvaltests.approvals import verify

from make_mocs import make_moc_for_directory, make_moc_for_sub_directories


def test_output_for_files():
    directory = '01 - Topic 1/01.02 Subtopic'
    files = ['README.md', 'publish.css', 'logo.svg', 'File 1.md', 'File 2.md']
    result = make_moc_for_directory(directory, files)
    verify(result)


def test_output_for_sub_directories():
    directory = '01 - Community'
    sub_directories = ['Authors - Persons', 'Events', 'Obsidian Roundup', 'Video Channels']
    result = make_moc_for_sub_directories(directory, sub_directories)
    verify(result)
