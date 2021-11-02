#!/usr/bin/env bash

cd ../..

# Delete cases where there is also a '# MOC'
find . -type f -name '*.md' \
  -exec grep -l --null '%% Zoottelkeeper: Beginning' {} \; |
  xargs -0 sed -i '' '/## MOC/,/%% Zoottelkeeper: End/d'

# Delete cases without a '# MOC'
find . -type f -name '*.md' \
  -exec grep -l --null '%% Zoottelkeeper: Beginning' {} \; |
  xargs -0 sed -i '' '/%% Zoottelkeeper: Beginning/,/%% Zoottelkeeper: End/d'
