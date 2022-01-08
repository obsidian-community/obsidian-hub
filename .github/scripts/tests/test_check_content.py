import os.path

import check_content


def test_get_root_of_vault() -> None:
    root = check_content.get_root_of_vault()
    contributing = os.path.join(root, 'CONTRIBUTING.md')
    assert os.path.exists(contributing), contributing
