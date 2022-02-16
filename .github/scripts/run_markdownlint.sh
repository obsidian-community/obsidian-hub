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
    no-alt-text \
    no-duplicate-heading \
    no-space-in-links \
  -o ${OUTPUT_FILE}"

${MARKDOWN_COMMAND} .
LINT_EXIT_CODE=$?
# For error codes, see https://github.com/igorshubovych/markdownlint-cli#exit-codes

echo '-------------------------------------------------------------------------------'
echo "Raw output:"
cat ${OUTPUT_FILE}

echo '-------------------------------------------------------------------------------'
echo "Summary of output:"
sed 's/^.* MD/MD/' ${OUTPUT_FILE} | sort

exit ${LINT_EXIT_CODE}
