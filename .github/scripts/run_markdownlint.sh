#!/usr/bin/env bash

cd ../..

OUTPUT_FILE='.github/scripts/markdownlint_output.txt'
# --disable no-multiple-blanks no-trailing-spaces added to make review of other changes easier
# For discussion:
#  blanks-around-headings
#  no-trailing-punctuation - in headings
MARKDOWN_COMMAND=".github/scripts/node_modules/.bin/markdownlint \
  --disable \
    no-multiple-blanks \
    no-trailing-spaces \
    list-marker-space \
    blanks-around-fences \
    fenced-code-language \
    heading-increment \
    heading-style \
    list-indent \
    blanks-around-headings \
    heading-start-left \
    no-trailing-punctuation \
    ol-prefix \
    no-space-in-emphasis \
    no-empty-links \
    single-trailing-newline \
  -o ${OUTPUT_FILE}"

${MARKDOWN_COMMAND} \
  "00 - Contribute to the Obsidian Hub" \
  "04 - Guides, Workflows, & Courses"

sed 's/^.* MD/MD/' ${OUTPUT_FILE} | sort