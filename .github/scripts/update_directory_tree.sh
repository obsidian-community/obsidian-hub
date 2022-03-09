#!/usr/bin/env bash

# This script updates the directory tree and saves it as a code block in a new Markdown file which is located inside the Contributor Notes/Structure folder.

cd ../..

OUTPUT_FILE="00 - Contribute to the Obsidian Hub/03 Contributor Notes/03.01 Structure/Hub Tree Structure.md"

echo -e '%% Hub Tree: Don’t edit this file directly %%\n```' > "$OUTPUT_FILE"
tree -d -N -I venv --noreport >> "$OUTPUT_FILE"
echo -e '```\n%% Hub Tree: Don’t edit above %%' >> "$OUTPUT_FILE"
