#!/usr/bin/env sh

# This script can be used to help with the addition of type hints to new code,
# if you don't want to add the type hints by hand.
#
# How to use:
# 1. Add some passing test code, so that the new code is executed
# 2. Run this script
# 3. Review the differences, and tidy up any clutter, by adding type aliases, such as:
#       FileGroups = Dict[str, List[str]]
# 4. Run check_type_hints.sh and see comments in that script about fixing errors
#
# See also: check_type_hints.sh

# Reference material:
# https://github.com/Instagram/MonkeyType
# https://instagram-engineering.com/let-your-code-type-hint-itself-introducing-open-source-monkeytype-a855c7284881

rm -f monkeytype.sqlite3

# Run scripts to generate run-time data about object types:
monkeytype run -m pytest tests/*.py
# Note: You can always temporarily add a new 'monkeytype run' line here to invoke a new script,
#       to help generate type hints for any code it executes

# Apply any discovered type hints to source files:
for module in $(monkeytype list-modules) ; do
  echo updating $module
  monkeytype apply $module
done
