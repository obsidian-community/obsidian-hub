#!/usr/bin/env bash

cd ../..

OUTPUT_FILE='.github/scripts/markdownlint_output.txt'
# --disable no-multiple-blanks no-trailing-spaces added to make review of other changes easier
MARKDOWN_COMMAND=".github/scripts/node_modules/.bin/markdownlint --disable no-multiple-blanks no-trailing-spaces -o ${OUTPUT_FILE}"

${MARKDOWN_COMMAND} \
  "00 - Contribute to the Obsidian Hub" \
  "04 - Guides, Workflows, & Courses"

sed 's/^.* MD/MD/' ${OUTPUT_FILE} | sort | uniq -c | sort -n