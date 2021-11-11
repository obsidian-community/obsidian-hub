#!/usr/bin/env python3

# This script runs all the tests.
# And it can be run from inside PyCharm or other IDEs, allowing debugging

import os, pathlib
import pytest

# from https://stackoverflow.com/a/51334378/104370
os.chdir(pathlib.Path.cwd() / 'tests')

pytest.main()
