#!/usr/bin/env sh

# Make an edit to doc/Features.md, to cover more code...

# https://instagram-engineering.com/let-your-code-type-hint-itself-introducing-open-source-monkeytype-a855c7284881
rm -f monkeytype.sqlite3
monkeytype run -m pytest tests/*.py
monkeytype run ./add_footer.py > /dev/null
#monkeytype run ./check_contents.py
#monkeytype run ./update_mocs.py
#monkeytype run ./update_releases.py
#monkeytype run ./update_releases.py --all
#monkeytype run ./update_releases.py --update-download-counts

for module in $(monkeytype list-modules) ; do
  echo updating $module
  monkeytype apply $module
done
