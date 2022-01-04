#!/usr/bin/env python3

# This script runs all the tests.
# And it can be run from inside PyCharm or other IDEs, allowing debugging

# TODO Figure out how to add -s argument, meaning "show console output if test fails"
# TODO Then update run_tests.sh to invoke this script

import os, pathlib
import pytest

# from https://stackoverflow.com/a/51334378/104370
os.chdir(pathlib.Path.cwd() / 'tests')

result = pytest.main()
print(f'return code = {result}')
