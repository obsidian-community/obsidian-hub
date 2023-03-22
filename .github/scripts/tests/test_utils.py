import os.path

import utils
from themes import Theme


def test_get_root_of_vault() -> None:
    root = utils.get_root_of_vault()
    contributing = os.path.join(root, 'CONTRIBUTING.md')
    assert os.path.exists(contributing), contributing


def test_get_output_path() -> None:
    assert utils.get_output_path(Theme.template, 'CONTRIBUTING') == '../../02 - Community Expansions/02.05 All Community Expansions/Themes/CONTRIBUTING.md'


def test_get_output_dir() -> None:
    assert utils.get_output_dir(Theme.template) == '../../02 - Community Expansions/02.05 All Community Expansions/Themes'
