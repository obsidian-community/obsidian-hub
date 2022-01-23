#!/usr/bin/env bash

cd ../..

# --disable no-multiple-blanks no-trailing-spaces added to make review of other changes easier
MARKDOWN_COMMAND=".github/scripts/node_modules/.bin/markdownlint --disable no-multiple-blanks no-trailing-spaces --fix"

${MARKDOWN_COMMAND} 00\ -\ Contribute\ to\ the\ Obsidian\ Hub
${MARKDOWN_COMMAND}  "04 - Guides, Workflows, & Courses"
