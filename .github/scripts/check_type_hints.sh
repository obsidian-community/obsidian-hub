#!/usr/bin/env sh

# This script is used to check the completeness and correctness
# of type hints in all the Python code in the Hub repo.
#
# How to use:
# 1. Run this script
# 2. Review and fix each of the errors.
# 3. For tips in fixing errors, see comments in https://github.com/obsidian-community/obsidian-hub/issues/284
#
# See also: add_type_hints.sh
#
# Reference material:
# https://mypy.readthedocs.io/en/stable/
#
#  --disallow-untyped-calls  Disallow calling functions without type
#                            annotations from functions with type annotations
#                            (inverse: --allow-untyped-calls)
#  --disallow-untyped-defs   Disallow defining functions without type
#                            annotations or with incomplete type annotations
#                            (inverse: --allow-untyped-defs)
#  --disallow-incomplete-defs
#                            Disallow defining functions with incomplete type
#                            annotations (inverse: --allow-incomplete-defs)

python3 -m mypy \
  --strict \
  --follow-imports=skip \
  --ignore-missing-imports \
  --disallow-untyped-calls \
  --disallow-untyped-defs \
  --disallow-incomplete-defs \
  --allow-incomplete-defs \
  *.py \
  tests/*.py
