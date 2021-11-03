# TODO Figure out how to move this to a tests directory, abd still import make_moc

from approvaltests.approvals import verify

from make_mocs import make_moc_for_directory


def test_output_for_files():
    directory = '01 - Topic 1/01.02 Subtopic'
    files = ['README.md', 'publish.css', 'logo.svg', 'File 1.md', 'File 2.md']
    result = make_moc_for_directory(directory, files)
    verify(result)
