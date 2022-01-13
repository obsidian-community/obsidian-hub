import os.path

import utils


def test_get_root_of_vault() -> None:
    root = utils.get_root_of_vault()
    contributing = os.path.join(root, 'CONTRIBUTING.md')
    assert os.path.exists(contributing), contributing
