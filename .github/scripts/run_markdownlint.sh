#!/usr/bin/env bash

cd ../..

# --disable no-multiple-blanks no-trailing-spaces added to make review of other changes easier
MARKDOWN_COMMAND=".github/scripts/node_modules/.bin/markdownlint --disable no-multiple-blanks no-trailing-spaces -o .github/scripts/markdownlint_output.txt"

${MARKDOWN_COMMAND} \
  "00 - Contribute to the Obsidian Hub" \
  "04 - Guides, Workflows, & Courses"
