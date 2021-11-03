# TODO Figure out how to move this to a tests directory, abd still import make_moc

from approvaltests.approvals import verify

from make_mocs import make_moc


def test_simple_output():
    directory = '01 - Topic 1/01.02 Subtopic'
    files = ['File 1.md', 'File 2.md']
    result = make_moc(directory, files)
    verify(result)
