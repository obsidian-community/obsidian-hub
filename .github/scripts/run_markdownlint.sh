#!/usr/bin/env bash

cd ../..

OUTPUT_FILE='.github/scripts/markdownlint_output.txt'
# TODO The rules disabled here are things that we wish to enable, but first we will need
#      to fix the markdown files which break each rule, then we can enable the rule.
#      Recommendation: Fix and enable one rule at a time.
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