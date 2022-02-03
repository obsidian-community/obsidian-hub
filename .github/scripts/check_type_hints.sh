#!/usr/bin/env sh

#  --disallow-untyped-calls  Disallow calling functions without type
#                            annotations from functions with type annotations
#                            (inverse: --allow-untyped-calls)
#  --disallow-untyped-defs   Disallow defining functions without type
#                            annotations or with incomplete type annotations
#                            (inverse: --allow-untyped-defs)
#  --disallow-incomplete-defs
#                            Disallow defining functions with incomplete type
#                            annotations (inverse: --allow-incomplete-defs)

# TODO Add missing type hints then enable all the options above
python3 -m mypy \
  --follow-imports=skip \
  --ignore-missing-imports \
  *.py
#  tests/*.py
